import asyncio
from prisma import Prisma

async def main():
    prisma = Prisma()
    await prisma.connect()

    # すでにデータがあったら一旦全部消してもいい（テスト用なら）
    await prisma.memo.delete_many()

    # 12件登録
    for i in range(1, 13):
        await prisma.memo.create(
            data={
                "title": f"メモ {i}",
                "content": f"メモの内容 {i}",
            }
        )

    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(main())