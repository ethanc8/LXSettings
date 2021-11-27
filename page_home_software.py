import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_software(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        
        # pi-gpk commands:
        # pi-packages
        # pi-gpk-dbus-service
        # pi-gpk-install-local-file
        # pi-gpk-log
        # pi-gpk-prefs
        # pi-gpk-update-viewer

        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "emblem-default",
                label_str = "Default Apps",
                description_str = "Set the default apps.",
                onclick_command = ["lxsession-default-apps", "--profile=LXDE-pi"],
            ), LXSettings.DirectoryButton(
                icon_name = "system-software-install",
                label_str = "Add / Remove Software",
                description_str = "Select packages to install or remove.",
                onclick_command = ["pi-packages"],
            ), LXSettings.DirectoryButton(
                icon_name = "system-software-update",
                label_str = "Software Updates",
                description_str = "Install updates for the operating system and packages.",
                onclick_command = ["pi-gpk-update-viewer"],
            ), LXSettings.DirectoryButton(
                icon_name = "rpi",
                label_str = "Recommended Software",
                description_str = "Install software recommended by Raspberry Pi Trading Ltd.",
                onclick_command = ["rp-prefapps"],
            ), LXSettings.DirectoryButton(
                icon_name = "system-software-install",
                label_str = "Pi-Apps",
                description_str = "Install applications not available through APT.",
                onclick_command = ["/home/pi/pi-apps/gui"],
            ), LXSettings.DirectoryButton(
                icon_name = "system-software-update",
                label_str = "Pi-Apps Updater",
                description_str = "Update applications installed through Pi-Apps.",
                onclick_command = ["/home/pi/pi-apps/updater"],
            ), LXSettings.DirectoryButton(
                icon_name = "x-package-repository",
                label_str = "Pi-Apps Settings",
                description_str = "Configure the Pi-Apps app store.",
                onclick_command = ["/home/pi/pi-apps/settings"],
            ), 
        ]
        self.page_path_str = "Home -> Software"
        self.page_name = "Software"
        self.icon_name = "system-software-install"
        
        super().init_end()

page_home_software = __page_home_software()
