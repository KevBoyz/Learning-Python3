from httpx import AsyncClient
import asyncio as a


base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def sub_generator(number):
    print(number)
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number), timeout=None
        )
        print(number)
        return number, response.json()['name']


async def coro():
    print('s')
    res = await a.gather(*[sub_generator(n) for n in range(1, 10)])
    print('e')
    return res



print(a.run(coro()))
