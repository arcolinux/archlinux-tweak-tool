#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn
import os

# ====================================================================
#                       NEOFETCH
# ====================================================================

def get_neofetch():
    lines = []
    if os.path.isfile(fn.neofetch_config):
        with open(fn.neofetch_config, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()

    return lines

def pop_neofetch_box(combo):
    if os.path.isfile(fn.neofetch_config):
        com = []
        for image in os.listdir(fn.home + "/.config/neofetch/"):
            if ".png" in image:
                com.append(image)

        sorted_com = sorted(com)
        active = 0
        lines = get_neofetch()

        for i in range(len(lines)):
            if "image_source" in lines[i]:
                if not "#" in lines[i]:
                    line = lines[i].split("=")[1].replace("\"", "")
                    active = i+1

        for i in range(len(sorted_com)):
            combo.append_text(sorted_com[i])
            #if sorted_com[i] == active:
        combo.set_active(i)

def check_backend():
    if os.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for i in range(len(lines)):
            if "image_backend=" in lines[i]:
                if not "#" in lines[i]:
                    line = lines[i].split("=")[1].replace("\"", "").strip()
                    return line
    return "ascii"

def check_ascii():
    line = "auto"
    if os.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for i in range(len(lines)):
            if "ascii_distro=" in lines[i]:
                line = lines[i].split("=")[1].replace("\"", "").strip()
    return line

def apply_config(self, backend, ascii_size):
    if os.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        # try:
        for i in range(len(lines)):
            if self.os.get_active():
                fn.neofetch_set_value(lines, i, "info \"OS\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"OS\"", False)
            if self.host.get_active():
                fn.neofetch_set_value(lines, i, "info \"Host\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Host\"", False)
            if self.kernel.get_active():
                fn.neofetch_set_value(lines, i, "info \"Kernel\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Kernel\"", False)
            if self.uptime.get_active():
                fn.neofetch_set_value(lines, i, "info \"Uptime\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Uptime\"", False)
            if self.packages.get_active():
                fn.neofetch_set_value(lines, i, "info \"Packages\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Packages\"", False)
            if self.shell.get_active():
                fn.neofetch_set_value(lines, i, "info \"Shell\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Shell\"", False)
            if self.res.get_active():
                fn.neofetch_set_value(lines, i, "info \"Resolution\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Resolution\"", False)
            if self.de.get_active():
                fn.neofetch_set_value(lines, i, "info \"DE\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"DE\"", False)
            if self.wm.get_active():
                fn.neofetch_set_value(lines, i, "info \"WM\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"WM\"", False)
            if self.wmtheme.get_active():
                fn.neofetch_set_value(lines, i, "info \"WM Theme\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"WM Theme\"", False)
            if self.themes.get_active():
                fn.neofetch_set_value(lines, i, "info \"Theme\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Theme\"", False)
            if self.icons.get_active():
                fn.neofetch_set_value(lines, i, "info \"Icons\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Icons\"", False)
            if self.term.get_active():
                fn.neofetch_set_value(lines, i, "info \"Terminal\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Terminal\"", False)
            if self.termfont.get_active():
                fn.neofetch_set_value(lines, i, "info \"Terminal Font\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Terminal Font\"", False)
            if self.cpu.get_active():
                fn.neofetch_set_value(lines, i, "info \"CPU\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"CPU\"", False)
            if self.gpu.get_active():
                fn.neofetch_set_value(lines, i, "info \"GPU\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"GPU\"", False)
            if self.mem.get_active():
                fn.neofetch_set_value(lines, i, "info \"Memory\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Memory\"", False)
            if self.gpu_driver.get_active():
                fn.neofetch_set_value(lines, i, "info \"GPU Driver\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"GPU Driver\"", False)
            if self.cpu_usage.get_active():
                fn.neofetch_set_value(lines, i, "info \"CPU Usage\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"CPU Usage\"", False)
            if self.disks.get_active():
                fn.neofetch_set_value(lines, i, "info \"Disk\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Disk\"", False)
            if self.font.get_active():
                fn.neofetch_set_value(lines, i, "info \"Font\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Font\"", False)
            if self.song.get_active():
                fn.neofetch_set_value(lines, i, "info \"Song\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Song\"", False)
            if self.lIP.get_active():
                fn.neofetch_set_value(lines, i, "info \"Local IP\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Local IP\"", False)
            if self.PIP.get_active():
                fn.neofetch_set_value(lines, i, "info \"Public IP\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Public IP\"", False)
            if self.users.get_active():
                fn.neofetch_set_value(lines, i, "info \"Users\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Users\"", False)
            if self.local.get_active():
                fn.neofetch_set_value(lines, i, "info \"Locale\"", True)
            else:
                fn.neofetch_set_value(lines, i, "info \"Locale\"", False)
            if self.title.get_active():
                fn.neofetch_set_value(lines, i, "info title", True)
                fn.neofetch_set_value(lines, i, "info underline", True)
            else:
                fn.neofetch_set_value(lines, i, "info title", False)
                fn.neofetch_set_value(lines, i, "info underline", False)

            if not backend == "ascii" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, "image_backend=\"", "w3m")
                # fn.neofetch_set_backend_value(lines, i, "image_backend=\"ascii\"")
                fn.neofetch_set_value(lines, i, "image_source=", False)
                #fn.neofetch_set_value(lines, i, emblem, True)

            elif not backend == "w3m" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, "image_backend=\"", "ascii")
                # fn.neofetch_set_value(lines, i, "image_backend=\"ascii\"", True)
                # fn.neofetch_set_value(lines, i, "image_backend=\"" + backend_val + "\"", False)
                if "ascii_distro=" in lines[i]:
                    lines[i] = "ascii_distro=\"" + ascii_size + "\"\n"
            else:
                fn.neofetch_set_backend_value(lines, i, "image_backend=\"", "off")

            if self.cblocks.get_active():
                fn.neofetch_set_backend_value(lines, i, "color_blocks=\"", "on")
            else:
                fn.neofetch_set_backend_value(lines, i, "color_blocks=\"", "off")

        with open(fn.neofetch_config, "w") as f:
            f.writelines(lines)
            f.close()
        print("Neofetch settings saved successfully")
        fn.show_in_app_notification(self, "Neofetch settings saved successfully")

