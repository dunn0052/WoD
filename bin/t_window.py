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

        self.pack(fill = BOTH, expand = 1)

        quitButton = Button(self, text = "Quit", command = self.client_exit)
        quitButton.place(x = 0, y = 0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = "Load", command = self.load_char)
        file.add_command(label = "Save", command = self.save_char)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label = "Undo")
        menu.add_cascade(label="Edit", menu=edit)

        text = Label(self, text = "Test text")
        text.pack( side = LEFT)
        entry = Entry(self, width = 30)
        entry.pack(side = RIGHT)


    def client_exit(self):
        exit()

    def load_char(self):
        self.player.load_char("RAGE")
        self.title = self.player.character.final_touches["Character Name"][0] + " - " + self.player.character.final_touches["Player"][0]

    def save_char(self):
        self.player.save_char("RAGE")

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
