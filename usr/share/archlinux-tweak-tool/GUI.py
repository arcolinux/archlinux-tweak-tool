# =================================================================
# =               Author: Brad Heffernan & Erik Dubois            =
# =================================================================

# ============Functions============
import Functions
import autostart
import desktopr
import fish
import distro
import fixes
import lightdm
import neofetch
import sddm
import termite
import themer
import user
import zsh_theme
#import polybar
#import slim
#import Gtk_Functions
#import oblogout
#import skelapp

# =============GUI=================
import autostart_GUI
import desktopr_GUI
import Fish_GUI
import Fixes_GUI
import Grub_GUI
import HBlock_GUI
import Lightdm_GUI
import Arcolinuxmirrors_GUI
import Neofetch_GUI
import Pacman_GUI
import Termite_GUI
import Utilities_GUI
import Sddm_GUI
import Themer_GUI
import zsh_theme_GUI
import User_GUI
#import Oblogout_GUI
#import Slimlock_GUI
#import polybar_GUI
#import GTK_GUI
#import SkelApp_GUI

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os, Pango):  # noqa
    process = Functions.subprocess.run(["sh", "-c", "echo \"$SHELL\""],
                             stdout=Functions.subprocess.PIPE)

    output = process.stdout.decode().strip()

    # =======================================================
    #                       App Notifications
    # =======================================================

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.notification_revealer = Gtk.Revealer()
    self.notification_revealer.set_reveal_child(False)

    self.notification_label = Gtk.Label()

    pb_panel = GdkPixbuf.Pixbuf().new_from_file(base_dir + '/images/panel.png')
    panel = Gtk.Image().new_from_pixbuf(pb_panel)

    overlayFrame = Gtk.Overlay()
    overlayFrame.add(panel)
    overlayFrame.add_overlay(self.notification_label)

    self.notification_revealer.add(overlayFrame)

    hbox0.pack_start(self.notification_revealer, True, False, 0)

    # ==========================================================
    #                       CONTAINER
    # ==========================================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    vbox.pack_start(hbox, True, True, 0)
    self.add(vbox)

    # ==========================================================
    #                    INITIALIZE STACK
    # ==========================================================
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
    stack.set_transition_duration(350)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack11 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack12 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack13 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack14 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack15 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack16 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack17 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack18 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack19 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack20 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)



    # ==========================================================
    #                AUTOSTART
    # ==========================================================

    autostart_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack13, autostart,
                      Functions, base_dir)

    # ==========================================================
    #                DESKTOP
    # ==========================================================

    desktopr_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack12, desktopr,
                     Functions, base_dir, Pango)

    # ==========================================================
    #                FISH
    # ==========================================================

    Fish_GUI.GUI(self, Gtk, vboxStack2, fish, base_dir, GdkPixbuf)

    # # ==========================================================
    # #               FIXES
    # # ==========================================================

    Fixes_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack19, user, Functions)

    # ==========================================================
    #                 GRUB
    # ==========================================================

    if Functions.file_check("/boot/grub/themes/Vimix/theme.txt"):
        Grub_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack4, Functions)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Grub")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack4.pack_start(hbox31, False, False, 0)
        vboxStack4.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("We did not find a <b>/boot/grub/themes/Vimix/themes.txt</b> file\nMake sure the ArcoLinux repos are activated in the Pacman tab\nWe will reload ATT automatically")

        install_arco_vimix = Gtk.Button(label="Install Vimix theme and it will be applied automatically")
        install_arco_vimix.connect("clicked", self.on_click_install_arco_vimix_clicked)

        vboxStack4.pack_start(install_arco_vimix, False, False, 0)
        vboxStack4.pack_start(ls, True, False, 0)

    # # ==========================================================
    # #               LIGHTDM
    # # ==========================================================

    if Functions.file_check(Functions.lightdm_conf):
        Lightdm_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack11, lightdm, Functions)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Lightdm Autologin")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack11.pack_start(hbox31, False, False, 0)
        vboxStack11.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("We did not find an <b>/etc/lightdm/lightdm.conf</b> file\nIf you install <b>lightdm</b> you can toggle autologin and set your default desktop session\nWe will reload ATT automatically ")

        install_lightdm = Gtk.Button(label="Install Lightdm and enable it")
        install_lightdm.connect("clicked", self.on_click_att_lightdm_clicked)

        vboxStack11.pack_start(install_lightdm, False, False, 0)
        vboxStack11.pack_start(ls, True, False, 0)

    # ==========================================================
    #                 MIRRORLIST ARCOLINUX
    # ==========================================================

    Arcolinuxmirrors_GUI.GUI(self, Gtk, vboxStack16, Functions)

    # # ==========================================================
    # #               NEOFETCH
    # # ==========================================================

    if Functions.file_check(Functions.neofetch_config):
        Neofetch_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack8, neofetch, Functions)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Neofetch Editor")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack8.pack_start(hbox31, False, False, 0)
        vboxStack8.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("If you install <b>Neofetch</b> and the <i>ArcoLinux themes</i> you can customize <b>Neofetch</b>")
        vboxStack8.pack_start(ls, True, False, 0)

    # ==========================================================
    #                 PACMAN
    # ==========================================================
    if Functions.file_check(Functions.pacman):
        Pacman_GUI.GUI(self, Gtk, vboxStack1, Functions)

    # ==========================================================
    #                 PRIVACY - HBLOCK
    # ==========================================================

    HBlock_GUI.GUI(self, Gtk, vboxStack3, Functions)

    # # ==========================================================
    # #               SDDM
    # # ==========================================================

    # if "plasma" in self.desktop.lower():
    #     hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    #     hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    #     lbl1 = Gtk.Label(xalign=0)
    #     lbl1.set_text("Sddm Autologin")
    #     lbl1.set_name("title")
    #     hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    #     hbox41.pack_start(hseparator, True, True, 0)
    #     hbox31.pack_start(lbl1, False, False, 0)
    #     vboxStack17.pack_start(hbox31, False, False, 0)
    #     vboxStack17.pack_start(hbox41, False, False, 0)
    #     ls = Gtk.Label()
    #     ls.set_markup("Use the Plasma settings manager to set Sddm")
    #     reset_sddm_original = Gtk.Button(label="Apply the sddm.conf from ArcoLinux")
    #     reset_sddm_original.connect("clicked", self.on_click_fix_sddm_conf)

    #     vboxStack17.pack_end(reset_sddm_original, False, False, 0)
    #     vboxStack17.pack_start(ls, True, False, 0)

    # else:

    if Functions.file_check(Functions.sddm_default_d1) and Functions.file_check(Functions.sddm_default_d2) and os.path.exists("/usr/bin/sddm"):
        Sddm_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack17, sddm, Functions)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Sddm Autologin")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack17.pack_start(hbox31, False, False, 0)
        vboxStack17.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("No /usr/bin/sddm, /etc/sddm.conf and/or /etc/sddm.conf.d/kde_settings.conf file found. \nUse button 1 to install and enable <b>Sddm</b>.\n ")
        #reset_sddm_original = Gtk.Button(label="2. Apply the sddm.conf from ArcoLinux")
        #reset_sddm_original.connect("clicked", self.on_click_no_sddm_reset_original)
        install_sddm = Gtk.Button(label="1. Install Sddm and enable it")
        install_sddm.connect("clicked", self.on_click_att_sddm_clicked)
        reset_sddm_original_restart = Gtk.Button(label="2. Restart ArchLinux Tweak Tool")
        reset_sddm_original_restart.connect("clicked", self.on_refresh_att_clicked)

        vboxStack17.pack_start(ls, False, False, 0)
        vboxStack17.pack_end(reset_sddm_original_restart, False, False, 0)
        #vboxStack17.pack_end(reset_sddm_original, False, False, 0)
        vboxStack17.pack_end(install_sddm, False, False, 0)

    # # ==========================================================
    # #               TERMINALS - TERMITE CONFIG
    # # ==========================================================

    Termite_GUI.GUI(self, Gtk, vboxStack7, termite, GdkPixbuf, base_dir)

    # # ==========================================================
    # #               TERMINAL FUN
    # # ==========================================================

    Utilities_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack20, Functions)

    # ==========================================================
    #                 THEMES
    # ==========================================================

    if distro.id() == "arcolinux":
        Themer_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions, base_dir)

    # # ==========================================================
    # #                USER
    # # ==========================================================

    User_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack18, user, Functions)
    ls = Gtk.Label()
    ls.set_markup("Fill in the fields and create your account")
    vboxStack18.pack_start(ls, True, False, 0)

     # ==========================================================
    #                   ZSH
    # ==========================================================

    zsh_theme_GUI.GUI(self, Gtk, vboxStack15, zsh_theme, base_dir, GdkPixbuf)

    # ==========================================================
    #                   ADD TO WINDOW
    # ==========================================================

    stack.add_titled(vboxStack13, "stack13", "Autostart")  # Autostart

    stack.add_titled(vboxStack12, "stack12", "Desktop")  # Desktop installer

    #stack.add_titled(vboxStack2, "stack5", "Fish")  # Fish

    stack.add_titled(vboxStack19, "stack19", "Fixes")  # Fixes

    stack.add_titled(vboxStack4, "stack1", "Grub")  # Grub config

    stack.add_titled(vboxStack11, "stack3", "Lightdm")  # Lightdm config

    stack.add_titled(vboxStack16, "stack16", "Mirrors")  # mirrors

    stack.add_titled(vboxStack8, "stack4", "Neofetch")  # Neofetch config

    stack.add_titled(vboxStack1, "stack6", "Pacman")  # Pacman config

    stack.add_titled(vboxStack3, "stack2", "Privacy")  # Hblock

    stack.add_titled(vboxStack17, "stack17", "Sddm")  # Sddm config

    stack.add_titled(vboxStack7, "stack8", "Terminals")  # Termite themes

    stack.add_titled(vboxStack20, "stack20", "Terminal Fun") # lolcat and others

    if distro.id() == "arcolinux":
        stack.add_titled(vboxStack10, "stack11", "Themes")  # Theme changer

    stack.add_titled(vboxStack18, "stack18", "User")  # Sddm config

    stack.add_titled(vboxStack15, "stack15", "Zsh")  # Zsh themes

    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_name("sidebar")
    stack_switcher.set_stack(stack)

    # =====================================================
    #                       LOGO
    # =====================================================

    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-stock.png'), 45, 45)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    # =====================================================
    #               RESTART BUTTON
    # =====================================================

    lbl_distro = Gtk.Label(xalign=0)
    lbl_distro.set_markup("Working on\n" + Functions.change_distro_label(distro.id()))
    btnReStartAtt = Gtk.Button(label="Restart ATT")
    btnReStartAtt.connect('clicked', self.on_refresh_att_clicked)
    #btnReStartAtt.set_property("has-tooltip", True)
    #btnReStartAtt.connect("query-tooltip", self.tooltip_callback,
    #           "Restart the Arch Linux Tweak Tool")

    # =====================================================
    #                      PACKS
    # =====================================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

    hbox2.pack_start(lbl_distro, False, False, 0)
    hbox3.pack_start(btnReStartAtt, False, False, 0)

    #ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)

    ivbox.pack_start(hbox2, False, False, 0)
    ivbox.pack_start(hbox3, False, False, 0)

    vbox1.pack_start(hbox0, False, False, 0)
    vbox1.pack_start(stack, True, True, 0)

    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(vbox1, True, True, 0)

    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
