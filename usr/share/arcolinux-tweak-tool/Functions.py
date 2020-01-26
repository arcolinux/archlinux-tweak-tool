import os
import fileinput
import shutil

home = os.environ['HOME']

pacman = "/etc/pacman.conf"
oblogout_conf = "/etc/oblogout.conf"
# oblogout_conf = home + "/oblogout.conf"
lightdm_conf = "/etc/lightdm/lightdm-gtk-greeter.conf"


def rgb_to_hex(rgb):
    if "rgb" in rgb:
        rgb = rgb.replace("rgb(", "").replace(")", "")
        vals = rgb.split(",")
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(int(vals[0])), clamp(int(vals[1])), clamp(int(vals[2])))
    return rgb
    
def clamp(x):
  return max(0, min(x, 255))


#=====================================================
#               LIGHTDM CONF
#=====================================================
def file_check(file):
    if os.path.isfile(file):
        return True
    
    return False

#=====================================================
#               LIGHTDM CONF
#=====================================================
def get_gtk_themes(self, combo):
    if os.path.isfile(lightdm_conf):
        active_combo = ""
        coms = []
        with open(lightdm_conf, "r") as f:
            lines = f.readlines()
            for line in lines:

                if line.startswith("theme-name = "):
                    output = line.split("=")
                    active_combo = output[1].lstrip().rstrip()

        for folder in os.listdir("/usr/share/themes"):
            if os.path.isdir("/usr/share/themes/" + folder):
                check = os.listdir("/usr/share/themes/" + folder)
                if "gtk-3.0" in check:
                    coms.append(folder)

        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active_combo):
                combo.set_active(i)

def get_icon_themes(self, combo):
    if os.path.isfile(lightdm_conf):
        active_combo_icon = ""
        coms = []
        with open(lightdm_conf, "r") as f:
            lines = f.readlines()
            for line in lines:

                if line.startswith("icon-theme-name ="):
                    output = line.split("=")
                    active_combo_icon = output[1].lstrip().rstrip()

        for folder in os.listdir("/usr/share/icons"):
            if os.path.isdir("/usr/share/icons/" + folder):
                check = os.listdir("/usr/share/icons/" + folder)
                if not "cursors" in check:
                    coms.append(folder)
                    # print(folder)

        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active_combo_icon):
                combo.set_active(i)

def get_cursor_themes(self, combo):
    if os.path.isfile(lightdm_conf):
        active_combo_cursor = ""
        coms = []
        with open(lightdm_conf, "r") as f:
            lines = f.readlines()
            for line in lines:

                if line.startswith("cursor-theme-name ="):
                    output = line.split("=")
                    active_combo_cursor = output[1].lstrip().rstrip()

        for folder in os.listdir("/usr/share/icons"):
            if os.path.isdir("/usr/share/icons/" + folder):
                check = os.listdir("/usr/share/icons/" + folder)
                if "cursors" in check:
                    coms.append(folder)
                    # print(folder)

        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active_combo_cursor):
                combo.set_active(i)

#=====================================================
#               PACMAN CONF
#=====================================================
def append_repo(self, text):
    with open(pacman, "a") as myfile:
        myfile.write("\n\n")
        myfile.write(text)


