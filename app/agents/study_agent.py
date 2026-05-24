from llama_index.core.agent.workflow import (
    FunctionAgent
)

from app.core.llm import get_llm

from app.agents.prompts import (
    SYSTEM_PROMPT
)

from app.rag.tools import (
    build_search_tool
)


def create_agent(index):

    llm = get_llm()

    search_tool = build_search_tool(index)

    agent = FunctionAgent(
        tools=[search_tool],
        llm=llm,
        system_prompt=SYSTEM_PROMPT
    )

    return agent