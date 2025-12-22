<script lang='ts'>
    function handleEcho() {
        const echoMessage = { message: "hi" };

        fetch('http://localhost:8000//users/echo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(echoMessage)
        })
            .then(response => response.json())
            .then(result => console.log(result));
    }
</script>

<button on:click={handleEcho} type='button' class="btn"> Click me </button>

<style>
    .btn {
        background: #849F5D;
        color: white;
        padding: 1rem 2rem;
        cursor: pointer;
        border-radius: 20px;
    }
</style>