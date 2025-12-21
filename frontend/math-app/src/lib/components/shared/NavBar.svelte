<script lang="ts">
    import { fade, fly } from 'svelte/transition';
    export let activePage = 'home';
    
    let mobileMenuOpen = false;

    function toggleMenu() {
        mobileMenuOpen = !mobileMenuOpen;
    }

    function handleLogout() { /* Logic */ }
</script>

<nav class="nav-container">
    <div class="nav-inner">
        <div class="brand">
            <span class="brand-dot"></span>
            <h1 class="brand-name">Fungusan</h1>
        </div>
      
        <div class="menu desktop-only">
            <a href="/" class:active={activePage === 'home'}>Home</a>
            <a href="/about" class:active={activePage === 'about'}>About</a>
            <a href="/statistics" class:active={activePage === 'statistics'}>Statistics</a>
            
            <div class="v-divider"></div>
            
            <button class="logout-btn" on:click={handleLogout}>
                Logout <span class="arrow">→</span>
            </button>
        </div>

        <button class="mobile-toggle" on:click={toggleMenu} aria-label="Toggle Menu">
            <div class="hamburger-box">
                <span class="line" class:open-top={mobileMenuOpen}></span>
                <span class="line" class:open-bottom={mobileMenuOpen}></span>
            </div>
        </button>
    </div>

    {#if mobileMenuOpen}
        <div class="mobile-overlay" transition:fade={{ duration: 200 }}>
            <div class="mobile-menu-content" transition:fly={{ y: -20, duration: 400 }}>
                <div class="mobile-links">
                    <a href="/" on:click={toggleMenu} class:active={activePage === 'home'}>Home</a>
                    <a href="/about" on:click={toggleMenu} class:active={activePage === 'about'}>About</a>
                    <a href="/statistics" on:click={toggleMenu} class:active={activePage === 'statistics'}>Statistics</a>
                </div>
                
                <div class="mobile-footer">
                    <button class="logout-btn-large" on:click={handleLogout}>
                        Logout <span class="arrow">→</span>
                    </button>
                </div>
            </div>
        </div>
    {/if}
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

    .desktop-only { display: flex; }
    .mobile-toggle { display: none; }

    @media (max-width: 768px) {
        .desktop-only { display: none; }
        
        .mobile-toggle {
            display: block;
            background: none;
            border: none;
            cursor: pointer;
            z-index: 2000;
            padding: 0.5rem;
        }

        .hamburger-box {
            width: 24px;
            height: 14px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .line {
            width: 100%;
            height: 2px;
            background: #1a1a1a;
            transition: all 0.3s ease;
        }

        /* Animation for hamburger to X */
        .open-top { transform: translateY(6px) rotate(45deg); }
        .open-bottom { transform: translateY(-6px) rotate(-45deg); }

        .mobile-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: #FDFCF8;
            z-index: 1000;
            padding-top: 80px;
        }

        .mobile-links {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2.5rem;
            margin-top: 4rem;
        }

        .mobile-links a {
            font-family: serif;
            font-size: 1.5rem;
            text-decoration: none;
            color: #1a1a1a;
        }

        .mobile-links a.active {
            color: #849F5D;
        }

        .mobile-footer {
            margin-top: 5rem;
            display: flex;
            justify-content: center;
        }

        .logout-btn-large {
            background: transparent;
            border: 1px solid #E6E8E2;
            padding: 1rem 3rem;
            border-radius: 100px;
            font-family: serif;
            font-size: 1rem;
            color: #888;
        }
    }
</style>