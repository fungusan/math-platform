<script lang="ts">
    import NavBar from '../../lib/components/shared/NavBar.svelte';
    import Footer from '../../lib/components/shared/Footer.svelte';
    import UserInfo from '../../lib/components/users/UserInfo.svelte';
    import Stat from '../../lib/components/users/Stat.svelte';

    // Mock Data
    const userData = {
        name: "Fungusan",
        id: "DSE-MATH-2025",
        streak: 14
    };

    const historyData = [
        { topic: "Number and Algebra", rate: 85, date: "18 Dec 2025", wrongQids: [102, 105] },
        { topic: "Measures, Shape and Space", rate: 60, date: "17 Dec 2025", wrongQids: [204, 208, 211, 215] },
        { topic: "Data Handling", rate: 100, date: "16 Dec 2025", wrongQids: [] }
    ];
</script>

<NavBar activePage="statistics" />

<main class="stats-container">
    <UserInfo 
        userName={userData.name} 
        userId={userData.id} 
        streak={userData.streak} 
    />

    <Stat records={historyData} />
</main>

<Footer />

<style>
    .stats-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 6rem 2rem;
        min-height: 80vh;
    }
</style>