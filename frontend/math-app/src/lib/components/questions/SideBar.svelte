<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    export let totalQuestions: number = 0;
    export let currentIndex: number = 0;
    export let answers: Record<number, string | null> = {};

    const dispatch = createEventDispatcher();

    // Calculate progress percentage
    $: answeredCount = Object.keys(answers).filter(key => answers[Number(key)] !== null).length;
    $: progressPercent = (answeredCount / totalQuestions) * 100;

    function selectQuestion(index: number): void {
        dispatch('jump', index);
    }

    $: isAnswered = (index: number): boolean => {
        return answers.hasOwnProperty(index) && answers[index] !== null;
    };
</script>

<aside class="sidebar">
    <div class="progress-container">
        <div class="progress-fill" style="width: {progressPercent}%"></div>
    </div>

    <div class="sidebar-header">
        <span class="label">Index</span>
        <span class="progress-text">{answeredCount}/{totalQuestions} solved</span>
    </div>

    <div class="question-nav">
        {#each Array(totalQuestions) as _, i}
            <button 
                class="nav-item" 
                class:active={i === currentIndex}
                class:answered={isAnswered(i)}
                on:click={() => selectQuestion(i)}
            >
                <span class="status-indicator"></span>
                <span class="q-number">Q{i + 1}</span>
            </button>
        {/each}
    </div>
</aside>

<style>
    /* 1. Container - Unified into a single definition */
    .sidebar {
        position: relative;
        padding: 2rem 0;
        border-right: 1px solid #e5e7eb;
        background: #FDFCF8;
        /* Flexbox is mandatory for the internal scroll to work */
        height: 680px;
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
    }

    .sidebar::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40px;
        background: linear-gradient(transparent, #FDFCF8);
        pointer-events: none; /* Allows clicking through the fade */
    }

    /* 2. Progress Bar */
    .progress-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: #F4F5F0;
        z-index: 10;
    }

    .progress-fill {
        height: 100%;
        background: #849F5D;
        transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* 3. Header */
    .sidebar-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        padding: 1rem 1.5rem 1.5rem 1.5rem;
    }

    .label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        font-weight: 700;
        display: block;
    }

    .progress-text {
        font-size: 0.7rem;
        font-family: serif;
        font-style: italic;
        color: #888;
    }

    /* 4. Scrollable Navigation Area */
    .question-nav {
        flex: 1; /* Takes up all remaining vertical space */
        overflow-y: auto; /* Enables vertical scroll */
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        padding-bottom: 2rem;
        
        /* Thin Scrollbar for Firefox */
        scrollbar-width: thin;
        scrollbar-color: #E6E8E2 transparent;
    }

    /* Scrollbar for Chrome/Safari/Edge */
    .question-nav::-webkit-scrollbar {
        width: 6px;
    }
    .question-nav::-webkit-scrollbar-thumb {
        background-color: #E6E8E2;
        border-radius: 10px;
    }
    .question-nav::-webkit-scrollbar-thumb:hover {
        background-color: #849F5D;
    }

    /* 5. Navigation Items */
    .nav-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.75rem 1.5rem;
        background: transparent;
        border: none;
        cursor: pointer;
        text-align: left;
        font-family: inherit;
        color: #666;
        transition: all 0.2s ease;
        position: relative;
    }

    .nav-item:hover {
        color: #849F5D;
        background: #F9FAF7;
    }

    .status-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        border: 2px solid #ccc;
        flex-shrink: 0;
    }

    .nav-item.answered .status-indicator {
        border-color: #849F5D;
        background-color: #849F5D;
    }

    .nav-item.active {
        color: #1a1a1a;
        font-weight: 600;
        background: #F9FAF7;
    }

    .nav-item.active::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background-color: #849F5D;
    }

    /* 6. Tablet & Mobile (Responsive) */
    @media (max-width: 1024px) {
        .sidebar {
            position: sticky;
            bottom: 0;
            width: 100%;
            height: auto;
            display: block; /* Back to block for sticky content flow */
            border-right: none;
            border-top: 1px solid #e5e7eb;
            padding: 0;
            z-index: 100;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.05);
        }

        .sidebar::after { display: none; }

        .sidebar-header {
            padding: 0.75rem 1rem 0.25rem 1rem;
        }

        .question-nav {
            flex-direction: row; /* Horizontal scroll */
            overflow-x: auto;
            overflow-y: hidden;
            padding: 0.5rem 1rem 1rem 1rem;
            scrollbar-width: none;
        }

        .question-nav::-webkit-scrollbar {
            display: none;
        }

        .nav-item {
            flex-direction: column;
            min-width: 65px;
            padding: 0.5rem;
            gap: 4px;
            align-items: center;
        }

        .nav-item.active::before {
            width: 100%;
            height: 3px;
            top: auto;
            bottom: 0;
        }
    }
</style>