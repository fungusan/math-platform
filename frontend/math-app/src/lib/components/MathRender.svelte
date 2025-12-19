<script lang="ts">
    import { onMount, tick } from 'svelte';
    import renderMathInElement from 'katex/dist/contrib/auto-render.mjs';

    export let content: string = "";
    let container: HTMLElement;

    async function render() {
        if (!container) return;

        // 1. Wait for Svelte to apply the new 'content' string to the DOM
        await tick();

        // 2. Trigger the KaTeX auto-render
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

    // 3. This reactive statement is key. 
    // We explicitly watch 'content'. When it changes, we re-run render.
    $: if (content && container) {
        render();
    }

    onMount(render);
</script>

{#key content}
    <span class="unified-renderer" bind:this={container}>
        {content}
    </span>
{/key}

<style>
    .unified-renderer {
        display: contents; /* Makes this wrapper "invisible" for layout/sizing */
        white-space: pre-wrap;
        font-size: 1.2rem;
        font-family: serif;
    }

    /* Global KaTeX font scaling */
    :global(.katex) {
        font-size: 1em !important; /* Scale math up to match text */
    }

    :global(.katex-display) {
        margin: 1rem 0 !important;
        background: #F9FAF7;
        padding: 1rem;
        border-radius: 4px;
    }
</style>