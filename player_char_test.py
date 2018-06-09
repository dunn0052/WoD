from wod_character import wChar
from player_char import playerCharacter

rage = playerCharacter("RAGE")
rage.load_char("RAGE")
rage.add_item("Eye For The Strange", [4], 2, "Merit", "Mental")
rage.add_skill_specialization("Firearms", "Archery", free = True)
rage.add_skill_specialization("Occult", "Casting Circles", free = True)
rage.add_skill_specialization("Animal Ken", "Cat", free = True)
rage.print_char()
