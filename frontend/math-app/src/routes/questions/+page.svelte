<script lang="ts">
    import NavBar from '../../lib/components/NavBar.svelte';
    import SideBar from '../../lib/components/SideBar.svelte';
    import QuestionBook from '../../lib/components/QuestionBook.svelte';
	import Footer from '$lib/components/Footer.svelte';

    // 1. MOCK DATA
    const mockQuestions = [
        {
            id: 104,
            text: "Solve for the value of $x$ in the following quadratic equation: $$f(x) = ax^2 + bx + c$$",
            difficulty: "hard",
            options: [
                { key: 'A', value: "$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$" },
                { key: 'B', value: "$x = \\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}$" },
                { key: 'C', value: "$x = \\frac{-b \\pm \\sqrt{b^2 + 4ac}}{2a}$" },
                { key: 'D', value: "$x = \\frac{-b \\pm (b^2 - 4ac)}{2a}$" }
            ]
        },
        {
            id: 105,
            text: "$1+1 = ?$",
            difficulty: "easy",
            options: [
                { key: 'A', value: "1" },
                { key: 'B', value: "2" },
                { key: 'C', value: "3" },
                { key: 'D', value: "4" }
            ]
        },
    ];

    // 2. STATE MANAGEMENT
    let currentIndex = 0;
    // Stores answers as index -> optionKey (e.g., { 0: 'C', 1: 'A' })
    let userAnswers: Record<number, string> = {}; 

    // 3. DERIVED STATE
    $: currentQuestion = mockQuestions[currentIndex];
    $: totalCount = mockQuestions.length;
    // Check if current question has an answer stored
    $: currentSelectedOption = userAnswers[currentIndex] || null;
    // Check if total answers stored equals total questions
    $: allQuestionsAnswered = Object.keys(userAnswers).length === totalCount;

    // 4. EVENT HANDLERS
    function handleNext() {
        if (currentIndex < totalCount - 1) currentIndex++;
    }

    function handlePrev() {
        if (currentIndex > 0) currentIndex--;
    }

    function handleJump(event: CustomEvent<number>) {
        currentIndex = event.detail;
    }

    function handleOptionSelect(event: CustomEvent<{questionId: number, option: string}>) {
        // Update the answers object. Using spread to trigger Svelte reactivity.
        userAnswers = {
            ...userAnswers,
            [currentIndex]: event.detail.option
        };
    }
</script>

<NavBar activePage="practice" />

<main class="practice-layout">
    <div class="layout-grid">
        <div class="sidebar-container">
            <SideBar 
                totalQuestions={totalCount}
                {currentIndex}
                answers={userAnswers}
                on:jump={handleJump}
            />
        </div>

        <div class="book-container">
            <QuestionBook 
                question={currentQuestion}
                {currentIndex}
                totalQuestions={totalCount}
                selectedOption={currentSelectedOption}
                allAnswered={allQuestionsAnswered}
                on:next={handleNext}
                on:prev={handlePrev}
                on:select={handleOptionSelect}
            />
        </div>
    </div>
</main>

<Footer />

<style>
    /* Ensure the page fills height so sidebar looks correct */
    :global(body, html) {
        height: 100%;
        background-color: #FDFCF8; /* Ensure background matches book paper */
    }

    .practice-layout {
        height: calc(100vh - 80px); /* Adjust based on your navbar height */
        max-width: 1200px;
        margin: 0 auto;
    }

    .layout-grid {
        display: grid;
        grid-template-columns: 280px 1fr; /* Fixed sidebar width, flexible content */
        height: 100%;
    }

    .sidebar-container {
        height: 100%;
        background: #f8f9fa; /* Slightly darker cream for sidebar contrast */
    }

    .book-container {
        height: 100%;
        overflow-y: auto; /* Allows scrolling if question is very long */
    }

    /* Responsive design for smaller screens */
    @media (max-width: 900px) {
        .layout-grid {
            grid-template-columns: 80px 1fr; /* Shrink sidebar */
        }
        /* You might want to hide labels in SideBar.svelte on small screens */
    }

    @media (max-width: 640px) {
        .layout-grid {
            grid-template-columns: 1fr;
            grid-template-rows: auto 1fr; /* Stack vertically */
        }
        .sidebar-container {
            height: auto;
            border-right: none;
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 1rem;
        }
        /* In SideBar.svelte, you'd change flex-direction to row for mobile */
    }
</style>