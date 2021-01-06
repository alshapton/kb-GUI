#kivy.require("2.0.0")
import os

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kb.config import get_current_base, DEFAULT_CONFIG,BASE
from functions.list import list_categories
from pathlib import Path

from presentation import populate_categories

class gui(MDApp):

    def build(self):

        # Change the application icon
        self.icon=str(Path("../img/","kb-icon.png")) 

        # Get the list of categories from the knowledgebase
        populate_categories(self)

        pass

    def left_menu_click(self):  
        print("left menu")

    def right_menu_click(self):  
        print("right menu")


gui().run()