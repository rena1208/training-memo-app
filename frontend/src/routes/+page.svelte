<script lang="ts">
	import { onMount } from 'svelte';

	let memoData = $state<{ title: string; content: string }[]>([]);
	let page = $state(1);

	async function fetchData() {
		console.log('おした');
		try {
			const response = await fetch(`/api`);
			if (response.ok) {
				console.log(`/api`);
				const data = await response.json();
				console.log(data);
			}
		} catch (e) {
			console.error('Failed to fetch data:', e);
		}
	}

	onMount(() => {
		fetchMemoData();
	});

	const fetchMemoData = async () => {
		try {
			const response = await fetch(`/api/memoData?page=${page}`);
			if (response.ok) {
				const data = await response.json();
				memoData = data;
			} else {
				console.error('Failed to fetch memo data:', response.statusText);
			}
		} catch (error) {
			console.error('Error fetching memo data:', error);
		}
	};

	$effect(() => {
		fetchMemoData();
	});
</script>

<!-- <button on:click={fetchData}>Fetch Data</button> -->

<!-- メモ一覧を表示 -->
<div class="grid grid-cols-3 gap-4">
	{#each memoData as memo}
		<div class="flex-col">
			<h2>{memo.title}</h2>
			<p>{memo.content}</p>
		</div>
	{/each}
</div>

<!-- メモ投稿フォーム -->

<button onclick={() => (page = page - 1)} disabled={page === 1}>← 前へ</button>
{#if memoData.length === 6}
<button onclick={() => (page = page + 1)}>次へ →</button>
{/if}
