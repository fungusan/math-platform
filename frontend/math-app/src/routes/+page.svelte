<script lang="ts">
    import TopicList from '$lib/components/TopicList.svelte';
    import NavBar from '../lib/components/NavBar.svelte';
    import Footer from'../lib/components/Footer.svelte';
</script>

<svelte:head>
    <title>Maths | The Story of Practice</title>
</svelte:head>

<NavBar />

<main class="editorial-container">
    <header class="hero">
        <div class="hero-accent-bar"></div>
        <div class="hero-main">
            <h1 class="title">Maths</h1>
            <p class="tagline">The Story of a Maths Lover — Practice Edition</p>
            <p class="intro-text">
                Select a topic to start practicing. Like the underlying structure of nature, 
                mathematics is the key to understanding the universe.
            </p>
        </div>
        
        <aside class="side-stats">
            <div class="stat-item">03 Topics</div>
            <div class="stat-item">100+ Qns</div>
            <div class="stat-item">Progress</div>
        </aside>
    </header>

    <section class="content-split">
        <div class="list-header">
            <h2 class="section-label">Available Topics</h2>
            <div class="divider"></div>
        </div>
        
        <div class="topic-section">
            <TopicList />
        </div>
    </section>
</main>

<Footer />

<style>
    /* Editorial Theme Colors */
    :global(body) {
        background-color: #FDFCF8; /* Creamy paper background from your screenshot */
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }

    .editorial-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 4rem 2rem;
    }

    /* Hero Layout */
    .hero {
        display: grid;
        grid-template-columns: 40px 1fr 150px;
        gap: 3rem;
        margin-bottom: 8rem;
        position: relative;
    }

    .hero-accent-bar {
        width: 40px;
        height: 250px;
        background-color: #849F5D; /* Your characteristic green */
    }

    .title {
        font-size: 6rem;
        font-weight: 400;
        font-family: serif; /* Matches your Figma "Maths" title */
        margin: 0;
        line-height: 0.9;
    }

    .tagline {
        font-size: 1.5rem;
        margin-top: 1rem;
        font-weight: 500;
    }

    .intro-text {
        max-width: 450px;
        margin-top: 2rem;
        color: #555;
        line-height: 1.6;
    }

    .side-stats {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        gap: 2rem;
        border-left: 1px solid #e5e7eb;
        padding-left: 2rem;
    }

    .stat-item {
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-size: 0.9rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #888;
    }

    /* Content Split */
    .content-split {
        margin-bottom: 6rem;
    }

    .list-header {
        margin-bottom: 3rem;
    }

    .section-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        margin-bottom: 0.5rem;
    }

    .divider {
        width: 80px;
        height: 2px;
        background: #849F5D;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero { grid-template-columns: 1fr; gap: 2rem; }
        .hero-accent-bar { width: 100%; height: 10px; }
        .side-stats { flex-direction: row; border-left: none; border-top: 1px solid #eee; padding-top: 1rem; }
        .stat-item { writing-mode: horizontal-tb; }
        .title { font-size: 4rem; }
    }
</style>