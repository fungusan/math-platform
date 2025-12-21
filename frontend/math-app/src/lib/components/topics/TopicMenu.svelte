<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { fade, fly } from 'svelte/transition';

    export let topic: string = "";
    
    const dispatch = createEventDispatcher();

    let selectedMode = "Mix";
    let questionCount = 10;

    const modes = ["Easy", "Medium", "Hard", "Mix"];
    const counts = [5, 10, 15, 20];

    function startPractice() {
        dispatch('start', { mode: selectedMode, count: questionCount });
    }
</script>

<div class="backdrop" 
        on:click|self={() => dispatch('close')} 
        transition:fade={{duration: 200}} 
        on:keydown={(e) => {
            if (e.key === 'Enter' || e.key === ' ' || e.key === 'Escape') {
                e.preventDefault();
                dispatch('close');
            }
        }}
        role="button" 
        aria-label="Close menu"
        tabindex="0"
    >
    
    <div class="menu-window" transition:fly={{ y: 20, duration: 400 }}>
        
        <div class="topic-banner">
            <span class="banner-label">Curriculum Section</span>
            <h2>{topic}</h2>
            <div class="banner-decoration"></div>
        </div>

        <div class="menu-content">
            <section class="selection-group">
                <label>Select Difficulty</label>
                <div class="pill-grid">
                    {#each modes as mode}
                        <button 
                            class="pill" 
                            class:active={selectedMode === mode}
                            on:click={() => selectedMode = mode}
                        >
                            {mode}
                        </button>
                    {/each}
                </div>
            </section>

            <section class="selection-group">
                <label>Number of Questions</label>
                <div class="pill-grid">
                    {#each counts as count}
                        <button 
                            class="pill" 
                            class:active={questionCount === count}
                            on:click={() => questionCount = count}
                        >
                            {count}
                        </button>
                    {/each}
                </div>
            </section>

            <footer class="menu-footer">
                <button class="cancel-btn" on:click={() => dispatch('close')}>Cancel</button>
                <button class="start-btn" on:click={startPractice}>
                    Begin Session <span class="arrow">→</span>
                </button>
            </footer>
        </div>
    </div>
</div>

<style>
    .backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(26, 26, 26, 0.4);
        backdrop-filter: blur(4px);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        padding: 2rem;
    }

    .menu-window {
        background: #FDFCF8;
        width: 100%;
        max-width: 500px;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        border: 1px solid #E6E8E2;
    }

    .topic-banner {
        background-color: #849F5D;
        color: white;
        padding: 3rem 2rem;
        position: relative;
    }

    .banner-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        opacity: 0.8;
    }

    .topic-banner h2 {
        font-family: serif;
        font-size: 2rem;
        margin: 0.5rem 0 0 0;
        font-weight: 400;
    }

    .menu-content {
        padding: 2rem;
    }

    .selection-group {
        margin-bottom: 2rem;
    }

    label {
        display: block;
        font-size: 0.75rem;
        text-transform: uppercase;
        color: #888;
        margin-bottom: 1rem;
        letter-spacing: 0.1em;
    }

    .pill-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.5rem;
    }

    .pill {
        background: white;
        border: 1px solid #E6E8E2;
        padding: 0.6rem 0;
        border-radius: 6px;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.2s;
        font-family: inherit;
    }

    .pill.active {
        background: #849F5D;
        color: white;
        border-color: #849F5D;
    }

    .menu-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #E6E8E2;
    }

    .cancel-btn {
        background: none;
        border: none;
        color: #888;
        cursor: pointer;
        font-size: 0.9rem;
    }

    .start-btn {
        background: #1a1a1a;
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 100px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
</style>