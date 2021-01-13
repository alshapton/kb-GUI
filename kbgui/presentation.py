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
from functions.list import list_bases, list_categories
from kivy.uix.treeview import TreeViewLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup

from kivymd.uix.dialog import MDDialog


Builder.load_string('''
<BaseListPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Choose a knowledge base'
    BoxLayout:
        id: bl
        orientation: 'vertical'
        canvas.before:
            Color: 
                rgba:72/255,105/255,141/255,1
            Rectangle:
                pos: self.pos
                size: self.size
        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
            
        ScrollView:
            id: sv 
            MDList:
                id: container
        FloatLayout:
            orientation: 'vertical'
            Button:
                id: cancel_button
                pos_hint : {'center_x': 0.28, 'center_y': 0.5}
                size_hint: 0.3,0.3
                background_color: 36/255,148/255,243/255,1
                text: 'Cancel'    
                on_press: root.dismiss()
                color: 1,1,1,1
            Button:
                id: ok_button
                pos_hint : {'center_x': 0.71, 'center_y': 0.5}
                size_hint: 0.3,0.3
                background_color: 36/255,148/255,243/255,1
                text: 'OK'    
                on_press: root.dismiss()
                color: 1,1,1,1
''')

class Item(OneLineListItem):
    divider='Partial'

class BaseListPopup(Popup):
    pass


def show_resource_unavailable(self,resource, msg):
    self.dialog = MDDialog(
                title=resource + " Unavailable",
                text=msg,
                buttons=[
                    MDFlatButton(
                        text="OK", 
                        text_color=self.theme_cls.primary_color
                    ),
                ],
            )
    self.dialog.open()


def show_right_menu(self):
    print("here")
    pass


def show_bases_popup(self, bases:Dict[str,str]):
    bases_popup = BaseListPopup()
    idx = 1
    for base in bases:
        new_item = Item(text=base["name"] + " - " + base["description"],
        bg_color=(1,1,1,1))
        bases_popup.ids.container.add_widget(new_item,index=idx)
        idx = idx + 1
    bases_popup.open()

def populate_categories(self,KB_DETAILS):
    # Construct treeview for the current knowledgebase
    # Change the Root node to contain the name of the knowledgebase
    try:
        cats = list_categories(DEFAULT_CONFIG,KB_DETAILS)
    except Exception as _e:
        if KB_DETAILS['location'] == 'remote':
            show_resource_unavailable(self, "Server", "The server that contains your chosen knowledgebase is not currently available. Please either:\n* Select another knowledge base\n * Try again later\n* Inform the administrator of the server")
        pass
    else:
        self.title = construct_kb_title(KB_DETAILS, get_current_base(BASE))
        self.root.ids.tv.root.text = self.title
        
        # Populate treeview with categories
        for category in cats:
            self.root.ids.tv.add_node(TreeViewLabel(text=category))

def show_base_list(self,KB_DETAILS):
    # Get list of knoowledge bases
    try:
        bases = list_bases(DEFAULT_CONFIG,KB_DETAILS)
        show_bases_popup(self,bases)
    except Exception as _e:
        if KB_DETAILS['location'] == 'remote':
            show_resource_unavailable(self, "Server", "The server is not currently available. Please either:\n* Select another knowledge base on a different kb server\n * Try again later\n* Inform the administrator of the server")
        else:
            show_resource_unavailable(self, "KB Information", "The KB setup appears to be damaged. Please reinstall the software. Be sure to take backups of your data first")
        pass


def construct_kb_title(KB_DETAILS: Dict[str,str], current_base:str):
    return "kb - " + KB_DETAILS['location'] + ":" + current_base
 
    