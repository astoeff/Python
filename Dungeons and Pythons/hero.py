from playable import Playable


class Hero(Playable):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def known_as(self):
        return self.name + ' the ' + self.title

    def print_hero(self):
        print('Name: ', self.name)
        print('Title: ', self.title)
        print('Known as: ', self.known_as())
        print('Health: ', self.health)
        print('Mana: ', self.mana)
        print('Mana regeneration rate: ', self.mana_regeneration_rate)
        print('Weapon: ', self.weapon)
        print('Spell: ', self.spell)


    def attack(self, **kwargs):
        result_from_attack = 0
        try:
            result_from_attack = super().attack(**kwargs)
        except Exception as e:
            raise e
        if result_from_attack is not None:
            return result_from_attack
        return 0

	def print_hero(self):
		print('Name: ', self.name)
		print('Title: ', self.title)
		print('Known as: ', self.known_as())
		print('Health: ', self.health)
		print('Mana: ', self.mana)
		print('Mana regeneration rate: ', self.mana_regeneration_rate)
		print('Weapon: ', self.weapon)
		print('Spell: ', self.spell)
		print()

