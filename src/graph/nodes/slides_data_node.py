import asyncio
from src.chains.slide_generator_chain import stream_slide_generator_chain

async def generate_slides_data_node(state):
    topic = state["topic"]
    theme = state["theme_info"]

    slides_data = state.get("slides_data", [])

    # --- TEST MODE: Only generate first slide safely ---
    if slides_data:
        slides_data = [slides_data[0]]

    queue = asyncio.Queue()

    async def stream_single_slide(index, slide_data):
        try:
            async for token in stream_slide_generator_chain(
                topic, theme, slide_data
            ):
                await queue.put({
                    "slide_index": index,
                    "token": token,
                })
        except Exception as e:
            await queue.put({
                "slide_index": index,
                "error": str(e)
            })
        finally:
            await queue.put({
                "slide_index": index,
                "done": True
            })

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

            yield item

    return stream_results()