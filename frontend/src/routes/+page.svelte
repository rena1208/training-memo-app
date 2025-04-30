<script lang="ts">
	import { onMount } from 'svelte';

	let memoData = $state<{ id: number; title: string; content: string }[]>([]);
	let page = $state(1);

	let title = $state('');
	let content = $state('');
	// TODO: フラッシュメッセージ
	// let createSuccess = $state(false);

	// 編集中のメモの内容
	let editMode = $state(false);
	let editMemoId = $state<number | null>(null);
	let editMemoTitle = $state('');
	let editMemoContent = $state('');

	onMount(() => {
		fetchMemoData();
	});
	$effect(() => {
		fetchMemoData();
	});

	const fetchMemoData = async () => {
		try {
			const response = await fetch(`/api/memo-data?page=${page}`);
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
			const response = await fetch('/api/memo-data', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ title, content })
			});

			if (!response.ok) throw new Error('失敗しました');

			// createSuccess = true;
			title = '';
			content = '';
			await fetchMemoData();
		} catch (e) {
			console.error(e, 'エラーが発生しました');
		}
	}

	// 投稿フォームを編集モードに切り替える
	const startEditingMemo = (id: number) => {
		const memo = memoData.find((memo) => memo.id === id);
		if (!memo) return;
		editMode = true;
		editMemoId = id;
		editMemoTitle = memo.title;
		editMemoContent = memo.content;
	};

	// 編集したメモを送信する
	const submitUpdateMemo = async (event: Event) => {
		event.preventDefault(); // リロードしないように
		if (editMemoId === null) return;

		try {
			console.log(editMemoId);
			const response = await fetch(`/api/memo-data/${editMemoId}`, {
				method: 'PATCH',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ title: editMemoTitle, content: editMemoContent })
			});

			if (!response.ok) throw new Error('更新に失敗しました');

			// フォームのリセット
			editMode = false;
			editMemoId = null;
			editMemoTitle = '';
			editMemoContent = '';

			await fetchMemoData();
		} catch (e) {
			console.error(e, 'エラーが発生しました');
		}
	};

	// メモの削除
	const deleteMemo = async (id: number) => {
		if (!confirm('本当に削除しますか？')) return;
		try {
			const response = await fetch(`/api/memo-data/${id}`, {
				method: 'DELETE'
			});
			if (!response.ok) {
				throw new Error('削除に失敗しました');
			}

			await fetchMemoData();
		} catch (e) {
			console.error(e, 'エラーが発生しました');
		}
	};
</script>

<!-- メモ一覧を表示 -->
<h1>メモ一覧</h1>
<div class="grid grid-cols-3 gap-4">
	{#each memoData as memo}
		<div class="flex-col">
			<h2>{memo.title}</h2>
			<p>{memo.content}</p>
			<button class="" onclick={() => startEditingMemo(memo.id)}>編集</button>
			<button class="" onclick={() => deleteMemo(memo.id)}>削除</button>
		</div>
	{/each}
</div>

<!-- メモ投稿フォーム -->
<h1>メモの追加</h1>
{#if editMode}
	<form onsubmit={submitUpdateMemo} class="">
		<input type="string" bind:value={editMemoTitle} required class="border px-2 py-1" />
		<textarea bind:value={editMemoContent} class="border px-2 py-1"></textarea>

		<button type="submit">投稿</button>
	</form>
{:else}
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
{/if}
<button onclick={() => (page = page - 1)} disabled={page === 1}>← 前へ</button>
{#if memoData.length === 6}
	<button onclick={() => (page = page + 1)}>次へ →</button>
{/if}
