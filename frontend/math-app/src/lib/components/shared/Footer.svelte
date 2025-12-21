<script lang="ts">
    export let currentYear = new Date().getFullYear();
</script>

<footer class="colophon">
    <div class="colophon-inner">
        <div class="brand-section">
            <span class="brand-name">Fungusan</span>
            <p class="bio">A personal space for mathematics and structured learning.</p>
        </div>

        <div class="links-section">
            <span class="footer-label">Index</span>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/statistics">Statistics</a>
        </div>

        <div class="legal-section">
            <p>&copy; {currentYear}</p>
            <p>Designed by Fungusan.</p>
        </div>
    </div>
</footer>

<style>
    .colophon {
        margin-top: 8rem;
        padding: 4rem 2rem;
        border-top: 1px solid #e5e7eb;
        background-color: #FDFCF8; /* Cream background to match the page */
    }

    .colophon-inner {
        max-width: 1100px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr auto auto;
        gap: 4rem;
        align-items: start;
    }

    .brand-name {
        font-family: serif;
        font-size: 1.2rem;
        color: #849F5D;
        display: block;
        margin-bottom: 0.5rem;
    }

    .bio {
        font-size: 0.9rem;
        color: #888;
        max-width: 250px;
        line-height: 1.5;
    }

    .links-section {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }

    .links-section a {
        text-decoration: none;
        color: #1a1a1a;
        font-size: 0.9rem;
        transition: color 0.2s;
    }

    .links-section a:hover {
        color: #849F5D;
    }

    .legal-section p {
        font-size: 0.85rem;
        color: #aaa;
        text-align: right;
    }

    @media (max-width: 768px) {
        .colophon-inner {
            grid-template-columns: 1fr;
            gap: 2rem;
        }
        .legal-section p { text-align: left; }
    }

    .footer-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #849F5D;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    @media (max-width: 768px) {
        .colophon {
            padding: 4rem 1.5rem;
            margin-top: 4rem;
        }

        .colophon-inner {
            grid-template-columns: 1fr; /* Single column stack */
            gap: 3rem;
            text-align: center;
        }

        .brand-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: -1rem;
        }

        .bio {
            max-width: 100%;
        }

        .links-section {
            align-items: center;
            display: none;
        }

        .legal-section p {
            text-align: center;
        }
    }
</style>