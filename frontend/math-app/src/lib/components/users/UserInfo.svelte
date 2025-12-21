<script>
    // Props
    export let userName = "Fungusan";
    export let userId = "CS-2025-089";
    export let streak = 12;
</script>

<section class="user-bio">
    <div class="bio-accent-bar"></div>
    <div class="bio-content">
        <h2 class="label">The Student</h2>
        <h1 class="serif-name">{userName}</h1>
        <div class="details-grid">
            <div class="detail">
                <span class="detail-label">Identifier</span>
                <span class="detail-value">#{userId}</span>
            </div>
            <div class="detail">
                <span class="detail-label">Current Streak</span>
                <span class="detail-value streak">{streak} Days</span>
            </div>
        </div>
        <p class="bio-text">
            A scholar in the mechanics of mathematics, currently exploring the intersection 
            of algorithms and architectural systems. Progress is documented daily.
        </p>
    </div>
</section>

<style>
    .user-bio {
        display: grid;
        grid-template-columns: 8px 1fr;
        gap: 2rem;
        margin-bottom: 5rem;
        align-items: start;
    }

    .bio-accent-bar {
        height: 100%;
        min-height: 180px;
        background-color: #849F5D;
        border-radius: 4px;
    }

    .label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }

    .serif-name {
        font-family: serif;
        font-size: 3rem;
        margin: 0 0 1.5rem 0;
        color: #1a1a1a;
    }

    .details-grid {
        display: flex;
        gap: 3rem;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid #e5e7eb;
        padding-bottom: 1.5rem;
    }

    .detail {
        display: flex;
        flex-direction: column;
    }

    .detail-label {
        font-size: 0.75rem;
        color: #888;
        text-transform: uppercase;
    }

    .detail-value {
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
    }

    .streak { color: #849F5D; }

    .bio-text {
        max-width: 500px;
        line-height: 1.6;
        color: #555;
        font-style: italic;
    }
</style>