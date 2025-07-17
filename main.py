from config import *
from rulekeeper import load_rulebook, split_into_sections, build_vectorstore, predict_relevant_sections
from agent import create_agent
from tools import characters, character_name

def game_loop():
    text = load_rulebook()
    section_chunks, _ = split_into_sections(text)
    vectorstore = build_vectorstore(section_chunks)
    agent = create_agent()

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print(r"""
        
                                    
          ░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░  ░▒▓███████▓▒░ 
              ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░        
              ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░        
              ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  ░▒▓███████▓▒░ ░▒▓███████▓▒░  ░▒▓██████▓▒░  
              ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░              ░▒▓█▓▒░ 
              ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░              ░▒▓█▓▒░ 
              ░▒▓█▓▒░     ░▒▓█████████████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░  
          
        """)

    print(r"""
         ===========================================
                TWERPS — The World's Easiest 
                Role-Playing System™
        ===========================================

        This is a "Hello World" demo to showcase
        retrieval-augmented generation (RAG) and function calling using LangChain
        and the TWERPS game system as a test.

        1. In TWERPS, you’ve got one stat: Strength. That’s it. Easy, huh?
        2. To create a character, we’ll roll a 10-sided die and figure out how tough you are.
        3. You can move, fight, or do something clever but just once per turn!
        4. Combat's simple: roll high, hit hard, hope you don’t pass out.
        5. Pick up cool stuff along the way daggers, apples, maybe even armor.
        6. Find the tresure, outwit sharks, and have some laughs doing it.
        7. Type "exit" to exit.      """)
    
    history = []

    response = agent.invoke({
        "input": r"""
        Ask the player to create a charachter by asking for a name and a description.       
"""
    })

    print("\n")
    print("=> DM:", response["output"])
    history.append({"role": "DM", "content": response["output"]})

    while True:
        user_input = input("=> You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("DM: Thanks for playing!")
            break

        history.append({"role": "Player", "content": user_input})
        rules_context = "\n\n".join(predict_relevant_sections(vectorstore, user_input))
        conversation = "\n".join(f"{e['role']}: {e['content']}" for e in history)

        char_display = characters[character_name] if character_name in characters else "STLL_NO"

        input_data = {
            "input": f"""
                Conversation History:
                {conversation}

                Rules Context (for this turn only):
                {rules_context}

                Current Character:
                {char_display}

                User Input:
                {user_input}
                """
        }

        response = agent.invoke(input_data)
        print("\n")
        print("=> DM:", response["output"])
        history.append({"role": "DM", "content": response["output"]})

if __name__ == "__main__":
    game_loop()
