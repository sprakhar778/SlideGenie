from src.models.slide_data_models import Slides
from src.prompts.slide_data_prompt import SLIDE_DATA_PROMPT
from src.llm.llm_provider import get_llm
from langchain_core.prompts import PromptTemplate




def get_slides_data_chain(topic: str, content: str):
    """Generate slide data based on the given topic and content."""
    
    llm = get_llm().with_structured_output(Slides)

    slide_prompt = PromptTemplate(
        template=SLIDE_DATA_PROMPT,
        input_variables=["topic", "content"]
    )

    slides_data_chain = slide_prompt | llm

    slides_data = slides_data_chain.invoke(
        {"topic": topic, "content": content}
    )

    slides_data = slides_data.slides

    for s in slides_data:
        print(f"Slide Type: {s.slide_type}")
        print(f"Content: {s.content}")
        print(f"Description: {s.description}")

    # ✅ convert to dict before returning
    return [s.model_dump() for s in slides_data]

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

    slides_data = get_slides_data_chain(topic, content)

#  python -m src.chains.slide_data_chain