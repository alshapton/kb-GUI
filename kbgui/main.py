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
import os

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kb.config import get_current_base, DEFAULT_CONFIG,BASE
from functions.list import list_categories
from pathlib import Path

from presentation import populate_categories, construct_kb_title

class gui(MDApp):

    def build(self):

        # Change the application icon
        self.icon=str(Path("../img/","kb-icon.png")) 
        self.title = construct_kb_title(KB_DETAILS, get_current_base(BASE))

        # Get the list of categories from the knowledgebase
        populate_categories(self,KB_DETAILS)

        pass

    def left_menu_click(self):  
        print("left menu")

    def right_menu_click(self):  
        print("right menu")

KB_DETAILS = dict(
    location = 'remote',
    server = 'http://localhost:5000',
    user = 'kbuser',
    pwd = 'kbuser'
)

gui().run()