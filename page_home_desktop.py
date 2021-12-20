import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_desktop(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        # env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui
        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Desktop", 
                description_str = 
"""The first place to go if you want
to change your desktop's look and feel.""",
                onclick_command = ['pcmanfm', '--desktop-pref'],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Panel",
                description_str = "Change the look and behavior of the panel/menubar.",
                onclick_command = ["lxpanelctl", "config"],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Main Menu",
                description_str = "Change the items within the main menu.",
                onclick_command = ["alacarte"],
            ), LXSettings.DirectoryButton(
                icon_name = "system-file-manager",
                label_str = "File Manager",
                description_str = "Change how the file manager looks and behaves.",
                onclick_command = ["pcmanfm", "--show-pref=1"],
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
                icon_name = "xfce4-notifyd",
                label_str = "App Notifications",
                description_str = "Configure how app notifications work and see past notifications.",
                onclick_page_str = "Home -> Desktop -> Notifications",
            )
        ]
        self.page_path_str = "Home -> Desktop"
        self.page_name = "Desktop"
        self.icon_name = "user-desktop"
        
        super().init_end()

page_home_desktop = __page_home_desktop()
