<script>
	async function fetchData() {
		console.log('おした');
		// const url = 'http://127.0.0.1:8000/api'; // FastAPI エンドポイント
		try {
			const response = await fetch(`/api`);
			if (response.ok) {
				console.log(`/api`);
				// throw new Error(`HTTP error! status: ${response.status}`);
				const data = await response.json();
				console.log(data);
			}
		} catch (e) {
			console.error('Failed to fetch data:', e);
		}
	}
</script>
<button on:click={fetchData}>Fetch Data</button>