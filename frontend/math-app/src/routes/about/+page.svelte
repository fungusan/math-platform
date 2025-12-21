<script lang="ts">
    import NavBar from '../../lib/components/shared/NavBar.svelte';
    import Footer from '../../lib/components/shared/Footer.svelte';
</script>

<NavBar activePage="about" />

<main class="editorial-container">
    <header class="page-header">
        <h1 class="serif-title">The Story</h1>
        <div class="header-line"></div>
    </header>

    <section class="book-frame">
        <div class="book-gutter"></div>
        
        <div class="book-page left-page">
            <h2 class="section-label">01. The Platform</h2>
            <h3 class="serif-subtitle">A Daily Practice Ritual</h3>
            <p>
                Inspired by the persistence of <em>LeetCode</em>, this platform was built to 
                transform the way we approach DSE Mathematics. It isn't just about finding 
                an answer; it's about the mechanics of the solution.
            </p>
            <ul class="feature-list">
                <li>Randomized problem sets across different DSE math topics.</li>
                <li>Adaptive difficulty tiers: from Easy to Mixed mastery.</li>
                <li>Daily challenges and streaks to cultivate persistence.</li>
                <li>Deep statistics to visualize your progress through nature's logic.</li>
            </ul>
        </div>

        <div class="book-page right-page">
            <h2 class="section-label">02. The Architect</h2>
            <h3 class="serif-subtitle">Systems & Mechanics</h3>
            <p>
                As a Computer Science student with a deep fascination for algorithms, 
                my curiosity eventually led me toward the intricate world of system architecture.
            </p>
            <p>
                I find that the complex mechanics of nature are mirrored in the elegance 
                of mathematics. This project is the intersection of my technical 
                pursuits and my love for scientific discovery.
            </p>
            <div class="signature">Fungusan</div>
        </div>
    </section>

    <section class="portfolio-redirect">
        <div class="green-accent-block"></div>
        <div class="redirect-content">
            <h2 class="serif-title small">The Main Gallery</h2>
            <p>Discover more projects, thoughts, and architectural designs at my primary portfolio.</p>
            <a href="https://fungusan.com/" target="_blank" class="portfolio-btn">
                Visit fungusan.com <span class="arrow">→</span>
            </a>
        </div>
    </section>
</main>

<Footer />

<style>
    .editorial-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 4rem 2rem;
    }

    .page-header {
        margin-bottom: 4rem;
        text-align: center;
    }

    .serif-title {
        font-family: serif;
        font-size: 4rem;
        font-weight: 400;
        margin: 0;
    }

    .serif-title.small { font-size: 2.5rem; }

    .header-line {
        width: 60px;
        height: 3px;
        background: #849F5D;
        margin: 1.5rem auto 0;
    }

    /* Book Frame Styling */
    .book-frame {
        background-color: #FDFCF8; /* Matches your Figma cream background */
        border: 1px solid #E6E8E2;
        border-radius: 4px;
        box-shadow: 10px 10px 0px #F4F5F0; /* "Paper stack" effect */
        display: grid;
        grid-template-columns: 1fr 1fr;
        position: relative;
        min-height: 500px;
        margin-bottom: 8rem;
    }

    .book-gutter {
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 1px;
        background: linear-gradient(to right, transparent, rgba(0,0,0,0.05), transparent);
        z-index: 2;
    }

    .book-page {
        padding: 4rem;
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }

    .left-page { border-right: 1px solid #f0f0f0; }

    .section-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        font-weight: 700;
    }

    .serif-subtitle {
        font-family: serif;
        font-size: 1.8rem;
        color: #1a1a1a;
    }

    p {
        line-height: 1.7;
        color: #444;
        font-size: 1.05rem;
    }

    .feature-list {
        list-style: none;
        padding: 0;
        margin-top: 1rem;
    }

    .feature-list li {
        padding-left: 1.5rem;
        position: relative;
        margin-bottom: 0.75rem;
        font-size: 0.95rem;
        color: #666;
    }

    .feature-list li::before {
        content: "•";
        color: #849F5D;
        position: absolute;
        left: 0;
        font-weight: bold;
    }

    .signature {
        margin-top: auto;
        font-family: serif;
        font-style: italic;
        font-size: 1.4rem;
        color: #849F5D;
    }

    /* Portfolio Section */
    .portfolio-redirect {
        display: grid;
        grid-template-columns: 150px 1fr;
        gap: 4rem;
        align-items: center;
        background: #F4F5F0;
        padding: 4rem;
        border-radius: 20px;
    }

    .green-accent-block {
        height: 150px;
        background: #849F5D;
        border-radius: 12px;
    }

    .redirect-content {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .portfolio-btn {
        display: inline-block;
        margin-top: 1rem;
        color: #849F5D;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
    }

    .portfolio-btn:hover .arrow {
        padding-left: 8px;
    }

    .arrow {
        transition: padding 0.2s ease;
    }

    /* Mobile view: Stack the "pages" */
    @media (max-width: 850px) {
        .book-frame { grid-template-columns: 1fr; }
        .book-gutter { display: none; }
        .left-page { border-right: none; border-bottom: 1px solid #f0f0f0; }
        .portfolio-redirect { grid-template-columns: 1fr; padding: 2rem; }
        .green-accent-block { height: 10px; }
    }
</style>