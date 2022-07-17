# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

from ast import literal_eval
import Functions as fn


def get_startups(self, n):

    try:
        with open(fn.autostart + n + ".desktop", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
        state = True
    except:
        return True

    if fn.check_content("Hidden=", fn.autostart + n + ".desktop"):
        try:
            pos = fn.get_position(lines, "Hidden=")
            state = lines[pos].split("=")[1].strip()

            state = state.capitalize()
            state = not literal_eval(state)
            return state
        except Exception as e:
            print(e)
            return True
    else:
        return state


def add_autostart(self, name, com, comnt):
    # lists = [x for x in fn.os.listdir(fn.home + "/.config/autostart/")]
    lists = list(fn.listdir(fn.home + "/.config/autostart"))
    if not (name + ".desktop") in lists:
        content = (
            "[Desktop Entry]\n\
Encoding=UTF-8\n\
Version=1.0\n\
Type=Application\n\
Name="
            + name
            + "\n\
Comment="
            + comnt
            + "\n\
Exec="
            + com
            + "\n\
TryExec="
            + com
            + "\n\
StartupNotify=false\n\
X-GNOME-Autostart-enabled=true\n\
Terminal=false\n\
Hidden=false\n"
        )

        with open(
            fn.home + "/.config/autostart/" + name + ".desktop", "w", encoding="UTF-8"
        ) as f:
            f.write(content)
            f.close()
        self.add_row(name)
        # self.startups.append([True, name, comnt])
