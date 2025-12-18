<script lang="ts">
    interface HistoryRecord {
        topic: string;
        rate: number;
        date: string;
        wrongQids: number[];
    }

    // Props: array of { topic, rate, date, wrongQids }
    export let records: HistoryRecord[] = [];
    
    let expandedIndex: number | null = null;

    function toggle(index: number): void {
        expandedIndex = expandedIndex === index ? null : index;
    }
</script>

<section class="index-section">
    <h2 class="index-title">Archives of Practice</h2>
    
    <div class="index-list">
        {#each records as record, i}
            <div class="index-item" class:active={expandedIndex === i}>
                <button class="index-row" on:click={() => toggle(i)}>
                    <span class="topic">{record.topic}</span>
                    <span class="dots"></span>
                    <span 
                        class="rate" 
                        style="color: {record.rate <= 35 ? '#FF6B6B' : record.rate <= 65 ? '#FFA726' : '#849F5D'};"
                    >
                        {record.rate}%
                    </span>
                    <span class="date">{record.date}</span>
                </button>

                {#if expandedIndex === i}
                    <div class="expansion">
                        <p class="expansion-label">Points for Correction (QIDs):</p>
                        <div class="qid-grid">
                            {#each record.wrongQids as qid}
                                <span class="qid-tag">#{qid}</span>
                            {/each}
                        </div>
                    </div>
                {/if}
            </div>
        {/each}
    </div>
</section>

<style>
    .index-title {
        font-family: serif;
        font-size: 1.8rem;
        margin-bottom: 2rem;
        border-bottom: 2px solid #1a1a1a;
        padding-bottom: 0.5rem;
        display: inline-block;
    }

    .index-list { width: 100%; }

    .index-item {
        border-bottom: 1px solid #eee;
        transition: background 0.2s;
    }

    .index-row {
        width: 100%;
        display: flex;
        align-items: baseline;
        padding: 1.25rem 0;
        background: none;
        border: none;
        cursor: pointer;
        font-family: inherit;
        text-align: left;
    }

    .topic {
        font-size: 1.1rem;
        font-weight: 500;
        color: #1a1a1a;
    }

    /* The "Book Index" dots */
    .dots {
        flex-grow: 1;
        border-bottom: 1px dotted #ccc;
        margin: 0 1rem;
        position: relative;
        top: -4px;
    }

    .rate {
        font-weight: 700;
        margin-right: 2rem;
    }

    .date {
        color: #999;
        font-size: 0.9rem;
        min-width: 100px;
        text-align: right;
    }

    .expansion {
        padding: 0 0 1.5rem 0;
        animation: slideIn 0.3s ease-out;
    }

    .expansion-label {
        font-size: 0.8rem;
        color: #888;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
    }

    .qid-grid {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .qid-tag {
        background: #F4F5F0;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-size: 0.85rem;
        color: #555;
        border: 1px solid #E6E8E2;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateY(-5px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>