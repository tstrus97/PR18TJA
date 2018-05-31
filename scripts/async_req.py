import asyncio
from aiohttp import ClientSession


def async_request(urls):
    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.read()


    async def bound_fetch(sem, url, session):
        # Getter function with semaphore.
        async with sem:
           return await fetch(url, session)   


    async def run(urls):
        tasks = []
        # Fetch all responses within one Client session,
        # keep connection alive for all requests.
        sem = asyncio.Semaphore(500)
        async with ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(bound_fetch(sem, url, session))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            # you now have all response bodies in this variable
            #print(responses[0])
            return responses

    def print_responses(result):
        print(result)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(urls))
    responses = loop.run_until_complete(future)
    return responses