import os
import fileinput
import shutil
import getpass
import psutil
import time
import subprocess
import dbus
import gi
from gi.repository import GLib

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)
print(home)
pacman = "/etc/pacman.conf"
oblogout_conf = "/etc/oblogout.conf"
# oblogout_conf = home + "/oblogout.conf"
gtk3_settings = home + "/.config/gtk-3.0/settings.ini"


def rgb_to_hex(rgb):
    if "rgb" in rgb:
        rgb = rgb.replace("rgb(", "").replace(")", "")
        vals = rgb.split(",")
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(int(vals[0])), clamp(int(vals[1])), clamp(int(vals[2])))
    return rgb
    
def clamp(x):
  return max(0, min(x, 255))


# Get list value index.
def _get_position(list, value):
    data = [string for string in list if value in string]
    position = list.index(data[0])
    return position

# Search variable and value.
def _get_variable(list, value):
    data = [string for string in list if value in string]

    # Search # line
    if len(data) >= 1:

        data1 = [string for string in data if "#" in string]

        # If data1 not empty
        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    # If not empty
    if data:
        data_clean = [data[0].strip('\n').replace(" ", "")][0].split("=")
    return data_clean

# Check  value exists
def check_value(list, value):
    data = [string for string in list if value in string]
    if len(data) >= 1:
        data1 = [string for string in data if "#" in string]
        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    return data
#=====================================================
#               Check if File Exists
#=====================================================
def file_check(file):
    if os.path.isfile(file):
        return True
    
    return False

#=====================================================
#               GTK3 CONF
#=====================================================
def get_gtk_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            active_combo = ""
            combo.get_model().clear()
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                for line in lines:

                    if line.startswith("gtk-theme-name"):
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
        except:
            pass

def get_icon_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            active_combo_icon = ""
            combo.get_model().clear()
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                for line in lines:

                    if line.startswith("gtk-icon-theme-name"):
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
        except:
            pass

def get_cursor_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            combo.get_model().clear()
            active_combo_cursor = ""
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                for line in lines:

                    if line.startswith("gtk-cursor-theme-name"):
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
        except:
            pass

def get_gtk_settings(self, item):
    if os.path.isfile(gtk3_settings):
        active_cursor = ""
        try:
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            for line in lines:
                if line.startswith(item):
                    output = line.split("=")
                    active_cursor = output[1].lstrip().rstrip()
        except:
            pass
        
        return active_cursor

