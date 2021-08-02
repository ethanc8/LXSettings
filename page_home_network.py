import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

class __page_home_network(LXSettings.DirectoryPage):
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
                icon_name = "network-wireless-connected-100",
                label_str = "Wi-Fi (advanced)",
                description_str = "Configure advanced Wi-Fi settings.",
                onclick_command = ["wpa_gui", "-i", "wlan0"],
            ), 
        ]
        self.page_path_str = "Home -> Network"
        self.page_name = "Network"
        self.icon_name = "preferences-system-network"
        
        super().init_end()

page_home_network = __page_home_network()
