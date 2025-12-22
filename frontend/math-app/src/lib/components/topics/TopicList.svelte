<script lang="ts">
    import { onMount } from 'svelte';
    import TopicMenu from './TopicMenu.svelte';

    // 1. STATE MANAGEMENT
    let topics: any[] = [];
    let isLoading = true;
    let error: string | null = null;

    let searchQuery = "";
    let currentPage = 1;
    let itemsPerPage = 3;

    // 2. FETCH LOGIC
    async function fetchTopics() {
        try {
            isLoading = true;
            const response = await fetch('http://localhost:8000/questions/topics');
            
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.status}`);
            }

            const result = await response.json();
            // Assigning result directly as it is an array per schema
            topics = result;
        } catch (err: any) {
            error = err.message;
            console.error('Error fetching topics:', err);
        } finally {
            isLoading = false;
        }
    }

    onMount(fetchTopics);

    // 3. REACTIVE LOGIC (Search & Pagination)
    $: filteredTopics = topics.filter(t => 
        t.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        t.description.toLowerCase().includes(searchQuery.toLowerCase())
    );

    $: totalPages = Math.ceil(filteredTopics.length / itemsPerPage);
    $: paginatedTopics = filteredTopics.slice(
        (currentPage - 1) * itemsPerPage, 
        currentPage * itemsPerPage
    );

    $: if (searchQuery) currentPage = 1;

    // 4. MENU LOGIC
    let showMenu = false;
    let selectedTopic = { title: "", id: "" };

    function openMenu(topic: any) {
        selectedTopic = { title: topic.title, id: topic.topic_id };
        showMenu = true;
    }
</script>

<div class="list-controls">
    <div class="search-container">
        <span class="search-label">Filter</span>
        <input 
            type="text" 
            bind:value={searchQuery} 
            placeholder="Search topics..." 
            class="search-input"
            disabled={isLoading}
        />
    </div>
</div>

<div class="editorial-list">
    {#if isLoading}
        <div class="status-message">
            <span class="loading-dots">Gathering the Story of Practice...</span>
        </div>
    {:else if error}
        <div class="status-message error">
            <p>We couldn't load the topics. ({error})</p>
            <button on:click={fetchTopics} class="retry-btn">Retry</button>
        </div>
    {:else}
        {#each paginatedTopics as topic, i}
            <button class="topic-row" on:click={() => openMenu(topic)}>
                <span class="index">0{(currentPage - 1) * itemsPerPage + i + 1}</span>
                <div class="text-group">
                    <span class="topic-name">{topic.title}</span>
                    <span class="description">{topic.description}</span>
                </div>
                <div class="action-line"></div>
            </button>
        {:else}
            <p class="no-results">No topics found matching "{searchQuery}"</p>
        {/each}
    {/if}
</div>

{#if totalPages > 1 && !isLoading}
    <div class="pagination">
        {#each Array(totalPages) as _, i}
            <button 
                class="page-btn" 
                class:active={currentPage === i + 1}
                on:click={() => currentPage = i + 1}
            >
                {i + 1}
            </button>
        {/each}
    </div>
{/if}

{#if showMenu}
    <TopicMenu 
        topic={selectedTopic.title} 
        on:close={() => showMenu = false} 
    />
{/if}

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
        border-top: none; border-left: none; border-right: none;
        cursor: pointer;
    }

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

    .topic-row:hover { padding-left: 2rem; }
    .topic-row:hover::before { transform: scaleY(1); }

    .index {
        font-family: serif;
        font-size: 1.25rem;
        color: #849F5D;
        font-weight: 600;
        opacity: 0.6;
    }

    .text-group { display: flex; flex-direction: column; gap: 0.25rem; }
    .topic-name { font-size: 1.5rem; font-weight: 500; color: #1a1a1a; letter-spacing: -0.01em; }
    .description { font-size: 0.9rem; color: #666; font-weight: 400; }

    .action-line {
        width: 40px;
        height: 1px;
        background: #849F5D;
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.3s ease;
    }
    .topic-row:hover .action-line { transform: scaleX(1); }

    /* --- New Styles for Search & Pagination --- */
    .list-controls {
        max-width: 800px;
        margin: 0 auto 2rem auto;
    }

    .search-container {
        display: flex;
        align-items: center;
        gap: 1rem;
        border-bottom: 1px solid #e5e7eb;
        padding: 0.5rem 0;
    }

    .search-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #849F5D;
        font-weight: 700;
    }

    .search-input {
        border: none;
        background: transparent;
        font-family: inherit;
        font-size: 1rem;
        width: 100%;
        outline: none;
        color: #1a1a1a;
    }

    .pagination {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 3rem;
    }

    .page-btn {
        background: none;
        border: 1px solid #e5e7eb;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-family: serif;
        transition: all 0.2s;
        border-radius: 4px;
    }

    .page-btn.active {
        background: #849F5D;
        color: white;
        border-color: #849F5D;
    }

    .no-results {
        text-align: center;
        padding: 3rem;
        color: #888;
        font-style: italic;
    }

    .status-message {
        text-align: center;
        padding: 4rem;
        font-family: serif;
        font-style: italic;
        color: #888;
    }

    .error { color: #c0392b; }

    .retry-btn {
        margin-top: 1rem;
        background: none;
        border: 1px solid #E6E8E2;
        padding: 0.5rem 1rem;
        font-family: inherit;
        cursor: pointer;
        color: #1a1a1a;
    }

    .retry-btn:hover {
        background: #F4F5F0;
    }

    /* Subtle animation for the loading text */
    .loading-dots {
        display: inline-block;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { opacity: 0.4; }
        50% { opacity: 1; }
        100% { opacity: 0.4; }
    }

    @media (max-width: 768px) {
        .topic-row { grid-template-columns: 40px 1fr; padding: 1.5rem 0; }
        .topic-name { font-size: 1.25rem; }
        .action-line { display: none; }
    }
</style>