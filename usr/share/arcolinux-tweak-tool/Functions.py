import dbus
import os
import shutil
import psutil
import time
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
from xml.etree import ElementTree as et

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)

pacman = "/etc/pacman.conf"
oblogout_conf = "/etc/oblogout.conf"
# oblogout_conf = home + "/oblogout.conf"
gtk3_settings = home + "/.config/gtk-3.0/settings.ini"
gtk2_settings = home + "/.gtkrc-2.0"
grub_theme_conf = "/boot/grub/themes/Vimix/theme.txt"
xfce_config = home + "/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml"
slimlock_conf = "/etc/slim.conf"
#=====================================================
#               MESSAGEBOX
#=====================================================
def MessageBox(title, message):
    md2 = Gtk.MessageDialog(parent=None, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text=title)
    md2.format_secondary_markup(message)
    md2.run()
    md2.destroy()

#=====================================================
#               CONVERT COLOR
#=====================================================
def rgb_to_hex(rgb):
    if "rgb" in rgb:
        rgb = rgb.replace("rgb(", "").replace(")", "")
        vals = rgb.split(",")
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(int(vals[0])), clamp(int(vals[1])), clamp(int(vals[2])))
    return rgb
    
def clamp(x):
  return max(0, min(x, 255))


#=====================================================
#               GLOBAL FUNCTIONS
#=====================================================

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

def gtk_check_value(my_list, value):
    data = [string for string in my_list if value in string]
    if len(data) >= 1:
        data1 = [string for string in data if "#" in string]
        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    return data

def get_gtk_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            active_combo = ""
            combo.get_model().clear()
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(gtk_get_position(lines, "gtk-theme-name"))
            output = lines[pos].split("=")
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
            MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-theme-name\'")

def get_icon_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            active_combo_icon = ""
            combo.get_model().clear()
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(gtk_get_position(lines, "gtk-icon-theme-name"))
            output = lines[pos].split("=")
            active_combo_icon = output[1].lstrip().rstrip()

            for folder in os.listdir("/usr/share/icons"):
                if os.path.isdir("/usr/share/icons/" + folder):
                    check = os.listdir("/usr/share/icons/" + folder)
                    if not "cursors" in check:
                        coms.append(folder)

            coms.sort()

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if(coms[i] == active_combo_icon):
                    combo.set_active(i)
        except:
            MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-icon-theme-name\'")

def gtk_get_position(my_list, value):
    data = [string for string in my_list if value in string]
    position = my_list.index(data[0])
    return position

def get_cursor_themes(self, combo):
    if os.path.isfile(gtk3_settings):
        try:
            combo.get_model().clear()
            active_combo_cursor = ""
            coms = []
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(gtk_get_position(lines, "gtk-cursor-theme-name"))
            output = lines[pos].split("=")
            active_combo_cursor = output[1].lstrip().rstrip()

            for folder in os.listdir("/usr/share/icons"):
                if os.path.isdir("/usr/share/icons/" + folder):
                    check = os.listdir("/usr/share/icons/" + folder)
                    if "cursors" in check:
                        coms.append(folder)

            coms.sort()

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if(coms[i] == active_combo_cursor):
                    combo.set_active(i)
        except:
            MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-cursor-theme-name\'")


