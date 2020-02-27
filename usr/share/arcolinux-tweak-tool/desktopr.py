# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import Functions as fn

desktops = [
    "gnome",
    "cinnamon",
    "deepin",
    "mate",
    "budgie",
    "plasma",
    "xfce"
]


def check_desktop(desktop):
    # /usr/share/xsessions/xfce.desktop
    lst = fn.os.listdir("/usr/share/xsessions/")
    for x in lst:
        if desktop + ".desktop" == x:
            return True

    return False


def install_desktop(self, desktop):
    if desktop == "plasma":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed plasma-meta packagekit-qt5 partitionmanager kdeconnect systemd-kcm ocs-url systemd-kcm yakuake spectacle okular gwenview dolphin-plugins kde-gtk-config ark ffmpegthumbs kdeadmin-meta kdebase-meta"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "xfce":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed ristretto thunar-archive-plugin thunar-media-tags-plugin xfburn xfce4-battery-plugin xfce4-clipman-plugin xfce4-cpufreq-plugin xfce4-cpugraph-plugin xfce4-datetime-plugin xfce4-dict xfce4-diskperf-plugin xfce4-eyes-plugin xfce4-fsguard-plugin xfce4-genmon-plugin xfce4-mailwatch-plugin xfce4-mount-plugin xfce4-mpc-plugin xfce4-netload-plugin xfce4-notes-plugin xfce4-notifyd xfce4-pulseaudio-plugin xfce4-screensaver xfce4-screenshooter xfce4-sensors-plugin xfce4-smartbookmark-plugin xfce4-systemload-plugin xfce4-taskmanager xfce4-time-out-plugin xfce4-timer-plugin xfce4-verve-plugin xfce4-wavelan-plugin xfce4-weather-plugin xfce4-whiskermenu-plugin xfce4-xkb-plugin xfce4-panel-profiles"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "gnome":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed gnome gnome-extra nautilus-image-converter gnome-mplayer gnome-multi-writer gnome-pie chrome-gnome-shell libappindicator-gtk3 guake"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "budgie":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed budgie-desktop budgie-extras gnome gnome-extra nautilus-image-converter gnome-mplayer gnome-multi-writer gnome-pie gnome-screensaver guake"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "deepin":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed deepin deepin-extra dtkwidget linux-headers"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "cinnamon":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --noconfirm --needed cinnamon nemo-fileroller cinnamon-translations gnome-terminal gnome-system-monitor gnome-screenshot"])
        fn.show_in_app_notification(self, desktop + " has been installed")
    if desktop == "mate":
        fn.subprocess.call(["sh", "-c", "pkexec pacman -S --needed mate mate-extra pasystray paprefs"])
        fn.show_in_app_notification(self, desktop + " has been installed")
