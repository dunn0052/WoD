# random char generator

# @TODO
# increase_stat to serch by type instead of direct dictionary access
import random
from wod_character import wChar

class wChar_rand:
    def __init__(self, character):
        self.character = character

        # params


    def rand_char(self, name = ""):
        self.character.initialize_char_data()
        self.rand_att()
        self.character.change_name(name)
        self.character.print_char()

    def add_weapon(self, name, list = "Weapons"):
      # reads data from weapon list - could be made generic for all items
      # should probably use add_field from wod_character
      # GM tool
      data = []
      with open(list + ".csv", 'rt') as weapon_file:
          reader = csv.reader(weapon_file, delimiter=',')
          for row in reader:
              if row[0] == name:
                  self.character.weapons[row[0]] = row[1:]
                  print("Added " + row[0] + " to weapons.")
                  break


    def rand_dot_dist(self, phys, ment, socl, first = 0, second = 0, third = 0):
        n = [first,second,third]
        random.shuffle(n)
        self.rand_point_distribute(n[0], phys)
        self.rand_point_distribute(n[1], ment)
        self.rand_point_distribute(n[2], socl)


    def rand_point_distribute(self, dots, attributes):
        i = 0
        while (i < dots):
            choice = random.choice(list(attributes))
            if(attributes[choice][0] < attributes[choice][3] - 1):
                attributes[choice][0] += 1
                i+= 1
            elif(attributes[choice][0] == attributes[choice][3] - 1 and i < dots - 1):
                attributes[choice][0] += 1
                i+= 2

    def rand_merit_dist(self, dots = 7):
        for i in range(dots):
            r = random.randint(0,2)
            if(r == 0):
                self.rand_point_distribute(1, self.character.mental_merits)
            elif(r == 1):
                self.rand_point_distribute(1, self.character.physical_merits)
            else:
                self.rand_point_distribute(1, self.character.social_merits)

    def rand_att(self):
        # Could make generic initial stat dots in __init__
        self.rand_dot_dist(self.character.physical, self.character.mental, self.character.social, 5, 4, 3)
        self.rand_dot_dist(self.character.physical_skills, self.character.mental_skills, self.character.social_skills, 11, 7, 4)
        self.rand_merit_dist(7)
        self.rand_der(3)
        self.character.char_calc()
        self.rand_choice(dictionary = self.character.virtue, value = True)
        self.rand_choice(dictionary = self.character.vice, value = True)
        self.rand_choice(dictionary = self.character.weapons, value = 1, stack = True)
        self.rand_choice(dictionary = self.character.inventory, value = 1, stack = True)
        self.rand_choice(dictionary = self.character.armor, value = 1)

    def rand_der(self, n = 3):
        chance = random.randint(0,n)
        for i in range(chance):
            pair = self.character.der_map(random.choice(list(self.character.derangements)))
            # if no derangment is present then make mild choice
            if not self.character.derangements[pair[0]][0] and not self.character.derangements[pair[1]][0]:
                self.character.derangements[pair[0]][0] = True
            # if mild derangment is present then upgrade to major
            elif self.character.derangements[pair[0]]:
                self.character.derangements[pair[0]][0] = False
                self.character.derangements[pair[1]][0] = True
            # if already major, then ignore

    def rand_choice(self, dictionary, value, number = 1, index = 0, stack = False):
        # value = what indicator, number = how many, index = which entry, stack if value can be stacked
        if stack:
            for i in range(number):
                dictionary[random.choice(list(dictionary))][index] += value
        else:
            for i in range(number):
                dictionary[random.choice(list(dictionary))][index] = value
