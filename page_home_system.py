import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_system(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        # env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui
        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "rpi",
                label_str = "Raspberry Pi Configuration",
                description_str = "Change system settings, Raspberry Pi hardware settings, and localisation settings.",
                onclick = lambda _: [
                    LXSettings.open_process(["sudo", "-AE", "rc_gui"], {
                        "SUDO_ASKPASS" : "/usr/lib/rc-gui/pwdrcg.sh"
                    })
                ]
            ), LXSettings.DirectoryButton(
                icon_name = "xfce4-notifyd",
                label_str = "Notifications",
                description_str = "Configure how notifications work and see past notifications.",
                onclick_page_str = "Home -> System -> Notifications",
            ), LXSettings.DirectoryButton(
                icon_name = "timeshift",
                label_str = "Backup and Restore",
                description_str = "Back up and restore backups of the operating system.",
                onclick = lambda _: [
                    LXSettings.open_process(["sudo", "-A", "timeshift-launcher"], {
                        "SUDO_ASKPASS" : "/usr/lib/rc-gui/pwdrcg.sh"
                    })
                ]
            ), LXSettings.DirectoryButton(
                icon_name = "system-users",
                label_str = "Users",
                description_str = "Add, give permissions to, and remove users.",
                onclick_command = ["users-admin"],
            ), LXSettings.DirectoryButton(
                icon_name = "user-info",
                label_str = "About Me",
                description_str = "Add basic information to your profile.",
                onclick_command = ["mugshot"],
            ), LXSettings.DirectoryButton(
                icon_name = "time-admin",
                label_str = "Date and Time",
                description_str = "Change the date, time, and timezone",
                onclick_command = ["time-admin"],
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
                icon_name = "preferences-system-windows",
                label_str = "Window management (advanced)",
                description_str = "Change how windows look and are managed",
                onclick_command = ["obconf", "--tab", "3"],
            )
        ]
        self.page_path_str = "Home -> System"
        self.page_name = "System"
        self.icon_name = "preferences-system"
        
        super().init_end()

page_home_system = __page_home_system()
