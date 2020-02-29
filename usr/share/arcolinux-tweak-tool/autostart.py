# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import Functions as fn


def get_startups(self):
    lst = fn.os.listdir(fn.home + "/.config/autostart/")

    for n in [x.replace(".desktop", "") for x in lst]:
        self.startups.append([n])


def add_autostart(self, name, com):
    content = "[Desktop Entry]\n\
Encoding=UTF-8\n\
Version=0.9.4\n\
Type=Application\n\
Name=" + name + "\n\
Comment=\n\
Exec=" + com + "\n\
OnlyShowIn=XFCE;\n\
RunHook=0\n\
StartupNotify=false\n\
Terminal=false\n\
Hidden=false\n"

    with open(fn.home + "/.config/autostart/" + name + ".desktop", "w") as f:
        f.write(content)
        f.close()
    self.startups.append([name])
