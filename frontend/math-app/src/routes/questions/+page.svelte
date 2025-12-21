<script lang="ts">
    import NavBar from '../../lib/components/shared/NavBar.svelte';
    import SideBar from '../../lib/components/questions/SideBar.svelte';
    import QuestionBook from '../../lib/components/questions/QuestionBook.svelte';
	import Footer from '$lib/components/shared/Footer.svelte';

    // 1. MOCK DATA
    export const mockQuestions = [
        {
            id: 104,
            text: `Solve for the value of $x$ in the following quadratic equation: $$f(x) = ax^2 + bx + c$$
                    A super long block equation: $$
                    \\begin{aligned}
                    1+1+1+1+1+1+1+1+1+1+1+ \\\ 
                    1+1+1+1+1+1+1+1+1+1+1
                    \\end{aligned}
                    $$ This is not an equation, but an extremely long text!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Still hasn't ended...
                    .............. OMG so longggggggggg!!!!`,
            difficulty: "hard",
            options: [
                { key: 'A', value: "$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$" },
                { key: 'B', value: "$x = \\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}$" },
                { key: 'C', value: "$x = \\frac{-b \\pm \\sqrt{b^2 + 4ac}}{2a}$" },
                { key: 'D', value: "$x = \\frac{-b \\pm (b^2 - 4ac)}{2a}$" }
            ]
        },
        {
            id: 106,
            text: `Consider the geometric figure below. Given that $O$ is the center of the circle and $\\angle ABC = 30^\\circ$:
                <div class="image-wrapper">
                    <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=400" alt="Circle Geometry" />
                </div>
                Find the value of $\\angle AOC$.`,
            difficulty: "medium",
            options: [
                { key: 'A', value: "$30^\\circ$" },
                { key: 'B', value: "$45^\\circ$" },
                { key: 'C', value: "$60^\\circ$" },
                { key: 'D', value: "$90^\\circ$" }
            ]
        },
        {
            id: 107,
            text: `The following table records the frequency of scores in a recent math quiz:
                <table class="editorial-table">
                    <tr><th>Score Range</th><th>Frequency ($f$)</th></tr>
                    <tr><td>$0 - 10$</td><td>$2$</td></tr>
                    <tr><td>$10 - 20$</td><td>$5$</td></tr>
                    <tr><td>$20 - 30$</td><td>$x$</td></tr>
                </table>
                If the total frequency is $15$, find the value of $x$.`,
            difficulty: "easy",
            options: [
                { key: 'A', value: "6" },
                { key: 'B', value: "8" },
                { key: 'C', value: "10" },
                { key: 'D', value: "12" }
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
    .practice-layout {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    .layout-grid {
        display: grid;
        grid-template-columns: 280px 1fr;
        gap: 2rem;
        align-items: start; /* CRITICAL: Prevents sidebar from stretching to match book height */
    }

    /* THE FIX: Unify Tablet and Mobile behavior at 1024px */
    @media (max-width: 1024px) {
        .layout-grid {
            display: flex;
            flex-direction: column; /* Stack vertically */
            grid-template-columns: 1fr;
        }

        .sidebar-container {
            order: 2; /* Move sidebar to the bottom of the stack */
            width: 100%;
        }

        .book-container {
            order: 1; /* Keep book at the top */
            width: 100%;
        }
    }
</style>