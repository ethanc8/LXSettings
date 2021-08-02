import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_devices(LXSettings.DirectoryPage):
    def __init__(self):
        super().init_begin()
        
        self.items = [
            LXSettings.DirectoryButton(
                icon_name = "preferences-desktop-peripherals",
                label_str = "Keyboard and Mouse",
                description_str = "Change mouse speed and keyboard layout.",
                onclick_command = ["lxinput"],
            ), LXSettings.DirectoryButton(
                icon_name = "computer",
                label_str = "Monitors",
                description_str = "Change monitor resolution, display rate, and layout",
                onclick_command = ["arandr"],
            ), LXSettings.DirectoryButton(
                icon_name = "preferences-system-bluetooth",
                label_str = "Bluetooth",
                description_str = "Connect and disconnect from Bluetooth devices",
                onclick_command = ["blueman-manager"],
            ), LXSettings.DirectoryButton(
                icon_name = "printer",
                label_str = "Printers",
                description_str = "Connect to printers and view print jobs.",
                onclick_command = ["system-config-printer"],
            ), LXSettings.DirectoryButton(
                icon_name = "printer",
                label_str = "Printers (advanced)",
                description_str = "Manage the printing system via the CUPS web interface.",
                onclick_command = ["chromium-browser", "--app=https://localhost:631", "--allow-insecure-localhost"],
            ), LXSettings.DirectoryButton(
                icon_name = "multimedia-volume-control",
                label_str = "Speaker and Microphone",
                description_str = "Change the preferred audio devices and their volumes.",
                onclick_command = ["pavucontrol"],
            ), 
            # ["preferences-desktop-peripherals", "Keyboard and Mouse", "Change mouse speed and keyboard layout.", lambda _: [
            #     LXSettings.open_process(["lxinput"]),
            # ]],
            # ["computer", "Monitors", "Change monitor resolution, display rate, and layout", lambda _: [
            #     LXSettings.open_process(["arandr"]),
            # ]],
            # ["preferences-system-bluetooth", "Bluetooth (advanced)", "Connect and disconnect from Bluetooth devices.", lambda _: [
            #     LXSettings.open_process(["blueman-manager"]),
            # ]],
            # ["printer", "Printing", "Connect to printers and view print jobs.", lambda _: [
            #     LXSettings.open_process(["system-config-printer"]),
            # ]],
            # ["printer", "Printing (advanced)", "Manage the printing system via the CUPS web interface.", lambda _: [
            #     LXSettings.open_process(["chromium-browser", "--app=https://localhost:631", "--allow-insecure-localhost"]),
            # ]]
        ]
        self.page_path_str = "Home -> Devices"
        self.page_name = "Devices"
        self.icon_name = "preferences-desktop-peripherals"
        
        super().init_end()

page_home_devices = __page_home_devices()
