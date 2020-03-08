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
    "budgie-desktop",
    "cinnamon",
    "deepin",
    "gnome",
    "herbstluftwm",
    "i3",
    "lxqt",
    "mate",
    "openbox",
    "plasma",
    "qtile",
    "xfce",
    "xmonad"
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm"]
pkexec_reinstall = ["pkexec", "pacman", "-S", "--noconfirm"]
copy = ["cp", "-Rv"]

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
    "awesome-terminal-fonts",
    "arcolinux-oblogout",
    "arcolinux-oblogout-themes-git"
]
i3 = [
    "i3-gaps",
    "i3status",
    "arcolinux-i3wm-git",
    "dmenu"
]
lxqt = [
    "lxqt",
    "arcolinux-lxqt-git",
    "lxqt-arc-dark-theme-git",
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
    "nitrogen",
    "arcolinux-nitrogen-git",
    "tint2",
    "arcolinux-tint2-git",
    "arcolinux-tint2-themes-git",
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
    "awesome-terminal-fonts",
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


def install_desktop(self, desktop, state):
    src = ["/etc/skel/.config/polybar"]
    twm = False

    if desktop == "awesome":
        command = awesome
        src.append("/etc/skel/.config/awesome")
        twm = True
    elif desktop == "bspwm":
        command = bspwm
        src.append("/etc/skel/.config/bspwm")
        twm = True
    elif desktop == "budgie-desktop":
        command = budgie
    elif desktop == "cinnamon":
        command = cinnamon
    elif desktop == "deepin":
        command = deepin
    elif desktop == "gnome":
        command = gnome
    elif desktop == "herbstluftwm":
        command = hlwm
        src.append("/etc/skel/.config/herbstluftwm")
        twm = True
    elif desktop == "i3":
        command = i3
        src.append("/etc/skel/.config/i3")
        twm = True
    elif desktop == "lxqt":
        command = lxqt
        # src.append([])
        # twm = True
    elif desktop == "mate":
        command = mate
    elif desktop == "openbox":
        command = openbox
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/obmenu-generator")
        twm = True
    elif desktop == "plasma":
        command = plasma
    elif desktop == "qtile":
        command = qtile
        src.append("/etc/skel/.config/qtile")
        twm = True
    elif desktop == "xfce":
        command = xfce
    elif desktop == "xmonad":
        command = xmonad
        src.append("/etc/skel/.xmonad")
        twm = True
    # fn.subprocess.call(list(np.append(pkexec, command)))

    GLib.idle_add(self.desktopr_prog.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, fn.do_pulse, None, self.desktopr_prog)

    if state == "reinst":
        com1 = pkexec_reinstall
        if self.ch1.get_active():
            GLib.idle_add(self.desktopr_stat.set_text, "Clearing cache .....")
            fn.subprocess.call(["sh", "-c", "yes | pkexec pacman -Scc"], shell=False, stdout=fn.subprocess.PIPE)
    else:
        com1 = pkexec

    GLib.idle_add(self.desktopr_stat.set_text, "installing " + self.d_combo.get_active_text() + "...")

    with fn.subprocess.Popen(list(np.append(com1, command)), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
        for line in p.stdout:
            GLib.idle_add(self.desktopr_stat.set_text, line.strip())

    if twm is True:
        for x in src:
            if fn.os.path.isdir(x):
                dest = x.replace("/etc/skel", fn.home)
                # print(dest)
                l1 = np.append(copy, [x])
                l2 = np.append(l1, [dest])
                GLib.idle_add(self.desktopr_stat.set_text, "Copying " + x + " to " + dest)

                fn.subprocess.call(list(l2), shell=False, stdout=fn.subprocess.PIPE)
                fn.permissions(dest)

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(self.desktopr_prog.set_fraction, 0)
    GLib.idle_add(self.desktopr_stat.set_text, "")
    GLib.idle_add(self.desktop_status.set_text, "This desktop is installed")
    GLib.idle_add(fn.show_in_app_notification, self, desktop + " has been installed")
