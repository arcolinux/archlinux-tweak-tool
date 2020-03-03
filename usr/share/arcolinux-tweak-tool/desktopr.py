# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import numpy as np
import Functions as fn
import Settings
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib  # noqa

desktops = [
    "awesome",
    "bspwm",
    "budgie",
    "cinnamon",
    "deepin",
    "gnome",
    "hlwm",
    "i3wm",
    "lxqt",
    "mate",
    "openbox",
    "plasma",
    "qtile",
    "xfce",
    "xmonad"
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm"]

awesome = [
    "awesome",
    "vicious",
    "arcolinux-awesome-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
bspwm = [
    "bspwm",
    "arcolinux-bspwm-git",
    "sxhkd",
    "awesome-terminal-fonts",
    "polybar",
    "arcolinux-polybar-git",
    "sutils-git",
    "xtitle-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
budgie = [
    "budgie-desktop",
    "budgie-extras",
    "gnome",
    "gnome-extra"
]
cinnamon = [
    "cinnamon",
    "nemo-fileroller",
    "cinnamon-translations",
    "gnome-terminal",
    "gnome-system-monitor",
    "gnome-screenshot",
    "mintlocale",
    "iso-flag-png"
]
deepin = [
    "deepin",
    "deepin-extra"
]
gnome = [
    "gnome",
    "gnome-extra",
    "guake"
]
hlwm = [
    "herbstluftwm",
    "arcolinux-herbstluftwm-git",
    "sxhkd",
    "polybar",
    "arcolinux-polybar-git",
    "xtitle-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
i3wm = [
    "i3-gaps",
    "i3status",
    "arcolinux-i3wm-git",
    "dmenu"
]
lxqt = [
    "lxqt",
    "arcolinux-lxqt-git",
    "dmenu"
]
mate = [
    "mate",
    "mate-extra",
    "mate-tweak"
]
openbox = [
    "openbox",
    "obmenu-generator",
    "obconf",
    "obmenu3",
    "gtk2-perl",
    "perl-linux-desktopfiles",
    "arcolinux-openbox-git",
    "arcolinux-obmenu-generator-git",
    "arcolinux-pipemenus-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
plasma = [
    "plasma-meta",
    "packagekit-qt5",
    "partitionmanager",
    "yakuake",
    "spectacle",
    "okular",
    "gwenview",
    "dolphin-plugins",
    "kde-gtk-config",
    "ark",
    "ffmpegthumbs",
    "kdeadmin-meta",
    "kdebase-meta"
]
qtile = [
    "qtile",
    "python-psutil",
    "arcolinux-qtile-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
xfce = [
    "xfce4",
    "xfce4-goodies",
    "ristretto",
    "thunar-archive-plugin",
    "thunar-media-tags-plugin",
    "xfburn",
    "xfce4-battery-plugin",
    "xfce4-clipman-plugin",
    "xfce4-cpufreq-plugin",
    "xfce4-cpugraph-plugin",
    "xfce4-datetime-plugin",
    "xfce4-dict",
    "xfce4-diskperf-plugin",
    "xfce4-eyes-plugin",
    "xfce4-fsguard-plugin",
    "xfce4-genmon-plugin",
    "xfce4-mailwatch-plugin",
    "xfce4-mount-plugin",
    "xfce4-mpc-plugin",
    "xfce4-netload-plugin",
    "xfce4-notes-plugin",
    "xfce4-notifyd",
    "xfce4-pulseaudio-plugin",
    "xfce4-screensaver",
    "xfce4-screenshooter",
    "xfce4-sensors-plugin",
    "xfce4-smartbookmark-plugin",
    "xfce4-systemload-plugin",
    "xfce4-taskmanager",
    "xfce4-time-out-plugin",
    "xfce4-timer-plugin",
    "xfce4-verve-plugin",
    "xfce4-wavelan-plugin",
    "xfce4-weather-plugin",
    "xfce4-whiskermenu-plugin",
    "xfce4-xkb-plugin"
]
xmonad = [
    "xmonad",
    "xmonad-contrib",
    "haskell-dbus",
    "polybar",
    "arcolinux-polybar-git",
    "xmonad-utils",
    "xmonad-log",
    "arcolinux-xmonad-polybar-git",
    "dmenu",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]


def check_desktop(desktop):
    # /usr/share/xsessions/xfce.desktop
    lst = fn.os.listdir("/usr/share/xsessions/")
    for x in lst:
        if desktop + ".desktop" == x:
            return True

    return False


def uninstall_desktop_check(self, desktop):
    dsk = Settings.read_settings("DESKTOP", "default")
    if not desktop == dsk.strip():
        if check_desktop(desktop):
            uninstall_desktop(desktop)
        else:
            fn.show_in_app_notification(self,
                                        "Not installed...")
    else:
        fn.show_in_app_notification(self,
                                    "That is your default desktop!")


def uninstall_desktop(desktop):
    print("Uninstalling.....")


def install_desktop(self, desktop):
    if desktop == "awesome":
        command = awesome
    if desktop == "bspwm":
        command = bspwm
    if desktop == "budgie":
        command = budgie
    if desktop == "cinnamon":
        command = cinnamon
    if desktop == "deepin":
        command = deepin
    if desktop == "gnome":
        command = gnome
    if desktop == "hlwm":
        command = hlwm
    if desktop == "i3wm":
        command = i3wm
    if desktop == "lxqt":
        command = lxqt
    if desktop == "mate":
        command = mate
    if desktop == "openbox":
        command = openbox
    if desktop == "plasma":
        command = plasma
    if desktop == "qtile":
        command = qtile
    if desktop == "xfce":
        command = xfce
    if desktop == "xmonad":
        command = xmonad
    # fn.subprocess.call(list(np.append(pkexec, command)))

    with fn.subprocess.Popen(list(np.append(pkexec, command)), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
        for line in p.stdout:
            # GLib.idle_add(self.inst_tv.get_buffer())
            text = self.inst_tv.get_buffer()
            # start_iter, end_iter = text.get_iter()
            try:
                end_iter = text.get_end_iter()
                text.insert(end_iter, line.strip() + "/n")
            except:
                pass
            # GLib.idle_add(self.inst_tv.scroll_to_mark, text.get_insert(), 0.0, False, 0.5, 0.5)

            # adj = self.sb.get_vadjustment()
            # adj.set_value(adj.get_upper() - adj.get_page_size())

    GLib.idle_add(fn.show_in_app_notification, self, desktop + " has been installed")
