# -*- encoding: utf-8 -*-
# kb-gui v0.1.0
# A GUI for "kb" - a knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-GUI main module
:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

#kivy.require("2.0.0")


from kivymd.app import MDApp
from kb.config import BASE, get_current_base
from pathlib import Path
from presentation import populate_categories, construct_kb_title, show_base_list,show_right_menu

class gui(MDApp):

    def build(self):

        # Change the application icon
        self.icon=str(Path("../img/","kb-icon.png")) 

        # Get the list of knowledge bases available
        show_base_list(self,KB_DETAILS)

        # Get the list of categories from the knowledgebase
        populate_categories(self,KB_DETAILS)

        # Change the title of the window and the root node of the treeview
        self.title = construct_kb_title(KB_DETAILS, get_current_base(BASE))
        
        pass

    def left_menu_click(self):  
        print("left menu")

    def right_menu_click(self):  
        print("right menu")
        show_right_menu(self)

KB_DETAILS = dict(
    location = 'local',
    server = 'http://localhost:5000',
    user = 'kbuser',
    pwd = 'kbuser'
)

gui().run()