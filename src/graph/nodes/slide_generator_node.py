import os
from src.chains.slide_generator_chain import stream_slide_generator_chain


import asyncio



async def generate_slides_node(state):
    topic = state["topic"]
    theme = state["theme_info"]
    # FIX: Assuming slides_data is a list of slide dicts based on your JSON
    slides_data = state.get("slides_data", [])
    slides_data =[slides_data[0], slides_data[1]]  # --- TEST MODE: Only generate first slide safely ---

    queue = asyncio.Queue()
    sem = asyncio.Semaphore(2)  # Max 2 concurrent LLM calls to avoid rate limits

    async def stream_single_slide(index, slide_data):
        async with sem:
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

    finished = 0
    total = len(tasks)

    try:
        while finished < total:
            item = await queue.get()

            if "done" in item:
                finished += 1
                yield item
            else:
                yield item
    finally:
        await asyncio.gather(*tasks, return_exceptions=True)


# if __name__ == "__main__":
#     # Example state for testing
#     state = {
#         "topic": "Sustainable Energy Solutions",
#         "theme_info": "A modern, clean design with green and blue accents to reflect the sustainability theme.",
#         "slides_data": [
#             {
#                 "slide_type": "Title Slide",
#                 "content": "Introduction to Sustainable Energy Solutions",
#                 "layout": "Title and Subtitle"
#             },
#             {
#                 "slide_type": "Content Slide",
#                 "content": "Overview of different sustainable energy solutions including solar, wind, and hydro power.",
#                 "layout": "Title and Bullet Points"
#             }
#         ]
#     }

#     async def test_generate_slides():
#         async for item in generate_slides_node(state):
#             print(item)

#     asyncio.run(test_generate_slides())

# python -m src.graph.nodes.slide_generator_node

