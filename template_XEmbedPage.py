import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_PAGE_PATH_IDENTIFIER(LXSettings.XEmbedPage):
    def __init__(self):
        super().init_begin()

        self.page_path_str = "PAGE_PATH_STR"
        self.page_name = "PAGE_NAME_STR"
        self.icon_name = "PAGE_ICON_NAME"
        
        super().init_end()
    
    def on_enter(self):
        super().on_enter_begin()

        print(self.window_id)

        if self.window_id != 0:
            LXSettings.open_process(["EMBEDDED_WINDOW_COMMANDS", str(self.window_id)])
        else:
            print("The window ID is equal to 0!")

        print(self.socket)
        print(self.socket.get_plug_window())

        super().on_enter_end()

page_PAGE_PATH_IDENTIFIER = __page_PAGE_PATH_IDENTIFIER()
