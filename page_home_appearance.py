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
                onclick = lambda _: [
                    LXSettings.open_process(["pipanel", {
                        "SUDO_ASKPASS" : "/usr/lib/pipanel/pwdpip.sh"
                    }])
                ]
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Additional appearance settings",
                description_str = """Change the look of:
- Gtk applications
- window borders
- icons
- fonts""", 
                onclick_command = ["lxappearance"]
            ), LXSettings.DirectoryButton(
                icon_name = "system-file-manager",
                label_str = "Gtk File Chooser",
                description_str = "Change the look and feel of the Gtk file chooser",
                onclick_command = [
                    # "gtk3-nocsd",
                    "dconf-editor",
                    "/org/gtk/settings/file-chooser/",
                    "--I-understand-that-changing-options-can-break-applications"
                ],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Qt5 (advanced)",
                description_str = "Change the look of Qt5 applications",
                onclick_command = ["qt5ct"],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-system-windows",
                label_str = "Window management (advanced)",
                description_str = "Change how windows look and are managed",
                onclick_command = ["obconf", "--tab", "3"],
            )
        ]
        self.page_path_str = "Home -> Appearance"
        self.page_name = "Appearance"
        self.icon_name = "preferences-desktop-theme"
        
        super().init_end()

page_home_appearance = __page_home_appearance()
