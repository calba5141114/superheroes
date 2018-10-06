import random


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        ''' returns psuedo random attack strength between the min attack value (self.attack_strength //2 ) and the max (self.attack_strength'''
        lowest_attack_value = self.attack_strength // 2
        return random.randint(lowest_attack_value, self.attack_strength)

    def update_attack(self, attack_strength):
        ''' Setter for attack strength'''
        self.attack_strength = attack_strength


class Hero:

    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        ''' push new ability to list of abilities'''
        self.abilities.append(ability)

    def attack(self):
        ''' returns the sum attack values of all the abilities'''
        sum_of_attacks = 0
        for ability in self.abilities:
            sum_of_attacks += ability.attack()
        return sum_of_attacks


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)


class Team():

    def __init__(self, team_name):
        ''' instantiate resources '''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):

        for hero in self.heroes:

            if hero.name == name:
                index_main = self.heroes.index(hero)
                self.heroes.remove(index_main)
            else:
                pass
            return 0

    def find_hero(self, name):

        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                pass
        # returns 0 with no hero
        return 0

    def view_all_heroes(self):
        if len(self.heroes) == 0:
            return 'There are no heroes on this team'
        else:
            for hero in self.heroes:
                print(hero)


if __name__ == "__main__":
    ''' runs when inside of the class file '''
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
