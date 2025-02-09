# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import datetime
import numpy as np
from gi.repository import GLib, Gtk  # noqa
import functions as fn
import os

# import Settings
# import gi
# import distro
# import os

# gi.require_version('Gtk', '3.0')

default_app = ["nano", "ttf-hack"]

# =================================================================
# =                         Desktops                             =
# =================================================================

desktops = [
    "awesome",
    "berry",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "chadwm",
    "cutefish-xsession",
    "cwm",
    "fvwm3",
    "dk",
    "dusk",
    "dwm",
    "enlightenment",
    "gnome",
    "herbstluftwm",
    "hyprland",
    "i3",
    "icewm",
    "jwm",
    "leftwm",
    "lxqt",
    "mate",
    "nimdow",
    "niri",
    "openbox",
    "pantheon",
    "plasma",
    "qtile",
    "spectrwm",
    "ukui",
    "wayfire",
    "wmderland",
    "worm",
    "xfce",
    "xmonad",
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm", "--ask=4"]
pkexec_reinstall = ["pkexec", "pacman", "-S", "--noconfirm", "--ask=4"]
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

if fn.distr == "arcolinux":
    awesome = [
        "alacritty",
        "arcolinux-awesome-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "autorandr",
        "awesome",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "noto-fonts",
        "picom-git",
        "polkit-gnome",
        "rofi-lbonn-wayland",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "vicious",
        "volumeicon",
        "xfce4-terminal",
    ]
    berry = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-berry-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "berry-dev-git",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    bspwm = [
        "alacritty",
        "arcolinux-bspwm-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "bspwm",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polybar",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-guake-autostart-git",
        "arcolinux-root-git",
        "arconet-wallpapers",
        "budgie-desktop",
        "budgie-extras",
        "dconf-editor",
        "gvfs",
        "guake",
        "ttf-hack",
    ]
    cinnamon = [
        "arcolinux-cinnamon-dconf-git",
        "arcolinux-cinnamon-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-root-git",
        "arconet-wallpapers",
        "arconet-xfce",
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
    chadwm = [
        "alacritty",
        "arcolinux-chadwm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "rofi-lbonn-wayland",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "ttf-jetbrains-mono-nerd",
        "ttf-meslo-nerd-font-powerlevel10k",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "autorandr",
        "cwm",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    dk = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-dk-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "dk",
        "feh",
        "gvfs",
        "lxappearance",
        "nerd-fonts-source-code-pro",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
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
    dusk = [
        "alacritty",
        "a-candy-beauty-icon-theme-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-dwm-st-git",
        "arcolinux-dusk-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
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
        "a-candy-beauty-icon-theme-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-dwm-git",
        "arcolinux-dwm-slstatus-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "gvfs",
        "gsimplecal",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "autorandr",
        "dmenu",
        "feh",
        "fvwm3-git",
        "gvfs",
        "gsimplecal",
        "lxappearance",
        "picom-git",
        "polybar",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-guake-autostart-git",
        "arcolinux-root-git",
        "arconet-wallpapers",
        "dconf-editor",
        "extension-manager",
        "file-roller",
        "gnome",
        "gnome-tweaks",
        "guake",
        "gvfs",
        "ttf-hack",
    ]
    hlwm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-herbstluftwm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "herbstluftwm",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
        "xtitle-git",
    ]
    hyprland = [
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-hyprland-git",
        "arcolinux-kitty-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-wayland-app-hooks-git",
        "arconet-xfce",
        "btop",
        "grim",
        "hyprcursor-git",
        "hyprland-git",
        "hyprlang-git",
        "hyprutils-git",
        "hyprwayland-scanner-git",
        "kitty",
        "lxappearance",
        "mako",
        "micro",
        "pamixer",
        "pulsemixer",
        "python-pywal",
        "rofi-lbonn-wayland",
        "swaybg",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "uwsm",
        "waybar-git",
        "wofi",
        "xfce4-terminal",
    ]
    i3 = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-i3wm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-nitrogen-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "autotiling",
        "dmenu",
        "feh",
        "gvfs",
        "i3blocks",
        "i3-wm",
        "i3status",
        "lxappearance",
        "nitrogen",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-icewm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "autorandr",
        "dmenu",
        "feh",
        "gvfs",
        "icewm",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-jwm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "autorandr",
        "dmenu",
        "feh",
        "gvfs",
        "jwm",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
        "a-candy-beauty-icon-theme-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-leftwm-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "gvfs",
        "leftwm-git",
        "leftwm-theme-git",
        "lxappearance",
        "nerd-fonts-source-code-pro",
        "picom-git",
        "polybar",
        "polkit-gnome",
        "rofi-lbonn-wayland",
        "rofi-theme-fonts",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-lxqt-git",
        "arcolinux-root-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "gvfs",
        "ksuperkey",
        "lxqt",
        "lxqt-arc-dark-theme-git",
        "obconf-qt",
        "picom-git",
        "polkit-gnome",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-mate-dconf-git",
        "arcolinux-mate-git",
        "arcolinux-root-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "gnome-screenshot",
        "gvfs",
        "mate",
        "mate-extra",
        "mate-tweak",
        "xfce4-terminal",
    ]
    nimdow = [
        "archlinux-logout-git",
        "arcolinux-btop-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-nimdow-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-powermenu-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "btop",
        "gvfs",
        "dex",
        "dmenu",
        "lxappearance",
        "nim",
        "nimdow-bin",
        "picom-git",
        "rofi-lbonn-wayland",
        "rofi-theme-fonts",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "xfce4-terminal",
        "xorg-xsetroot",
    ]
    niri = [
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-niri-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-wayland-app-hooks-git",
        "arconet-xfce",
        "btop",
        "dex",
        "grim",
        "niri",
        "lxappearance",
        "mako",
        "micro",
        "pamixer",
        "python-pywal",
        "pulsemixer",
        "rofi-lbonn-wayland",
        "swaybg",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "waybar-git",
        "wofi",
        "xwayland-satellite",
        "yad",
    ]
    openbox = [
        "alacritty",
        "arcolinux-common-git",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-docs-git",
        "arcolinux-geany-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-nitrogen-git",
        "arcolinux-obmenu-generator-git",
        "arcolinux-openbox-git",
        "arcolinux-pipemenus-git",
        "arcolinux-plank-git",
        "arcolinux-plank-themes-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-tint2-git",
        "arcolinux-tint2-themes-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
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
        "obmenu-generator",
        "obmenu3",
        "openbox",
        "openbox-arc-git",
        "openbox-themes-pambudi-git",
        "perl-linux-desktopfiles",
        "picom-git",
        "plank",
        "polkit-gnome",
        "rofi-lbonn-wayland",
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
    pantheon = [
        "pantheon",
    ]
    plasma = [
        "plasma",
        "kde-system-meta",
        "arcolinux-arc-kde",
        "arcolinux-root-git",
        "arconet-wallpapers",
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
        "packagekit-qt6",
        "partitionmanager",
        "spectacle",
        "surfn-plasma-dark-icons-git",
        "yakuake",
    ]
    qtile = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-qtile-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "python-setuptools",
        "python-psutil",
        "qtile",
        "rofi-lbonn-wayland",
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
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-spectrwm-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
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
        "volumeicon",
        "xdo",
        "xfce4-terminal",
        "xtitle-git",
    ]
    wayfire = [
        "a-candy-beauty-icon-theme-git",
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-foot-git",
        "arcolinux-kitty-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-wallpapers-wayfire-git",
        "arcolinux-wayfire-git",
        "arcolinux-wayland-app-hooks-git",
        "arconet-xfce",
        "btop",
        "feh",
        "foot",
        "grim",
        "kitty",
        "libliftoff",
        "lxappearance",
        "mako",
        "micro",
        "pamixer",
        "python-pywal",
        "pulsemixer",
        "polkit-gnome",
        "rofi-lbonn-wayland",
        "slurp",
        "swaybg",
        "swayidle",
        "swaylock",
        "swww",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "waybar-git",
        "wayfire-git",
        "wayfire-plugins-extra-git",
        "wcm-git",
        "wf-kill-git",
        "wf-shell-git",
        "wl-clipboard",
        "wofi",
        "xfce4-terminal",
    ]
    wmderland = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-wmderland-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "wmderland-git",
        "xfce4-terminal",
    ]
    worm = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-worm-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "rofi-lbonn-wayland",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "worm-dev-git",
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
        "ttf-hack",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-root-git",
        "arconet-xfce",
        "arconet-wallpapers",
    ]
    xmonad = [
        "alacritty",
        "arcolinux-config-all-desktops-git",
        "arcolinux-dconf-all-desktops-git",
        "arcolinux-gtk-surfn-arc-git",
        "arcolinux-local-xfce4-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "arcolinux-xmonad-polybar-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "gvfs",
        "haskell-dbus",
        "lxappearance",
        "perl-checkupdates-aur",
        "perl-www-aur",
        "picom-git",
        "polybar",
        "rofi-lbonn-wayland",
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

# if fn.distr == "arch" or fn.distr == "endeavouros" or fn.distr == "manjaro"\
#                 or fn.distr == "garudalinux":
if fn.distr != "arcolinux":
    awesome = [
        "alacritty",
        "arcolinux-awesome-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "awesome",
        "dmenu",
        "feh",
        "noto-fonts",
        "picom-git",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "vicious",
    ]
    berry = [
        "alacritty",
        "arcolinux-berry-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-root-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "arconet-xfce",
        "dmenu",
        "feh",
        "berry-dev-git",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    bspwm = [
        "alacritty",
        "arcolinux-bspwm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "awesome-terminal-fonts",
        "bspwm",
        "dmenu",
        "feh",
        "picom-git",
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
    chadwm = [
        "alacritty",
        "arcolinux-chadwm-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-volumeicon-git",
        "arconet-wallpapers",
        "dmenu",
        "feh",
        "gvfs",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "ttf-jetbrains-mono-nerd",
        "ttf-meslo-nerd-font-powerlevel10k",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
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
        "picom-git",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    dk = [
        "alacritty",
        "arcolinux-dk-git",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "dmenu",
        "dk",
        "feh",
        "gvfs",
        "lxappearance",
        "nerd-fonts-source-code-pro",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    dusk = [
        "alacritty",
        "arcolinux-dwm-st-git",
        "arcolinux-dusk-git",
        "arcolinux-powermenu-git",
        "archlinux-logout-git",
        "archlinux-wallpapers-git",
        "dmenu",
        "feh",
        "picom-git",
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
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "dmenu",
        "feh",
        "gsimplecal",
        "picom-git",
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
        "picom-git",
        "polybar",
        "polkit-gnome",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    gnome = [
        "dconf-editor",
        "file-roller",
        "gnome",
        "gnome-tweaks",
    ]
    hlwm = [
        "alacritty",
        "arcolinux-herbstluftwm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "herbstluftwm",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "xtitle-git",
        "ttf-hack",
    ]
    hyprland = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-hyprland-git",
        "arcolinux-kitty-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-wayland-app-hooks-git",
        "arconet-xfce",
        "btop",
        "grim",
        "hyprcursor-git",
        "hyprland-git",
        "hyprlang-git",
        "hyprutils-git",
        "hyprwayland-scanner-git",
        "kitty",
        "lxappearance",
        "mako",
        "micro",
        "pamixer",
        "python-pywal",
        "pulsemixer",
        "rofi-lbonn-wayland",
        "swaybg",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "waybar-git",
        "wofi",
        "xfce4-terminal",
    ]
    i3 = [
        "alacritty",
        "arcolinux-i3wm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "autotiling",
        "dmenu",
        "feh",
        "i3blocks",
        "i3-wm",
        "i3status",
        "picom-git",
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
        "picom-git",
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
        "picom-git",
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
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "dmenu",
        "feh",
        "leftwm-git",
        "leftwm-theme-git",
        "nerd-fonts-source-code-pro",
        "picom-git",
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
        "picom-git",
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
    nimdow = [
        "alacritty",
        "arcolinux-nimdow-git",
        "arcolinux-powermenu-git",
        "dmenu",
        "nim",
        "nimdow-bin",
        "picom-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "xfce4-terminal",
        "xorg-xsetroot",
    ]
    niri = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-niri-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arconet-xfce",
        "btop",
        "dex",
        "grim",
        "lxappearance",
        "mako",
        "micro",
        "niri",
        "python-pywal",
        "rofi-lbonn-wayland",
        "swaybg",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "waybar-git",
        "wofi",
        "xwayland-satellite",
        "yad",
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
        "arcolinux-powermenu-git",
        "arcolinux-tint2-git",
        "arcolinux-tint2-themes-git",
        "archlinux-wallpapers-git",
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
        "obmenu-generator",
        "obmenu3",
        "openbox",
        "openbox-arc-git",
        "perl-linux-desktopfiles",
        "picom-git",
        "polkit-gnome",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "tint2",
        "ttf-hack",
        "xcape",
        "yad",
    ]
    pantheon = [
        "pantheon",
    ]
    plasma = [
        "plasma",
        "arcolinux-sddm-simplicity-git",
        "kde-system-meta",
        "discover",
        "kate",
        "packagekit-qt6",
    ]
    qtile = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-powermenu-git",
        "arcolinux-qtile-git",
        "archlinux-wallpapers-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "picom-git",
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
        "archlinux-wallpapers-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "picom-git",
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
    wayfire = [
        "a-candy-beauty-icon-theme-git",
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-alacritty-git",
        "arcolinux-foot-git",
        "arcolinux-kitty-git",
        "arcolinux-powermenu-git",
        "arcolinux-pywal-cache-git",
        "arcolinux-rofi-git",
        "arcolinux-rofi-themes-git",
        "arcolinux-wallpapers-wayfire-git",
        "arcolinux-wayfire-git",
        "arcolinux-wayland-app-hooks-git",
        "arconet-xfce",
        "btop",
        "feh",
        "foot",
        "grim",
        "kitty",
        "libliftoff",
        "lxappearance",
        "mako",
        "micro",
        "pamixer",
        "python-pywal",
        "pulsemixer",
        "polkit-gnome",
        "rofi-lbonn-wayland",
        "slurp",
        "swaybg",
        "swayidle",
        "swaylock",
        "swww",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-jetbrains-mono-nerd",
        "waybar-git",
        "wayfire-git",
        "wayfire-plugins-extra-git",
        "wcm-git",
        "wf-kill-git",
        "wf-shell-git",
        "wl-clipboard",
        "wofi",
        "xfce4-terminal",
    ]
    wmderland = [
        "alacritty",
        "arcolinux-wmderland-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "archlinux-wallpapers-git",
        "dmenu",
        "feh",
        "wmderland-git",
        "picom-git",
        "polkit-gnome",
        "polybar",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
    ]
    worm = [
        "alacritty",
        "arcolinux-worm-git",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-root-git",
        "arconet-xfce",
        "dmenu",
        "feh",
        "worm-dev-git",
        "picom-git",
        "polkit-gnome",
        "polybar",
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
        "polkit-gnome",
        "ttf-hack",
    ]
    xmonad = [
        "alacritty",
        "archlinux-logout-git",
        "arcolinux-polybar-git",
        "arcolinux-powermenu-git",
        "arcolinux-xmonad-polybar-git",
        "awesome-terminal-fonts",
        "archlinux-wallpapers-git",
        "dmenu",
        "feh",
        "haskell-dbus",
        "picom-git",
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
    """check if desktop is installed"""
    # /usr/share/xsessions/xfce.desktop
    if os.path.exists("/usr/share/xsessions"):
        lst = fn.listdir("/usr/share/xsessions/")
        for xsession in lst:
            if desktop + ".desktop" == xsession:
                return True
    if os.path.exists("/usr/share/wayland-sessions"):
        lst = fn.listdir("/usr/share/wayland-sessions/")
        for xsession in lst:
            if desktop + ".desktop" == xsession:
                return True

    return False


def check_lock(self, desktop, state):
    """check pacman lock"""
    if fn.path.isfile("/var/lib/pacman/db.lck"):
        mess_dialog = Gtk.MessageDialog(
            parent=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Lock File Found",
        )
        mess_dialog.format_secondary_markup(
            "pacman lock file found, do you want to remove it and continue?"
        )  # noqa

        result = mess_dialog.run()
        mess_dialog.destroy()

        if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
            fn.unlink("/var/lib/pacman/db.lck")
            # print("YES")
            t1 = fn.threading.Thread(
                target=install_desktop,
                args=(self, self.d_combo.get_active_text(), state),
            )
            t1.daemon = True
            t1.start()
    else:
        # print("NO FILE")
        t1 = fn.threading.Thread(
            target=install_desktop, args=(self, self.d_combo.get_active_text(), state)
        )
        t1.daemon = True
        t1.start()

    return False


def check_package_and_remove(self, package):
    """remove a package if exists"""
    if fn.check_package_installed(package):
        fn.remove_package(self, package)


def install_desktop(self, desktop, state):
    src = []
    twm = False
    # error = False
    # make backup of your .config
    now = datetime.datetime.now()
    if not fn.path.exists(fn.home + "/.config-att"):
        fn.makedirs(fn.home + "/.config-att")
        fn.permissions(fn.home + "/.config-att")
    # for all users that have now root permissions
    if fn.path.exists(fn.home + "/.config-att"):
        fn.permissions(fn.home + "/.config-att")
    fn.copy_func(
        fn.home + "/.config/",
        fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S"),
        isdir=True,
    )
    fn.permissions(
        fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S")
    )

    if fn.distr == "archcraft":
        fn.clear_skel_directory()

    check_package_and_remove(self, "rofi")
    check_package_and_remove(self, "rofi-lbonn-wayland-git")
    check_package_and_remove(self, "rofi-lbonn-wayland-only-git")

    if desktop == "awesome":
        command = list(np.append(awesome, default_app))
        src.append("/etc/skel/.config/awesome")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "berry":
        command = list(np.append(berry, default_app))
        src.append("/etc/skel/.config/berry")
        src.append("/etc/skel/.config/polybar")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "bspwm":
        command = list(np.append(bspwm, default_app))
        src.append("/etc/skel/.config/bspwm")
        src.append("/etc/skel/.config/polybar")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "budgie-desktop":
        check_package_and_remove(self, "catfish")
        command = budgie
    elif desktop == "cutefish-xsession":
        command = cutefish
        src.append("/etc/skel/.config/cutefishos")
        twm = True
    elif desktop == "chadwm":
        command = list(np.append(chadwm, default_app))
        src.append("/etc/skel/.config/arco-chadwm")
        src.append("/etc/skel/.config/eww")
        src.append("/etc/skel/.config/powermenu")
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
    elif desktop == "dk":
        command = list(np.append(dk, default_app))
        src.append("/etc/skel/.config/dk")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "dusk":
        command = list(np.append(dusk, default_app))
        src.append("/etc/skel/.config/arco-dusk")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "dwm":
        command = list(np.append(dwm, default_app))
        src.append("/etc/skel/.config/arco-dwm")
        src.append("/etc/skel/.config/powermenu")
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
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "hyprland":
        command = list(np.append(hyprland, default_app))
        src.append("/etc/skel/.config/alacritty")
        src.append("/etc/skel/.bin")
        src.append("/etc/skel/.config/hypr")
        src.append("/etc/skel/.cache/wal")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "i3":
        command = list(np.append(i3, default_app))
        src.append("/etc/skel/.config/i3")
        src.append("/etc/skel/.config/polybar")
        src.append("/etc/skel/.config/powermenu")
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
        src.append("/etc/skel/.config/powermenu")
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
    elif desktop == "nimdow":
        command = list(np.append(nimdow, default_app))
        src.append("/etc/skel/.config/nimdow")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "niri":
        command = list(np.append(niri, default_app))
        src.append("/etc/skel/.config/alacritty")
        src.append("/etc/skel/.bin")
        src.append("/etc/skel/.config/powermenu")
        src.append("/etc/skel/.config/niri")
        src.append("/etc/skel/.cache/wal")
        twm = True
    elif desktop == "pantheon":
        command = pantheon
    elif desktop == "openbox":
        command = list(np.append(openbox, default_app))
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/obmenu-generator")
        src.append("/etc/skel/.config/tint2")
        src.append("/etc/skel/.config/nitrogen")
        src.append("/etc/skel/.config/picom.conf")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "plasma":
        check_package_and_remove(self, "qt5ct")
        command = plasma
        src.append("/etc/skel/.config")
        src.append("/etc/skel/.local/share")
        twm = True
    elif desktop == "qtile":
        command = list(np.append(qtile, default_app))
        src.append("/etc/skel/.config/qtile")
        src.append("/etc/skel/.config/powermenu")
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
    elif desktop == "wayfire":
        command = list(np.append(wayfire, default_app))
        src.append("/etc/skel/.bin")
        src.append("/etc/skel/.config/alacritty")
        src.append("/etc/skel/.config/wayfire")
        src.append("/etc/skel/.config/wayfire.ini")
        src.append("/etc/skel/.config/wayfire-azerty.ini")
        src.append("/etc/skel/.config/wf-shell.ini")
        src.append("/etc/skel/.cache/wal")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "wmderland":
        command = list(np.append(wmderland, default_app))
        src.append("/etc/skel/.config/wmderland")
        src.append("/etc/skel/.config/polybar")
        src.append("/etc/skel/.config/powermenu")
        twm = True
    elif desktop == "worm":
        command = list(np.append(worm, default_app))
        src.append("/etc/skel/.config/worm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "xfce":
        command = list(np.append(xfce, default_app))
    elif desktop == "xmonad":
        command = list(np.append(xmonad, default_app))
        src.append("/etc/skel/.xmonad")
        src.append("/etc/skel/.config/polybar")
        src.append("/etc/skel/.config/powermenu")
        twm = True

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
            fn.subprocess.call(
                ["sh", "-c", "yes | pkexec pacman -Scc"],
                shell=False,
                stdout=fn.subprocess.PIPE,
            )
    else:
        com1 = pkexec

    # print(list(np.append(com1, command)))
    GLib.idle_add(
        self.desktopr_stat.set_text,
        "Installing " + self.d_combo.get_active_text() + "...",
    )

    for line in command:
        package_name = line if isinstance(line, str) else line[0]
        print(f"   Installing: {package_name}")
        GLib.idle_add(
            self.desktopr_stat.set_text,
            f"   Installing {package_name}...",
        )

        try:
            process = fn.subprocess.Popen(
                list(np.append(com1, line)),
                bufsize=1,
                stdout=fn.subprocess.PIPE,
                stderr=fn.subprocess.PIPE,  # Capture stderr for error handling
                universal_newlines=True,
            )

            stdout, stderr = process.communicate()  # Read both stdout and stderr
            process_return_code = process.returncode  # Get the return code

            for output_line in stdout.splitlines():
                GLib.idle_add(self.desktopr_stat.set_text, output_line.strip())

            # List of group packages
            group_packages = [
                "budgie-desktop",
                "budgie-extras",
                "cinnamon",
                "cutefish",
                "enlightenment",
                "gnome-extra",
                "gnome",
                "mate-extra",
                "mate",
                "pantheon",
                "plasma",
                "ukui",
                "xfce4-goodies",
                "xfce4",
            ]

            try:
                # Check the return code for success or failure
                if process_return_code == 0:
                    if package_name in group_packages:
                        print(
                            "There is no way to check if a group package is installed"
                        )
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            "There is no way to check if a group package is installed.",
                        )
                    elif fn.check_package_installed(package_name):
                        print(f"{package_name} is installed")
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Successfully installed {package_name}.",
                        )
                    else:
                        print(
                            f"{package_name} IS NOT INSTALLED - REMOVE CONFLICTING PACKAGE(S)"
                        )
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Failed to install {package_name}. Possible conflicts detected.",
                        )
                else:
                    print(f"Failed to install {package_name}: {stderr}")
                    GLib.idle_add(
                        self.desktopr_stat.set_text,
                        f"Failed to install {package_name}. Error: {stderr}",
                    )

            except Exception as e:
                print(f"An error occurred while installing {package_name}: {str(e)}")
                GLib.idle_add(
                    self.desktopr_stat.set_text,
                    f"An error occurred: {str(e)}",
                )
        except Exception as e:
            print(f"An error occurred while installing {package_name}: {str(e)}")
            GLib.idle_add(
                self.desktopr_stat.set_text,
                f"An error occurred: {str(e)}",
            )

    # with fn.subprocess.Popen(
    #     list(np.append(com1, command)),
    #     bufsize=1,
    #     stdout=fn.subprocess.PIPE,
    #     universal_newlines=True,
    # ) as p:
    #     for line in p.stdout:
    #         GLib.idle_add(self.desktopr_stat.set_text, line.strip())
    # print("----------------------------------------------------------------")

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(self.desktopr_prog.set_fraction, 0)

    if check_desktop(desktop):
        print(src)
        if twm is True:
            for x in src:
                if fn.path.isdir(x) or fn.path.isfile(x):
                    print(x)
                    dest = x.replace("/etc/skel", fn.home)
                    # print(dest)
                    if fn.path.isdir(x):
                        dest = fn.path.split(dest)[0]
                    l1 = np.append(copy, [x])
                    l2 = np.append(l1, [dest])
                    GLib.idle_add(
                        self.desktopr_stat.set_text, "Copying " + x + " to " + dest
                    )

                    with fn.subprocess.Popen(
                        list(l2),
                        bufsize=1,
                        stdout=fn.subprocess.PIPE,
                        universal_newlines=True,
                    ) as p:
                        for line in p.stdout:
                            GLib.idle_add(self.desktopr_stat.set_text, line.strip())
                    fn.permissions(dest)

        GLib.idle_add(self.desktopr_stat.set_text, "")
        GLib.idle_add(self.desktop_status.set_text, "This desktop is installed")
        GLib.idle_add(
            fn.show_in_app_notification, self, desktop + " has been installed"
        )
        print("----------------------------------------------------------------")
        print(desktop + " has been installed")
        print("----------------------------------------------------------------")
    else:
        GLib.idle_add(
            self.desktop_status.set_markup, "This desktop is <b>NOT</b> installed"
        )
        GLib.idle_add(
            self.desktopr_error.set_text, "Install " + desktop + " via terminal"
        )
        # GLib.idle_add(self.desktopr_stat.set_text, "An error has occured in installation")
        GLib.idle_add(
            fn.show_in_app_notification, self, desktop + " has not been installed"
        )
        print("----------------------------------------------------------------")
        print(desktop + " has NOT been installed")
        print("----------------------------------------------------------------")
    fn.create_log(self)
