from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.prompts.edit_slide_prompt import EDIT_SLIDE_PROMPT
from src.llm.llm_provider import get_llm

async def stream_edit_slide_code_chain(theme: str,slide_layout: str,slide_code: str, user_input: str,slide_content: str):
    """
    Streams the regenerated slide HTML code based on the user's edit request.
    """
    llm = get_llm(streaming=True)

    prompt = PromptTemplate(
        template=EDIT_SLIDE_PROMPT,
        input_variables=["theme", "slide_layout", "slide_code", "user_input","slide_content"],
    )

    chain = prompt | llm | StrOutputParser()

    async for chunk in chain.astream({
        "slide_code": slide_code,
        "user_input": user_input,
        "slide_layout": slide_layout,
        "theme": theme,
        "slide_content": slide_content,
    }):
        yield chunk