def gtk3_save_settings(value, item):
    if not os.path.isfile(gtk3_settings + ".bak"):
        shutil.copy(gtk3_settings,gtk3_settings + ".bak")

    if os.path.isfile(gtk3_settings):
        with open(gtk3_settings, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                if item in lines[i]:
                    lines[i] = ''.join([item,"=",str(value),"\n"])

            with open(gtk3_settings, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            pass



#=====================================================
#               PACMAN CONF
#=====================================================
def append_repo(self, text):
    with open(pacman, "a") as myfile:
        myfile.write("\n\n")
        myfile.write(text)

def check_repo(value):
    with open(pacman, "r") as myfile:
        lines = myfile.readlines()
        myfile.close()
    
    for line in lines:
        if "#" + value in line:
            return False
    return True

def toggle_test_repos(state, widget):
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
# Get shortcuts index
def get_shortcuts(conflist):
    sortcuts = _get_variable(conflist, "shortcuts")
    shortcuts_index = _get_position(conflist, sortcuts[0])
    return int(shortcuts_index)

# Get commands index
def get_commands(conflist):
    commands = _get_variable(conflist, "commands")
    commands_index = _get_position(conflist, commands[0])
    return int(commands_index)

def get_shortcut(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, "r") as f:
            lines = f.readlines()
            f.close()
        shortcu = check_value(lines[get_shortcuts(lines):get_commands(lines)], value)
        if not shortcu:
            shortcut = [value, '']            
        else:
            shortcut = [shortcu[0].lstrip().rstrip().replace(" ", "")][0].split("=")
        return shortcut[1]

def set_shorcut(value, value_sk):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        shortcuts_pos = _get_position(lines, "[shortcuts]")
        commandss_pos = _get_position(lines, "[commands]")
        data1_shortcut = check_value(lines[shortcuts_pos:commandss_pos], value)

        if not data1_shortcut:

            pos = shortcuts_pos + 5
            lines.insert(pos, value + ' = ' + str(value_sk) + '\n')
        else:
            pos = int(_get_position(lines[shortcuts_pos:commandss_pos], value))
            lines[shortcuts_pos + pos] = value + ' = ' + str(value_sk) + '\n'
        
        with open(oblogout_conf, 'w') as f:            
            f.writelines(lines)
            f.close()

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
                        lines[i] = line.replace("#","")
            
            f.writelines(lines)
            f.close()

def get_opacity():
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        data = check_value(lines, "opacity")
        if not data:
            opacity = 80
        else:
            opacity = _get_variable(lines, "opacity")
        return int(opacity[1].split(".")[0])

def set_opacity(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        data = check_value(lines, 'opacity')
        if not data:
            pos = int(_get_position(lines, "[looks]")) + 1
            lines.insert(pos, 'opacity = ' + str(int(value.split(".")[0])) + '\n')
        else:
            pos = int(_get_position(lines, 'opacity'))
            lines[pos] = 'opacity = ' + str(int(value.split(".")[0])) + '\n'

        with open(oblogout_conf, 'w') as f:            
            f.writelines(lines)
            f.close()
        
def set_buttons(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        
        for i in range(0, len(lines)):
            line = lines[i]
            if "buttons =" in line:
                nline = line.split("=")
                val = nline[1].lstrip().rstrip()
                lines[i] = line.replace(val, value)

        with open(oblogout_conf, 'w') as f:
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

def get_command(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        comman = check_value(lines[get_commands(lines):], value)
        if not comman:
            command = ['', '']
            command[0] = value
        else:
            command = [comman[0].strip('\n')][0].split("=")
            command[0] = command[0].replace(' ', '').replace('#', '')
            command[1] = command[1][:1].replace(' ', '') + command[1][1:]
        # command[1] = command1[:1].replace(' ', '')
        return command[1]

def set_command(value, value_sk):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        commandss_pos = _get_position(lines, "[commands]")
        data_command = check_value(lines[commandss_pos:], value)
        if not data_command:
            pos = data_command + 4
            lines.insert(pos, value + ' = ' + str(value_sk) + '\n')
        else:
            pos = int(_get_position(lines[commandss_pos:], value))
            lines[commandss_pos + pos] = value + ' = ' + str(value_sk) + '\n'
        
        with open(oblogout_conf, 'w') as f:            
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
        for i in range(0, len(lines)):
            line = lines[i]
            if "bgcolor =" in line:
                nline = line.split("=")
                val = nline[1].lstrip().rstrip()
                lines[i] = line.replace(val, color)

        with open(oblogout_conf, 'w') as f:
            f.writelines(lines)
            f.close()

#=====================================================
#               HBLOCK CONF
#=====================================================

def hblock_get_state():
    lines = int(subprocess.check_output('wc -l /etc/hosts', shell=True).strip().split()[0])
    if os.path.exists("/usr/local/bin/hblock") and lines > 100:
        return True
    
    return False

def do_pulse(self, user_data, progress):
    progress.pulse()
    return True

def set_hblock(self, toggle, state):
    print("RUNNING")
    GLib.idle_add(toggle.set_sensitive,False)
    GLib.idle_add(self.label7.set_text,"Run..")
    GLib.idle_add(self.progress.set_fraction,0.2)
    # Call self.do_pulse every 100 ms
    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self, self.progress)

    # Dbus
    bus = dbus.SystemBus()
    try:
        print("################### 1")
        remote_object = bus.get_object("org.arcolinux.tweaktool", "/ArcoLinux")
        print("################### 2")
        # Commands
        install = 'pacman -S arcolinux-hblock-git --needed --noconfirm'
        # remove = 'pacman -Rsn arcolinux-hblock-git --noconfirm'
        enable = "hblock"
        disable = "HBLOCK_SOURCES='' hblock"

        # Install
        if state:
            if os.path.exists("/usr/local/bin/hblock"):
                GLib.idle_add(self.label7.set_text,"Database update...")
                remote_object.shell_commands(enable)

            else:
                GLib.idle_add(self.label7.set_text,"Install Hblock......")
                remote_object.shell_commands(install)
                GLib.idle_add(self.label7.set_text,"Database update...")
                remote_object.shell_commands(enable)
        else:

            # Disable Hblock
            GLib.idle_add(self.label7.set_text,"Remove update...")
            remote_object.shell_commands(disable)
        GLib.idle_add(self.label7.set_text,"Complete")
        # self.hblock_quit_btn.set_sensitive(True)
        # Don't call self.do_pulse anymore
        GLib.source_remove(timeout_id)
        timeout_id = None
        # prog.set_fraction(0)

        remote_object.Exit()
        GLib.idle_add(toggle.set_sensitive,True)

    except dbus.DBusException as e:
        print(e)

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:        
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if processName == pinfo['pid']:
                return True       
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass                
    return False