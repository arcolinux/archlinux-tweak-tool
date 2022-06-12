# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

import Functions, os
from Functions import GLib

def check_sddmk_session(value):
    with open(Functions.sddm_default_d2, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False

def insert_session(text):
    with open(Functions.sddm_default_d2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    pos = Functions._get_position(lines, "[Autologin]")
    num = pos+2

    lines.insert(num, text + "\n")

    with open(Functions.sddm_default_d2, "w") as f:
        f.writelines(lines)
        f.close()


def check_sddmk_user(value):
    with open(Functions.sddm_default_d2, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False

def insert_user(text):
    with open(Functions.sddm_default_d2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    pos = Functions._get_position(lines, "[Autologin]")
    num = pos+3

    lines.insert(num, text + "\n")

    with open(Functions.sddm_default_d2, "w") as f:
        f.writelines(lines)
        f.close()


def check_sddm(lists, value):
    pos = Functions._get_position(lists, value)
    val = lists[pos].strip()
    return val

def set_sddm_value(self, lists, value, session, state, theme,cursor):
    try:
        com = Functions.subprocess.run(["sh", "-c", "su - " + Functions.sudo_username + " -c groups"], shell=False, stdout=Functions.subprocess.PIPE)
        groups = com.stdout.decode().strip().split(" ")
        # print(groups)
        if "autologin" not in groups:
            Functions.subprocess.run(["gpasswd", "-a", Functions.sudo_username, "autologin"], shell=False)

        pos = Functions._get_position(lists, "Session=")
        pos_session = Functions._get_position(lists, "User=")

        if state:
            lists[pos_session] = "User=" + value + "\n"
            lists[pos] = "Session=" + session + "\n"
        else:
            if "#" not in lists[pos]:
                lists[pos] = "#" + lists[pos]
                lists[pos_session] = "#" + lists[pos_session]

        pos_theme = Functions._get_position(lists, "Current=")
        lists[pos_theme] = "Current=" + theme + "\n"

        pos_theme = Functions._get_position(lists, "CursorTheme=")
        lists[pos_theme] = "CursorTheme=" + cursor + "\n"

        with open(Functions.sddm_default_d2, "w") as f:
            f.writelines(lists)
            f.close()

#        GLib.idle_add(Functions.show_in_app_notification, self, "Settings Saved Successfully")

    except Exception as e:
        print(e)
        Functions.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_sddm_value\"")

def get_sddm_lines(files):
    if Functions.os.path.isfile(files):
        with open(files, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
        return lines


def pop_box(self, combos):
    comss = []
    combos.get_model().clear()

    for items in Functions.os.listdir("/usr/share/xsessions/"):
        comss.append(items.split(".")[0].lower())
    lines = get_sddm_lines(Functions.sddm_default_d2)

    name = check_sddm(lines, "Session=").split("=")[1]

    comss.sort()
    if 'i3-with-shmlog' in comss:
        comss.remove('i3-with-shmlog')
    if 'openbox-kde' in comss:
        comss.remove('openbox-kde')
    if 'cinnamon2d' in comss:
        comss.remove('cinnamon2d')
    if 'icewm-session' in comss:
        comss.remove('icewm-session')

    for i in range(len(comss)):
        combos.append_text(comss[i])
        if name.lower() == comss[i].lower():
           combos.set_active(i)

def pop_theme_box(self, combo):
    coms = []
    combo.get_model().clear()

    if os.path.exists("/usr/share/sddm") and os.path.exists(Functions.sddm_default_d2) and os.path.exists(Functions.sddm_default_d1):
        for items in Functions.os.listdir("/usr/share/sddm/themes/"):
            coms.append(items.split(".")[0].lower())
        lines = get_sddm_lines(Functions.sddm_default_d2)

        name = check_sddm(lines, "Current=").split("=")[1]

        coms.sort()
        for i in range(len(coms)):
            #excludes = ['maya', 'maldives', 'elarun', '']
            #if not coms[i] in excludes:
            combo.append_text(coms[i])
            if name.lower() == coms[i].lower():
                combo.set_active(i)

def pop_cursor_box(self, combo):
    coms = []
    com1 = []
    com2 = []
    combo.get_model().clear()

    if Functions.check_package_installed("bibata-cursor-theme-bin"):
        com1 = ["Bibata-Modern-Amber",
                "Bibata-Modern-Classic",
                "Bibata-Modern-Ice",
                "Bibata-Original-Amber",
                "Bibata-Original-Classic",
                "Bibata-Original-Ice"]
        coms = com1

    if Functions.check_package_installed("breeze-icons"):
        com2 = ["Breeze-Snow","breeze_cursors"]
        coms = coms + com2

    if Functions.check_package_installed("sweet-cursor-theme-git"):
        com3 = ["Sweet-cursors"]
        coms = coms + com3

    if Functions.check_package_installed("adwaita-icon-theme"):
        com4 = ["Adwaita"]
        coms = coms + com4

    lines = get_sddm_lines(Functions.sddm_default_d2)

    name = check_sddm(lines, "CursorTheme=").split("=")[1]

    coms.sort()
    for i in range(len(coms)):
        #excludes = ['maya', 'maldives', 'elarun', '']
        #if not coms[i] in excludes:
        combo.append_text(coms[i])
        if name.lower() == coms[i].lower():
            combo.set_active(i)
