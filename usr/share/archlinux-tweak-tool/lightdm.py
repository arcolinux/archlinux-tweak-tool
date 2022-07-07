# =================================================================
# =             Author: Brad Heffernan Erik Dubois                =
# =================================================================

import Functions as fn
from Functions import GLib

def check_lightdm(lists, value):
    if fn.os.path.isfile(fn.lightdm_conf):
        try:
            pos = fn._get_position(lists, value)
            val = lists[pos].strip()
            return val
        except Exception as e:
            print(e)

def check_lightdm_greeter(lists, value):
    if fn.os.path.isfile(fn.lightdm_greeter):
        try:
            pos = fn._get_position(lists, value)
            val = lists[pos].strip()
            return val
        except Exception as e:
            print(e)

def set_lightdm_value(self, lists, value, session, state):
    if fn.os.path.isfile(fn.lightdm_conf):
        try:
            com = fn.subprocess.run(["sh", "-c", "su - " + fn.sudo_username + " -c groups"], shell=False, stdout=fn.subprocess.PIPE)
            groups = com.stdout.decode().strip().split(" ")
            # print(groups)
            if "autologin" not in groups:
                fn.subprocess.run(["gpasswd", "-a", fn.sudo_username, "autologin"], shell=False)

            pos = fn._get_position(lists, "autologin-user=")
            pos_session = fn._get_position(lists, "autologin-session=")

            if state:
                lists[pos] = "autologin-user=" + value + "\n"
                lists[pos_session] = "autologin-session=" + session + "\n"
            else:
                if "#" not in lists[pos]:
                    lists[pos] = "#" + lists[pos]
                    lists[pos_session] = "#" + lists[pos_session]

            with open(fn.lightdm_conf, "w") as f:
                f.writelines(lists)
                f.close()

            GLib.idle_add(fn.show_in_app_notification, self, "Settings Saved Successfully")

            # GLib.idle_add(fn.MessageBox,self, "Success!!", "Settings applied successfully")
        except Exception as e:
            print(e)
            fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_lightdm_value\"")

def set_lightdm_icon_theme(self, lists, theme, icon_theme):
    if fn.os.path.isfile(fn.lightdm_greeter):
        try:
            pos_theme = fn._get_position(lists, "theme-name=")
            pos_icon_theme = fn._get_position(lists, "icon-theme-name=")

            lists[pos_theme] = "theme-name=" + theme + "\n"
            lists[pos_icon_theme] = "icon-theme-name=" + icon_theme + "\n"


            with open(fn.lightdm_greeter, "w") as f:
                f.writelines(lists)
                f.close()

            GLib.idle_add(fn.show_in_app_notification, self, "Settings Saved Successfully")

            # GLib.idle_add(fn.MessageBox,self, "Success!!", "Settings applied successfully")
        except Exception as e:
            print(e)
            fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_lightdm_value\"")

    if fn.os.path.isfile(fn.lightdm_slick_greeter):
        try:
            pos_theme = fn._get_position(lists, "theme-name=")
            pos_icon_theme = fn._get_position(lists, "icon-theme-name=")

            lists[pos_theme] = "theme-name=" + theme + "\n"
            lists[pos_icon_theme] = "icon-theme-name=" + icon_theme + "\n"


            with open(fn.lightdm_slick_greeter, "w") as f:
                f.writelines(lists)
                f.close()

            GLib.idle_add(fn.show_in_app_notification, self, "Settings Saved Successfully")

            # GLib.idle_add(fn.MessageBox,self, "Success!!", "Settings applied successfully")
        except Exception as e:
            print(e)
            fn.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_lightdm_value\"")

def pop_box_sessions_lightdm(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.lightdm_conf):
        for items in fn.os.listdir("/usr/share/xsessions/"):
            coms.append(items.split(".")[0].lower())
        lines = fn.get_lines(fn.lightdm_conf)

        try:
            name = check_lightdm(lines, "autologin-session=").split("=")[1]
        except IndexError:
            name = None
            pass

        coms.sort()
        for i in range(len(coms)):
            #TODO
            #excludes = ['gnome-classic', 'gnome-xorg', 'i3-with-shmlog', 'openbox-kde', 'cinnamon2d', '']
            excludes = []
            if not coms[i] in excludes:
                combo.append_text(coms[i])
                if name.lower() == coms[i].lower():
                    combo.set_active(i)

def pop_gtk_theme_names_lightdm(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.lightdm_greeter):
        for item in fn.os.listdir("/usr/share/themes/"):
            if fn.file_check("/usr/share/themes/" + item + "/index.theme"):
                coms.append(item)
                coms.sort()
        lines = fn.get_lines(fn.lightdm_greeter)

        pos = fn._get_position(lines, "theme-name=")
        try:
            theme_name = check_lightdm_greeter(lines, "theme-name=").split("=")[1]
        except IndexError:
            theme_name = None
            pass

        coms.sort()
        for i in range(len(coms)):
            combo.append_text(coms[i])
            if theme_name.lower() == coms[i].lower():
                # print("Name = " + name)
                combo.set_active(i)

def pop_gtk_icon_names_lightdm(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.lightdm_greeter):
        for item in fn.os.listdir("/usr/share/icons/"):
            if not fn.path_check("/usr/share/icons/" + item + "/cursors/"):
                coms.append(item)
                coms.sort()
        lines = fn.get_lines(fn.lightdm_greeter)

        pos = fn._get_position(lines, "icon-theme-name=")
        try:
            icon_theme_name = check_lightdm(lines, "icon-theme-name=").split("=")[1]
        except IndexError:
            icon_theme_name = None
            pass

        coms.sort()
        for i in range(len(coms)):
            combo.append_text(coms[i])
            if icon_theme_name.lower() == coms[i].lower():
                combo.set_active(i)

def pop_gtk_cursor_names(self, combo):
    coms = []
    combo.get_model().clear()

    if fn.os.path.isfile(fn.lightdm_conf):
        for item in fn.os.listdir("/usr/share/icons/"):
            if fn.path_check("/usr/share/icons/" + item + "/cursors/"):
                coms.append(item)
                coms.sort()
        lines = fn.get_lines(fn.lightdm_conf)

        #pos = fn._get_position(lines, "icon-theme-name=")
        #theme_name = check_lightdm(lines, "icon-theme-name=").split("=")[1]

        coms.sort()
        for i in range(len(coms)):
            combo.append_text(coms[i])
            #if theme_name.lower() == coms[i].lower():
            #    combo.set_active(i)
