<!-- src/routes/+error.svelte -->
<script>
    import { goto } from '$app/navigation';
</script>

<div class="error-page">
    <div class="error-number">404</div>
    <button class="home-link mt-5" on:click={() => goto('/')}>← Go home</button>
</div>

<style>
    .error-page {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background-color: #f9fafb;
        padding: 2rem;
    }
    
    .error-number {
        font-size: 8rem;
        font-weight: 300;
        color: #849F5D;
        line-height: 1;
        margin-bottom: 2rem;
        letter-spacing: -2px;
    }
    
    .home-link {
        color: #849F5D;
        font-size: 1.125rem;
        text-decoration: underline;
        cursor: pointer;
        transition: opacity 0.2s ease;
    }
    
    .home-link:hover {
        opacity: 0.7;
    }
</style>