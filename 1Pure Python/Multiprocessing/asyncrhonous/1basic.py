import asyncio as a


async def bilega():
    print('n1')
    await a.sleep(1)
    print('n2')
    return 'nega'


async def leibe():
    print('biru')
    return 'biru'



async def dele():
    print('start')
    task1 = a.create_task(bilega())
    task2 = a.create_task(leibe())
    b = await task1
    c = await task2
    print('finish')
    return (b, c)


a.run(dele())

