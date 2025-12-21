<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    // Type for the answers object
    interface Answers {
        [key: number]: string | null;
    }

    // Define event dispatch types
    interface DispatchEvents {
        jump: number;
    }

    // Props with explicit typing
    export let totalQuestions: number = 0;
    export let currentIndex: number = 0;
    export let answers: Answers = {};

    const dispatch = createEventDispatcher<DispatchEvents>();

    function selectQuestion(index: number): void {
        dispatch('jump', index);
    }

    // Type the reactive statement
    $: isAnswered = (index: number): boolean => {
        return answers.hasOwnProperty(index) && answers[index] !== null;
    };
</script>

<aside class="sidebar">
    <div class="sidebar-header">
        <span class="label">Index</span>
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
                <span class="q-number">Question {i + 1}</span>
                {#if isAnswered(i)}
                    <span class="answer-hint">({answers[i]})</span>
                {/if}
            </button>
        {/each}
    </div>
</aside>

<style>
    .sidebar {
        padding: 2rem 0;
        border-right: 1px solid #e5e7eb;
        height: 100%;
    }

    .label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        font-weight: 700;
        padding-left: 1.5rem;
        margin-bottom: 1.5rem;
        display: block;
    }

    .question-nav {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

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

    /* The circular indicator */
    .status-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        border: 2px solid #ccc;
        transition: all 0.2s ease;
    }

    /* State: Answered (Filled green circle) */
    .nav-item.answered .status-indicator {
        border-color: #849F5D;
        background-color: #849F5D;
    }

    /* State: Active (Currently viewing) */
    .nav-item.active {
        color: #1a1a1a;
        font-weight: 600;
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
    
    .nav-item.active .status-indicator {
        border-color: #849F5D;
    }

    .answer-hint {
        margin-left: auto;
        font-size: 0.85rem;
        color: #849F5D;
    }
</style>