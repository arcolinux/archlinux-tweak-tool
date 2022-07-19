# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

# import os
import functions as fn


# ====================================================================
#                       NEOFETCH
# ====================================================================


def get_neofetch():
    """get lines from neofetch_config"""
    lines = []
    if fn.path.isfile(fn.neofetch_config):
        with open(fn.neofetch_config, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()

    return lines


def check_backend():
    """see if image is active"""
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for item in enumerate(lines):
            if "image_backend=" in item:
                if not "#" in item:
                    line = item.split("=")[1].replace('"', "").strip()
                    return line
    return "ascii"


def check_ascii():
    """see if ascii is active"""
    line = "auto"
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for item in enumerate(lines):
            if "ascii_distro=" in item:
                line = item.split("=")[1].replace('"', "").strip()
                return line


def apply_config(self, backend, ascii_size):
    """apply neofetch configuration"""
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        # TODO:enumerate lines
        for i in range(len(lines)):
            if self.os.get_active():
                fn.neofetch_set_value(lines, i, 'info "OS"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "OS"', False)
            if self.host.get_active():
                fn.neofetch_set_value(lines, i, 'info "Host"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Host"', False)
            if self.kernel.get_active():
                fn.neofetch_set_value(lines, i, 'info "Kernel"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Kernel"', False)
            if self.uptime.get_active():
                fn.neofetch_set_value(lines, i, 'info "Uptime"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Uptime"', False)
            if self.packages.get_active():
                fn.neofetch_set_value(lines, i, 'info "Packages"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Packages"', False)
            if self.shell.get_active():
                fn.neofetch_set_value(lines, i, 'info "Shell"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Shell"', False)
            if self.res.get_active():
                fn.neofetch_set_value(lines, i, 'info "Resolution"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Resolution"', False)
            if self.de.get_active():
                fn.neofetch_set_value(lines, i, 'info "DE"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "DE"', False)
            if self.wm.get_active():
                fn.neofetch_set_value(lines, i, 'info "WM"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "WM"', False)
            if self.wmtheme.get_active():
                fn.neofetch_set_value(lines, i, 'info "WM Theme"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "WM Theme"', False)
            if self.themes.get_active():
                fn.neofetch_set_value(lines, i, 'info "Theme"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Theme"', False)
            if self.icons.get_active():
                fn.neofetch_set_value(lines, i, 'info "Icons"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Icons"', False)
            if self.term.get_active():
                fn.neofetch_set_value(lines, i, 'info "Terminal"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Terminal"', False)
            if self.termfont.get_active():
                fn.neofetch_set_value(lines, i, 'info "Terminal Font"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Terminal Font"', False)
            if self.cpu.get_active():
                fn.neofetch_set_value(lines, i, 'info "CPU"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "CPU"', False)
            if self.gpu.get_active():
                fn.neofetch_set_value(lines, i, 'info "GPU"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "GPU"', False)
            if self.mem.get_active():
                fn.neofetch_set_value(lines, i, 'info "Memory"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Memory"', False)
            if self.gpu_driver.get_active():
                fn.neofetch_set_value(lines, i, 'info "GPU Driver"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "GPU Driver"', False)
            if self.cpu_usage.get_active():
                fn.neofetch_set_value(lines, i, 'info "CPU Usage"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "CPU Usage"', False)
            if self.disks.get_active():
                fn.neofetch_set_value(lines, i, 'info "Disk"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Disk"', False)
            if self.font.get_active():
                fn.neofetch_set_value(lines, i, 'info "Font"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Font"', False)
            if self.song.get_active():
                fn.neofetch_set_value(lines, i, 'info "Song"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Song"', False)
            if self.lIP.get_active():
                fn.neofetch_set_value(lines, i, 'info "Local IP"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Local IP"', False)
            if self.PIP.get_active():
                fn.neofetch_set_value(lines, i, 'info "Public IP"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Public IP"', False)
            if self.users.get_active():
                fn.neofetch_set_value(lines, i, 'info "Users"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Users"', False)
            if self.local.get_active():
                fn.neofetch_set_value(lines, i, 'info "Locale"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Locale"', False)
            if self.title.get_active():
                fn.neofetch_set_value(lines, i, "info title", True)
                fn.neofetch_set_value(lines, i, "info underline", True)
            else:
                fn.neofetch_set_value(lines, i, "info title", False)
                fn.neofetch_set_value(lines, i, "info underline", False)

            if not backend == "ascii" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "w3m")
                # fn.neofetch_set_backend_value(lines, i, "image_backend=\"ascii\"")
                fn.neofetch_set_value(lines, i, "image_source=", False)
                # fn.neofetch_set_value(lines, i, emblem, True)

            elif not backend == "w3m" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "ascii")
                # fn.neofetch_set_value(lines, i, "image_backend=\"ascii\"", True)
                # fn.neofetch_set_value(lines, i, "image_backend=\"" + backend_val + "\"", False)
                if "ascii_distro=" in lines[i]:
                    lines[i] = 'ascii_distro="' + ascii_size + '"\n'
            else:
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "off")

            if self.cblocks.get_active():
                fn.neofetch_set_backend_value(lines, i, 'color_blocks="', "on")
            else:
                fn.neofetch_set_backend_value(lines, i, 'color_blocks="', "off")

        with open(fn.neofetch_config, "w", encoding="utf-8") as f:
            f.writelines(lines)
            f.close()
        print("Neofetch settings saved successfully")
        fn.show_in_app_notification(self, "Neofetch settings saved successfully")


