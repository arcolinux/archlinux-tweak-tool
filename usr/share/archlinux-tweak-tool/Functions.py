# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import distro
import sys
import shutil
import psutil
import datetime
# import time
import subprocess
import threading  # noqa
import gi
# import configparser
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk  # noqa

# =====================================================
#              BEGIN DECLARATION OF VARIABLES
# =====================================================

distr = distro.id()

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)

gpg_conf = "/etc/pacman.d/gnupg/gpg.conf"
gpg_conf_local = home + "/.gnupg/gpg.conf"

gpg_conf_original = "/usr/share/archlinux-tweak-tool/data/any/gpg.conf"
gpg_conf_local_original = "/usr/share/archlinux-tweak-tool/data/any/gpg.conf"

sddm_default = "/etc/sddm.conf"
sddm_default_original = "/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf"

samba_config = "/etc/samba/smb.conf"

sddm_default_d1 = "/etc/sddm.conf"
sddm_default_d2 = "/etc/sddm.conf.d/kde_settings.conf"
sddm_default_d2_dir = "/etc/sddm.conf.d/"
sddm_default_d_sddm_original_1 = "/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf"
sddm_default_d_sddm_original_2 = "/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf"

# if os.path.exists("/etc/sddm.conf.d/kde_settings.conf"):
#     sddm_conf = "/etc/sddm.conf.d/kde_settings.conf"
# else:
#     sddm_conf = "/etc/sddm.conf"

mirrorlist = "/etc/pacman.d/mirrorlist"
arcolinux_mirrorlist = "/etc/pacman.d/arcolinux-mirrorlist"
xerolinux_mirrorlist = "/etc/pacman.d/xerolinux-mirrorlist"
arcolinux_mirrorlist_original = "/usr/share/archlinux-tweak-tool/data/arco/arcolinux-mirrorlist"
pacman = "/etc/pacman.conf"
pacman_arch = "/usr/share/archlinux-tweak-tool/data/arch/pacman/pacman.conf"
pacman_arco = "/usr/share/archlinux-tweak-tool/data/arco/pacman/pacman.conf"
pacman_eos = "/usr/share/archlinux-tweak-tool/data/eos/pacman/pacman.conf"
pacman_garuda = "/usr/share/archlinux-tweak-tool/data/garuda/pacman/pacman.conf"
blank_pacman_arch = "/usr/share/archlinux-tweak-tool/data/arch/pacman/blank/pacman.conf"
blank_pacman_arco = "/usr/share/archlinux-tweak-tool/data/arco/pacman/blank/pacman.conf"
blank_pacman_eos = "/usr/share/archlinux-tweak-tool/data/eos/pacman/blank/pacman.conf"
blank_pacman_garuda = "/usr/share/archlinux-tweak-tool/data/garuda/pacman/blank/pacman.conf"
neofetch_arco = "/usr/share/archlinux-tweak-tool/data/arco/neofetch/config.conf"
alacritty_arco = "/usr/share/archlinux-tweak-tool/data/arco/alacritty/alacritty.yml"
lightdm_greeter_arco = "/usr/share/archlinux-tweak-tool/data/any/lightdm-gtk-greeter.conf"
lightdm_greeter = "/etc/lightdm/lightdm-gtk-greeter.conf"
lightdm_conf = "/etc/lightdm/lightdm.conf"
oblogout_conf = "/etc/oblogout.conf"
# oblogout_conf = home + "/oblogout.conf"
gtk3_settings = home + "/.config/gtk-3.0/settings.ini"
gtk2_settings = home + "/.gtkrc-2.0"
grub_theme_conf = "/boot/grub/themes/Vimix/theme.txt"
grub_default_grub = "/etc/default/grub"
xfce_config = home + "/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml"
xfce4_terminal_config = home + "/.config/xfce4/terminal/terminalrc"
alacritty_config = home + "/.config/alacritty/alacritty.yml"
alacritty_config_dir = home + "/.config/alacritty"
slimlock_conf = "/etc/slim.conf"
termite_config = home + "/.config/termite/config"
neofetch_config = home + "/.config/neofetch/config.conf"
nsswitch_config ="/etc/nsswitch.conf"
bd = ".att_backups"
config = home + "/.config/archlinux-tweak-tool/settings.ini"
config_dir = home + "/.config/archlinux-tweak-tool/"
polybar = home + "/.config/polybar/"
desktop = ""
autostart = home + "/.config/autostart/"

bash_config = ""
zsh_config = ""
fish_config = ""

if os.path.isfile(home + "/.config/fish/config.fish"):
    fish_config = home + "/.config/fish/config.fish"
if os.path.isfile(home + "/.zshrc"):
    zsh_config = home + "/.zshrc"