def get_state(value):
    lines = get_neofetch()

    for i in range(len(lines)):
        if value in lines[i]:
            if "#" in lines[i]:
                return False
    return True

def get_checkboxes(self):
    self.os.set_active(get_state("info \"OS\""))
    self.host.set_active(get_state("info \"Host\""))
    self.kernel.set_active(get_state("info \"Kernel\""))
    self.uptime.set_active(get_state("info \"Uptime\""))
    self.packages.set_active(get_state("info \"Packages\""))
    self.shell.set_active(get_state("info \"Shell\""))
    self.res.set_active(get_state("info \"Resolution\""))
    self.de.set_active(get_state("info \"DE\""))
    self.wm.set_active(get_state("info \"WM\""))
    self.wmtheme.set_active(get_state("info \"WM Theme\""))
    self.themes.set_active(get_state("info \"Theme\""))
    self.icons.set_active(get_state("info \"Icons\""))
    self.term.set_active(get_state("info \"Terminal\""))
    self.termfont.set_active(get_state("info \"Terminal Font\""))
    self.cpu.set_active(get_state("info \"CPU\""))
    self.gpu.set_active(get_state("info \"GPU\""))
    self.mem.set_active(get_state("info \"Memory\""))
    self.title.set_active(get_state("info title"))

    self.gpu_driver.set_active(get_state("info \"GPU Driver\""))
    self.cpu_usage.set_active(get_state("info \"CPU Usage\""))
    self.disks.set_active(get_state("info \"Disk\""))
    self.font.set_active(get_state("info \"Font\""))
    self.song.set_active(get_state("info \"Song\""))
    self.lIP.set_active(get_state("info \"Local IP\""))
    self.PIP.set_active(get_state("info \"Public IP\""))
    self.users.set_active(get_state("info \"Users\""))
    self.local.set_active(get_state("info \"Locale\""))

    lines = get_neofetch()

    line = [x for x in lines if "color_blocks=" in x]
    if "on" in line[0]:
        self.cblocks.set_active(True)
    else:
        self.cblocks.set_active(False)
