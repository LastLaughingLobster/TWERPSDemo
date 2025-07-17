import random
import re
from langchain_core.tools import Tool
from character import Character

# Global character state
characters = {}
character_name = ""

# ANSI green color code
def green(msg): return f"\033[92m{msg}\033[0m"

def roll_dice(input_string: str = "1d10") -> str:
    print(green(f"[TOOL CALLED] roll_dice('{input_string}')"))
    match = re.match(r"(?i)(\d*)d(\d+)", input_string.strip())
    if not match:
        return "Invalid format. Use 'NdM' (e.g., '2d20', 'd6')."
    num_dice = int(match.group(1)) if match.group(1) else 1
    num_sides = int(match.group(2))
    if num_dice < 1 or num_sides < 2:
        return "Invalid dice. Dice must be >= 1 and sides >= 2."
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return f"Rolling {input_string}: Rolls: {rolls}, Total: {sum(rolls)}"

def create_character_with_state(player_id: str = "Player") -> str:
    global character_name
    print(green(f"[TOOL CALLED] create_character('{player_id}')"))

    if player_id in characters:
        return f"A character already exists:\n{characters[player_id]}"

    result = roll_dice("1d10")
    match = re.search(r"Total:\s*(\d+)", result)
    if not match:
        return "Failed to roll dice for character creation."

    roll = int(match.group(1))
    strength = {1: 3, 2: 4, 3: 4, 4: 5, 5: 5, 6: 5, 7: 5, 8: 6, 9: 6, 10: 7}.get(roll, 3)

    new_char = Character(strength=strength, name=player_id)
    characters[player_id] = new_char
    character_name = player_id

    return f"Character created for {player_id} (Roll={roll}):\n{new_char}"

def give_items(items: str) -> str:
    global character_name
    print(green(f"[TOOL CALLED] give_items('{items}')"))
    character = characters[character_name]
    character.add_item(items)
    return f"Added item to {character_name}: {items}"

# LangChain tool definitions
roll_dice_tool = Tool(
    name="roll_dice",
    func=roll_dice,
    description="Roll dice when an rpg action is required by the user. Only d10 (e.g., '1d10', '1d10')."
)

create_character_tool = Tool(
    name="create_character",
    func=create_character_with_state,
    description="Create a character only if the player gives a name in the context of creating a charachter."
)

give_items_tool = Tool(
    name="give_items",
    func=give_items,
    description="Give an item to the current character. Format: 'Bow, Range=7, Damage=2'."
)
