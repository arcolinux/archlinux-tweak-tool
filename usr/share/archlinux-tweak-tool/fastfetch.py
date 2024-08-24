# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import os
import subprocess
import functions as fn
import re
import json

# ====================================================================
#                       Fastfetch
# ====================================================================

def get_fastfetch():
    """Get data from fastfetch_config JSONC file."""
    data = {}
    if fn.path.isfile(fn.fastfetch_config):
        with open(fn.fastfetch_config, "r", encoding="utf-8") as f:
            jsonc_content = f.read()
            print("Original JSONC Content:\n", jsonc_content)
            
            if not jsonc_content.strip():
                print("Error: Content is empty or invalid.")
                return data
            
            try:
                data = json.loads(jsonc_content)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON detected: {e}")
                print("Error: The configuration file is not valid JSON.")
    
    return data

def check_backend():
    """See if image backend is active."""
    if fn.path.isfile(fn.fastfetch_config):
        config = get_fastfetch()
        if config:
            image_backend = config.get("image_backend", None)
            if image_backend and not image_backend.startswith("#"):
                return image_backend.strip('"')
    return "ascii"

def check_ascii():
    """See if ASCII distro is active."""
    if fn.path.isfile(fn.fastfetch_config):
        config = get_fastfetch()
        if config:
            ascii_distro = config.get("ascii_distro", "auto")
            return ascii_distro.strip('"')
    return "auto"

