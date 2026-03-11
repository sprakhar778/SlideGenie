from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.prompts.edit_slide_prompt import EDIT_SLIDE_PROMPT
from src.llm.llm_provider import get_llm

async def stream_edit_slide_code_chain(slide_code: str, user_input: str):
    """
    Streams the regenerated slide HTML code based on the user's edit request.
    """
    llm = get_llm(streaming=True)

    prompt = PromptTemplate(
        template=EDIT_SLIDE_PROMPT,
        input_variables=["slide_code", "user_input"],
    )

    chain = prompt | llm | StrOutputParser()

    async for chunk in chain.astream({
        "slide_code": slide_code,
        "user_input": user_input,
    }):
        yield chunk
