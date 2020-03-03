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
    "gnome",
    "cinnamon",
    "deepin",
    "mate",
    "budgie",
    "plasma",
    "xfce"
]
pkexec = ["pkexec", "pacman", "-S", "--needed"]  # , "--noconfirm"]

plasma = [
    "plasma-meta",
    "packagekit-qt5",
    "partitionmanager",
    "kdeconnect",
    "systemd-kcm",
    "ocs-url",
    "systemd-kcm",
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
xfce = [
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
gnome = [
    "gnome",
    "gnome-extra",
    "nautilus-image-converter",
    "gnome-mplayer",
    "gnome-multi-writer",
    "gnome-pie",
    "chrome-gnome-shell",
    "libappindicator-gtk3",
    "guake"
]
budgie = [
    "budgie-desktop",
    "budgie-extras",
    "gnome",
    "gnome-extra",
    "nautilus-image-converter",
    "gnome-mplayer",
    "gnome-multi-writer",
    "gnome-pie",
    "gnome-screensaver",
    "guake"
]
deepin = [
    "deepin",
    "deepin-extra",
    "dtkwidget",
    "linux-headers"
]
cinnamon = [
    "cinnamon",
    "nemo-fileroller",
    "cinnamon-translations",
    "gnome-terminal",
    "gnome-system-monitor",
    "gnome-screenshot"
]
mate = [
    "mate",
    "mate-extra",
    "pasystray",
    "paprefs"
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
    if desktop == "plasma":
        command = plasma
    if desktop == "xfce":
        command = xfce
    if desktop == "gnome":
        command = gnome
    if desktop == "budgie":
        command = budgie
    if desktop == "deepin":
        command = deepin
    if desktop == "cinnamon":
        command = cinnamon
    if desktop == "mate":
        command = mate

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
