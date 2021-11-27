import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_PAGE_PATH_IDENTIFIER(LXSettings.Page):
    def __init__(self):
        super().init_begin()

        self.page_path_str = "PAGE_PATH_STR"
        self.page_name = "PAGE_NAME_STR"
        self.icon_name = "PAGE_ICON_NAME"
        
        super().init_end()
    
    def on_enter(self):
        super().on_enter_begin()

        

        super().on_enter_end()

page_PAGE_PATH_IDENTIFIER = __page_PAGE_PATH_IDENTIFIER()
