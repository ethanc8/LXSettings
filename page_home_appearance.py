import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_appearance(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        
        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Appearance", 
                description_str = 
"""The first place to go if you want
to change your desktop's look and feel.""",
                onclick_command = ['pcmanfm', '--desktop-pref'],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Additional appearance settings",
                description_str = """Change the look of:
- Gtk applications
- window borders
- icons
- fonts""", 
                onclick_command = ["lxappearance"],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Qt5 (advanced)",
                description_str = "Change the look of Qt5 applications",
                onclick_command = ["qt5ct"],
            )
        ]
        self.page_path_str = "Home -> Appearance"
        self.page_name = "Appearance"
        self.icon_name = "preferences-desktop-theme"
        
        super().init_end()

page_home_appearance = __page_home_appearance()
