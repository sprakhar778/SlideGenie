from src.prompts.slide_types_prompt import SLIDE_TYPES_PROMPT
from src.models.slide_types import Slides_Types
from src.llm.llm_provider import get_llm
from langchain_core.prompts import PromptTemplate
from src.llm.llm_provider import get_llm



def get_slide_types_chain(topic: str, content: str):
    """Generate slide types based on the given topic and content."""
    
    # Initialize LLM with structured output
    llm = get_llm().with_structured_output(Slides_Types)

    # Build prompt
    slide_types_prompt = PromptTemplate(
        template=SLIDE_TYPES_PROMPT,
        input_variables=["topic", "content"]
    )

    # Create chain
    slide_types_chain = slide_types_prompt | llm

    # Invoke chain
    slide_types = slide_types_chain.invoke(
        {"topic": topic, "content": content}
    )
    
    print("Generated Slide Types:")
    for s in slide_types.slide_types:
        print(f"Slide Type: {s.slide_type}")
        print(f"Description: {s.description}\n")
    return slide_types.slide_types

if __name__ == "__main__":
    topic = "The Future of Artificial Intelligence"
    content = (
        "This presentation explores the future of artificial intelligence (AI) and its potential impact on various industries and society as a whole. "
        "We begin by examining the evolution of AI, from rule-based systems to modern deep learning models, highlighting key breakthroughs that have shaped today's AI landscape.\n\n"

        "We will discuss emerging trends in AI research, including advancements in machine learning, generative AI, reinforcement learning, natural language processing, and computer vision. "
        "Special attention will be given to foundation models, multimodal systems, autonomous agents, and real-time decision-making systems.\n\n"

        "The presentation will analyze AI’s impact across industries such as healthcare, finance, education, transportation, cybersecurity, manufacturing, and entertainment. "
        "Examples include AI-assisted medical diagnosis, predictive analytics in finance, personalized learning systems, autonomous vehicles, fraud detection, smart factories, and AI-generated content.\n\n"

        "We will also explore the integration of AI with other transformative technologies such as robotics, the Internet of Things (IoT), blockchain, edge computing, and quantum computing, "
        "and how these combinations may accelerate innovation.\n\n"

        "Ethical and societal considerations will be a central focus. Topics include algorithmic bias, fairness, transparency, explainability, privacy concerns, data security, misinformation, deepfakes, and workforce displacement. "
        "We will examine the importance of responsible AI governance, regulatory frameworks, and international collaboration.\n\n"

        "Additionally, we will discuss the future of human-AI collaboration, including augmented intelligence, AI copilots, decision-support systems, and the changing nature of work. "
        "We will consider how education and skill development must evolve to prepare for an AI-driven world.\n\n"

        "Finally, we will look ahead to long-term possibilities such as artificial general intelligence (AGI), superintelligence, and AI alignment challenges. "
        "The presentation concludes by reflecting on how AI can be harnessed responsibly for positive societal impact, sustainability, scientific discovery, and global problem-solving."
    )

    slides_data = get_slide_types_chain(topic, content)
