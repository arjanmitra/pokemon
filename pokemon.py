class Item:
       def __init__(self, name, description):
              self.name = name
              self.description = description
       def __repr__(self):
              return self.description

class Ability:
       def __init__(self, name, type, description):
              self.name = name
              self.type = type
              self.description = description
       def __repr__(self):
              return self.description

class Move:
       def __init__(self, name, category, contest, power, accuracy, pp, target, description):
              self.name = name
              self.category = category
              self.contest = contest
              self.power = power
              self.accuracy = accuracy
              self.pp = pp
              self.target = target
              self.description = description
       def __repr__(self):
              return self.description

class Type:
       def __init__(self, name, moves, abilities, items):
              self.name = name
              self.moves = moves
              self.abilities = abilities
              self.items = items

class Pokemon:
       def __init__(self, name, level, type, maxhealth, curhealth, description, ko):
              self.name = name
              self.level = level
              self.type = type
              self.maxhealth = maxhealth
              self.curhealth = curhealth
              self.description = description
              self.ko = ko
       def __repr__(self):
              return("Pokemon: " + self.name + "\n Level: " + self.level + "\n Type: " + self.type +
                     "\n Max Health: " + self.maxhealth + "\n Current Health: " + self.curhealth +
                     "\n KO?: " + self.ko)
       def knockout(self):
              self.curhealth = 0
              self.ko = True
              print(self.name + " has knocked out!")
       def losehealth(self, loss):
              self.curhealth = self.curhealth - loss
              if loss >= self.maxhealth/2:
                     print("Critical hit!" + self.name + " now has " + str(self.curhealth) + " health!")
              elif self.maxhealth/2 > loss > 0:
                     print(self.name + " just took a hit! It now has " + str(self.curhealth) + " health!")
              else:
                     self.ko = True
                     print(self.name + " knocked out! ")
       def gainhealth(self, gain):
              self.curhealth = self.curhealth + gain
              print(self.name + " just gained health! It now has " + str(self.curhealth) + " health!")
       def revive(self, gain):
              self.curhealth = gain
              self.ko = False
              print(self.name + " just gained health! It now has " + str(self.curhealth) + " health!")

class Party:
       def __init__(self, pokemonlist):
              if len(pokemonlist) <= 6:
                     self.pokemonlist = pokemonlist
              else:
                     print("Your party cannot exceed 6 pokemon!")
       def __repr__(self):
              desc = ""
              for pokemon in self.pokemonlist:
                     desc = "\n" + pokemon.description
              return desc
       def add(self, pokemon):
              if len(self.pokemonlist) >= 6:
                     print("Your party is full!")
              else:
                     self.pokemonlist = self.pokemonlist + [pokemon]
                     print("Party updated with " + pokemon + "!")
       def remove(self, pokemon):
              if pokemon in self.pokemonlist:
                     self.pokemonlist.remove(pokemon)
              else:
                     print("The Pokemon doesn't exist in party!")

class Showdown:
       def __init__(self, p1, p2):
              self.p1 = p1
              self.p2 = p2
       def __repr__(self):
              return("Showdown between " + self.p1 + " and " + self.p2 + "!")
       def fight(self, p, move):
              print(p + " used " + move + "!" + move.description)

bitterberry = Item("Bitter Berry", "The Bitter Berry is a type of berry. It cures a Pokémon of confusion.")

overgrow = Ability("Overgrow", "Grass", "All Grass-type starter Pokémon have this Ability.")
chlorophyll = Ability("Chlorophyll", "Grass - Hidden", "During harsh sunlight, the Speed stat of Pokémon with this Ability is doubled.")

tackle = Move("Tackle", "Physical", "Toughness", 40, 100, 35, "Adjacent", "A physical attack in which the " \
       "user charges and slams into the target with its whole body.")

normal = Type("Normal", [tackle], [overgrow, chlorophyll], [bitterberry])

bulbasaur = Pokemon("Bulbasaur", 23, [normal], 100, 100, False)

