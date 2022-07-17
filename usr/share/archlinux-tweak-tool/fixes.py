# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import Functions as fn
from Functions import GLib


def check_cursor_global(lists, value):
    if fn.path.isfile(fn.icons_default):
        try:
            pos = fn.get_position(lists, value)
            val = lists[pos].strip()
            return val
        except Exception as e:
            print(e)


def set_global_cursor(self, cursor):
    if fn.path.isfile(fn.icons_default):
        try:
            with open(fn.icons_default, "r", encoding="utf-8") as f:
                lines = f.readlines()
                f.close()

            pos_cursor_theme = fn.get_position(lines, "Inherits=")
            lines[pos_cursor_theme] = "Inherits=" + cursor + "\n"

            with open(fn.icons_default, "w", encoding="utf-8") as f:
                f.writelines(lines)
                f.close()

            GLib.idle_add(
                fn.show_in_app_notification, self, "Settings Saved Successfully"
            )

            # GLib.idle_add(fn.MessageBox,self, "Success!!", "Settings applied successfully")
        except Exception as e:
            print(e)
            fn.MessageBox(
                self,
                "Failed!!",
                'There seems to have been a problem in "set_lightdm_value"',
            )


def pop_gtk_cursor_names(combo):
    coms = []
    combo.get_model().clear()
    for item in fn.listdir("/usr/share/icons/"):
        if fn.path_check("/usr/share/icons/" + item + "/cursors/"):
            coms.append(item)
            coms.sort()

    lines = fn.get_lines(fn.icons_default)
    # pos = fn.get_position(lines, "Inherits=")

    try:
        cursor_theme = check_cursor_global(lines, "Inherits=").split("=")[1]
    except IndexError:
        cursor_theme = ""

    coms.sort()
    for i in range(len(coms)):
        combo.append_text(coms[i])
        if cursor_theme.lower() == coms[i].lower():
            combo.set_active(i)
