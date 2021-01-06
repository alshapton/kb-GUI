# -*- encoding: utf-8 -*-
# kb-gui v0.1.0
# A GUI for "kb" - a knowledge base organizer
# Copyright © 2020, alshapton.
# See /LICENSE for licensing information.

"""
kb-GUI presentation module
:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict

from kb.config import get_current_base, DEFAULT_CONFIG,BASE
from functions.list import list_categories
from kivy.uix.treeview import TreeView, TreeViewLabel

def populate_categories(self,KB_DETAILS):
    # Construct treeview for the current knowledgebase
    # Change the Root node to contain the name of the knowledgebase
    cats = list_categories(DEFAULT_CONFIG,KB_DETAILS)
    self.title = construct_kb_title(KB_DETAILS, get_current_base(BASE))
    #self.root.ids.tv.root.text = "kb - " + KB_DETAILS['location'] + ":" + get_current_base(BASE) 
    self.root.ids.tv.root.text = self.title
    # Populate treeview with categories
    for category in cats:
        self.root.ids.tv.add_node(TreeViewLabel(text=category))

def construct_kb_title(KB_DETAILS: Dict[str,str], current_base:str):
    return "kb - " + KB_DETAILS['location'] + ":" + current_base
 
    