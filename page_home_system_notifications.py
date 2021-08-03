import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_system_notifications(LXSettings.XEmbedPage):
    def __init__(self):
        super().init_begin()

        self.page_path_str = "Home -> System -> Notifications"
        self.page_name = "Notifications"
        self.icon_name = "xfce4-notifyd"
        
        super().init_end()
    
    def on_enter(self):
        super().on_enter_begin()

        print(self.window_id)

        if self.window_id != 0:
            LXSettings.open_process(["xfce4-notifyd-config", "--socket-id=" + str(self.window_id)])
        else:
            print("The window ID is equal to 0!")

        print(self.socket)
        print(self.socket.get_plug_window())

        super().on_enter_end()

page_home_system_notifications = __page_home_system_notifications()
