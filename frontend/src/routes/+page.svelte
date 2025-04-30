<script lang="ts">
	import { onMount } from 'svelte';

	let memoData = $state<{ title: string; content: string }[]>([]);
	let page = $state(1);

	let title = $state('');
	let content = $state('');
	let createSuccess = $state(false);

	onMount(() => {
		fetchMemoData();
	});
	$effect(() => {
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

	async function createMemo() {
		try {
			const response = await fetch('/api/memoData', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ title, content })
			});

			if (!response.ok) throw new Error('失敗しました');

			createSuccess = true;
			title = '';
			content = '';
		} catch (e) {
			console.error(e, 'エラーが発生しました');
		}
	}
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
<form onsubmit={createMemo} class="">
	<input
		type="string"
		bind:value={title}
		placeholder="メモのタイトル"
		required
		class="border px-2 py-1"
	/>
	<textarea bind:value={content} placeholder="本文" class="border px-2 py-1"></textarea>

	<button type="submit">投稿</button>
</form>

<button onclick={() => (page = page - 1)} disabled={page === 1}>← 前へ</button>
{#if memoData.length === 6}
	<button onclick={() => (page = page + 1)}>次へ →</button>
{/if}
