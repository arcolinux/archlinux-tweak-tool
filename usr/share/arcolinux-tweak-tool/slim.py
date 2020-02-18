# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import Functions
from Functions import os
# ====================================================================
#                       SLIMLOCK
# ====================================================================
# @threaded


def get_slimlock(combo):
    coms = []
    if os.path.isfile(Functions.slimlock_conf):
        with open(Functions.slimlock_conf, "r") as f:
            lines = f.readlines()
            f.close()

        for line in lines:
            if "current_theme" in line:

                # value = line.split(" ")
                # val = value[len(value)-1].lstrip().rstrip()
                # coms.append(val)

                if "#" not in line:
                    value = line.split(" ")
                    val = value[len(value)-1].lstrip().rstrip()
                    active = val.strip()

        for folder in os.listdir("/usr/share/slim/themes/"):
            if os.path.isdir("/usr/share/slim/themes/" + folder):
                coms.append(folder)

        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active):
                combo.set_active(i)


def reload_import(combo, theme):
    combo.get_model().clear()
    coms = []
    if os.path.isfile(Functions.slimlock_conf):
        # with open(Functions.slimlock_conf, "r") as f:
        #     lines = f.readlines()
        #     f.close()
        for folder in os.listdir("/usr/share/slim/themes/"):
            if os.path.isdir("/usr/share/slim/themes/" + folder):
                coms.append(folder)

        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == theme):
                combo.set_active(i)


def remove_theme(name):
    with open(Functions.slimlock_conf, "r") as f:
        lines = f.readlines()
        f.close()
    try:
        pos = Functions._get_position(lines, name)
        pos2 = Functions._get_position(lines, "  arcolinux_eyes")

        lines[pos2] = lines[pos2].replace("#", "")

        if pos:
            del lines[pos]

        with open(Functions.slimlock_conf, "w") as f:
            f.writelines(lines)
            f.close()

    except Exception as e:
        print(e)


def set_slimlock(self, theme):
    if not os.path.isfile(Functions.slimlock_conf + ".bak"):
        Functions.shutil.copy(Functions.slimlock_conf,
                              Functions.slimlock_conf + ".bak")

    with open(Functions.slimlock_conf, 'r') as f:
        lines = f.readlines()
        f.close()

    # try:
    for i in range(0, len(lines)):
        line = lines[i]
        if "current_theme" in line:
            if "#" not in lines[i]:
                lines[i] = line.replace(lines[i], "#" + lines[i])
    # current_theme       arcolinux
    data = Functions.gtk_check_value(lines, theme)
    if not data:
        themes = Functions._get_position(lines, "current_theme       ")
        lines.insert(int(themes) + 1, "current_theme       " + theme + "\n")
    else:
        for i in range(0, len(lines)):
            line = lines[i]
            if "current_theme" in line:
                value = lines[i].split(" ")
                if theme == lines[i].split(" ")[len(value)-1].strip():
                    lines[i] = line.replace("#", "")

    with open(Functions.slimlock_conf, 'w') as f:
        f.writelines(lines)
        f.close()
    Functions.show_in_app_notification(self, "Settings Saved Successfully")
    # except:
    #     MessageBox(self, "ERROR!!",
    #                "An error has occured setting this setting \'oblogout_change_theme\'")  # noqa