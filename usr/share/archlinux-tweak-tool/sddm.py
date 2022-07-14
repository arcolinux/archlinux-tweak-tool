#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn
from Functions import GLib
import os

def check_sddmk_complete(self):
    with open(fn.sddm_default_d2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    flag_a = False
    flag_s = False
    flag_u = False
    flag_t = False
    flag_c = False
    flag_ct = False
    flag_f = False

    for line in lines:
        if "[Autologin]" in line:
            flag_a = True
        if "Session=" in line:
            flag_s = True
        if "User=" in line:
            flag_u = True
        if "[Theme]" in line:
            flag_t = True
        if "Current=" in line:
            flag_c = True
        if "CursorTheme=" in line:
            flag_ct = True
        if "Font=" in line:
            flag_f = True

    if flag_a and flag_s and flag_u and flag_t and flag_c and flag_ct and flag_f:
        return True
    else:
        return False

def check_sddmk_session(value):
    with open(fn.sddm_default_d2, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False

def insert_session(text):
    with open(fn.sddm_default_d2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    pos = fn._get_position(lines, "[Autologin]")
    num = pos+2

    lines.insert(num, text + "\n")

    with open(fn.sddm_default_d2, "w") as f:
        f.writelines(lines)
        f.close()


def check_sddmk_user(value):
    with open(fn.sddm_default_d2, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False

def insert_user(text):
    with open(fn.sddm_default_d2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    pos = fn._get_position(lines, "[Autologin]")
    num = pos+3

    lines.insert(num, text + "\n")

    with open(fn.sddm_default_d2, "w") as f:
        f.writelines(lines)
        f.close()


def check_sddm(lists, value):
    pos = fn._get_position(lists, value)
    val = lists[pos].strip()
    return val

def set_sddm_value(self, lists, value, session, state, theme, cursor):
    try:
        com = fn.subprocess.run(["sh", "-c", "su - " + fn.sudo_username + " -c groups"], shell=False, stdout=fn.subprocess.PIPE)
        groups = com.stdout.decode().strip().split(" ")
        # print(groups)
        if "autologin" not in groups:
            fn.subprocess.run(["gpasswd", "-a", fn.sudo_username, "autologin"], shell=False)

        pos = fn._get_position(lists, "Session=")
        pos_session = fn._get_position(lists, "User=")

        if state:
            lists[pos_session] = "User=" + value + "\n"
            lists[pos] = "Session=" + session + "\n"
        else:
            if "#" not in lists[pos]:
                lists[pos] = "#" + lists[pos]
                lists[pos_session] = "#" + lists[pos_session]

        pos_theme = fn._get_position(lists, "Current=")
        lists[pos_theme] = "Current=" + theme + "\n"

        pos_theme = fn._get_position(lists, "CursorTheme=")
        lists[pos_theme] = "CursorTheme=" + cursor + "\n"

        with open(fn.sddm_default_d2, "w") as f:
            f.writelines(lists)
            f.close()

    except Exception as e:
        print(e)
        fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_sddm_value\"")

def set_user_autologin_value(self, lists, value, session, state):
    try:
        com = fn.subprocess.run(["sh", "-c", "su - " + fn.sudo_username + " -c groups"], shell=False, stdout=fn.subprocess.PIPE)
        groups = com.stdout.decode().strip().split(" ")
        # print(groups)
        if "autologin" not in groups:
            fn.subprocess.run(["gpasswd", "-a", fn.sudo_username, "autologin"], shell=False)

        pos_session = fn._get_positions(lists, "Session=")
        #print(pos_session)
        pos_session = pos_session[-1]
        pos_user = fn._get_position(lists, "User=" + value)
        #print(pos_user)

        if state:
            lists[pos_user] = "User=" + value + "\n"
            lists[pos_session] = "Session=" + session + "\n"
        else:
            if "#" not in lists[pos_user]:
                lists[pos_user] = "#" + lists[pos_user]
                lists[pos_session] = "#" + lists[pos_session]

        with open(fn.sddm_default_d1, "w") as f:
            f.writelines(lists)
            f.close()

#        GLib.idle_add(fn.show_in_app_notification, self, "Settings Saved Successfully")

    except Exception as e:
        print(e)
        fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_sddm_value\"")

def get_sddm_lines(files):
    if fn.os.path.isfile(files):
        with open(files, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
        return lines


def pop_box(self, combos):
    comss = []
    combos.get_model().clear()

    for items in fn.os.listdir("/usr/share/xsessions/"):
        comss.append(items.split(".")[0].lower())
    lines = get_sddm_lines(fn.sddm_default_d2)

    try:
        name = check_sddm(lines, "Session=").split("=")[1]
    except IndexError:
        name = ""
        pass

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

    if os.path.exists("/usr/share/sddm") and os.path.exists(fn.sddm_default_d2) and os.path.exists(fn.sddm_default_d1):
        for items in fn.os.listdir("/usr/share/sddm/themes/"):
            #coms.append(items.split(".")[0].lower())
            coms.append(items.split(".")[0])
        lines = get_sddm_lines(fn.sddm_default_d2)

        try:
            name = check_sddm(lines, "Current=").split("=")[1]
        except IndexError:
            name = ""
            pass

        coms.sort()
        for i in range(len(coms)):
            #excludes = ['maya', 'maldives', 'elarun', '']
            #if not coms[i] in excludes:
            combo.append_text(coms[i])
            if name.lower() == coms[i].lower():
                combo.set_active(i)

def pop_gtk_cursor_names(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.sddm_default_d2):
        for item in fn.os.listdir("/usr/share/icons/"):
            if fn.path_check("/usr/share/icons/" + item + "/cursors/"):
                coms.append(item)
                coms.sort()

        lines = fn.get_lines(fn.sddm_default_d2)

        pos = fn._get_position(lines, "CursorTheme=")
        try:
            cursor_theme = check_sddm(lines, "CursorTheme=").split("=")[1]
        except IndexError:
            cursor_theme = ""
            pass

        coms.sort()
        for i in range(len(coms)):
            combo.append_text(coms[i])
            if cursor_theme.lower() == coms[i].lower():
                combo.set_active(i)

def pop_login_managers_combo (self,combo):
    options = ['sddm', 'lightdm', 'lxdm']
    for option in options:
        self.login_managers_combo.append_text(option)
        if fn.check_content("sddm", "/etc/systemd/system/display-manager.service"):
            self.login_managers_combo.set_active(0)
        if fn.check_content("lightdm", "/etc/systemd/system/display-manager.service"):
            self.login_managers_combo.set_active(1)
        if fn.check_content("lxdm", "/etc/systemd/system/display-manager.service"):
            self.login_managers_combo.set_active(2)