import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import LXSettings

class __page_home(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        
        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-theme",
                label_str = "Appearance",
                description_str = "Change how your desktop and apps look and feel.",
                onclick_page_str = "Home -> Appearance",
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-system",
                label_str = "System",
                description_str = "Configure your operating system.",
                onclick_page_str = "Home -> System",
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-peripherals",
                label_str = "Devices",
                description_str = "Add, remove, and configure USB, Bluetooth, and networked devices.",
                onclick_page_str = "Home -> Devices",
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-system-network",
                label_str = "Network",
                description_str = "Manage Internet connections and what you share with others.",
                onclick_page_str = "Home -> Network",
            ), LXSettings.DirectoryButton(
                icon_name = "system-software-install",
                label_str = "Software",
                description_str = "Install and remove software.",
                onclick_page_str = "Home -> Software",
            ), 
#             ["preferences-desktop-theme", "Appearance", "Change how your desktop and apps look and feel.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Appearance"),
#             ]],
#             ["preferences-desktop-peripherals", "Devices", "Add, remove, and configure USB, Bluetooth, and networked devices.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Devices"),
#             ]],
#             ["preferences-system-network", "Network", "Manage Ethernet, Wi-Fi, local network, and Internet connections.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Network"),
#             ]],
#             ["rpi", "Raspberry Pi Hardware", "Manage your Raspberry Pi.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Raspberry Pi Hardware"),
#             ]],
#             ["system-software-install", "Software", "Install and remove software.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Software"),
#             ]],
#             ["user-info", "Users", "Manage users and their passwords.", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> Users"),
#             ]],
#             ["help-about", "About", 
# """Information about this Raspberry Pi,
# the operating system, and other information.""", lambda sender: [
#                 LXSettings.main_stack.navigateToPage("Home -> About"),
#             ]]
        ]
        self.page_path_str = "Home"
        self.page_name = "Home"
        self.icon_name = "user-home"
        
        super().init_end()

page_home = __page_home()
