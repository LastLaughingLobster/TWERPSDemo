class Character:
    def __init__(self, strength: int, name: str = "Brave adventurer"):
        self.strength = strength
        self.current_strength = strength
        self.items = []
        self.name = name

    def add_item(self, item_name: str):
        self.items.append(item_name)

    def __str__(self):
        items_str = "\n".join([f"- {item}" for item in self.items])
        return (
            f"Character Details:\n"
            f"Description: {self.name} (Short description of the character)\n"
            f"Strength: {self.strength} (Base combat ability)\n"
            f"Current Strength: {self.current_strength} (Tracks wounds and current capability)\n"
            f"Items:\n{items_str if items_str else 'None'}"
        )
