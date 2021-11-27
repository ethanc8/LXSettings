import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import LXSettings

from SystemInformation import sysinfo

class actual_page_home_about(LXSettings.Page):
    def __init__(self):
        super().init_begin()

        self.top_widget = Gtk.Box(spacing = 6)
        self.top_widget.props.orientation = Gtk.Orientation.VERTICAL

        self.page_path_str = "Home -> About (loaded)"
        self.page_name = "About (loaded)"
        self.icon_name = "help-about"

        self.top_widget = Gtk.Box(spacing = 6)
        self.top_widget.props.orientation = Gtk.Orientation.VERTICAL

        os_logo = Gtk.Image.new_from_icon_name("rpi", Gtk.IconSize.DIALOG)
        self.top_widget.add(os_logo)

        os_label = Gtk.Label.new()
        os_label.set_markup("<big><b>" + "Raspberry Pi OS" + "</b></big>")
        self.top_widget.add(os_label)
        
        os_version_label = Gtk.Label.new()
        os_version_label.set_markup("based on " + sysinfo.lsb_release_full_name(True) + ".")
        self.top_widget.add(os_version_label)

        os_date_label = Gtk.Label.new()
        os_date_label.set_markup("Version " + sysinfo.rpi_os_release_date.strftime("%Y %B %d") + "")
        self.top_widget.add(os_date_label)

        self.top_widget.show()
        super().init_end()
    
        LXSettings.main_stack.addPage(self)

    @classmethod
    def sharedPage(cls):
        if cls.shared_page == None:
            cls.shared_page = cls()
        return cls.shared_page

setattr(actual_page_home_about, "shared_page", None)

class __page_home_about(LXSettings.Page):
    def __init__(self):
        super().init_begin()

        self.top_widget = Gtk.Box(spacing = 6)
        self.top_widget.props.orientation = Gtk.Orientation.VERTICAL

        self.page_path_str = "Home -> About (loading...)"
        self.page_name = "About (loading...)"
        self.icon_name = "help-about"

        self.has_loaded = False

        self.top_widget.show()
        super().init_end()
    
    def on_enter(self):
        super().on_enter_begin()

        if not self.has_loaded:
            actual_page_home_about.sharedPage()

        super().on_enter_end()

        print("Navigating to loaded page...")
        LXSettings.main_stack.navigateToPage("Home -> About (loaded)")


        

page_home_about = __page_home_about()