def get_state(value):
    """found out what is active and what is not active"""
    lines = get_neofetch()
    # TODO:enumerate lines
    for i in range(len(lines)):
        if value in lines[i]:
            if "#" in lines[i]:
                return False
    return True


def get_checkboxes(self):
    """read the state of the checkbouxes"""
    self.os.set_active(get_state('info "OS"'))
    self.host.set_active(get_state('info "Host"'))
    self.kernel.set_active(get_state('info "Kernel"'))
    self.uptime.set_active(get_state('info "Uptime"'))
    self.packages.set_active(get_state('info "Packages"'))
    self.shell.set_active(get_state('info "Shell"'))
    self.res.set_active(get_state('info "Resolution"'))
    self.de.set_active(get_state('info "DE"'))
    self.wm.set_active(get_state('info "WM"'))
    self.wmtheme.set_active(get_state('info "WM Theme"'))
    self.themes.set_active(get_state('info "Theme"'))
    self.icons.set_active(get_state('info "Icons"'))
    self.term.set_active(get_state('info "Terminal"'))
    self.termfont.set_active(get_state('info "Terminal Font"'))
    self.cpu.set_active(get_state('info "CPU"'))
    self.gpu.set_active(get_state('info "GPU"'))
    self.mem.set_active(get_state('info "Memory"'))
    self.title.set_active(get_state("info title"))

    self.gpu_driver.set_active(get_state('info "GPU Driver"'))
    self.cpu_usage.set_active(get_state('info "CPU Usage"'))
    self.disks.set_active(get_state('info "Disk"'))
    self.font.set_active(get_state('info "Font"'))
    self.song.set_active(get_state('info "Song"'))
    self.lIP.set_active(get_state('info "Local IP"'))
    self.PIP.set_active(get_state('info "Public IP"'))
    self.users.set_active(get_state('info "Users"'))
    self.local.set_active(get_state('info "Locale"'))

    lines = get_neofetch()

    line = [x for x in lines if "color_blocks=" in x]
    if "on" in line[0]:
        self.cblocks.set_active(True)
    else:
        self.cblocks.set_active(False)


def set_checkboxes_normal(self):
    """set the state of the checkboxes"""
    self.os.set_active(True)
    self.host.set_active(True)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.res.set_active(True)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(True)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.title.set_active(True)

    self.gpu_driver.set_active(True)
    self.cpu_usage.set_active(True)
    self.disks.set_active(True)
    self.font.set_active(True)
    self.song.set_active(False)
    self.lIP.set_active(False)
    self.PIP.set_active(False)
    self.users.set_active(False)
    self.local.set_active(False)
    self.cblocks.set_active(True)


def set_checkboxes_small(self):
    """set the state of the checkboxes"""
    self.os.set_active(False)
    self.host.set_active(False)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.res.set_active(False)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(False)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.title.set_active(False)

    self.gpu_driver.set_active(False)
    self.cpu_usage.set_active(False)
    self.disks.set_active(False)
    self.font.set_active(False)
    self.song.set_active(False)
    self.lIP.set_active(False)
    self.PIP.set_active(False)
    self.users.set_active(False)
    self.local.set_active(False)
    self.cblocks.set_active(False)


def set_checkboxes_all(self):
    """set the state of the checkboxes"""
    self.os.set_active(True)
    self.host.set_active(True)
    self.kernel.set_active(True)
    self.uptime.set_active(True)
    self.packages.set_active(True)
    self.shell.set_active(True)
    self.res.set_active(True)
    self.de.set_active(True)
    self.wm.set_active(True)
    self.wmtheme.set_active(True)
    self.themes.set_active(True)
    self.icons.set_active(True)
    self.term.set_active(True)
    self.termfont.set_active(True)
    self.cpu.set_active(True)
    self.gpu.set_active(True)
    self.mem.set_active(True)
    self.title.set_active(True)

    self.gpu_driver.set_active(True)
    self.cpu_usage.set_active(True)
    self.disks.set_active(True)
    self.font.set_active(True)
    self.song.set_active(True)
    self.lIP.set_active(True)
    self.PIP.set_active(True)
    self.users.set_active(True)
    self.local.set_active(True)
    self.cblocks.set_active(True)


def set_checkboxes_none(self):
    """set the state of the checkboxes"""
    self.os.set_active(False)
    self.host.set_active(False)
    self.kernel.set_active(False)
    self.uptime.set_active(False)
    self.packages.set_active(False)
    self.shell.set_active(False)
    self.res.set_active(False)
    self.de.set_active(False)
    self.wm.set_active(False)
    self.wmtheme.set_active(False)
    self.themes.set_active(False)
    self.icons.set_active(False)
    self.term.set_active(False)
    self.termfont.set_active(False)
    self.cpu.set_active(False)
    self.gpu.set_active(False)
    self.mem.set_active(False)
    self.title.set_active(False)

    self.gpu_driver.set_active(False)
    self.cpu_usage.set_active(False)
    self.disks.set_active(False)
    self.font.set_active(False)
    self.song.set_active(False)
    self.lIP.set_active(False)
    self.PIP.set_active(False)
    self.users.set_active(False)
    self.local.set_active(False)
    self.cblocks.set_active(False)


def pop_distro_combobox(self, combo):
    """populate distro box"""
    coms = []
    combo.get_model().clear()
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
        "Redhat,SalentOS",
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

    for items in list_distros:
        coms.append(items)

    # try:
    #     name = fn.get_position(fn.neofetch_config, "ascii_distro=").split("=")[1]
    # except IndexError:
    #     name = ""

    # coms.sort()
    for i, item in enumerate(coms):
        combo.append_text(item)
        # if name.lower() == item.lower():
        #     combo.set_active(i)
