# =================================================================
# =           Author: Erik Dubois  and Brad Heffernan             =
# =================================================================
import numpy as np
import Functions as fn
import Settings
import gi
import distro
import os
import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk  # noqa

default_app = [
    "nano"
]

# =================================================================
# =                         Desktops                             =
# =================================================================

desktops = [
    "awesome",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "cutefish-xsession",
    "cwm",
    "deepin",
    "fvwm3",
    "dusk",
    "dwm",
    "enlightenment",
    "gnome",
    "herbstluftwm",
    "i3",
    "icewm",
    "jwm",
    "leftwm",
    "lxqt",
    "mate",
    "openbox",
    "plasma",
    "qtile",
    "spectrwm",
    "ukui",
    "wmderland",
    "xfce",
    "xmonad"
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm", "--ask=4"]
pkexec_reinstall = ["pkexec", "pacman", "-S", "--noconfirm"]
copy = ["cp", "-Rv"]

# =================================================================
# =                         Distros                               =
# =================================================================


# =================================================================
# =================================================================
# =================================================================
# =                         ARCOLINUX                             =
# =================================================================
# =================================================================
# =================================================================

if distro.id() == "arcolinux":
    awesome = [
        "alacritty",
        "arcolinux-awesome-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autorandr",
        "awesome",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "noto-fonts",
        "picom",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "vicious",
        "volumeicon",
        "xfce4-terminal",
    ]
    bspwm = [
        "alacritty",
        "arcolinux-bspwm-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "awesome-terminal-fonts",
        "bspwm",
        "dmenu",
        "feh",
        "gvfs",
        "picom",
        "polybar",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "sutils-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
        "xtitle-git",
    ]
    budgie = [
        "arcolinux-budgie-dconf-git",
        "arcolinux-budgie-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-guake-autostart-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "budgie-desktop",
        "budgie-extras",
        "dconf-editor",
        "gnome",
        "gvfs",
        "guake",
        "ttf-hack",
    ]
    cinnamon = [
        "arcolinux-cinnamon-dconf-git",
        "arcolinux-cinnamon-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk3-surfn-arc-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "cinnamon",
        "cinnamon-translations",
        "gnome-screenshot",
        "gnome-system-monitor",
        "gnome-terminal",
        "gvfs",
        "iso-flag-png",
        "mintlocale",
        "nemo-fileroller",
        "xfce4-terminal",
    ]
    cutefish = [
        "cutefish",
        "arcolinux-cutefish-git",
    ]
    cwm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-cwm-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autorandr",
        "cwm",
        "dmenu",
        "feh",
        "gvfs",
        "picom",
        "polybar",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    deepin = [
        "arcolinux-config-all-desktops-git",
        "arcolinux-deepin-dconf-git",
        "arcolinux-deepin-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "deepin",
        "deepin-extra",
        "gvfs",
    ]
    dusk = [
        "alacritty",
        "arcolinux-candy-beauty-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-dwm-st-git",
        "arcolinux-dusk-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "feh",
        "gvfs",
        "picom",
        "polkit-gnome",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    dwm = [
        "alacritty",
        "arcolinux-candy-beauty-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-dwm-git",
        "arcolinux-dwm-slstatus-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "feh",
        "gvfs",
        "gsimplecal",
        "picom",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    enlightenment = [
        "enlightenment",
    ]
    fvwm3 = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-fvwm3-git",
        "arcolinux-gtk3-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autorandr",
        "dmenu",
        "feh",
        "fvwm3-git",
        "gvfs",
        "gsimplecal",
        "lxappearance",
        "picom",
        "polybar",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    gnome = [
        "arcolinux-config-all-desktops-git",
        "arcolinux-gnome-dconf-git",
        "arcolinux-gnome-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-guake-autostart-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "dconf-editor",
        "gnome",
        "gnome-extra",
        "gvfs",
        "guake",
        "ttf-hack",
    ]
    hlwm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-herbstluftwm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "herbstluftwm",
        "picom",
        "polkit-gnome",
        "polybar",
        "rofi",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
        "xtitle-git",
    ]
    i3 = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-i3wm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-nitrogen-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autotiling",
        "dmenu",
        "feh",
        "gvfs",
        "i3blocks",
        "i3-gaps",
        "i3status",
        "nitrogen",
        "picom",
        "polkit-gnome",
        "polybar",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    icewm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-surfn-arc-git",
        "arcolinux-icewm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autorandr",
        "dmenu",
        "feh",
        "gvfs",
        "icewm",
        "picom",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xdgmenumaker",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    jwm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-surfn-arc-git",
        "arcolinux-jwm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "autorandr",
        "dmenu",
        "feh",
        "gvfs",
        "jwm",
        "picom",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xdgmenumaker",
        "xfce4-notifyd",
        "xfce4-screenshooter",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    leftwm = [
        "alacritty",
        "arcolinux-candy-beauty-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-leftwm-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "feh",
        "gvfs",
        "leftwm-dev-git",
        "leftwm-theme-git",
        "lxappearance",
        "nerd-fonts-source-code-pro",
        "picom",
        "polybar",
        "polkit-gnome",
        "rofi",
        "rofi-theme-fonts",
        "rxvt-unicode",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "ttf-iosevka-nerd",
        "ttf-material-design-iconic-font",
        "ttf-meslo-nerd-font-powerlevel10k",
        "volumeicon",
        "xfce4-appfinder",
        "xfce4-screenshooter",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    lxqt = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-lxqt-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "gvfs",
        "lxqt",
        "lxqt-arc-dark-theme-git",
        "obconf-qt",
        "picom",
        "polkit-gnome",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xfce4-screenshooter",
        "xfce4-taskmanager",
        "xfce4-terminal",
        "xscreensaver",
    ]
    mate = [
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk3-surfn-arc-git",
        "arcolinux-mate-dconf-git",
        "arcolinux-mate-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "gnome-screenshot",
        "gvfs",
        "mate",
        "mate-extra",
        "mate-tweak",
        "xfce4-terminal",
    ]
    openbox = [
        "alacritty",
        "arcolinux-common-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-docs-git",
        "arcolinux-geany-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-nitrogen-git",
        "arcolinux-obmenu-generator-git",
        "arcolinux-openbox-git",
        "arcolinux-pipemenus-git",
        "arcolinux-plank-git",
        "arcolinux-plank-themes-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-tint2-git",
        "arcolinux-tint2-themes-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "feh",
        "geany",
        "gksu",
        "gnome-screenshot",
        "gvfs",
        "gsimplecal",
        "gtk2-perl",
        "lxappearance-obconf",
        "lxrandr",
        "nitrogen",
        "obconf",
        "obkey",
        "obmenu-generator",
        "obmenu3",
        "openbox",
        "openbox-arc-git",
        "openbox-themes-pambudi-git",
        "perl-linux-desktopfiles",
        "picom",
        "plank",
        "polkit-gnome",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "tint2",
        "ttf-hack",
        "volumeicon",
        "xcape",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
        "yad",
    ]
    plasma = [
        "plasma",
        "kde-system-meta",
        "arcolinux-arc-kde",
        "arcolinux-config-plasma-git",
        "arcolinux-gtk3-surfn-plasma-dark-git",
        "arcolinux-plasma-dconf-git",
        "arcolinux-plasma-git",
        "arcolinux-plasma-kservices-git",
        "arcolinux-root-git",
        "arcolinux-wallpapers-git",
        "ark",
        "breeze",
        "cryfs",
        "discover",
        "dolphin",
        "dolphin-plugins",
        "encfs",
        "ffmpegthumbs",
        "gocryptfs",
        "gvfs",
        "gwenview",
        "kate",
        "kde-gtk-config",
        "kdeconnect",
        "kdenetwork-filesharing",
        "ktorrent",
        "ocs-url",
        "okular",
        "packagekit-qt5",
        "partitionmanager",
        "sddm-kcm",
        "spectacle",
        "surfn-plasma-dark-icons-git",
        "systemd-kcm",
        "yakuake",
    ]
    qtile = [
    "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-qtile-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "picom",
        "polkit-gnome",
        "python-setuptools",
        "python-psutil",
        "qtile",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    spectrwm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-spectrwm-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "picom",
        "polkit-gnome",
        "polybar",
        "python-psutil",
        "rxvt-unicode",
        "spectrwm",
        "sutils-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xdo",
        "xfce4-terminal",
        "xtitle-git",
    ]
    wmderland = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-wmderland-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "dmenu",
        "feh",
        "wmderland-git",
        "picom",
        "polkit-gnome",
        "polybar",
        "rofi",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    ukui = [
        "arcolinux-root-git",
        "arcolinux-ukui-git",
        "gvfs",
        "ukui",
    ]
    xfce = [
        "alacritty",
        "xfce4",
        "xfce4-goodies",
        "catfish",
        "dmenu",
        "gvfs",
        "mugshot",
        "polkit-gnome",
        "rxvt-unicode",
        "ttf-hack",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-root-git",
        "arcolinux-xfce-git",
        "arcolinux-wallpapers-git",
    ]
    xmonad = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk3-sardi-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arcolinux-wallpapers-git",
        "arcolinux-xfce-git",
        "arcolinux-xmonad-polybar-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "haskell-dbus",
        "perl-checkupdates-aur",
        "perl-www-aur",
        "picom",
        "polybar",
        "rofi",
        "rxvt-unicode",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
        "xmonad",
        "xmonad-contrib",
        "xmonad-log",
        "xmonad-utils",
    ]
# =================================================================
# =================================================================
# =================================================================
# =                         ARCHLINUX                             =
# =================================================================
# =================================================================
# =================================================================

# if distro.id() == "arch" or distro.id() == "endeavouros" or distro.id() == "manjaro"\
#                 or distro.id() == "garudalinux":
if not distro.id() == "arcolinux":
    awesome = [
        "alacritty",
        "arcolinux-awesome-git",
        "archlinux-logout-git",
        "awesome",
        "dmenu",
        "feh",
        "lxappearance",
        "noto-fonts",
        "picom",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "vicious",
    ]
    bspwm = [
        "alacritty",
        "arcolinux-bspwm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "awesome-terminal-fonts",
        "bspwm",
        "dmenu",
        "feh",
        "picom",
        "polybar",
        "polkit-gnome",
        "sutils-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xtitle-git",
    ]
    budgie = [
        "budgie-desktop",
        "budgie-extras",
        "gnome",
    ]
    cinnamon = [
        "cinnamon",
        "cinnamon-translations",
        "gnome-screenshot",
        "gnome-system-monitor",
        "gnome-terminal",
        "iso-flag-png",
        "mintlocale",
        "nemo-fileroller",
    ]
    cutefish = [
        "cutefish",
    ]
    cwm = [
        "alacritty",
        "arcolinux-cwm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "cwm",
        "dmenu",
        "feh",
        "picom",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    deepin = [
        "deepin",
        "deepin-extra",
    ]
    dusk = [
        "alacritty",
        "arcolinux-dwm-st-git",
        "arcolinux-dusk-git",
        "archlinux-logout-git",
        "dmenu",
        "feh",
        "picom",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    dwm = [
        "alacritty",
        "arcolinux-dwm-git",
        "arcolinux-dwm-slstatus-git",
        "archlinux-logout-git",
        "dmenu",
        "feh",
        "gsimplecal",
        "picom",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    enlightenment = [
        "enlightenment",
    ]
    fvwm3 = [
        "alacritty",
        "arcolinux-fvwm3-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "dmenu",
        "feh",
        "fvwm3-git",
        "gsimplecal",
        "lxappearance",
        "picom",
        "polybar",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    gnome = [
        "gnome",
        "gnome-extra",
    ]
    hlwm = [
        "alacritty",
        "arcolinux-herbstluftwm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "herbstluftwm",
        "picom",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "xtitle-git",
        "ttf-hack",
    ]
    i3 = [
        "alacritty",
        "arcolinux-i3wm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "dmenu",
        "feh",
        "i3blocks",
        "i3-gaps",
        "i3status",
        "picom",
        "polkit-gnome",
        "polybar",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    icewm = [
        "alacritty",
        "arcolinux-icewm-git",
        "archlinux-logout-git",
        "dmenu",
        "feh",
        "icewm",
        "picom",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xdgmenumaker",
    ]
    jwm = [
        "alacritty",
        "arcolinux-jwm-git",
        "archlinux-logout-git",
        "dmenu",
        "feh",
        "jwm",
        "picom",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xdgmenumaker",
    ]
    leftwm = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-leftwm-git",
        "dmenu",
        "feh",
        "leftwm-dev-git",
        "leftwm-theme-git",
        "lxappearance",
        "nerd-fonts-source-code-pro",
        "picom",
        "polybar",
        "polkit-gnome",
        "rofi-theme-fonts",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-iosevka-nerd",
        "ttf-hack",
        "ttf-material-design-iconic-font",
        "ttf-meslo-nerd-font-powerlevel10k",
    ]
    lxqt = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-lxqt-git",
        "dmenu",
        "lxqt",
        "lxqt-arc-dark-theme-git",
        "obconf-qt",
        "picom",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    mate = [
        "mate",
        "mate-extra",
        "mate-tweak",
    ]
    openbox = [
        "alacritty",
        "arcolinux-common-git",
        "arcolinux-docs-git",
        "arcolinux-geany-git",
        "archlinux-logout-git",
        "arcolinux-obmenu-generator-git",
        "arcolinux-openbox-git",
        "arcolinux-pipemenus-git",
        "arcolinux-tint2-git",
        "arcolinux-tint2-themes-git",
        "dmenu",
        "feh",
        "geany",
        "gksu",
        "gnome-screenshot",
        "gsimplecal",
        "gtk2-perl",
        "lxappearance-obconf",
        "lxrandr",
        "obconf",
        "obkey",
        "obmenu-generator",
        "obmenu3",
        "openbox",
        "openbox-arc-git",
        "perl-linux-desktopfiles",
        "picom",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "tint2",
        "ttf-hack",
        "xcape",
        "yad",
    ]
    plasma = [
        "plasma",
        "arcolinux-sddm-simplicity-git",
        "kde-system-meta",
        "discover",
        "kate",
        "packagekit-qt5",
    ]
    qtile = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-qtile-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "picom",
        "polkit-gnome",
        "python-setuptools",
        "python-psutil",
        "qtile",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    spectrwm = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-spectrwm-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "picom",
        "polkit-gnome",
        "polybar",
        "python-psutil",
        "spectrwm",
        "sutils-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xdo",
        "xtitle-git",
    ]
    wmderland = [
        "alacritty",
        "arcolinux-wmderland-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "dmenu",
        "feh",
        "wmderland-git",
        "picom",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    ukui = [
        "arcolinux-root-git",
        "arcolinux-ukui-git",
        "gvfs",
        "ukui",
    ]
    xfce = [
        "alacritty",
        "xfce4",
        "xfce4-goodies",
        "polkit-gnome",
        "ttf-hack",
    ]
    xmonad = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-xmonad-polybar-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "haskell-dbus",
        "picom",
        "polybar",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "xmonad",
        "xmonad-contrib",
        "xmonad-log",
        "xmonad-utils",
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

    src = []
    twm = False
    # error = False
    # make backup of your .config
    now = datetime.datetime.now()
    if not os.path.exists(fn.home + "/.config-att"):
        os.makedirs(fn.home + "/.config-att")
        fn.permissions(fn.home + "/.config-att")
    #for all users that have now root permissions
    if os.path.exists(fn.home + "/.config-att"):
        fn.permissions(fn.home + "/.config-att")
    fn.copy_func(fn.home + "/.config/", fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S"), isdir=True)
    fn.permissions(fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S"))
    if desktop == "awesome":
        command = list(np.append(awesome, default_app))
        src.append("/etc/skel/.config/awesome")
        twm = True
    elif desktop == "bspwm":
        command = list(np.append(bspwm, default_app))
        src.append("/etc/skel/.config/bspwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "budgie-desktop":
        check_package(self, "/usr/bin", "catfish")
        command = budgie
    elif desktop == "cutefish-xsession":
        command = cutefish
        src.append("/etc/skel/.config/cutefishos")
        twm = True
    elif desktop == "cinnamon":
        command = cinnamon
    elif desktop == "cwm":
        command = list(np.append(cwm, default_app))
        src.append("/etc/skel/.config/cwm")
        src.append("/etc/skel/.cwmrc")
        src.append("/etc/skel/.xprofile")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "deepin":
        check_package(self, "/usr/bin", "qt5ct")
        command = deepin
    elif desktop == "dusk":
        command = list(np.append(dusk, default_app))
        src.append("/etc/skel/.config/arco-dusk")
        twm = True
    elif desktop == "dwm":
        command = list(np.append(dwm, default_app))
        src.append("/etc/skel/.config/arco-dwm")
        twm = True
    elif desktop == "enlightenment":
        command = enlightenment
    elif desktop == "fvwm3":
        command = list(np.append(fvwm3, default_app))
        src.append("/etc/skel/.config/fvwm3")
        src.append("/etc/skel/.fvwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "gnome":
        command = gnome
    elif desktop == "herbstluftwm":
        command = list(np.append(hlwm, default_app))
        src.append("/etc/skel/.config/herbstluftwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "i3":
        command = list(np.append(i3, default_app))
        src.append("/etc/skel/.config/i3")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "icewm":
        command = list(np.append(icewm, default_app))
        src.append("/etc/skel/.config/icewm")
        twm = True
    elif desktop == "jwm":
        command = list(np.append(jwm, default_app))
        src.append("/etc/skel/.config/jwm")
        src.append("/etc/skel/.jwmrc")
        twm = True
    elif desktop == "leftwm":
        command = list(np.append(leftwm, default_app))
        src.append("/etc/skel/.config/leftwm")
        twm = True
    elif desktop == "lxqt":
        command = list(np.append(lxqt, default_app))
        src.append("/etc/skel/.config/lxqt")
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/pcmanfm-qt")
        src.append("/etc/skel/.config/qterminal.org")
        src.append("/etc/skel/.local/share/filemanager/actions/")
        twm = True
    elif desktop == "mate":
        command = mate
    elif desktop == "openbox":
        command = list(np.append(openbox, default_app))
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/obmenu-generator")
        src.append("/etc/skel/.config/tint2")
        src.append("/etc/skel/.config/nitrogen")
        src.append("/etc/skel/.config/picom.conf")
        twm = True
    elif desktop == "plasma":
        check_package(self, "/usr/bin", "qt5ct")
        command = plasma
        src.append("/etc/skel/.config")
        src.append("/etc/skel/.local/share")
        twm = True
    elif desktop == "qtile":
        command = list(np.append(qtile, default_app))
        src.append("/etc/skel/.config/qtile")
        twm = True
    elif desktop == "spectrwm":
        command = list(np.append(spectrwm, default_app))
        src.append("/etc/skel/.config/spectrwm")
        src.append("/etc/skel/.spectrwm.conf")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "ukui":
        command = list(np.append(ukui, default_app))
        src.append("/etc/skel/.config/")
        twm = True
    elif desktop == "wmderland":
        command = list(np.append(wmderland, default_app))
        src.append("/etc/skel/.config/wmderland")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "xfce":
        command = list(np.append(xfce, default_app))
    elif desktop == "xmonad":
        command = list(np.append(xmonad, default_app))
        src.append("/etc/skel/.xmonad")
        src.append("/etc/skel/.config/polybar")
        twm = True
    # fn.subprocess.call(list(np.append(pkexec, command)))

    GLib.idle_add(self.desktopr_prog.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, fn.do_pulse, None, self.desktopr_prog)
    print("----------------------------------------------------------------")
    print("Packages list to install")
    print("----------------------------------------------------------------")
    print(command)
    print("----------------------------------------------------------------")

    if state == "reinst":
        com1 = pkexec_reinstall
        if self.ch1.get_active():
            GLib.idle_add(self.desktopr_stat.set_text, "Clearing cache .....")
            fn.subprocess.call(["sh", "-c", "yes | pkexec pacman -Scc"], shell=False, stdout=fn.subprocess.PIPE)
    else:
        com1 = pkexec

    # print(list(np.append(com1, command)))
    GLib.idle_add(self.desktopr_stat.set_text, "Installing " + self.d_combo.get_active_text() + "...")
    with fn.subprocess.Popen(list(np.append(com1, command)), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
        for line in p.stdout:
            GLib.idle_add(self.desktopr_stat.set_text, line.strip())
    print("----------------------------------------------------------------")

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
        print("----------------------------------------------------------------")
        print(desktop + " has been installed")
        print("----------------------------------------------------------------")
    else:
        GLib.idle_add(self.desktop_status.set_markup, "This desktop is <b>NOT</b> installed")
        GLib.idle_add(self.desktopr_error.set_text, "Install " + desktop + " via terminal")
        # GLib.idle_add(self.desktopr_stat.set_text, "An error has occured in installation")
        GLib.idle_add(fn.show_in_app_notification, self, desktop + " has not been installed")
        print("----------------------------------------------------------------")
        print(desktop + " has NOT been installed")
        print("----------------------------------------------------------------")
    fn.create_log(self)