def apply_config(self, backend, ascii_size):
    """Apply fastfetch configuration"""
    if fn.path.isfile(fn.fastfetch_config):
        with open(fn.fastfetch_config, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Mapping keys to checkboxes
        # Reads config file line by line for each model
        key_to_checkbox = {
            '"os"': self.os,
            '"host"': self.host,
            '"kernel"': self.kernel,
            '"uptime"': self.uptime,
            '"packages"': self.packages,
            '"shell"': self.shell,
            '"display"': self.display,
            '"de"': self.de,
            '"wm"': self.wm,
            '"wmtheme"': self.wmtheme,
            '"theme"': self.themes,
            '"icons"': self.icons,
            '"font"': self.font,
            '"cursor"': self.cursor,
            '"terminal"': self.term,
            '"terminalfont"': self.termfont,
            '"cpu"': self.cpu,
            '"gpu"': self.gpu,
            '"memory"': self.mem,
            '"swap"': self.swap,
            '"disk"': self.disks,
            '"localIP"': self.lIP,
            '"battery"': self.batt,
            '"poweradapter"': self.pwr,
            '"locale"': self.local,
            '"title"': self.title,
            '"underline"': self.title,  # Assuming underline is tied to the title checkbox
            '"colors"': self.cblocks,
        }
 
        # Comment or uncomment each key based on the checkbox state
        for i in range(len(lines)):
            for key, checkbox in key_to_checkbox.items():
                if key.lower() in lines[i].lower():
                    if checkbox.get_active() and lines[i].startswith("//"):
                        lines[i] = lines[i][2:]  # Uncomment the line
                    elif not checkbox.get_active() and not lines[i].startswith("//"):
                        lines[i] = "//" + lines[i]  # Comment the line

        # Write the updated lines back to the file
        with open(fn.fastfetch_config, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print("fastfetch settings saved successfully")
        fn.show_in_app_notification(self, "fastfetch settings saved successfully")

def get_checkbox_state(self, key):
    """Return the state of the checkbox corresponding to the given key."""
    # Mapping keys to checkboxes
    key_to_checkbox = {
        '"OS"': self.os,
        '"Host"': self.host,
        '"Kernel"': self.kernel,
        '"Uptime"': self.uptime,
        '"Packages"': self.packages,
        '"Shell"': self.shell,
        '"Display"': self.display,
        '"DE"': self.de,
        '"WM"': self.wm,
        '"WM Theme"': self.wmtheme,
        '"Theme"': self.themes,
        '"Icons"': self.icons,
        '"Font"': self.font,
        '"Cursor"': self.cursor,
        '"Terminal"': self.term,
        '"Terminal Font"': self.termfont,
        '"CPU"': self.cpu,
        '"GPU"': self.gpu,
        '"Memory"': self.mem,
        '"Swap"': self.swap,
        '"PowerAdapter"': self,
        '"Disk"': self.disks,
        '"Local IP"': self.lIP,
        '"Battery"': self.batt,
        '"Power Adapter"': self.pwr,
        '"Locale"': self.local,
        '"title"': self.title,
        '"underline"': self.title,  
        '"Color Blocks"': self.cblocks,
    }

    checkbox = key_to_checkbox.get(key)
    if checkbox is not None:
        return checkbox.get_active()

    return None

def get_checkboxes(self):
    """Read the state of the checkboxes from the JSONC configuration."""
    config = get_fastfetch()

    # Setting the active state of checkboxes based on configuration
    self.title.set_active(config.get("info", {}).get("title", False))
    self.os.set_active(config.get("info", {}).get("OS", False))
    self.host.set_active(config.get("info", {}).get("Host", False))
    self.kernel.set_active(config.get("info", {}).get("Kernel", False))
    self.uptime.set_active(config.get("info", {}).get("Uptime", False))
    self.packages.set_active(config.get("info", {}).get("Packages", False))
    self.shell.set_active(config.get("info", {}).get("Shell", False))
    self.display.set_active(config.get("info", {}).get("Display", False))
    self.de.set_active(config.get("info", {}).get("DE", False))
    self.wm.set_active(config.get("info", {}).get("WM", False))
    self.wmtheme.set_active(config.get("info", {}).get("WM Theme", False))
    self.themes.set_active(config.get("info", {}).get("Theme", False))
    self.icons.set_active(config.get("info", {}).get("Icons", False))
    self.font.set_active(config.get("info", {}).get("Font", False))
    self.cursor.set_active(config.get("info", {}).get("Cursor", False))
    self.term.set_active(config.get("info", {}).get("Terminal", False))
    self.termfont.set_active(config.get("info", {}).get("Terminal Font", False))
    self.cpu.set_active(config.get("info", {}).get("CPU", False))
    self.gpu.set_active(config.get("info", {}).get("GPU", False))
    self.mem.set_active(config.get("info", {}).get("Memory", False))
    self.swap.set_active(config.get("info", {}).get("Swap", False))
    self.disks.set_active(config.get("info", {}).get("Disk", False))
    self.lIP.set_active(config.get("info", {}).get("Local IP", False))
    self.batt.set_active(config.get("info", {}).get("Battery", False))
    self.pwr.set_active(config.get("info", {}).get("Power Adapter", False))
    self.local.set_active(config.get("info", {}).get("Locale", False))
    self.cblocks.set_active(config.get("info", {}).get("Color Blocks", False))

    # Setting the color blocks checkbox based on the configuration
    #self.cblocks.set_active(config.get("color_blocks", "off") == "on")

def set_checkboxes_normal(self):
    """Set the state of the checkboxes to the default or normal state."""
    self.title.set_active(True)
    self.os.set_active(True)
    self.host.set_active(True)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.display.set_active(True)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.font.set_active(True)
    self.cursor.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(True)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.swap.set_active(True)
    self.disks.set_active(True)
    self.lIP.set_active(False)
    self.batt.set_active(True)
    self.pwr.set_active(True)
    self.local.set_active(False)
    self.cblocks.set_active(False)

def set_checkboxes_small(self):
    """set the state of the checkboxes"""
    self.title.set_active(True)
    self.os.set_active(False)
    self.host.set_active(False)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.display.set_active(False)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.font.set_active(True)
    self.cursor.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(False)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.swap.set_active(True)
    self.disks.set_active(False)
    self.lIP.set_active(False)
    self.batt.set_active(True)
    self.pwr.set_active(True)
    self.local.set_active(False)
    self.cblocks.set_active(False)

def set_checkboxes_all(self):
    """set the state of the checkboxes"""
    self.title.set_active(True)
    self.os.set_active(True)
    self.host.set_active(True)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.display.set_active(True)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.font.set_active(True)
    self.cursor.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(True)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.swap.set_active(True)
    self.disks.set_active(True)
    self.lIP.set_active(True)
    self.batt.set_active(True)
    self.pwr.set_active(True)
    self.local.set_active(True)
    self.cblocks.set_active(True)
    
def set_checkboxes_none(self):
    """set the state of the checkboxes"""
    self.title.set_active(False)
    self.os.set_active(False)
    self.host.set_active(False)
    self.kernel.set_active(False)
    self.uptime.set_active(False)
    self.packages.set_active(False)
    self.shell.set_active(False)
    self.display.set_active(False)
    self.de.set_active(False)
    self.wm.set_active(False)
    self.wmtheme.set_active(False)
    self.themes.set_active(False)
    self.icons.set_active(False)
    self.font.set_active(False)
    self.cursor.set_active(False)
    self.term.set_active(False)
    self.termfont.set_active(False)
    self.cpu.set_active(False)
    self.gpu.set_active(False)
    self.mem.set_active(False)
    self.swap.set_active(False)
    self.disks.set_active(False)
    self.lIP.set_active(False)
    self.batt.set_active(False)
    self.pwr.set_active(False)
    self.local.set_active(False)
    self.cblocks.set_active(False)

def pop_distro_combobox(self, combo):
    """Populate the distro combo box with available options."""
    
    # Clear the existing items in the combo box
    combo.get_model().clear()
    
    # List of available distributions and operating systems
    list_distros = [
        "auto",
        "Antergos",
        "Anarchy",
        "Android",
        "Antergos",
        "antiX",
        "ArcoLinux",
        "ArchBox",
        "ARCHlabs",
        "ArchStrike",
        "Arch",
        "Artix",
        "Arya",
        "Bedrock",
        "BlackArch",
        "BSD",
        "BunsenLabs",
        "CentOS",
        "Chakra",
        "ClearOS",
        "Debian",
        "Deepin",
        "Elementary",
        "EndeavourOS",
        "Fedora",
        "Feren",
        "FreeBSD",
        "Frugalware",
        "Funtoo",
        "Garuda",
        "Gentoo",
        "GNOME",
        "GNU",
        "Kali",
        "KaOS",
        "KDE_neon",
        "Kubuntu",
        "LMDE",
        "Lubuntu",
        "macos",
        "Mageia",
        "MagpieOS",
        "Mandriva",
        "Manjaro",
        "Maui",
        "LinuxMint",
        "MX_Linux",
        "Namib",
        "NetBSD",
        "Netrunner",
        "Nitrux",
        "NixOS",
        "OBRevenge",
        "OpenBSD",
        "OpenMandriva",
        "Oracle",
        "PCLinuxOS",
        "Peppermint",
        "popos",
        "Puppy",
        "PureOS",
        "Raspbian",
        "Reborn_OS",
        "Redcore",
        "Redhat",
        "SalentOS",
        "Slackware",
        "Solus",
        "SteamOS",
        "SunOS",
        "openSUSE_Leap",
        "openSUSE_Tumbleweed",
        "openSUSE",
        "SwagArch",
        "Ubuntu-Budgie",
        "Ubuntu-GNOME",
        "Ubuntu-MATE",
        "Ubuntu-Studio",
        "Ubuntu",
        "Venom",
        "Void",
        "windows10",
        "Windows7",
        "Xubuntu",
        "Zorin",
    ]

    # Add each distro to the combo box
    for item in list_distros:
        combo.append_text(item)

    # Optional: Automatically set the active item based on a config value
    # Uncomment and adjust the following code if you want to pre-select an item
    # try:
    #     name = fn.get_position(fn.fastfetch_config, "ascii_distro=").split("=")[1].strip().lower()
    #     for i, item in enumerate(list_distros):
    #         if name == item.lower():
    #             combo.set_active(i)
    #             break
    # except IndexError:
    #     pass