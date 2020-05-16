# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import numpy as np
import Functions as fn
import Settings
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk  # noqa

arco_logout = [
    "arcolinux-logout-git"
]

desktops = [
    "awesome",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "deepin",
    "gnome",
    "herbstluftwm",
    "i3",
    "jwm",
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
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polkit-gnome",
    "vicious",
    "arcolinux-awesome-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
bspwm = [
    "bspwm",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polybar",
    "polkit-gnome",
    "sutils-git",
    "sxhkd",
    "xtitle-git",
    "arcolinux-bspwm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-polybar-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
budgie = [
    "budgie-desktop",
    "budgie-extras",
    "gnome",
    "dconf-editor",
    "guake",
    "ttf-hack",
    "arcolinux-budgie-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
]
cinnamon = [
    "cinnamon",
    "nemo-fileroller",
    "cinnamon-translations",
    "gnome-screenshot",
    "gnome-system-monitor",
    "gnome-terminal",
    "mintlocale",
    "iso-flag-png",
    "arcolinux-cinnamon-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "xfce4-terminal",
]
deepin = [
    "deepin",
    "deepin-extra",
    "arcolinux-deepin-git",
    "arcolinux-wallpapers-git",
    "arcolinux-tweak-tool-git",
]
gnome = [
    "gnome",
    "dconf-editor",
    "guake",
    "ttf-hack",
    "arcolinux-gnome-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
]
hlwm = [
    "herbstluftwm",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polkit-gnome",
    "polybar",
    "sxhkd",
    "xtitle-git",
    "arcolinux-herbstluftwm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-polybar-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-wallpapers-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
i3 = [
    "i3-gaps",
    "i3status",
    "autotiling",
    "dmenu",
    "feh",
    "picom",
    "polkit-gnome",
    "polybar",
    "arcolinux-i3wm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-polybar-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-wallpapers-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
jwm = [
    "jwm",
    "autorandr",
    "dmenu",
    "feh",
    "picom",
    "polkit-gnome",
    "sxhkd",
    "xdgmenumaker",
    "arcolinux-jwm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-notifyd",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
lxqt = [
    "lxqt",
    "dmenu",
    "lxqt-arc-dark-theme-git",
    "obconf-qt",
    "pavucontrol-qt",
    "picom",
    "polkit-gnome",
    "xscreensaver",
    "arcolinux-logout-git",
    "arcolinux-lxqt-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
mate = [
    "mate",
    "mate-extra",
    "mate-tweak",
    "dmenu",
    "gnome-screenshot",
    "arcolinux-mate-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
openbox = [
    "openbox",
    "dmenu",
    "feh",
    "geany",
    "gksu",
    "gmrun",
    "gnome-screenshot",
    "gtk2-perl",
    "nitrogen",
    "obconf",
    "obmenu3",
    "obmenu-generator",
    "perl-linux-desktopfiles",
    "picom",
    "polkit-gnome",
    "rofi",
    "tint2",
    "xcape",
    "yad",
    "arcolinux-common-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-nitrogen-git",
    "arcolinux-obmenu-generator-git",
    "arcolinux-openbox-git",
    "arcolinux-pipemenus-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-tint2-git",
    "arcolinux-tint2-themes-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
plasma = [
    "plasma-meta",
    "ark",
    "discover",
    "ffmpegthumbs",
    "gwenview",
    "kde-system-meta",
    "okular",
    "packagekit-qt5",
    "yakuake",
    "spectacle",
    "surfn-arc-breeze-icons-git",
    "arcolinux-plasma-git",
    "arcolinux-arc-kde",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
]
qtile = [
    "qtile",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polkit-gnome",
    "python-psutil",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-qtile-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
]
xfce = [
    "xfce4",
    "xfce4-goodies",
    "dmenu",
    "gmrun",
    "polkit-gnome",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-wallpapers-git",
]
xmonad = [
    "xmonad",
    "xmonad-contrib",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "haskell-dbus",
    "perl-checkupdates-aur",
    "perl-www-aur",
    "picom",
    "polkit-gnome",
    "polybar",
    "xmonad-log",
    "xmonad-utils",
    "arcolinux-local-xfce4-git",
    "arcolinux-logout-git",
    "arcolinux-polybar-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-xmonad-polybar-git",
    "arcolinux-wallpapers-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-terminal",
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

def check_lock(self, desktop, state):
    if fn.os.path.isfile("/var/lib/pacman/db.lck"):
        md = Gtk.MessageDialog(parent=self,
                            flags=0,
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.YES_NO,
                            text="Lock File Found")
        md.format_secondary_markup(
            "pacman lock file found, do you want to remove it and continue?")  # noqa

        result = md.run()
        md.destroy()

        if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
            fn.os.unlink("/var/lib/pacman/db.lck")
            # print("YES")
            t1 = fn.threading.Thread(target=install_desktop,
                                    args=(self,
                                        self.d_combo.get_active_text(),
                                        state))
            t1.daemon = True
            t1.start()
    else:
        # print("NO FILE")
        t1 = fn.threading.Thread(target=install_desktop,
                                 args=(self,
                                       self.d_combo.get_active_text(),
                                       state))
        t1.daemon = True
        t1.start()

    return False


def check_package(self, path, package):
    if fn.os.path.isfile(path + "/" + package):
        with fn.subprocess.Popen(["sh", "-c", "yes | pkexec pacman -R " + package], bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
            for line in p.stdout:
                GLib.idle_add(self.desktopr_stat.set_text, line.strip())


def install_desktop(self, desktop, state):

    src = ["/etc/skel/.config/polybar"]
    twm = False
    # error = False

    if desktop == "awesome":
        command = list(np.append(awesome, arco_logout))
        src.append("/etc/skel/.config/awesome")
        twm = True
    elif desktop == "bspwm":
        command = list(np.append(bspwm, arco_logout))
        src.append("/etc/skel/.config/bspwm")
        twm = True
    elif desktop == "budgie-desktop":
        check_package(self, "/usr/bin", "catfish")
        command = budgie
    elif desktop == "cinnamon":
        command = cinnamon
    elif desktop == "deepin":
        check_package(self, "/usr/bin", "qt5ct")
        command = deepin
    elif desktop == "gnome":
        command = gnome
    elif desktop == "herbstluftwm":
        command = list(np.append(hlwm, arco_logout))
        src.append("/etc/skel/.config/herbstluftwm")
        twm = True
    elif desktop == "i3":
        command = list(np.append(i3, arco_logout))
        src.append("/etc/skel/.config/i3")
        twm = True
    elif desktop == "jwm":
        command = list(np.append(jwm, arco_logout))
        src.append("/etc/skel/.config/jwm")
        src.append("/etc/skel/.jwmrc")
        twm = True
    elif desktop == "lxqt":
        command = list(np.append(lxqt, arco_logout))
        src.append("/etc/skel/.config/lxqt")
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/pcmanfm-qt")
        src.append("/etc/skel/.config/qterminal.org")
        src.append("/etc/skel/.local/share/filemanager/actions/")
        twm = True
    elif desktop == "mate":
        command = mate
    elif desktop == "openbox":
        command = list(np.append(openbox, arco_logout))
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/obmenu-generator")
        src.append("/etc/skel/.config/tint2")
        src.append("/etc/skel/.config/nitrogen")
        twm = True
    elif desktop == "plasma":
        check_package(self, "/usr/bin", "qt5ct")
        command = plasma
        src.append("/etc/skel/.config")
        src.append("/etc/skel/.local/share")
        twm = True
    elif desktop == "qtile":
        command = list(np.append(qtile, arco_logout))
        src.append("/etc/skel/.config/qtile")
        twm = True
    elif desktop == "xfce":
        command = list(np.append(xfce, arco_logout))
    elif desktop == "xmonad":
        command = list(np.append(xmonad, arco_logout))
        src.append("/etc/skel/.xmonad")
        twm = True
    # fn.subprocess.call(list(np.append(pkexec, command)))

    GLib.idle_add(self.desktopr_prog.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, fn.do_pulse, None, self.desktopr_prog)
    # print(command)

    if state == "reinst":
        com1 = pkexec_reinstall
        if self.ch1.get_active():
            GLib.idle_add(self.desktopr_stat.set_text, "Clearing cache .....")
            fn.subprocess.call(["sh", "-c", "yes | pkexec pacman -Scc"], shell=False, stdout=fn.subprocess.PIPE)
    else:
        com1 = pkexec

    # print(list(np.append(com1, command)))

    GLib.idle_add(self.desktopr_stat.set_text, "installing " + self.d_combo.get_active_text() + "...")

    with fn.subprocess.Popen(list(np.append(com1, command)), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
        for line in p.stdout:
            GLib.idle_add(self.desktopr_stat.set_text, line.strip())

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(self.desktopr_prog.set_fraction, 0)

    if check_desktop(desktop):
        print(src)
        if twm is True:
            for x in src:
                if fn.os.path.isdir(x) or fn.os.path.isfile(x):
                    print(x)
                    dest = x.replace("/etc/skel", fn.home)
                    # print(dest)
                    if fn.os.path.isdir(x):
                        dest = fn.os.path.split(dest)[0]
                    l1 = np.append(copy, [x])
                    l2 = np.append(l1, [dest])
                    GLib.idle_add(self.desktopr_stat.set_text, "Copying " + x + " to " + dest)

                    with fn.subprocess.Popen(list(l2), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
                        for line in p.stdout:
                            GLib.idle_add(self.desktopr_stat.set_text, line.strip())
                    # fn.subprocess.call(list(l2), shell=False, stdout=fn.subprocess.PIPE)
                    fn.permissions(dest)

        GLib.idle_add(self.desktopr_stat.set_text, "")
        GLib.idle_add(self.desktop_status.set_text, "This desktop is installed")
        GLib.idle_add(fn.show_in_app_notification, self, desktop + " has been installed")
    else:
        GLib.idle_add(self.desktop_status.set_markup, "This desktop is <b>NOT</b> installed")
        GLib.idle_add(self.desktopr_error.set_text, "Install " + desktop + " via terminal")
        # GLib.idle_add(self.desktopr_stat.set_text, "An error has occured in installation")
        GLib.idle_add(fn.show_in_app_notification, self, desktop + " has not been installed")