def get_gtk_settings(item):
    if os.path.isfile(gtk3_settings):
        active_cursor = ""
        try:
            with open(gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(gtk_get_position(lines, item))
            output = lines[pos].split("=")
            active_cursor = output[1].lstrip().rstrip()

        except:
            MessageBox("ERROR!!", "An error has occured getting this setting \'get_gtk_settings\'")
            if item == "gtk-cursor-theme-size":
                active_cursor = "24"
        
        return active_cursor

def gtk2_save_settings(value, item):
    if not os.path.isfile(gtk2_settings + ".bak"):
        shutil.copy(gtk2_settings,gtk2_settings + ".bak")

    if os.path.isfile(gtk2_settings):
        with open(gtk2_settings, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        try:
            data = check_value(lines, item)
            if not data:
                print("Lines = " + str(len(lines)))
                pos = 4
                print("Pos = " + str(pos))
                lines.insert(pos, ''.join([item,"=\"",str(value),"\"\n"]))
            else:
                pos = int(_get_position(lines, item))
                lines[pos] = ''.join([item,"=\"",str(value),"\"\n"])
    
    
            with open(gtk2_settings, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured getting this setting \'gtk2_save_settings\'")
    

def gtk3_save_settings(value, item):
    if not os.path.isfile(gtk3_settings + ".bak"):
        shutil.copy(gtk3_settings,gtk3_settings + ".bak")

    if os.path.isfile(gtk3_settings):
        with open(gtk3_settings, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        try:
            data = gtk_check_value(lines, item)
            if not data:
                print("Lines = " + str(len(lines)))
                pos = 4
                print("Pos = " + str(pos))
                lines.insert(pos, ''.join([item,"=",str(value),"\n"]))
            else:
                pos = int(gtk_get_position(lines, item))
                lines[pos] = ''.join([item,"=",str(value),"\n"])

            with open(gtk3_settings, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured getting this setting \'gtk3_save_settings\'")

def set_xfce_settings(theme, icon, cursor, cursize):
    if os.path.isfile(xfce_config):
        try:
            tree = et.parse(xfce_config)
            for rank in tree.iter('property'):
                if rank.get("name") == "ThemeName":
                    rank.set("value", str(theme))
                if rank.get("name") == "IconThemeName":
                    rank.set("value", str(icon))
                if rank.get("name") == "CursorThemeName":
                    rank.set("value", str(cursor))
                if rank.get("name") == "CursorThemeSize":
                    rank.set("value", str(cursize))


            tree.write(xfce_config, encoding="utf-8", xml_declaration=True)
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_xfce_settings\'")


def update_index_theme(theme):
    theme_file = "/usr/share/icons/default/index.theme"
    if os.path.isfile(theme_file):
        try:
            with open(theme_file, "r") as f:
                lines = f.readlines()
                f.close()
            for i in range(len(lines)):
                if "Inherits" in lines[i]:
                    lines[i] = "Inherits=" + theme
            
            with open(theme_file, "w") as f:
                f.writelines(lines)
                f.close()
        except:
            pass

def gtk_settings_saved(themeCombo, iconCombo, cursorCombo, cursor_size, fonts):
    # GLib.idle_add(widget.set_sensitive,False)
    gtk3_save_settings(themeCombo, "gtk-theme-name")
    gtk3_save_settings(iconCombo, "gtk-icon-theme-name")
    gtk3_save_settings(cursorCombo, "gtk-cursor-theme-name")
    gtk3_save_settings(int(str(cursor_size).split(".")[0]), "gtk-cursor-theme-size")
    gtk3_save_settings(fonts, "gtk-font-name")

    gtk2_save_settings(themeCombo, "gtk-theme-name")
    gtk2_save_settings(iconCombo, "gtk-icon-theme-name")
    gtk2_save_settings(cursorCombo, "gtk-cursor-theme-name")
    gtk2_save_settings(int(str(cursor_size).split(".")[0]), "gtk-cursor-theme-size")
    gtk2_save_settings(fonts, "gtk-font-name")

    set_xfce_settings(themeCombo, iconCombo, cursorCombo, int(str(cursor_size).split(".")[0]))
    update_index_theme(cursorCombo)

    # get_desktop()

    subprocess.call(["xsetroot -xcf /usr/share/icons/" + cursorCombo + "/cursors/left_ptr " + str(cursor_size)], shell=True)
    
    
    # GLib.idle_add(widget.set_sensitive,True)
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
        with open(pacman, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "arco":
                    if "[arcolinux_repo_testing]" in line:
                        lines[i] = line.replace("#", "")
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")
                if widget == "arch":
                    if "[testing]" in line:
                        lines[i] = line.replace("#", "")
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")
                if widget == "multilib":
                    if "[multilib-testing]" in line:
                        lines[i] = line.replace("#", "")
                        if (i+1) < len(lines):
                            lines[i + 1]  = lines[i + 1].replace("#", "") # you may want to check that i < len(lines)
                        if (i+2) < len(lines) and "Include" in lines[i+2]:
                            lines[i + 2]  = lines[i + 2].replace("#", "")

            with open(pacman, 'w') as f:
                # lines = f.readlines()
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'toggle_test_repos On\'")
    else:
        with open(pacman, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
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
            with open(pacman, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'toggle_test_repos Off\'")

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
        try:
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
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_shorcut\'")

def oblog_populate(combo):
    if os.path.isfile(oblogout_conf):
        coms = []
        active = ""
        with open(oblogout_conf, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "buttontheme" in line:
                    
                    value = line.split("=")
                    val = value[1].lstrip().rstrip()
                    coms.append(val)
                    
                    if not "#" in line:
                        active = val
        
        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active):
                combo.set_active(i)

def oblogout_change_theme(theme):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
                lines = f.readlines()
                f.close()

        try:
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

            with open(oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'oblogout_change_theme\'")

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
        try:
            data = check_value(lines, 'opacity')
            if not data:
                pos = int(_get_position(lines, "[looks]")) + 1
                lines.insert(pos, 'opacity = ' + str(int(value.split(".")[0])) + '\n')
            else:
                pos = int(_get_position(lines, 'opacity'))
                lines[pos] = 'opacity = ' + str(value).split(".")[0] + '\n'

            with open(oblogout_conf, 'w') as f:            
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_opacity\'")

def set_buttons(value):
    if os.path.isfile(oblogout_conf):
        with open(oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttons =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, value)

            with open(oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_buttons\'")

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
        try:
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
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_command\'")

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
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if "bgcolor =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, color)

            with open(oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            MessageBox("ERROR!!", "An error has occured setting this setting \'set_color\'")

#=====================================================
#               HBLOCK CONF
#=====================================================

def hblock_get_state(self):
    lines = int(subprocess.check_output('wc -l /etc/hosts', shell=True).strip().split()[0])
    if os.path.exists("/usr/local/bin/hblock") and lines > 100:
        return True

    self.firstrun = False
    return False

def do_pulse(data, self):
    self.progress.pulse()
    return True


def set_hblock(self, toggle, state):
    GLib.idle_add(toggle.set_sensitive,False)
    GLib.idle_add(self.label7.set_text,"Run..")
    GLib.idle_add(self.progress.set_fraction,0.2)
    # Call self.do_pulse every 100 ms
    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self)
    
    # Dbus
    print("#1")
    # bus = dbus.SystemBus()
    print("#2")
    try:

        # remote_object = bus.get_object("org.arcolinux.TweakTool", "/ArcoLinux")
        print("#3")
        # Commands
        install = 'pacman -S arcolinux-hblock-git --needed --noconfirm'
        # remove = 'pacman -Rsn arcolinux-hblock-git --noconfirm'
        enable = "/usr/local/bin/hblock"
        # disable = "HBLOCK_SOURCES='' hblock"

        # Install
        if state:
            if os.path.exists("/usr/local/bin/hblock"):
                GLib.idle_add(self.label7.set_text,"Database update...")
                # remote_object.shell_commands(enable)
                print("#4")
                subprocess.call([enable], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                print("#5")
            else:
                print("#4")
                GLib.idle_add(self.label7.set_text,"Install Hblock......")
                # remote_object.shell_commands(install)
                print("#5")
                subprocess.call(install.split(" "), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                GLib.idle_add(self.label7.set_text,"Database update...")
                # remote_object.shell_commands(enable)
                subprocess.call([enable], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                
        else:
            print("#4")
            # Disable Hblock
            GLib.idle_add(self.label7.set_text,"Remove update...")
            # remote_object.shell_commands(disable)
            print("#remove")
            subprocess.run(["sh", "-c", "HBLOCK_SOURCES=\'\' /usr/local/bin/hblock"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print("#5")

        GLib.idle_add(self.label7.set_text,"Complete")
        # self.hblock_quit_btn.set_sensitive(True)
        # Don't call self.do_pulse anymore
        GLib.source_remove(timeout_id)
        timeout_id = None
        GLib.idle_add(self.progress.set_fraction,0)

        # remote_object.Exit()
        GLib.idle_add(toggle.set_sensitive,True)
        GLib.idle_add(self.label7.set_text,"Idle ...")
        print("Complete")
    except Exception as e:
        MessageBox("ERROR!!", str(e))
        print(e)
        

#=====================================================
#               GRUB CONF
#=====================================================
def get_grub_wallpapers():
    if os.path.isdir("/boot/grub/themes/Vimix"):
        lists = os.listdir("/boot/grub/themes/Vimix")
        rems = ['select_e.png', 'terminal_box_se.png', 'select_c.png', 'terminal_box_c.png', 'terminal_box_s.png', 
        'select_w.png', 'terminal_box_nw.png', 'terminal_box_w.png', 'unifont-regular-16.pf2', 'icons', 'terminal_box_ne.png', 
        'theme.txt', 'theme.txt.bak', 'terminal_box_sw.png', 'terminal_box_n.png', 'terminal_box_e.png']
        new_list = [x for x in lists if x not in rems]
        new_list.sort()
        return new_list

def set_grub_wallpaper(image):
    if os.path.isfile(grub_theme_conf):
        if not os.path.isfile(grub_theme_conf + ".bak"):
            shutil.copy(grub_theme_conf, grub_theme_conf + ".bak")
        try:
            with open(grub_theme_conf, "r") as f:
                lists = f.readlines()
                f.close()

            val = _get_position(lists, "desktop-image: ")
            lists[val] = "desktop-image: \"" + image + "\"" + "\n"
            
            with open(grub_theme_conf, "w") as f:
                f.writelines(lists)
                f.close()
            
            MessageBox("Success!!", "Settings Saved Successfully")
        except:
            pass

        


#====================================================================
#                       SLIMLOCK
#====================================================================
def get_slimlock(combo):
    coms = []
    if os.path.isfile(slimlock_conf):
        with open(slimlock_conf, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "current_theme" in line:
                    
                    value = line.split(" ")
                    val = value[len(value)-1].lstrip().rstrip()
                    coms.append(val)
                    
                    if not "#" in line:
                        active = val
        
        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active):
                combo.set_active(i)

def set_slimlock(theme):
    if not os.path.isfile(slimlock_conf + ".bak"):
        shutil.copy(slimlock_conf, slimlock_conf + ".bak")

    with open(slimlock_conf, 'r') as f:
        lines = f.readlines()
        f.close()

    try:
        for i in range(0, len(lines)):
            line = lines[i]
            if "current_theme" in line:
                if not "#" in lines[i]:
                    lines[i] = line.replace(lines[i], "#" + lines[i])
        for i in range(0, len(lines)):
            line = lines[i]
            if "current_theme" in line:
                value = lines[i].split(" ")
                if theme == lines[i].split(" ")[len(value)-1].lstrip().rstrip():
                    lines[i] = line.replace("#","")

        with open(slimlock_conf, 'w') as f:
            f.writelines(lines)
            f.close()
        MessageBox("Success!!", "Settings Saved Successfully")
        # print(lines)
    except:
        MessageBox("ERROR!!", "An error has occured setting this setting \'oblogout_change_theme\'")
#====================================================================
#                       CUSTOM FUNCTION
#====================================================================
    
def get_desktop():
    base_dir = os.path.dirname(os.path.realpath(__file__))

    desktop = subprocess.run(["sh", base_dir + "/find_DE.sh", sudo_username], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dsk = desktop.stdout.decode().strip().split("\n")
    
    print(dsk[len(dsk)-1])

#=====================================================
#               CHECK RUNNING PROCESS
#=====================================================

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:        
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if processName == pinfo['pid']:
                return True       
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass                
    return False