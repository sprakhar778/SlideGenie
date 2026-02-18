import os
from src.chains.slide_generator_chain import stream_slide_generator_chain


import asyncio

import asyncio

async def generate_slides_node(state):
    topic = state["topic"]
    theme = state["theme_info"]
    slides_data = state["slides_data"]

    queue = asyncio.Queue()

    async def stream_single_slide(index, slide_data):
        async for token in stream_slide_generator_chain(
            topic, theme, slide_data
        ):
            await queue.put(
                {
                    "slide_index": index,
                    "token": token,
                }
            )
        await queue.put({"slide_index": index, "done": True})

    tasks = [
        asyncio.create_task(stream_single_slide(i, slide))
        for i, slide in enumerate(slides_data)
    ]

    async def stream_results():
        finished = 0
        total = len(tasks)

        while finished < total:
            item = await queue.get()

            if "done" in item:
                finished += 1
            else:
                yield item  # STREAM TO CLIENT HERE

    return stream_results()
