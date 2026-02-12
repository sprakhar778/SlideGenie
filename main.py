from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from prompts.extra.designer_prompt import DESIGNER_PROMPT
from src.prompts.slide_design_prompt import SLIDE_DESIGN_PROMPT 
import re
load_dotenv()

# model = ChatOpenAI(
#     model="gpt-4",
#     temperature=0.9
# )
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini chat model
model = ChatGoogleGenerativeAI(model="gemini-3-pro-preview", temperature=0.3)


# # -------- Chain 1: topic → manifesto --------
# designer_prompt = PromptTemplate(
#     template=DESIGNER_PROMPT,
#     input_variables=["topic"]
# )

# designer_chain = designer_prompt | model | StrOutputParser()

# res=designer_chain.invoke({
#     "topic": "Future of AI in Healthcare"
# })

# print("✅ Design Manifesto Generated:\n")
# print(res)
def clean_html_output(text: str) -> str:
    # This regex removes ```html at the start and ``` at the end
    cleaned = re.sub(r'^```html\s*|^```\s*', '', text, flags=re.MULTILINE)
    cleaned = re.sub(r'```\s*$', '', cleaned, flags=re.MULTILINE)
    return cleaned.strip()

# -------- Chain 2: topic + manifesto + content → HTML --------
slide_prompt = PromptTemplate(
    template=SLIDE_DESIGN_PROMPT,
    input_variables=[
        "topic", 
        "content", 

        "slide_type", 
        "heading_font", 
        "palette", 
        "body_font"
    ]
)

agent = slide_prompt | model | StrOutputParser() | RunnableLambda(clean_html_output)

# -------- Run --------
# result = agent.invoke({
#     "topic": "Future of AI in Healthcare",
#     "content": """
#     - AI-powered diagnostics
#     - Predictive patient risk models
#     - Personalized medicine
#     - Hospital workflow automation
#     """
# })
# Updated topic: Sustainable Energy Transition


# 1. Fix the template by pre-filling the design variables
slide_prompt_fixed = slide_prompt.partial(
    
    slide_type="Process Flow",
    heading_font="Arial Bold",
    body_font="Calibri",
    palette="Corporate Blue/Grey"
)

# 2. Now the invoke only needs the variables that AREN'T partialed
result = agent.invoke({
    "topic": "The Evolution of Artificial Intelligence",
    "content": """
1. Foundation: Early Rule-Based Systems
Defined by explicit programming and rigid logic, these initial systems operated on pre-defined 'if-then' rules to solve specific, structured problems.

2. Progression: The Evolutionary Shift
Tracing the development of intelligence involved moving away from static instructions toward dynamic adaptation.

3. Current State: Modern Deep Learning Models
Today's AI utilizes multi-layered neural networks to process vast amounts of unstructured information.
    """,
    # These must match the names in your PromptTemplate exactly
    "components": "Numbered list with process arrows",
    "slide_type": "Process/Timeline",
    "heading_font": "Arial Bold",
    "body_font": "Calibri",
    "palette": "Corporate Blue and White"
})
# result = agent.invoke({
#     "topic": "Renewable Energy Infrastructure 2030",
#     "content": """
#     Post-Quantum Cryptography and Zero Trust represent a foundational shift in how organizations secure systems against future quantum-enabled threats and today’s highly adaptive attackers. As quantum computing threatens traditional public-key cryptography, lattice-based algorithms and quantum-safe key exchanges are emerging to protect data longevity. At the same time, Zero Trust replaces perimeter-based security with continuous verification, assuming no implicit trust across users, devices, or workloads. When combined with AI-driven threat detection, automated response mechanisms, and hardware-rooted trust, this approach enables resilient, adaptive security architectures designed for cloud-native, distributed, and adversarial environments.

# Key Points:
# • Lattice-based encryption standards to replace quantum-vulnerable RSA/ECC  
# • Quantum Key Distribution (QKD) for theoretically secure key exchange  
# • Real-time AI threat hunting for continuous anomaly detection  
# • Biometric blockchain authentication for decentralized identity trust  
# • Automated incident response loops to reduce mean-time-to-contain  
# • Cloud-native micro-segmentation enforcing Zero Trust principles  
# • Hardware-level security modules (HSMs/TPMs) for root-of-trust enforcement  

#     """
# })



# -------- Save HTML --------
with open("slides.html", "w", encoding="utf-8") as f:
    f.write(result)

print("✅ slides.html generated successfully")
