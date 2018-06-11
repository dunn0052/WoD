from tkinter import *
from wod_character import *
from player_char import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.player = playerCharacter()
        self.title = self.player.character.final_touches["Character Name"][0] + " - " + self.player.character.final_touches["Player"][0]
        self.master.title(self.title)



        quitButton = Button(self, text = "Quit", command = self.client_exit)
        #quitButton.place(x = 0, y = 0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = "Load", command = self.load_char)
        file.add_command(label = "Save", command = self.save_char)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label="File", menu = file)

        edit = Menu(menu)
        edit.add_command(label = "Undo")
        menu.add_cascade(label="Edit", menu = edit)

        #Label(root, text = "Test text").grid(row = 0, column = 1)
        #entry = Entry(root, width = 30)
        #entry.grid(row = 0, column = 2)



    def client_exit(self):
        exit()

    def load_char(self, name = None):
        self.player.load_char("RAGE")
        self.char_title()
        self.display_character()


    def save_char(self, name = None):
        self.player.save_char("RAGE")

    def char_title(self, name = None, player = None):
        if not name or not player:
            self.title = self.player.character.final_touches["Character Name"][0] + " - " + self.player.character.final_touches["Player"][0]
            self.master.title(self.title)
        else:
            self.title = str(name) + " - " + str(player)
            self.master.title(self.title)

    def display_character(self):
        po = ["Attribute", "Skill", "Merit", "Physical", "Mental", "Social", "Derangement", "Virtue", "Vice", "Inventory", "Weapon", "Item", "Armor"]
        for i in range(3):
            for j in range(3,6):
                self.display_field(item_type = po[i], attribute = po[j])
        k = (0,1)
        for i in range(6,9):
            k = self.display_field(item_type = po[i], attribute = None, grid_row = k[0], grid_column = k[1])
        k = (0,2)
        for i in range(10,13):
            k = self.display_field(item_type = po[9], attribute = po[i], grid_row = k[0], grid_column = k[1])

    def display_field(self, item_type , attribute, grid_row = 0, grid_column = 0, title = None, horizontal = 0, vertical = 1, justification = "w", zero_flag = False):
        # can put in seperate title or default to attribute name
        # row, column are where to start in grid justification is based on cardinal directions for some reason so default, "w" for "left"
        if not title:
            title = attribute + " " + item_type if attribute else item_type
        Label(root, text = title, anchor = justification).grid(row = grid_row, column = grid_column)
        grid_row += vertical
        grid_column += horizontal
        dictionary = self.player.find_dict(item_type = item_type, attribute = attribute)
        for items in dictionary:
            self.display_stat(dictionary = dictionary, stat = items, grid_row = grid_row, grid_column = grid_column, justification = justification, zero_flag = zero_flag)
            # you can choose to print vertical, horizontal or I suppose diagonal for some reason..
            grid_row += vertical
            grid_column += horizontal
        return (grid_row, grid_column)

    def display_stat(self, dictionary, stat, grid_row, grid_column, justification, zero_flag = False):
        current_value = dictionary[stat][0]
        if zero_flag:
            Label(root, text = stat + ": " + str(current_value), anchor = justification).grid(row = grid_row, column = grid_column)
            return
        stat_text = stat if isinstance(stat, bool) else stat + ": " + str(current_value)
        Label(root, text = stat_text, anchor = justification).grid(row = grid_row, column = grid_column)


root = Tk()
#root.geometry("400x300")

app = Window(root)

root.mainloop()
