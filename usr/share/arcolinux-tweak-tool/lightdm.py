#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

import Functions
from Functions import GLib

def check_lightdm(lists, value):
    pos = Functions._get_position(lists, value)
    val = lists[pos].strip()
    return val
    # comman = Functions.check_lightdm_value(lines[Functions.get_lightdm(lines):], "autologin-user=")
            
def set_lightdm_value(lists, value, session, state):
    try:
        pos = Functions._get_position(lists, "autologin-user=")
        pos_session = Functions._get_position(lists, "user-session=")
        
        if state:
            lists[pos] = "autologin-user=" + value + "\n"
        else:
            if not "#" in lists[pos]:
                lists[pos] = "#" + lists[pos]
        
        lists[pos_session] = "user-session=" + session + "\n"

        with open(Functions.lightdm_conf, "w") as f:
            f.writelines(lists)
            f.close()

        GLib.idle_add(Functions.MessageBox,"Success!!", "Settings applied successfully")
    except Exception as e:
        print(e)
        Functions.MessageBox("Failed!!", "There seems to have been a problem in \"set_lightdm_value\"")


def get_lines(files):
    if Functions.os.path.isfile(files):
        with open(files, "r") as f:
            lines = f.readlines()
            f.close()
        return lines

def pop_box(combo):
    coms = []
    for items in Functions.os.listdir("/usr/share/xsessions/"):
        coms.append(items.split(".")[0].lower())
    lines = get_lines(Functions.lightdm_conf)

    # pos = Functions._get_position(lines, "user-session=")
    name = check_lightdm(lines, "user-session=").split("=")[1]

    for i in range(len(coms)):
        combo.append_text(coms[i])
        if name in coms[i]:
            combo.set_active(i)
