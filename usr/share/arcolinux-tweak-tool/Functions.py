#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

import dbus
import os
import shutil
import psutil
import time
import subprocess
import threading
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gdk

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
termite_config = home + "/.config/termite/config"
neofetch_config = home + "/.config/neofetch/config.conf"
bd = ".ATT_Backups"

desktop = ""


#=====================================================
#               COPY FUNCTION
#=====================================================
def copy_func(src, dst, isdir=False):
    if isdir:
        subprocess.run(["cp", "-R", src, dst], shell=False)
    else:
        subprocess.run(["cp", src, dst], shell=False)

#=====================================================
#               SOURCE
#=====================================================
def source_shell(self):
    process = subprocess.run(["sh", "-c", "echo \"$SHELL\""], 
                         stdout=subprocess.PIPE)
    
    output = process.stdout.decode().strip()
    print(output)
    if output == "/bin/bash":
        subprocess.run(["bash", "-c", "su - " + sudo_username + " -c \"source " + home + "/.bashrc\""], stdout=subprocess.PIPE)
    elif output == "/bin/zsh":
        subprocess.run(["zsh", "-c", "su - " + sudo_username + " -c \"source " + home + "/.zshrc\""], stdout=subprocess.PIPE)

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

def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position

# Search variable and value.
def _get_variable(lists, value):
    data = [string for string in lists if value in string]

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

def gtk_get_position(my_list, value):
    data = [string for string in my_list if value in string]
    position = my_list.index(data[0])
    return position

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
#     authority.check_authorization(subject, action_id, None, Polkit.CheckAuthorizationFlags.ALLOW_USER_INTERACTION, cancellable, set_test_repos, None, state, widget)

# def set_test_repos(authority, res, loop, state, widget):
#     result = authority.check_authorization_finish(res)
#     if result.get_is_authorized():
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
        except Exception as e:
            print(e)
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

        
#=====================================================
#               NEOFETCH CONF
#=====================================================
def neofetch_set_value(lists, pos, text, state):
    if state:
        if text in lists[pos]:
            if "#" in lists[pos]:
                lists[pos] = lists[pos].replace("#", "")
    else:
        if text in lists[pos]:
            if not "#" in lists[pos]:
                lists[pos] = "#" + lists[pos]

    return lists

def neofetch_set_backend_value(lists, pos, text, value):
    if text in lists[pos] and not "#" in lists[pos]:
        lists[pos] = text + value + "\"\n"

#====================================================================
#                       CUSTOM FUNCTION
#====================================================================
    
def get_desktop(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))

    desktop = subprocess.run(["sh", base_dir + "/find_DE.sh", sudo_username], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dsk = desktop.stdout.decode().strip().split("\n")
    
    # return dsk[len(dsk)-1].lstrip().rstrip()
    self.desktop = dsk[len(dsk)-1].lstrip().rstrip()
    self.lbl_desktop.set_markup("<span foreground=\'grey\'>" + self.desktop.capitalize() +"</span>")

def copytree(self, src, dst, symlinks=False, ignore=None):

    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
            except Exception as e:
                print(e)
                os.unlink(d)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except Exception as e:
                print(e)
                print("ERROR2")
                self.ecode = 1
        else:
            try:
                shutil.copy2(s, d)
            except:
                print("ERROR3")
                self.ecode = 1

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

