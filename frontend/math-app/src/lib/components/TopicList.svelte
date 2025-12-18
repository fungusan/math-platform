<script>
    export let topics = [
        'Number and Algebra',
        'Measures, Shape and Space',
        'Data Handling'
    ];
</script>

<div class="editorial-list">
    {#each topics as topic, i}
        <button class="topic-row">
            <span class="index">0{i + 1}</span>
            <div class="text-group">
                <span class="topic-name">{topic}</span>
                <span class="description">Master the core principles and practice problems.</span>
            </div>
            <div class="action-line"></div>
        </button>
    {/each}
</div>

<style>
    .editorial-list {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }

    .topic-row {
        display: grid;
        grid-template-columns: 60px 1fr auto;
        align-items: center;
        padding: 2rem 0;
        border-bottom: 1px solid #e5e7eb;
        background: transparent;
        text-align: left;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    /* The green vertical bar inspired by your Figma sidebar */
    .topic-row::before {
        content: "";
        position: absolute;
        left: 0;
        top: 20%;
        bottom: 20%;
        width: 4px;
        background-color: #849F5D;
        transform: scaleY(0);
        transition: transform 0.3s ease;
    }

    .topic-row:hover {
        padding-left: 2rem;
    }

    .topic-row:hover::before {
        transform: scaleY(1);
    }

    /* Large, bold index numbers */
    .index {
        font-family: serif; /* Matches your "Maths" heading style */
        font-size: 1.25rem;
        color: #849F5D;
        font-weight: 600;
        opacity: 0.6;
    }

    .text-group {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }

    .topic-name {
        font-size: 1.5rem;
        font-weight: 500;
        color: #1a1a1a;
        letter-spacing: -0.01em;
    }

    .description {
        font-size: 0.9rem;
        color: #666;
        font-weight: 400;
    }

    /* Subtle line that extends on hover */
    .action-line {
        width: 40px;
        height: 1px;
        background: #849F5D;
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.3s ease;
    }

    .topic-row:hover .action-line {
        transform: scaleX(1);
    }

    @media (max-width: 640px) {
        .topic-name { font-size: 1.2rem; }
        .index { font-size: 1rem; }
    }
</style>