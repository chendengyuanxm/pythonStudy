import asyncio


async def download(url):
    for i in range(100):
        print('download%s %s' % (url, i))


async def create_task():
    tasks = []
    for i in range(5):
        tasks.append(download(' %s' % i))
    await asyncio.wait(tasks)


def main():
    asyncio.run(create_task())


if __name__ == '__main__':
    main()