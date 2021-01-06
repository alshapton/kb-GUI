from kb.config import get_current_base, DEFAULT_CONFIG,BASE
from functions.list import list_categories
from kivy.uix.treeview import TreeView, TreeViewLabel

def populate_categories(self):
    # Construct treeview for the current knowledgebase
    # Change the Root node to contain the name of the knowledgebase
    self.root.ids.tv.root.text = "kb - " + get_current_base(BASE)
    cats = list_categories(DEFAULT_CONFIG,'remote')
    
    # Populate treeview with categories
    for category in cats:
        self.root.ids.tv.add_node(TreeViewLabel(text=category))
    