if os.path.isfile(home + "/.bashrc"):
    bash_config = home + "/.bashrc"

bashrc_arco = "/usr/share/archlinux-tweak-tool/data/arco/.bashrc"
zshrc_arco = "/usr/share/archlinux-tweak-tool/data/arco/.zshrc"
fish_arco = "/usr/share/archlinux-tweak-tool/data/arco/config.fish"
account_list = ["Standard","Administrator"]
i3wm_config = home + "/.config/i3/config"
awesome_config = home + "/.config/awesome/rc.lua"
qtile_config = home + "/.config/qtile/config.py"

seedhostmirror = "Server = https://ant.seedhost.eu/arcolinux/$repo/$arch"
aarnetmirror = "Server = https://mirror.aarnet.edu.au/pub/arcolinux/$repo/$arch"

atestrepo = "[arcolinux_repo_testing]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

arepo = "[arcolinux_repo]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

a3drepo = "[arcolinux_repo_3party]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

axlrepo = "[arcolinux_repo_xlarge]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

chaotics_repo = "[chaotic-aur]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/chaotic-mirrorlist"

endeavouros_repo = "[endeavouros]\n\
SigLevel = PackageRequired\n\
Include = /etc/pacman.d/endeavouros-mirrorlist"

nemesis_repo = "[nemesis_repo]\n\
SigLevel = Optional TrustedOnly\n\
Server = https://erikdubois.github.io/$repo/$arch"

xero_repo = "[xerolinux_repo]\n\
SigLevel = Optional TrustAll\n\
Include = /etc/pacman.d/xero-mirrorlist"

xero_xl_repo = "[xerolinux_repo_xl]\n\
SigLevel = Optional TrustAll\n\
Include = /etc/pacman.d/xero-mirrorlist"

xero_nv_repo = "[xerolinux_nvidia_repo]\n\
SigLevel = Optional TrustAll\n\
Include = /etc/pacman.d/xero-mirrorlist"

arch_testing_repo = "[testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_core_repo = "[core]\n\
Include = /etc/pacman.d/mirrorlist"

arch_extra_repo = "[extra]\n\
Include = /etc/pacman.d/mirrorlist"

arch_community_testing_repo = "[community-testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_community_repo = "[community]\n\
Include = /etc/pacman.d/mirrorlist"

arch_multilib_testing_repo = "[multilib-testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_multilib_repo = "[multilib]\n\
Include = /etc/pacman.d/mirrorlist"


# =====================================================
#              END DECLARATION OF VARIABLES
# =====================================================
# =====================================================
# =====================================================
# =====================================================
# =====================================================
#               BEGIN GLOBAL FUNCTIONS
# =====================================================

# get position in list
def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position

# get positions in list
def _get_positions(lists, value):
    data = [string for string in lists if value in string]
    position = []
    for d in data:
        position.append(lists.index(d))
    return position

# get variable from list
def _get_variable(lists, value):
    data = [string for string in lists if value in string]

    if len(data) >= 1:

        data1 = [string for string in data if "#" in string]

        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
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

# check backups
def check_backups(now):
    if not os.path.exists(home + "/" + bd + "/Backup-" +
                          now.strftime("%Y-%m-%d %H")):
        os.makedirs(home + "/" + bd + "/Backup-" +
                    now.strftime("%Y-%m-%d %H"), 0o777)
        permissions(home + "/" + bd + "/Backup-" + now.strftime("%Y-%m-%d %H"))

# check process is running
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if processName == pinfo['pid']:
                return True
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False

# copytree
def copytree(self, src, dst, symlinks=False, ignore=None):  # noqa

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
            except:  # noqa
                print("ERROR3")
                self.ecode = 1

# check lightdm value
def check_lightdm_value(list, value):
    data = [string for string in list if value in string]
    return data

# check sddm value
def check_sddm_value(list, value):
    data = [string for string in list if value in string]
    return data

# check if file exists
def file_check(file):
    if os.path.isfile(file):
        return True

    return False

# check if path exists
def path_check(path):
    if os.path.isdir(path):
        return True

    return False

# check if value is true or false in file
def check_content(value, file):         # noqa
    try:
        with open(file, "r", encoding="utf-8") as myfile:
            lines = myfile.readlines()
            myfile.close()

        for line in lines:
            if value in line:
                if value in line:
                    return True
                else:
                    return False
        return False
    except Exception as e:
        #print(e)
        return False

# check if package is installed or not
def check_package_installed(package):         # noqa
    try:
        subprocess.check_output("pacman -Qi " + package,shell=True,stderr=subprocess.STDOUT)
        #package is installed
        return True
    except subprocess.CalledProcessError as e:
        #package is not installed
        return False

