# data char generator

## @TODO
## Player GUI - began
## Seperate player creation module
## DM program/GUI - began
## add flaws/ method to add them?
## merit modifiers/prereqs??
## skill prereqs?
## keep this doc to strictly store, save, and load char data
import csv
import random

class wChar:
    def __init__(self, name = None):
        # All attributes must begin every word with capital for search to work
        self.physical = {}
        self.mental = {}
        self.social = {}
        self.virtue = {}
        self.vice = {}
        self.traits = {}
        self.mental_skills = {}
        self.physical_skills = {}
        self.social_skills = {}
        self.derangements = {}
        self.mental_merits = {}
        self.physical_merits = {}
        self.social_merits = {}
        self.flaws = {}
        self.final_touches = {}
        self.skill_specialization = {}

        self.weapons = {}
        self.armor = {}
        self.inventory = {}


        self.dict_map = {
        "Physical Attribute" : self.physical, "Mental Attribute" : self.mental,
        "Social Attribute" : self.social, "Physical Skill" : self.physical_skills,
        "Mental Skill" : self.mental_skills, "Social Skill" : self.social_skills,
        "Trait" : self.traits, "Physical Merit" : self.physical_merits,
        "Mental Merit" : self.mental_merits, "Social Merit" : self.social_merits,
        "Derangement" : self.derangements, "Virtue" : self.virtue, "Vice" : self.vice,
        "Final Touches" : self.final_touches, "Weapon Inventory" : self.weapons,
        "Item Inventory" : self.inventory, "Armor Inventory" : self.armor, "Flaw" : self.flaws
        }
        self.change_name(name)
        self.initialize_char_data()

    def add_field(self, file):
        # reads data from a file and adds to dictionary
        data = []
        with open(file + ".csv", 'rt') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            header = next(reader) # header of data file
            type_index = self.parse_header(header, "Type")
            # Change "Attribute" header to something better
            attribute_index = self.parse_header(header, "Attribute")
            name = self.parse_header(header, "Name")
            for row in reader:
                # find the proper dictionary and fill entry with clean data
                if row != header and type_index != None and attribute_index != None:
                    self.find_dict(self.clean_item(row[type_index]), self.clean_item(row[attribute_index]))[self.clean_key(row[name])] = self.clean_row(row[1:])
                elif row != header and type_index != None:
                    self.find_dict(self.clean_item(row[type_index]))[self.clean_key(row[name])] = self.clean_row(row[1:])
                else:
                    continue
        data_file.close()

    def add_item(self, name, data, current_value, type, attribute = None):
        dictionary = self.find_dict(type, attribute)
        if dictionary != None:
            dictionary[name] = [current_value, type, attribute]
            dictionary[name].extend(data)


    def parse_header(self, header, key):
        # find index of header - officially: [name, current value, type, attribute, etc. ]
        # order doesn't matter when loading initial data, but saved characters will
        # have all traits organized by the first 4 header values in that order
        # save as plain .csv - save as whatever the other files are in if errors
        clean_key = self.clean_key(key)
        if key in header:
            return header.index(key)
        else:
            return None

    def clean_key(self, key):
        # all keys have capital letters beginning each word
        return (str(key).lower()).title()

    def clean_row(self, row):
        # turns .csv row back into thier respective data types as .csv is all strings
        n = []
        for item in row:
            n.append(self.clean_item(item))
        return n

    def clean_item(self, item):
        # Mess with edgelords wanting to name their character "False"
        # Actually could be a big problem if string was meant to be "TRUE"/"FALSE"
        if item.upper() == "TRUE":
            return True
        elif item.upper() == "FALSE":
            return False
        elif isinstance(item, bool):
            return item
        elif isinstance(item, int):
            return item
        elif item.isnumeric():
            return int(item)
        elif item == "None":
            return None
        else:
            return item

    def find_dict(self, type, attribute = None):
        # Use attribute and type to index matching dictionary
        if(attribute != None and attribute != ""):
            return self.dict_map[self.clean_key(attribute) + " " + self.clean_key(type)]
        else:
            return self.dict_map[self.clean_key(type)]

    def change_name(self, name):
        self.final_touches["Character Name"] = [name, "Touches", "Final"]

    def find_stat(self, key):
        # find attribute in any dictionary - will return first found - no duplicates
        a = self.find_att(key)
        if(a != None):
            return a[self.clean_key(key)]
        else:
            return None

    def find_att(self, key):
        # return the first dictionary where the stat is found - no duplicates
        clean_key = self.clean_key(key)
        for attribute in self.dict_map.values():
            if clean_key in attribute:
                return attribute
        print(str(key) + " not found.")
        return None

    def initialize_char_data(self):
        self.add_field("char_data/Attributes")
        self.add_field("char_data/Final_Touches")
        self.add_field("char_data/Merits")
        self.add_field("char_data/Skills")
        self.add_field("char_data/Virtue_Vice")
        self.add_field("char_data/Derangements")
        self.add_field("char_data/Traits")
        self.add_field("item_data/Melee_Weapons")
        self.add_field("item_data/Ranged_Weapons")
        self.add_field("item_data/Items")
        self.add_field("item_data/Armor")

    def char_calc(self):
        self.traits["Size"][0] = 5
        self.traits["Health"][0] = self.traits["Size"][0] + self.physical["Stamina"][0]
        self.traits["Willpower"][0] = self.mental["Resolve"][0] + self.social["Composure"][0]
        self.traits["Defense"][0] = min(self.physical["Dexterity"][0], self.mental["Wits"][0])
        self.traits["Initiative"][0] = self.physical["Dexterity"][0] + self.social["Composure"][0]
        self.traits["Speed"][0] = self.physical["Strength"][0] + self.physical["Dexterity"][0] + 5
        self.traits["Morality"][0] = 7

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
        # tuple of (minor, major)
        return (derangements_map[place], derangements_map[place-1]) if (place % 2 == 1) else (derangements_map[place], derangements_map[place + 1])


    def save_char(self, path):
        if ("Character Name" not in self.final_touches or self.final_touches["Character Name"][0] == None or self.final_touches["Character Name"] == ""):
            print("The Characer needs a name to save. Use change_name().")
            return
        data = [["Name", "Current", "Type", "Attribute"]]
        for item in self.dict_map.values():
            if any(item):
                for key in item:
                    # can't do data.append([key].extend(item[key])) ??
                    row = [key]
                    row.extend(item[key])
                    # saving without attribute - default to None
                    if len(row) < 4:
                        row.append("None")
                    data.append(row)
        with open(path + ".csv", "w", newline='') as char_file:
            writer = csv.writer(char_file, delimiter=',')
            for stat in data:
                writer.writerow(stat)
        char_file.close()

    def load_char(self, name):
        # reads data from save file - name must be in quotes
        self.add_field(name)
        self.char_calc()

    def print_attributes(self, attributes, index = 0, present = False, bool_val = True):
        # present to print attributes even if they have a value of 0/False
        # bool_val = True if you don't want to print any bool values
        # present = True if you want to print out everything and ignore bool_val
        if present:
            for attribute in attributes:
                if attribute in self.skill_specialization:
                    print(attribute + ": ", end="", flush=True)
                    self.print_horizontal_list(self.skill_specialization[attribute])
                    return
                print(attribute + ": " + str(attributes[attribute][index]))
        else:
            for attribute in attributes:
                if (attributes[attribute][index] != 0 and bool_val):
                    if attribute in self.skill_specialization:
                        print(attribute + ": ", end="", flush=True)
                        self.print_horizontal_list(self.skill_specialization[attribute])
                        return
                    print(attribute + ": " + str(attributes[attribute][index]))
                elif(attributes[attribute][index] != 0 and not bool_val):
                    print(attribute)

    def print_horizontal_list(self, list):
        # only works for python 3
        for items in list:
            print((items + ", "), end="", flush=True)
            # for python 2 use:
            # print (items + ", ") ,
            print("")

    def print_char(self):
        self.print_attributes(self.final_touches, present = True)
        print("")
        print("Attributes")
        print("---------------------------------------------------------------")
        self.print_attributes(self.physical, present = True)
        self.print_attributes(self.mental, present = True)
        self.print_attributes(self.social, present = True)
        print("")
        print("Traits")
        print("---------------------------------------------------------------")
        self.print_attributes(self.traits, present = True)
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
        self.print_attributes(self.derangements, bool_val = False)
        print("")
        print("Virtue and Vice")
        print("---------------------------------------------------------------")
        self.print_attributes(self.virtue, bool_val = False)
        self.print_attributes(self.vice, bool_val = False)
        print("")
        print("Inventory")
        print("---------------------------------------------------------------")
        self.print_attributes(self.weapons)
        self.print_attributes(self.inventory)
        self.print_attributes(self.armor)
