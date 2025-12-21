<script lang="ts">
    import NavBar from '../../lib/components/shared/NavBar.svelte';
    import Footer from '../../lib/components/shared/Footer.svelte';
</script>

<NavBar activePage="login" />

<main class="auth-container">
    <div class="auth-grid">
        <section class="form-section">
            <header class="form-header">
                <span class="label">Step 01</span>
                <h1 class="serif-title">Welcome Back</h1>
                <p class="subtitle">Continue your story of mathematical discovery.</p>
            </header>

            <form on:submit|preventDefault>
                <div class="input-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" placeholder="e.g. name@email.com" />
                </div>

                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" />
                </div>

                <button type="submit" class="auth-btn">Sign In <span class="arrow">→</span></button>
            </form>

            <p class="switch-auth">
                New here? <a href="/register">Create an account</a>
            </p>
        </section>

        <section class="visual-sidebar">
            <div class="green-block">
                <div class="block-text">
                    <span class="quote">"Mathematics is the key to the universe."</span>
                </div>
            </div>
        </section>
    </div>
</main>

<Footer />

<style>
    .auth-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 4rem 2rem;
        min-height: 70vh;
        display: flex;
        align-items: center;
    }

    .auth-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6rem;
        width: 100%;
        align-items: center;
    }

    .label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #849F5D;
        font-weight: 700;
        display: block;
        margin-bottom: 0.5rem;
    }

    .serif-title {
        font-family: serif;
        font-size: 3rem;
        margin: 0 0 1rem 0;
        font-weight: 400;
    }

    .subtitle {
        color: #666;
        margin-bottom: 3rem;
    }

    /* Form Styling */
    .input-group {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }

    .input-group label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #888;
    }

    .input-group input {
        border: none;
        border-bottom: 1px solid #E6E8E2;
        background: transparent;
        padding: 0.75rem 0;
        font-size: 1rem;
        font-family: inherit;
        transition: border-color 0.2s;
    }

    .input-group input:focus {
        outline: none;
        border-bottom-color: #849F5D;
    }

    .auth-btn {
        margin-top: 2rem;
        background: #849F5D;
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 100px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 1rem;
        width: fit-content;
    }

    .switch-auth {
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #888;
    }

    .switch-auth a {
        color: #849F5D;
        text-decoration: none;
        font-weight: 600;
    }

    /* Visual Sidebar */
    .visual-sidebar {
        height: 100%;
        display: flex;
        justify-content: flex-end;
    }

    .green-block {
        width: 100%;
        height: 500px;
        background-color: #849F5D;
        border-radius: 40px;
        display: flex;
        align-items: center;
        padding: 3rem;
        position: relative;
    }

    .block-text {
        color: rgba(255, 255, 255, 0.9);
        font-family: serif;
        font-size: 2rem;
        line-height: 1.2;
    }

    @media (max-width: 850px) {
        .auth-grid { grid-template-columns: 1fr; }
        .visual-sidebar { display: none; }
    }
</style>