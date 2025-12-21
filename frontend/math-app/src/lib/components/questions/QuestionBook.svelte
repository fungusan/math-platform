<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import Math from './MathRender.svelte';

    interface Option {
        key: string;
        value: string; // This can now contain LaTeX strings
    }

    interface Question {
        id: number;
        text: string;
        difficulty: string;
        options: Option[];
    }

    export let question: Question;
    export let currentIndex: number = 0;
    export let totalQuestions: number = 0;
    export let selectedOption: string | null = null;
    export let allAnswered: boolean = false;

    const dispatch = createEventDispatcher<{
        select: { questionId: number; option: string };
        next: null;
        prev: null;
    }>();

    function handleOptionClick(optionKey: string): void {
        dispatch('select', { questionId: question.id, option: optionKey });
    }
</script>

<section class="book-page-container">
    <div class="book-page">
        <header class="page-header">
            <span class="page-number">Page {currentIndex + 1} of {totalQuestions}</span>
            <div class="question-content">
                    <Math content={question.text} />
            </div>
        </header>

        <div class="tag-container">
            <p 
                class="difficulty-tag"
                style="color: {question.difficulty === "hard" ? '#FF6B6B' : question.difficulty === "medium" ? '#FFA726' : '#849F5D'};
                    border-color: {question.difficulty === "hard" ? '#FF6B6B' : question.difficulty === "medium" ? '#FFA726' : '#849F5D'};"
            >
                {question.difficulty}
            </p>
        </div>

        <div class="options-list">
            {#each question.options as opt}
                <button 
                    class="option-item" 
                    class:selected={selectedOption === opt.key}
                    on:click={() => handleOptionClick(opt.key)}
                >
                    <span class="opt-key">{opt.key}</span>
                    <div class="opt-val">
                        <Math content={opt.value} />
                    </div>
                </button>
            {/each}
        </div>

        {#if allAnswered}
            <div class="submit-area">
                <button class="submit-btn">Submit All Answers</button>
            </div>
        {/if}

        <div class="page-corners">
            <button class="corner-btn prev" disabled={currentIndex === 0} on:click={() => dispatch('prev')}>← Prev</button>
            <button class="corner-btn next" disabled={currentIndex === totalQuestions - 1} on:click={() => dispatch('next')}>Next →</button>
        </div>
    </div>
</section>

<style>
    /* Styling remains identical to the previous editorial version */
    .book-page-container {
        padding: 2rem;
        min-height: calc(100vh - 80px);
        display: flex;
        justify-content: center;
        align-items: flex-start;
    }

    .book-page {
        background-color: #FDFCF8;
        width: 100%;
        max-width: 800px;
        min-height: 600px;
        padding: 4rem;
        padding-bottom: 8rem;
        box-shadow: 10px 10px 0px #F4F5F0;
        border: 1px solid #E6E8E2;
        border-radius: 4px;
        position: relative;
        display: flex;
        flex-direction: column;
    }

    .page-header { margin-bottom: 3rem; }

    .page-number {
        display: block;
        text-align: right;
        font-size: 0.85rem;
        color: #888;
        margin-bottom: 1rem;
        font-family: serif;
        font-style: italic;
    }

    .tag-container {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1rem;
    }

    .difficulty-tag {
        border: 1px solid #E6E8E2;
        border-radius: 12px;
        flex-shrink: 0;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.15rem 1rem;
        font-size: 1rem;
        font-family: serif;
        font-weight: 500;
        margin-right: 8px;
    }

    .options-list {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        flex-grow: 1;
    }

    .option-item {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        padding: 1.25rem;
        background: white;
        border: 1px solid #E6E8E2;
        border-radius: 8px;
        cursor: pointer;
        text-align: left;
        transition: all 0.2s ease;
    }

    .option-item:hover {
        border-color: #849F5D;
        background: #F9FAF7;
    }

    .option-item.selected {
        background-color: #F4F8F0;
        border-color: #849F5D;
    }

    .opt-key {
        font-weight: 700;
        color: #849F5D;
        width: 30px;
    }

    .submit-area {
        display: flex;
        justify-content: center;
        margin-top: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .submit-btn {
        background: #849F5D;
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 100px;
        font-weight: 500;
        cursor: pointer;
    }

    .corner-btn {
        position: absolute;
        bottom: 0;
        background: none;
        border: none;
        font-family: serif;
        font-size: 1rem;
        color: #849F5D;
        padding: 1.5rem 2rem;
        cursor: pointer;
    }

    .corner-btn.prev { left: 0; }
    .corner-btn.next { right: 0; }

    .question-content {
        margin-top: 1rem;
    }
    /* Ensure KaTeX symbols align well with our editorial text */
    :global(.katex) {
        font-size: 1.2em;
        color: #1a1a1a;
    }

    /* Responsive Logic */
    @media (max-width: 1024px) {
        .book-page-container {
            padding: 2rem 1rem; /* Balanced padding for iPad */
            align-items: center; /* Center the book page */
        }

        .book-page {
            padding: 3rem 2rem; /* Reduce desktop's 4rem padding */
            max-width: 700px;
            min-height: auto; /* Content drives height */
        }
    }

    @media (max-width: 640px) {
        .book-page {
            padding: 1rem 1rem 5rem 1rem;
            box-shadow: 4px 4px 0px #F4F5F0;
        }
    }
</style>