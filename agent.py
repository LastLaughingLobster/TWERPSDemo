from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from tools import roll_dice_tool, create_character_tool, give_items_tool
from prompts import base_system_prompt

def create_agent():
    llm = ChatOpenAI(
        model_name='gpt-4o',  # More powerful model
        temperature=0.7
    )
    memory = ConversationBufferMemory(return_messages=True)

    # Wrap the system prompt into a `ChatPromptValue`
    system_prompt_value = base_system_prompt.format_messages()

    return initialize_agent(
        tools=[roll_dice_tool, create_character_tool, give_items_tool],
        llm=llm,
        agent="openai-functions",
        memory=memory,
        verbose=False,
        system_message=system_prompt_value[0]  # This is key!
    )
