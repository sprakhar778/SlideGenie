import asyncio
from src.chains.slides_data_chain import get_slides_data_chain

def generate_slides_data_node(state):
    """Node to generate slide data for each slide based on the presentation state."""
    topic = state.get("topic")
    content=state.get("content")
   
    if not topic:
        raise ValueError("The 'topic' must be provided in the state.")
    if not content:
        raise ValueError("The 'content' must be provided in the state.")
    
    # Generate slides data using the chain
    generated_slides_data =  get_slides_data_chain(topic=topic, content=content)
    
    
    # Update the state with the generated slides data

    state["slides_data"] = generated_slides_data
    return state

if __name__ == "__main__":
    # Example state for testing
    state = {
        "topic": "Sustainable Energy Solutions",
        "content": "A presentation about various sustainable energy solutions and their benefits."
    }

    updated_state = generate_slides_data_node(state)
    print(updated_state["slides_data"])

#python -m src.graph.nodes.slides_data_node