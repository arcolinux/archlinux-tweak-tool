# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import Functions as fn


def get_startups(self):
    lst = fn.os.listdir(fn.home + "/.config/autostart/")

    for n in [x.replace(".desktop", "") for x in lst]:
        self.startups.append([n])


def add_autostart(self, name, com, comnt):
    content = "[Desktop Entry]\n\
Encoding=UTF-8\n\
Version=1.0\n\
Type=Application\n\
Name=" + name + "\n\
Comment=" + comnt + "\n\
Exec=" + com + "\n\
TryExec=" + com + "\n\
StartupNotify=false\n\
X-GNOME-Autostart-enabled=true\n\
Terminal=false\n\
Hidden=false\n"

    with open(fn.home + "/.config/autostart/" + name + ".desktop", "w") as f:
        f.write(content)
        f.close()
    self.startups.append([name])
