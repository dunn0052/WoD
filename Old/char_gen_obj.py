#char generator

##@TODO
##- Make GUI
##- Attack dice and modifiers
##- Skill modifier and roll
##- Merit modifiers

import csv
import random

class wChar:
    def __init__(self, name = None):

        # All attributes must begin every word with capital for search to work

        self.physical = {
            "Strength" : 1,
            "Dexterity" : 1,
            "Stamina" : 1
            }
        self.mental = {
            "Intelligence" : 1,
            "Wits" : 1,
            "Resolve" : 1
            }
        self.social = {
            "Presence" : 1,
            "Manipulation" : 1,
            "Composure" : 1
            }

        self.virtue = {
            "Charity" : False,
            "Faith" : False,
            "Fortitude" : False,
            "Hope" : False,
            "Justice" : False,
            "Prudence" : False,
            "Temperance" : False
            }

        self.vice = {
            "Envy" : False,
            "Gluttony" : False,
            "Greed" : False,
            "Lust" : False,
            "Pride" : False,
            "Sloth" : False,
            "Wraith" : False
            }
        self.traits = {
            "Health" : 0,
            "Willpower" : 0,
            "Speed" : 0,
            "Size" : 0,
            "Defense" : 0,
            "Initiative" : 0,
            "Morality" : 0
            }
        # name : [current value, type, specialties, effect]
        self.mental_skills = {
            "Academics" : 0,
            "Computer" : 0,
            "Crafts" : 0,
            "Investigation" : 0,
            "Medicine" : 0,
            "Occult" : 0,
            "Politics" : 0,
            "Science" : 0
        }

        self.physical_skills = {
            "Athletics" : 0,
            "Brawl" : 0,
            "Drive" : 0,
            "Firearms" : 0,
            "Larceny" : 0,
            "Stealth" : 0,
            "Survival" : 0,
            "Weaponry" : 0
        }

        self.social_skills = {
            "Animal Ken" : 0,
            "Empathy" : 0,
            "Expression" : 0,
            "Intimidation" : 0,
            "Persuasion" : 0,
            "Socialize" : 0,
            "Streetwise" : 0,
            "Subterfuge" : 0
        }

        self.derangements = {
            "Depression" :  False,
            "Phobia"  :  False,
            "Narcissism" :  False,
            "Fixation" :  False,
            "Suspicion" :  False,
            "Inferiority Complex" :  False,
            "Vocalization" :  False,
            "Irrationality" :  False,
            "Avoidance" :  False,
            "Melancholia" :  False,
            "Hysteria" :  False,
            "Megalomania" :  False,
            "Obsessive Compulsion" :  False,
            "Paranoia" :  False,
            "Anxiety" :  False,
            "Schizophrenia" :  False,
            "Multiple Personality" :  False,
            "Fugue" :  False
            }

        self.mental_merits = {
            "Common Sense" : 0,
            "Danger Sense" : 0,
            "Eidetic Memory" : 0,
            "Encyclopedic Knowledge" : 0,
            "Holistic Awareness" : 0,
            "Language" : 0,
            "Meditative Mind" : 0,
            "Unseen Sense" : 0,
        }

        self.physical_merits = {
            "Ambidextrous" : 0,
            "Brawling Dodge" : 0,
            "Direction Sense" : 0,
            "Disarm" : 0,
            "Fast Reflexes" : 0,
            "Fighting Finesse" : 0,
            "Fighting Style: Boxing" : 0,
            "Fighting Style: Kung Fu" : 0,
            "Fighting Style: Two Weapons" : 0,
            "Fleet Of Foot" : 0,
            "Fresh Start" : 0,
            "Giant" : 0,
            "Gunslinger" : 0,
            "Iron Stamina" : 0,
            "Iron Stomach" : 0,
            "Natural Immunity" : 0,
            "Quick Draw" : 0,
            "Quick Healer" : 0,
            "Strong Back" : 0,
            "Strong Lungs" : 0,
            "Stunt Driver" : 0,
            "Toxin Resistance" : 0,
            "Weaponry Dodge" : 0,
        }

        self.social_merits = {
            "Allies" : 0,
            "Barfly" : 0,
            "Contacts" : 0,
            "Fame" : 0,
            "Inspiring" : 0,
            "Mentor" : 0,
            "Resources" : 0,
            "Retainer" : 0,
            "Status" : 0,
            "Striking Looks" : 0,
        }

        self.final_touches = {
            "Name" : "",
            "Experience" : 0,
            "Age" : -1,
            "Player" : "",
            "Faction" : "",
            "Group Name" : "",
            "Concept" : "",
            "Group Name" : "",
            "Gender" : "",
            "Sex" : "",
            "Description" : ""
        }

        # name : [current value, max value, type, effect, desciption]
        self.merit_max = {
            "Allies" : 5,
            "Barfly" : 1,
            "Contacts" : 5,
            "Fame" : 3,
            "Inspiring" : 4,
            "Mentor" : 5,
            "Resources" : 5,
            "Retainer" : 5,
            "Status" : 5,
            "Stiking Looks" : 4,
            "Ambidextrous" : 3,
            "Brawling Dodge" : 1,
            "Direction Sense" : 1,
            "Disarm" : 2,
            "Fast Reflexes" : 2,
            "Fighting Finesse" : 2,
            "Fighting Style: Boxing" : 5,
            "Fighting Style: Kung Fu" : 5,
            "Fighting Style: Two Weapons" : 4,
            "Fleet Of Foot" : 3,
            "Fresh Start" : 1,
            "Giant" : 4,
            "Gunslinger" : 3,
            "Iron Stamina" : 3,
            "Iron Stomach" : 2,
            "Natural Immunity" : 1,
            "Quick Draw" : 1,
            "Quick Healer" : 4,
            "Strong Back" : 1,
            "Strong Lungs" : 3,
            "Stunt Driver" : 3,
            "Toxin Resistance" : 2,
            "Weaponry Dodge" : 1,
            "Common Sense" : 4,
            "Danger Sense" : 2,
            "Eidetic Memory" : 2,
            "Encyclopedic Knowledge" : 4,
            "Holistic Awareness" : 3,
            "Language" : 4,
            "Meditative Mind" : 1,
            "Unseen Sense" : 3,
        }

        self.skill_specialization = {

        }

        self.weapons = {

        }

        self.inventory = {

        }

        self.search_list = [self.physical, self.mental, self.social, self.physical_skills,
        self.mental_skills, self.social_skills, self.traits,
        self.physical_merits, self.mental_merits, self.social_merits,
        self.derangements, self.virtue, self.vice, self.final_touches]

        self.search_list_text = ["self.physical", "self.mental", "self.social", "self.physical_skills",
        "self.mental_skills", "self.social_skills", "self.traits",
        "self.physical_merits", "self.mental_merits", "self.social_merits",
        "self.derangements", "self.virtue", "self.vice", "self.final_touches"]

        self.change_name(name)

    def add_skill_specialization(self, skill, specialization):
        exp = self.final_touches["Experience"]
        if(exp >= 3 and (skill in self.physical_skills or skill in self.social_skills or skill in self.mental_skills)):
            exp -= 3
            if (skill not in self.skill_specialization):
                self.skill_specialization[skill] = [specialization]
            else:
                self.skill_specialization[skill].append(specialization)
        else:
            print("Could not add " + specialization + " to " + skill)

    def add_weapon(self, name, list = "weapons"):
        #reads data from weapon list - could be made generic
        data = []
        with open(list + ".csv", 'rt') as weapon_file:
            reader = csv.reader(weapon_file, delimiter=',')
            for row in reader:
                if row[0] == name:
                    self.weapons[row[0]] = row[1:]
                    print("Added " + row[0] + " to weapons.")
                    break

    def write_data(self, path, dict):
        # export char data to csv file for modifcation
        data = []
        data.extend(dict.items())
        with open(path + ".csv", "w", newline='') as data_file:
            writer = csv.writer(data_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)
        data_file.close()

    def write_all_data(self):
        paths = []
        for name in self.search_list_text:
            f = str(name)
            a = f.split('.')[-1]
            paths.append(a)
        i = 0
        for dictionary in self.search_list:
            self.write_data(paths[i], dictionary)
            i += 1


    def increase_exp(self, num = 1):
        self.final_touches["Experience"] += num

    def increase_stat(self, stat, dot = 1, free = False, override = False):
        # free = True if increase doesn't cost exp - override for GM override
        if (stat in self.physical or stat in self.mental or stat in self.social):
            mult = 5
            max_val = 5
        elif(stat in self.physical_skills or stat in self.mental_skills or stat in self.social_skills):
            mult = 3
            max_val = 5
        elif(stat in self.physical_merits or stat in self.mental_merits or stat in self.social_merits or stat == self.traits["Morality"]):
            mult = 2
            max_val = 10 if stat == self.traits["Morality"] else self.find_att(stat)[stat]
        else:
            print("Stat not found")
            return
        stat_val = self.find_stat(stat)
        cost = stat_val * mult
        if (cost <= self.final_touches["Experience"] and stat_val + dot <= max_val or free and stat_val + dot <= max_val or override):
             self.find_att(stat)[stat] += dot
             self.final_touches["Experience"] -= cost if not free else 0
        else:
             print("Can't increase " + str(stat))


    def change_name(self, name):
        self.final_touches["Name"] = str(name)

    def find_stat(self, key):
         a = self.find_att(key)
         if(a != None):
             return a[(str(key).lower()).title()]
         else:
             return None

    def find_att(self,key):
        clean_key = (str(key).lower()).title()
        for attribute in self.search_list:
            if clean_key in attribute:
                return attribute
        print(str(key) + " not found.")
        return None

    def rand_dot_dist(self, phys, ment, socl, first = 0, second = 0, third = 0):
        n = [first,second,third]
        random.shuffle(n)
        self.rand_point_distribute(n[0], phys)
        self.rand_point_distribute(n[1], ment)
        self.rand_point_distribute(n[2], socl)


    def rand_point_distribute(self, dots, attributes, max_val = 5):
        i = 0
        while (i < dots):
            choice = random.choice(list(attributes))
            if(attributes[choice] < max_val - 1):
                attributes[choice] += 1
                i+= 1
            elif(attributes[choice] == max_val - 1 and i < dots - 1):
                attributes[choice] += 1
                i+= 2

    def rand_merit_dist(self, dots):
        for i in range(dots):
            r = random.randint(0,2)
            if(r == 0):
                self.rand_point_distribute(1, self.mental_merits)
            elif(r == 1):
                self.rand_point_distribute(1, self.physical_merits)
            else:
                self.rand_point_distribute(1, self.social_merits)

    def rand_att(self):

        self.rand_dot_dist(self.physical, self.mental, self.social, 5, 4, 3)
        self.rand_dot_dist(self.physical_skills, self.mental_skills, self.social_skills, 11, 7, 4)
        self.rand_merit_dist(7)
        self.rand_der()
        self.char_calc()
        self.virtue_gen()
        self.vice_gen()


    def virtue_gen(self):
        self.virtue[random.choice(list(self.virtue))] = True

    def vice_gen(self):
        self.vice[random.choice(list(self.vice))] = True

    def der_map(self, key):
        derangements_map = [
        "Depression" , "Melancholia",
        "Phobia" , "Hysteria",
        "Narcissism" , "Megalomania",
        "Fixation" , "Obsessive Compulsion",
        "Suspicion" , "Paranoia",
        "Inferiority Complex" , "Anxiety",
        "Vocalization" , "Schizophrenia",
        "Irrationality" , "Multiple Personality",
        "Avoidance" , "Fugue"]

        place = derangements_map.index(key)
        return (derangements_map[place-1], derangements_map[place]) if (place % 2 == 1) else (derangements_map[place], derangements_map[place + 1])





    def rand_der(self, n = 3):
        chance = random.randint(0,n)
        print(chance)
        for i in range(chance):
            pair = self.der_map(random.choice(list(self.derangements)))
            # if no derangment is present then make mild choice
            if not self.derangements[pair[0]] and not self.derangements[pair[1]]:
                self.derangements[pair[0]] = True
            # if mild derangment is present then upgrade to major
            elif self.derangements[pair[0]]:
                self.derangements[pair[0]] = False
                self.derangements[pair[1]] = True
            # if already major, then ignore



    def char_calc(self):
        self.traits["Size"] = 5
        self.traits["Health"] = self.traits["Size"] + self.physical["Stamina"]
        self.traits["Willpower"] = self.mental["Resolve"] + self.social["Composure"]
        self.traits["Defense"] = min(self.physical["Dexterity"], self.mental["Wits"])
        self.traits["Initiative"] = self.physical["Dexterity"] + self.social["Composure"]
        self.traits["Speed"] = self.physical["Strength"] + self.physical["Dexterity"] + 5
        self.traits["Morality"] = 7

    def print_attributes(self, attributes, present = False):
        # present to print attributes even if they have a value of 0
        if present:
            for attribute in attributes:
                print(attribute + " " + str(attributes[attribute]))
        else:
            for attribute in attributes:
                if (attributes[attribute] != 0):
                   print(attribute + " " + str(attributes[attribute]))

    def print_char(self):
        # @TODO finish printing sheet
        self.print_attributes(self.final_touches, True)
        print("")
        print("Attributes")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical, True)
        self.print_attributes(self.mental, True)
        self.print_attributes(self.social, True)
        print("")
        print("Traits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.traits, True)
        print("")
        print("Skills")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical_skills)
        self.print_attributes(self.mental_skills)
        self.print_attributes(self.social_skills)
        print("")
        print("Merits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical_merits)
        self.print_attributes(self.mental_merits)
        self.print_attributes(self.social_merits)
        print("")
        print("Derangements")
        print("---------------------------------------------------------------")
        self.print_attributes(self.derangements)
        print("")
        print("Virtue and Vice")
        print("---------------------------------------------------------------")
        self.print_attributes(self.virtue)
        self.print_attributes(self.vice)

    def type_write(self, attribute, writer):
        for stat in attribute:
            if isinstance(attribute[stat], bool) and attribute[stat]:
                writer.writerow((str(stat), True))
            elif isinstance(attribute[stat], int):
                writer.writerow((str(stat), int(attribute[stat])))
            else:
                writer.writerow((str(stat), attribute[stat]))

    def type_read(self, item):
        print(item)
        if item[1] == "True":
            self.find_att(item[0])[item[0]] = True
        elif item[1] == "False":
            self.find_att(item[0])[item[0]] = False
        elif item[1].isnumeric():
            self.find_att(item[0])[item[0]] = int(item[1])
        else:
            self.find_att(item[0])[item[0]] = item[1]


    def save_char(self):
        if (self.final_touches["Name"]== None):
            print("The Characer needs a name to save. Use change_name().")
            return
        path = str(self.final_touches["Name"]) + ".csv"
        data = []
        data.extend(self.physical.items())
        data.extend(self.mental.items())
        data.extend(self.social.items())
        data.extend(self.traits.items())
        data.extend(self.physical_skills.items())
        data.extend(self.mental_skills.items())
        data.extend(self.social_skills.items())
        data.extend(self.physical_merits.items())
        data.extend(self.mental_merits.items())
        data.extend(self.social_merits.items())
        with open(path, "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)
            self.type_write(self.vice, writer)
            self.type_write(self.virtue, writer)
            self.type_write(self.derangements, writer)


    def load_char(self, name):
        #reads data from save file - name must be in quotes
        data = []
        with open(str(name) + ".csv", 'rt') as char_file:
            reader = csv.reader(char_file, delimiter=',')
            for row in reader:
                data.append(row)
        for item in data:
            self.type_read(item)

    def roll(self, attribute, skill = 0, items = 0, modifier = 0, again = 10, min = 8):
        # again is min success value - used when
        dice_pool = attribute + skill + items + modifier
        success = 0
        if dice_pool > 0:
            dice = 0
            while dice < dice_pool:
                print(dice)
                die = random.randint(0,10)
                if die >= min:
                    success += 1
                if die == again:
                    dice -= 1
                    print("again")
                dice += 1
            return success
        elif dice_pool < 1:
            die = random.randint(1,10)
            if die != 10 and roll != 0:
                return 0
            elif die == 10:
                return 1
            else:
                return 0


    def debug(self):
        self.rand_att()
        self.print_char()
        self.save_char()
