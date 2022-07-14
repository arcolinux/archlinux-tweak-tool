#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn
from Functions import GLib
import os

def check_lxdm(lists, value):
    if fn.os.path.isfile(fn.lxdm_conf):
        try:
            pos = fn._get_position(lists, value)
            val = lists[pos].strip()
            return val
        except Exception as e:
            print(e)

def check_lxdm_last(lists, value):
    if fn.os.path.isfile(fn.lxdm_conf):
        try:
            pos = fn._get_positions(lists, value)
            pos = pos[-1]
            val = lists[pos].strip()
            return val
        except Exception as e:
            print(e)

def set_lxdm_value(self, lists, username, gtk_theme, lxdm_theme, state, pane):
    if fn.os.path.isfile(fn.lxdm_conf):
        try:
            fn.add_autologin_group(self)
            pos = fn._get_position(lists, "autologin=")
            pos_gtk_theme = fn._get_position(lists, "gtk_theme=")
            lxdm_list = fn._get_positions(lists, "theme=")
            #get last instance
            lxdm =lxdm_list[-1]
            bot = fn._get_position(lists, "bottom_pane=")

            if state:
                lists[pos] = "autologin=" + username + "\n"
            else:
                if "#" not in lists[pos]:
                    lists[pos] = "#" + lists[pos]

            lists[pos_gtk_theme] = "gtk_theme=" + gtk_theme + "\n"

            lists[lxdm] = "theme=" + lxdm_theme + "\n"

            if pane:
                #at bottom
                lists[bot] = "bottom_pane=1" + "\n"
            else:
                #at top
                lists[bot] = "bottom_pane=0" + "\n"

            with open(fn.lxdm_conf, "w") as f:
                f.writelines(lists)
                f.close()

            GLib.idle_add(fn.show_in_app_notification, self, "Settings Saved Successfully")

            # GLib.idle_add(fn.MessageBox,self, "Success!!", "Settings applied successfully")
        except Exception as e:
            print(e)
            fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_lxdm_value\"")

def pop_gtk_theme_names_lxdm(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.lxdm_conf):
        for item in fn.os.listdir("/usr/share/themes/"):
            if fn.file_check("/usr/share/themes/" + item + "/index.theme"):
                coms.append(item)
                coms.sort()
        #print(coms)
        lines = fn.get_lines(fn.lxdm_conf)

        try:
            theme_name = check_lxdm(lines, "gtk_theme=").split("=")[1]
        except IndexError:
            theme_name = ""
            pass

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if theme_name.lower() == coms[i].lower():
                combo.set_active(i)

def pop_lxdm_theme_greeter(self, combo):
    coms = []
    combo.get_model().clear()

    if os.path.exists("/usr/share/lxdm/themes") and os.path.exists(fn.lxdm_conf):
        for items in fn.os.listdir("/usr/share/lxdm/themes/"):
            #coms.append(items.split(".")[0].lower())
            coms.append(items)

        lines = fn.get_lines(fn.lxdm_conf)
        try:
            name = check_lxdm_last(lines, "theme=").split("=")[1]
        except IndexError:
            name = ""
            pass

        coms.sort()
        for i in range(len(coms)):
            #excludes = ['maya', 'maldives', 'elarun', '']
            #if not coms[i] in excludes:
            combo.append_text(coms[i])
            #TODO:select second find
            if name.lower() == coms[i].lower():
                combo.set_active(i)