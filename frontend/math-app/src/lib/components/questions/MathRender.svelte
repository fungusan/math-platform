<script lang="ts">
    import { onMount, tick } from 'svelte';
    import renderMathInElement from 'katex/dist/contrib/auto-render.mjs';

    export let content: string = "";
    let container: HTMLElement;

    async function render() {
        if (!container) return;
        await tick();
        renderMathInElement(container, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false},
                {left: '\\(', right: '\\)', display: false},
                {left: '\\[', right: '\\]', display: true}
            ],
            throwOnError: false
        });
    }

    $: if (content && container) render();
    onMount(render);
</script>

{#key content}
    <div class="unified-renderer" bind:this={container}>
        {@html content}
    </div>
{/key}

<style>
    .unified-renderer {
        font-family: serif;
        line-height: 1.7;
        font-size: 1.15rem;
    }

    @media (max-width: 600px) {
        .unified-renderer {
            font-size: 1.05rem; /* Slightly smaller text for mobile */
        }
        
        :global(.katex-display) {
            padding: 0.75rem; /* Tighter padding on mobile */
            margin: 0.5rem 0 !important;
        }
    }

    /* Style for Tables stored in your DB */
    :global(.editorial-table) {
        width: 100%;
        margin: 2rem 0;
        border-collapse: collapse;
        font-family: sans-serif; /* Cleaner for data */
        font-size: 0.95rem;
    }

    :global(.editorial-table th) {
        background: #F4F5F0;
        border: 1px solid #E6E8E2;
        padding: 0.75rem;
        text-align: center;
    }

    :global(.editorial-table td) {
        border: 1px solid #E6E8E2;
        padding: 0.75rem;
        text-align: center;
    }

    /* Style for Images stored in your DB */
    :global(.unified-renderer img) {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1.5rem auto;
        border-radius: 4px;
    }

    :global(.katex-display) {
        margin: 1rem 0 !important;
        padding: 1rem;
        background: #F9FAF7;
        border-radius: 4px;
        
        /* THE FIX: Allow horizontal scrolling for long equations */
        overflow-x: auto;
        overflow-y: hidden;
        
        /* Optional: Custom scrollbar to match editorial style */
        scrollbar-width: thin;
        scrollbar-color: #849F5D transparent;
    }

    /* For Webkit browsers (Chrome/Safari) */
    :global(.katex-display::-webkit-scrollbar) {
        height: 4px;
    }
    :global(.katex-display::-webkit-scrollbar-thumb) {
        background-color: #849F5D;
        border-radius: 10px;
    }
</style>