def toggle_test_repos(state, widget):
    print(widget)
    if not os.path.isfile(pacman + ".bak"):
        shutil.copy(pacman, pacman + ".bak")
    lines = ""
    if state == True:
        # print("State = True")
        with open(pacman, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(pacman, 'w') as f:
            # lines = f.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "arco":
                    if "[arcolinux_repo_testing]" in line:
                        lines[i] = line.replace("#", "")
                        # print(line)
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                            # print(lines[i+1])
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")
                            # print(lines[i+2])
                if widget == "arch":
                    if "[testing]" in line:
                        lines[i] = line.replace("#", "")
                        # print(line)
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                            # print(lines[i+1])
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")
                            # print(lines[i+2])
                if widget == "multilib":
                    if "[multilib-testing]" in line:
                        lines[i] = line.replace("#", "")
                        # print(line)
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                            # print(lines[i+1])
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")
                            # print(lines[i+2])
            # f.seek(0, 0)
            f.writelines(lines)
            f.close()
    else:
        with open(pacman, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(pacman, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "arco":
                    if "[arcolinux_repo_testing]" in line:
                        if not "#" in lines[i]:
                            lines[i] = line.replace(lines[i], "#" + lines[i])
                        if (i+1) < len(lines):
                            if not "#" in lines[i + 1]:
                                lines[i + 1]  = lines[i + 1].replace(lines[i + 1], "#" + lines[i + 1]) # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            if not "#" in lines[i + 2]:
                                lines[i + 2]  = lines[i + 2].replace(lines[i + 2], "#" + lines[i + 2])
                if widget == "arch":
                    if "[testing]" in line:
                        if not "#" in lines[i]:
                            lines[i] = line.replace(lines[i], "#" + lines[i])
                        if (i+1) < len(lines):
                            if not "#" in lines[i + 1]:
                                lines[i + 1]  = lines[i + 1].replace(lines[i + 1], "#" + lines[i + 1]) # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            if not "#" in lines[i + 2]:
                                lines[i + 2]  = lines[i + 2].replace(lines[i + 2], "#" + lines[i + 2])
                if widget == "multilib":
                    if "[multilib-testing]" in line:
                        if not "#" in lines[i]:
                            lines[i] = line.replace(lines[i], "#" + lines[i])
                        if (i+1) < len(lines):
                            if not "#" in lines[i + 1]:
                                lines[i + 1]  = lines[i + 1].replace(lines[i + 1], "#" + lines[i + 1]) # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            if not "#" in lines[i + 2]:
                                lines[i + 2]  = lines[i + 2].replace(lines[i + 2], "#" + lines[i + 2])

            # f.seek(0, 0)
            f.writelines(lines)
            f.close()


#=====================================================
#               OBLOGOUT CONF
#=====================================================
def oblog_populate(combo):
    if os.path.isfile(oblogout_conf):
        coms = []
        active = ""
        with open(oblogout_conf, "r") as f:
            lines = f.readlines()
            for line in lines:
                # print(line)
                if "buttontheme" in line:
                    
                    value = line.split("=")
                    val = value[1].lstrip().rstrip()
                    coms.append(val)
                    
                    if not "#" in line:
                        active = val
        
        coms.sort()

        for i in range(len(coms)):
            # print(coms[i])
            combo.append_text(coms[i])
            if(coms[i] == active):
                combo.set_active(i)
        # combo.append_text('something')

def oblogout_change_theme(theme):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
                lines = f.readlines()
                f.close()

        with open(oblogout_conf, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttontheme" in line:
                    if not "#" in lines[i]:
                        lines[i] = line.replace(lines[i], "#" + lines[i])
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttontheme" in line:
                    
                    if theme == lines[i].split("=")[1].lstrip().rstrip():
                        print(lines[i].split("=")[1].lstrip().rstrip())
                        lines[i] = line.replace("#","")
            
            f.writelines(lines)
            f.close()

def get_value():
    opacity = 0
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()

            for i in range(0, len(lines)):
                line = lines[i]
                if "opacity" in line:
                    nline = line.split("=")
                    opacity = nline[1].lstrip().rstrip()
            
            f.close()
            return float(opacity)
    else:
        return 0

def set_value(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(oblogout_conf, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if "opacity" in line:
                    nline = line.split("=")
                    opacity = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(opacity, str(value).split(".")[0])
            f.writelines(lines)
            f.close()

def set_buttons(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(oblogout_conf, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttons =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, value)
            f.writelines(lines)
            f.close()

def get_buttons():
    buttons = "You do not have oblogout.conf"
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()

            for i in range(0, len(lines)):
                line = lines[i]
                if "buttons =" in line:
                    nline = line.split("=")
                    buttons = nline[1].lstrip().rstrip()
                    
            f.close()
            return buttons
    else:
        return buttons

def get_lockscreen():
    lock = "You do not have oblogout.conf"
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()

            for i in range(0, len(lines)):
                line = lines[i]
                if "lock =" in line and i == (len(lines) -1):
                    nline = line.split("=")
                    lock = nline[1].lstrip().rstrip()
                    
            f.close()
            return lock
    else:
        return lock

def set_lockscreen(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(oblogout_conf, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if "lock =" in line and i == (len(lines) -1):
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, value)
            f.writelines(lines)
            f.close()
 
def get_color():
    color = ""
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "bgcolor =" in line:
                    color = line.split("=")[1].lstrip().rstrip()
            f.close()
    return color

def set_color(color):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        with open(oblogout_conf, 'w') as f:
            for i in range(0, len(lines)):
                line = lines[i]
                if "bgcolor =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, color)
            f.writelines(lines)
            f.close()