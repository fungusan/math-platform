<script>
    export let activePage = 'home';
    function handleLogout() { /* Logic */ }
</script>

<nav class="nav-container">
    <div class="nav-inner">
        <div class="brand">
            <span class="brand-dot"></span>
            <h1 class="brand-name">Fungusan</h1>
        </div>
      
        <div class="menu">
            <a href="/" class:active={activePage === 'home'}>Home</a>
            <a href="/about" class:active={activePage === 'about'}>About</a>
            <a href="/statistics" class:active={activePage === 'statistics'}>Statistics</a>
            
            <div class="v-divider"></div>
            
            <button class="logout-btn" on:click={handleLogout}>
                Logout <span class="arrow">→</span>
            </button>
        </div>
    </div>
</nav>

<style>
    .nav-container {
        width: 100%;
        padding: 2rem 0;
        background: transparent; /* Cleaner than the grey bar */
    }
    
    .nav-inner {
        max-width: 1100px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .brand-dot {
        width: 12px;
        height: 12px;
        background-color: #849F5D;
        border-radius: 2px; /* Matches the "blocky" feel of your Figma sidebars */
    }

    .brand-name {
        font-family: serif;
        font-size: 1.5rem;
        font-weight: 500;
        letter-spacing: -0.02em;
        color: #1a1a1a;
    }
    
    .menu {
        display: flex;
        align-items: center;
        gap: 2rem;
    }
    
    .menu a {
        text-decoration: none;
        color: #666;
        font-size: 0.95rem;
        font-weight: 400;
        transition: color 0.2s;
        position: relative;
    }
    
    .menu a:hover, .menu a.active {
        color: #849F5D;
    }

    /* Subtle underline for active page instead of bolding */
    .menu a.active::after {
        content: "";
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 100%;
        height: 1px;
        background-color: #849F5D;
    }

    .v-divider {
        width: 1px;
        height: 20px;
        background: #e5e7eb;
    }
    
    .logout-btn {
        background: transparent;
        color: #999;
        border: 1px solid #e5e7eb;
        padding: 0.4rem 1rem;
        border-radius: 100px;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s;
    }

    .logout-btn:hover {
        border-color: #849F5D;
        color: #849F5D;
    }
</style>