# check if service is active
def check_service(service):         # noqa
    try:
        command = "systemctl is-active " + service
        output = subprocess.run(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        status = output.stdout.decode().strip()
        if status =="active":
            #print("Service is active")
            return True
        else:
            #print("Service is inactive")
            return False
    except Exception as e:
        return False

# list normal users
def list_users(filename): # noqa
    try:
        data = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                if "1001" in line:
                    data.append(line.split(":")[0])
                if "1002" in line:
                    data.append(line.split(":")[0])
                if "1003" in line:
                    data.append(line.split(":")[0])
                if "1004" in line:
                    data.append(line.split(":")[0])
                if "1005" in line:
                    data.append(line.split(":")[0])
            data.sort()
            return data
    except Exception as e:
        print(e)

# check if user is part of the group
def check_group(group):
    try:
        groups = subprocess.run(["sh", "-c", "id " +
                                sudo_username],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        for x in groups.stdout.decode().split(" "):
            if group in x:
                return True
            else:
                return False
    except Exception as e:
        print(e)

# =====================================================
#               END GLOBAL FUNCTIONS
# =====================================================
# =====================================================
# =====================================================
# =====================================================

def check_arco_repos_active():
    with open(pacman, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()

        arco_base = "[arcolinux_repo]"
        arco_3p = "[arcolinux_repo_3party]"
        #arco_xl = "[arcolinux_repo_xlarge]"

    for line in lines:
        if arco_base in line:
            if "#" + arco_base in line:
                return False
            else:
                return True

    for line in lines:
        if arco_3p in line:
            if "#" + arco_3p in line:
                return False
            else:
                return True

# =====================================================
#               ALACRITTY
# =====================================================

def install_alacritty(self):
    install = 'pacman -S alacritty --needed --noconfirm'

    if os.path.exists("/usr/bin/alacritty"):
        #print("Alacritty is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Alacritty is now installed")

# =====================================================
#               ALACRITTY-THEMES
# =====================================================

def install_alacritty_themes(self):
    install = 'pacman -S alacritty-themes --noconfirm'

    if os.path.exists("/usr/bin/alacritty-themes"):
        #print("Alacritty-themes is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Alacritty-themes is now installed")

# =====================================================
#               ARCOLINUX-DESKTOP-TRASHER
# =====================================================

def install_adt(self):
    install = 'pacman -S arcolinux-desktop-trasher-git --noconfirm'

    if os.path.exists("/usr/local/bin/arcolinux-desktop-trasher"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#                    BASH
# =====================================================

def install_bash(self):
    install = 'pacman -S bash bash-completion --needed --noconfirm'

    if os.path.exists("/usr/bin/bash"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        restart_program()

# =====================================================
#              CAJA SHARE PLUGIN
# =====================================================

def install_arco_caja_plugin(self, widget):
    install = 'pacman -S caja arcolinux-caja-share --noconfirm'

    if check_package_installed("arcolinux-caja-share"):
        print("Arcolinux-caja-share is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Arcolinux-caja-share is now installed - reboot")
        GLib.idle_add(self.label7.set_text, "Arcolinux-caja-share is now installed - reboot")
    print("Other apps that might be interesting for sharing are :")
    print(" - arcolinux-thunar-share-plugin (thunar)")
    print(" - arcolinux-nemo-share (cinnamon)")
    print(" - arcolinux-nautilus-share (gnome - budgie)")
    print(" - kdenetwork-filesharing (plasma)")

# =====================================================
#               CONVERT COLOR
# =====================================================

def rgb_to_hex(rgb):
    if "rgb" in rgb:
        rgb = rgb.replace("rgb(", "").replace(")", "")
        vals = rgb.split(",")
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(int(vals[0])),
                                               clamp(int(vals[1])),
                                               clamp(int(vals[2])))
    return rgb


def clamp(x):
    return max(0, min(x, 255))

# =====================================================
#               COPY FUNCTION
# =====================================================

def copy_func(src, dst, isdir=False):
    if isdir:
        subprocess.run(["cp", "-Rp", src, dst], shell=False)
    else:
        subprocess.run(["cp", "-p", src, dst], shell=False)

# =====================================================
#               DISTRO LABEL
# =====================================================

def change_distro_label(name):      # noqa
    if name == "arcolinux":
        name = "ArcoLinux"
    if name == "garuda":
        name = "Garuda"
    if name == "endeavouros":
        name = "EndeavourOS"
    if name == "arch":
        name = "Arch Linux"
    if name == "manjaro":
        name = "Manjaro"
    if name == "xerolinux":
        name = "Xerolinux"
    return name

# =====================================================
#               FISH + PACKAGES (ARCOLINUXD)
# =====================================================

def install_only_fish(self):
    install = 'pacman -S fish --needed --noconfirm'

    if os.path.exists("/usr/bin/fish"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("Only Fish has been installed")
    GLib.idle_add(self.label7.set_text, "Only Fish has been installed")

def install_arcolinux_fish_package(self):
    install = 'pacman -S arcolinux-fish-git --needed --noconfirm'

    try:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("ArcoLinux Fish has been installed")
    except Exception as e:
        print(e)

def remove_fish(self):
    install = 'pacman -Rs fish arcolinux-fish-git --noconfirm'

    if not os.path.exists("/usr/bin/fish") and os.path.exists("/etc/skel/.config/fish/config.fish") :
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    self.tobash_apply(self)

# ====================================================================
#                      GET DESKTOP
# ====================================================================

def get_desktop(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))

    desktop = subprocess.run(["sh", base_dir + "/get_desktop.sh", "-n"],
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    dsk = desktop.stdout.decode().strip().split("\n")
    self.desktop = dsk[-1].strip()

# ====================================================================
#                      GRUB
# ====================================================================
def make_grub(self):
    try:
        command = 'grub-mkconfig -o /boot/grub/grub.cfg'
        subprocess.call(command.split(" "),
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    except Exception as e:
        print(e)

# =====================================================
#               GRUB CONF
# =====================================================

def get_grub_wallpapers():
    if os.path.isdir("/boot/grub/themes/Vimix"):
        lists = os.listdir("/boot/grub/themes/Vimix")

        rems = ['select_e.png', 'terminal_box_se.png', 'select_c.png',
                'terminal_box_c.png', 'terminal_box_s.png',
                'select_w.png', 'terminal_box_nw.png',
                'terminal_box_w.png', 'terminal_box_ne.png',
                'terminal_box_sw.png', 'terminal_box_n.png',
                'terminal_box_e.png']

        ext = ['.png', '.jpeg', '.jpg']

        new_list = [x for x in lists if x not in rems for y in ext if y in x]

        new_list.sort()
        return new_list


def set_grub_wallpaper(self, image):
    if os.path.isfile(grub_theme_conf):
        if not os.path.isfile(grub_theme_conf + ".bak"):
            shutil.copy(grub_theme_conf, grub_theme_conf + ".bak")
        try:
            with open(grub_theme_conf, "r", encoding="utf-8") as f:
                lists = f.readlines()
                f.close()

            val = _get_position(lists, "desktop-image: ")
            lists[val] = "desktop-image: \"" + os.path.basename(image) + "\"" + "\n"

            with open(grub_theme_conf, "w") as f:
                f.writelines(lists)
                f.close()
            print("Grub wallpaper saved")
            show_in_app_notification(self, "Grub wallpaper saved")
            # MessageBox(self, "Success!!", "Settings Saved Successfully")
        except:  # noqa
            pass

def set_default_theme(self):
    if os.path.isfile(grub_default_grub):
        if not os.path.isfile(grub_default_grub + ".bak"):
            shutil.copy(grub_default_grub, grub_default_grub + ".bak")
        try:
            with open(grub_default_grub, "r", encoding="utf-8") as f:
                grubd = f.readlines()
                f.close()

            if distro.id() == "arch":
                try:
                    val = _get_position(grubd, '#GRUB_THEME="/path/to/gfxtheme"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "arch":
                try:
                    # for Carli
                    val = _get_position(grubd, 'GRUB_THEME=/usr/share/grub/themes/poly-dark/theme.txt')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "arcolinux":
                try:
                    val = _get_position(grubd, "#GRUB_THEME")
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "endeavouros":
                try:
                    val = _get_position(grubd, "GRUB_THEME=/boot/grub/themes/EndeavourOS/theme.txt")
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "garuda":
                try:
                    val = _get_position(grubd, 'GRUB_THEME="/usr/share/grub/themes/garuda/theme.txt"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                   pass

            if distro.id() == "manjaro":
                try:
                    val = _get_position(grubd, 'GRUB_THEME="/usr/share/grub/themes/manjaro/theme.txt"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                   pass

            if distro.id() == "xerolinux":
                try:
                    val = _get_position(grubd, 'GRUB_THEME="/boot/grub/themes/XeroKDE/theme.txt"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                   pass

            with open(grub_default_grub, "w") as f:
                f.writelines(grubd)
                f.close()

            print("Grub settings saved successfully in /etc/default/grub")
            print("We made sure you have a backup - /etc/default/grub.bak")
            print("This line has changed in /etc/default/grub")
            print('GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"')

            show_in_app_notification(self, "Grub settings saved in /etc/default/grub")
        except Exception as e:
            print(e)

# =====================================================
#               GTK3 CONF
# =====================================================

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

# =====================================================
#               HBLOCK CONF
# =====================================================

def hblock_get_state(self):
    lines = int(subprocess.check_output('wc -l /etc/hosts',
                                        shell=True).strip().split()[0])
    if os.path.exists("/usr/bin/hblock") and lines > 100:
        return True

    self.firstrun = False
    return False

def do_pulse(data, prog):
    prog.pulse()
    return True

def set_hblock(self, toggle, state):
    GLib.idle_add(toggle.set_sensitive, False)
    GLib.idle_add(self.label7.set_text, "Run..")
    GLib.idle_add(self.progress.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self.progress)

    if not os.path.isfile("/etc/hosts.bak"):
            shutil.copy("/etc/hosts", "/etc/hosts.bak")

    try:

        install = 'pacman -S arcolinux-hblock-git --needed --noconfirm'
        enable = "/usr/bin/hblock"

        if state:
            if os.path.exists("/usr/bin/hblock"):
                GLib.idle_add(self.label7.set_text, "Database update...")
                subprocess.call([enable],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
            else:
                GLib.idle_add(self.label7.set_text, "Install Hblock......")
                subprocess.call(install.split(" "),
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
                GLib.idle_add(self.label7.set_text, "Database update...")
                subprocess.call([enable],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)

        else:
            GLib.idle_add(self.label7.set_text, "Remove update...")
            subprocess.run(["sh", "-c",
                            "HBLOCK_SOURCES=\'\' /usr/bin/hblock"],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)

        GLib.idle_add(self.label7.set_text, "Complete")
        GLib.source_remove(timeout_id)
        timeout_id = None
        GLib.idle_add(self.progress.set_fraction, 0)

        GLib.idle_add(toggle.set_sensitive, True)
        if state:
            GLib.idle_add(self.label7.set_text, "HBlock Active")
        else:
            GLib.idle_add(self.label7.set_text, "HBlock Inactive")

    except Exception as e:
        MessageBox(self, "ERROR!!", str(e))
        print(e)

# =====================================================
#               LOG FILE CREATION
# =====================================================

log_dir="/var/log/archlinux/"
att_log_dir="/var/log/archlinux/att/"

def create_log(self):
    print('Making log in /var/log/archlinux')
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d-%H-%M-%S" )
    destination = att_log_dir + 'att-log-' + time
    command = 'sudo pacman -Q > ' + destination
    subprocess.call(command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    #GLib.idle_add(show_in_app_notification, self, "Log file created")

# =====================================================
#               MESSAGEBOX
# =====================================================


def MessageBox(self, title, message):
    md2 = Gtk.MessageDialog(parent=self,
                            flags=0,
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text=title)
    md2.format_secondary_markup(message)
    md2.run()
    md2.destroy()

# =====================================================
#              NEMO SHARE PLUGIN
# =====================================================

def install_arco_nemo_plugin(self, widget):
    install = 'pacman -S nemo arcolinux-nemo-share --noconfirm'

    if check_package_installed("arcolinux-nemo-share"):
        print("Arcolinux-nemo-share is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Arcolinux-nemo-share is now installed - reboot")
        GLib.idle_add(self.label7.set_text, "Arcolinux-nemo-share is now installed - reboot")
    print("Other apps that might be interesting for sharing are :")
    print(" - arcolinux-thunar-share-plugin (thunar)")
    print(" - arcolinux-caja-share (mate)")
    print(" - kdenetwork-filesharing (plasma)")
    print(" - arcolinux-nautilus-share (gnome - budgie)")

# =====================================================
#               NEOFETCH CONF
# =====================================================

def neofetch_set_value(lists, pos, text, state):
    if state:
        if text in lists[pos]:
            if "#" in lists[pos]:
                lists[pos] = lists[pos].replace("#", "")
    else:
        if text in lists[pos]:
            if "#" not in lists[pos]:
                lists[pos] = "#" + lists[pos]

    return lists

def neofetch_set_backend_value(lists, pos, text, value):
    if text in lists[pos] and "#" not in lists[pos]:
        lists[pos] = text + value + "\"\n"

# =====================================================
#               NOTIFICATIONS
# =====================================================

def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)

def timeOut(self):
    close_in_app_notification(self)


def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None

# =====================================================
#               NSSWITCH CONF COPY
# =====================================================

def copy_nsswitch(choice):
    command ="cp /usr/share/archlinux-tweak-tool/data/" + choice + "/nsswitch.conf /etc/nsswitch.conf"
    print(command)
    subprocess.call(command.split(" "),
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    print("/etc/nsswitch.conf has been overwritten - reboot")

# =====================================================
#               OBLOGOUT CONF
# =====================================================
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

# =====================================================
#               PACE INSTALLATION
# =====================================================

def install_pace(self):
    install = 'pacman -S pace --noconfirm --needed'

    if os.path.exists("/usr/bin/pace"):
        #print("Pace is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Pace is now installed")

# =====================================================
#               PACMAN EXTRA KEYS AND MIRRORS
# =====================================================

def install_chaotics(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "chaotic-keyring-20220514-1-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/garuda/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Chaotics keyring is now installed")
    except Exception as e:
        print(e)

    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "chaotic-mirrorlist-20220504-2-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/garuda/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Chaotics mirrorlist is now installed")
    except Exception as e:
        print(e)

def install_endeavouros(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "endeavouros-keyring-20220523-3-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/eos/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("EndeavourOS keyring is now installed")
    except Exception as e:
        print(e)

    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "endeavouros-mirrorlist-4.4.3-1-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/eos/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("EndeavourOS mirrorlist is now installed")
    except Exception as e:
        print(e)

def install_arcolinux(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "arcolinux-keyring-20230919-6-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/arco/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("ArcoLinux keyring is now installed")
    except Exception as e:
        print(e)

    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "arcolinux-mirrorlist-git-22.04-01-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/arco/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("ArcoLinux mirrorlist is now installed")
    except Exception as e:
        print(e)

def install_xerolinux(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    name1 = "xerolinux-mirrorlist-0.1.2-1-any.pkg.tar.zst"
    try:
        install = 'pacman -U ' + base_dir + '/data/xero/packages/' + name1 + ' --noconfirm'
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Xerolinux mirrorlist is now installed")
    except Exception as e:
        print(e)

# =====================================================
#               PERMISSIONS
# =====================================================

def test(dst):
    for root, dirs, filesr in os.walk(dst):
        # print(root)
        for folder in dirs:
            pass
            # print(dst + "/" + folder)
            for file in filesr:
                pass
                # print(dst + "/" + folder + "/" + file)
        for file in filesr:
            pass
            # print(dst + "/" + file)

def permissions(dst):
    try:
        # original_umask = os.umask(0)
        # calls = subprocess.run(["sh", "-c", "cat /etc/passwd | grep " +
        #                         sudo_username],
        #                        shell=False,
        #                        stdout=subprocess.PIPE,
        #                        stderr=subprocess.STDOUT)
        groups = subprocess.run(["sh", "-c", "id " +
                                 sudo_username],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        for x in groups.stdout.decode().split(" "):
            if "gid" in x:
                g = x.split("(")[1]
                group = g.replace(")", "").strip()
        # print(group)
        # name = calls.stdout.decode().split(":")[0].strip()
        # group = calls.stdout.decode().split(":")[4].strip()

        subprocess.call(["chown", "-R",
                         sudo_username + ":" + group, dst], shell=False)

    except Exception as e:
        print(e)

# =====================================================
#               RATE-MIRRORS
# =====================================================

def install_rate_mirrors(self):
    install = 'pacman -S rate-mirrors --needed --noconfirm'

    if os.path.exists("/usr/bin/rate-mirrors"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               REFLECTOR
# =====================================================

def install_reflector(self):
    install = 'pacman -S reflector --needed --noconfirm'

    if os.path.exists("/usr/bin/reflector"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               RESTART PROGRAM
# =====================================================

def restart_program():
    if os.path.exists("/tmp/att.lock"):
        os.unlink("/tmp/att.lock")
        python = sys.executable
        os.execl(python, python, *sys.argv)


# =====================================================
#               SERVICES - AVAHI
# =====================================================

def install_discovery(self):
    install = 'pacman -S avahi nss-mdns gvfs-smb --needed --noconfirm'

    if check_package_installed("avahi") and check_package_installed("nss-mdns") \
            and check_package_installed("gvfs-smb"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Avahi, nss-mdns and gvfs-smb is now installed")

    command = 'systemctl enable avahi-daemon.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We enabled avahi-daemon.service")

def remove_discovery(self):

    command = 'systemctl stop avahi-daemon.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    command = 'systemctl disable avahi-daemon.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We disabled avahi-daemon.service")

    command = 'systemctl stop avahi-daemon.socket -f'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    command = 'systemctl disable avahi-daemon.socket -f'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We disabled avahi-daemon.socket")

    command = 'pacman -Rs avahi --noconfirm'
    if check_package_installed("avahi"):
        subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Avahi was removed")

    command = 'pacman -Rs nss-mdns --noconfirm'
    if check_package_installed("nss-mdns"):
        subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("nss-mdns was removed")

    command = 'pacman -Rs gvfs-smb --noconfirm'
    if check_package_installed("gvfs-smb"):
        subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("gvfs-smb was removed")
    else:
        pass

# =====================================================
#               SERVICES - SAMBA
# =====================================================

def install_samba(self):
    install = 'pacman -S samba gvfs-smb --needed --noconfirm'

    if not os.path.isdir("/var/cache/samba"):
                os.makedirs("/var/cache/samba", 0o755)

    if check_package_installed("samba") and check_package_installed("gvfs-smb"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Samba and gvfs-smb are now installed")

    command = 'systemctl enable smb.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We enabled smb.service")

    command = 'systemctl enable nmb.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We enabled nmb.service")

def uninstall_samba(self):

    command = 'systemctl disable smb.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We disabled smb.service")

    command = 'systemctl disable nmb.service -f --now'
    subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    print("We disabled nmb.service")

    command = 'pacman -Rs samba --noconfirm'
    if check_package_installed("samba"):
        subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Samba was removed if there were no dependencies")

    command = 'pacman -Rs gvfs-smb --noconfirm'
    if check_package_installed("nss-mdns"):
        subprocess.call(command.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("gvfs-smb was removed")

# =====================================================
#               SAMBA CONF COPY
# =====================================================

def copy_samba(choice):
    command ="cp /usr/share/archlinux-tweak-tool/data/any/samba/" + choice + "/smb.conf /etc/samba/smb.conf"
    subprocess.call(command.split(" "),
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    if choice == "example":
        if not os.path.isdir("/home/" + sudo_username + "/Shared"):
            os.makedirs("/home/" + sudo_username + "/Shared", 0o755)
        permissions("/home/" + sudo_username + "/Shared")
        try:
            with open(samba_config, "r", encoding="utf-8") as f:
                lists = f.readlines()
                f.close()

            val = _get_position(lists, "[SAMBASHARE]")
            lists[val+1] = "path = " + "/home/" + sudo_username + "/Shared\n"

            print("You have choosen for the easy setup")
            print("We have added a folder called 'Shared' to your home directory")
            print("You can access this folder from any computer in your network")
            print("You can write and remove items from the shared folder")
            print("Reboot or restart smb first")
            print(lists[val+1])

            with open(samba_config, "w") as f:
                f.writelines(lists)
                f.close()
        except Exception as e:
            print(e)

    if choice == "usershares":
        #make folder
        if not os.path.isdir("/var/lib/samba/usershares"):
            os.makedirs("/var/lib/samba/usershares", 0o770)

        #create system sambashare group
        try:
            if check_group("sambashare"):
                pass
            else:
                try:
                    command ="groupadd -r sambashare"
                    subprocess.call(command.split(" "),
                                    shell=False,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

        #add user to group
        try:
            command ="gpasswd -a " + sudo_username + " sambashare"
            subprocess.call(command.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        except Exception as e:
            print(e)

        try:
            command ="chown root:sambashare /var/lib/samba/usershares"
            subprocess.call(command.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        except Exception as e:
            print(e)

        try:
            command ="chmod 1770 /var/lib/samba/usershares"
            subprocess.call(command.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        except Exception as e:
            print(e)

# =====================================================
#               SAMBA EDIT
# =====================================================

def save_samba_config(self,widget):
    #create smb.conf if there is none?
    if os.path.isfile(samba_config):
        if not os.path.isfile(samba_config + ".bak"):
            shutil.copy(samba_config, samba_config + ".bak")
        try:
            with open(samba_config, "r", encoding="utf-8") as f:
                lists = f.readlines()
                f.close()

            path = self.entry_path.get_text()
            browseable = self.samba_share_browseable.get_active()
            if browseable:
                browseable = "yes"
            else:
                browseable = "no"
            guest = self.samba_share_guest.get_active()
            if guest:
                guest = "yes"
            else:
                guest = "no"
            public = self.samba_share_public.get_active()
            if public:
                public = "yes"
            else:
                public = "no"
            writable = self.samba_share_writable.get_active()
            if writable:
                writable = "yes"
            else:
                writable = "no"

            val = _get_position(lists, "[SAMBASHARE]")
            if lists[val] == ";[SAMBASHARE]\n":
                lists[val] = "[SAMBASHARE]" +"\n"
            lists[val+1] = "path = " + path +"\n"
            lists[val+2] = "browseable  = " + browseable +"\n"
            lists[val+3] = "guest ok = " + guest +"\n"
            lists[val+4] = "public = " + public +"\n"
            lists[val+5] = "writable = " + writable +"\n"

            print("These lines have been saved at the end of /etc/samba/smb.conf")
            print("Edit this file to add more shares")
            print(lists[val])
            print(lists[val+1])
            print(lists[val+2])
            print(lists[val+3])
            print(lists[val+4])
            print(lists[val+5])

            with open(samba_config, "w") as f:
                f.writelines(lists)
                f.close()

            print("Smb.conf has been saved")
            show_in_app_notification(self, "Smb.conf has been saved")
        except:
            pass
    else:
        print("Choose or create your own smb.conf in /etc/samba/smb.conf then change settings")
        show_in_app_notification(self, "Choose or create your own smb.conf")

# =====================================================
#                       SDDM
# =====================================================

def create_sddm_k_dir():
    if not os.path.isdir(sddm_default_d2_dir):
        try:
            os.mkdir(sddm_default_d2_dir)
        except Exception as e:
            print(e)

# =====================================================
#                       SHELL
# =====================================================

def source_shell(self):
    process = subprocess.run(["sh", "-c", "echo \"$SHELL\""],
                             stdout=subprocess.PIPE)

    output = process.stdout.decode().strip()
    if output == "/bin/bash":
        subprocess.run(["bash", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.bashrc\""],
                       stdout=subprocess.PIPE)
    elif output == "/bin/zsh":
        subprocess.run(["zsh", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.zshrc\""],
                       stdout=subprocess.PIPE)
    elif output == "/usr/bin/fish":
        subprocess.run(["fish", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.config/fish/config.fish\""],
                       stdout=subprocess.PIPE)

def get_shell():
    process = subprocess.run(["su", "-", sudo_username,"-c","echo \"$SHELL\""],
                             #shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

    output = process.stdout.decode().strip().strip('\n')
    if output == "/bin/bash" or output == "/usr/bin/bash":
        return "bash"
    elif output == "/bin/zsh" or output == "/usr/bin/zsh":
        return "zsh"
    elif output == "/bin/fish" or output == "/usr/bin/fish":
        return "fish"

def run_as_user(script):
    subprocess.call(["su - " + sudo_username + " -c " + script], shell=False)

def install_extra_shell(package):
    install = 'pacman -S ' + package + ' --needed --noconfirm'
    print(install)
    try:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    except Exception as e:
        print(e)

# =====================================================
#               THUNAR SHARE PLUGIN
# =====================================================

def install_arco_thunar_plugin(self, widget):
    install = 'pacman -S thunar arcolinux-thunar-shares-plugin --noconfirm'

    if check_package_installed(" arcolinux-thunar-shares-plugin"):
        print("Arcolinux-thunar-shares-plugin is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Arcolinux-thunar-shares-plugin is now installed - reboot")
        GLib.idle_add(self.label7.set_text, "Arcolinux-thunar-shares-plugin is now installed - reboot")
    print("Other apps that might be interesting for sharing are :")
    print(" - arcolinux-nemo-share (cinnamon)")
    print(" - arcolinux-caja-share (mate)")
    print(" - arcolinux-nautilus-share (gnome - budgie)")
    print(" - kdenetwork-filesharing (plasma)")

# =====================================================
#               UBLOCK ORIGIN
# =====================================================

def ublock_get_state(self):
    if os.path.exists("/usr/lib/firefox/browser/extensions/uBlock0@raymondhill.net.xpi"):
        return True
    return False

def set_firefox_ublock(self, toggle, state):
    GLib.idle_add(toggle.set_sensitive, False)
    GLib.idle_add(self.label7.set_text, "Run..")
    GLib.idle_add(self.progress.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self.progress)

    try:

        install_ublock = "pacman -S firefox-ublock-origin --needed --noconfirm"
        uninstall_ublock = 'pacman -Rs firefox-ublock-origin --noconfirm'

        if state:
            GLib.idle_add(self.label7.set_text, "Installing ublock Origin...")
            subprocess.call(install_ublock.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        else:
            GLib.idle_add(self.label7.set_text, "Removing ublock Origin...")
            subprocess.call(uninstall_ublock.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

        GLib.idle_add(self.label7.set_text, "Complete")
        GLib.source_remove(timeout_id)
        timeout_id = None
        GLib.idle_add(self.progress.set_fraction, 0)

        GLib.idle_add(toggle.set_sensitive, True)
        if state:
            GLib.idle_add(self.label7.set_text, "uBlock Origin installed")
        else:
            GLib.idle_add(self.label7.set_text, "uBlock Origin removed")

    except Exception as e:
        MessageBox(self, "ERROR!!", str(e))
        print(e)

# =====================================================
#               ZSH + PACKAGES (ARCOLINUXD)
# =====================================================

def install_zsh(self):
    install = 'pacman -S zsh zsh-completions zsh-syntax-highlighting --needed --noconfirm'
    try:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("All Zsh packages have been installed - completions and syntax highlighting")
        GLib.idle_add(self.label7.set_text, "All Zsh packages have been installed")
    except Exception as e:
        print(e)

def install_only_zsh(self):
    install = 'pacman -S zsh --needed --noconfirm'
    try:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Only Zsh has been installed")
        GLib.idle_add(self.label7.set_text, "Only Zsh has been installed")
    except Exception as e:
        print(e)
