import subprocess
import os
import apt_pkg # Apparently, `apt` doesn't have a way to get the current version.
apt_pkg.init()
from datetime import datetime

class __SystemInformation:
    @property
    def lsb_release_distribution(self):
        return self.lsb_release_info("--id")
    
    def lsb_release_full_name(self, return_debian_minor_version: bool = False):
        if return_debian_minor_version:
            return self.lsb_release_info("--description", addenv={
                "LSB_OS_RELEASE" : "",
            })
        else:
            return self.lsb_release_info("--description")
    
    def lsb_release_number(self, return_debian_minor_version: bool = False):
        if return_debian_minor_version:
            return self.lsb_release_info("--release", addenv={
                "LSB_OS_RELEASE" : "",
            })
        else:
            return self.lsb_release_info("--release")
    
    def lsb_release_codename(self, return_debian_minor_version: bool = False):
        if return_debian_minor_version:
            return self.lsb_release_info("--codename", addenv={
                "LSB_OS_RELEASE" : "",
            })
        else:
            return self.lsb_release_info("--codename")
    
    def lsb_release_info(self, arg: str, addenv = {}):
        return subprocess.run(
            ["lsb_release", arg, "--short"],
            text=True, capture_output=True,
            env={
                **os.environ,
                **addenv,
            },
        ).stdout.strip()
    
    def apt_package_version(self, package_name: str) -> str:
        cache = apt_pkg.Cache()
        pkg = cache[package_name]
        return pkg.current_ver.ver_str

    def parse_rpi_version_date(self, rpi_version_date) -> datetime:
        return datetime.strptime(rpi_version_date, "%Y%m%d")
    
    def remove_affixes_from_str(self, string: str, prefix: str = "", suffix: str = ""):
        if (prefix != "") and (string.startswith(prefix)):
            string = string[len(prefix):]
        if (suffix != "") and (string.endswith(suffix)):
            string = string[:-len(suffix)]
        return string

    @property
    def rpi_firmware_release_date(self) -> datetime:
        version_str = self.apt_package_version("libraspberrypi0") # Example: "1:1.20210727-1"
        version_date = self.remove_affixes_from_str(version_str, "1:1.", "-1")
        return self.parse_rpi_version_date(version_date)
    
    @property
    def rpi_sys_mods_release_date(self) -> datetime:
        version_str = self.apt_package_version("raspberrypi-sys-mods") # Example: "20210706"
        return self.parse_rpi_version_date(version_str)

    @property
    def rpi_ui_mods_release_date(self) -> datetime:
        version_str = self.apt_package_version("raspberrypi-ui-mods") # Example: "1.20210706"
        version_date = self.remove_affixes_from_str(version_str, "1.", "")
        return self.parse_rpi_version_date(version_date)
    
    @property
    def rpi_os_release_date(self) -> datetime:
        return max(self.rpi_firmware_release_date, self.rpi_sys_mods_release_date, self.rpi_ui_mods_release_date)

sysinfo = __SystemInformation()
