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
import login
import neofetch
import os
import sddm
import services
import shell
import termite
import template
import themer
import user
import zsh_theme
#import polybar
#import slim
#import Gtk_Functions
#import oblogout
#import skelapp

# =============GUI=================
import Autostart_GUI
import Desktopr_GUI
import Fixes_GUI
import Grub_GUI
import Login_GUI
import Arcolinuxmirrors_GUI
import Neofetch_GUI
import Pacman_GUI
import Privacy_GUI
import Termite_GUI
#import Template_GUI
import Utilities_GUI
import Services_GUI
import Shell_GUI
import Themer_GUI
import User_GUI
#import Oblogout_GUI
#import Slimlock_GUI
#import Polybar_GUI
#import GTK_GUI
#import SkelApp_GUI

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os, Pango):  # noqa

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
    vboxStack14 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack15 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack16 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack17 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack18 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack19 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack20 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack21 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack22 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack23 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ==========================================================
    #                AUTOSTART
    # ==========================================================

    Autostart_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack13, autostart,
                      Functions, base_dir)

    # ==========================================================
    #                DESKTOP
    # ==========================================================

    Desktopr_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack12, desktopr,
                     Functions, base_dir, Pango)

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
        ls.set_markup("We did not find a <b>/boot/grub/themes/Vimix/themes.txt</b> file\n<b>First activate the ArcoLinux repos in the Pacman tab</b>\nThen you can install the grub Vimix theme\nWe will reload ATT automatically")

        install_arco_vimix = Gtk.Button(label="Install the grub Vimix theme and ATT will reboot automatically")
        install_arco_vimix.connect("clicked", self.on_click_install_arco_vimix_clicked)

        vboxStack4.pack_start(install_arco_vimix, False, False, 0)
        vboxStack4.pack_start(ls, True, False, 0)

    # ==========================================================
    #                         LOGIN
    # ==========================================================

    Login_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack22, sddm, lightdm, os, Functions)

    # ==========================================================
    #                 MIRRORLIST ARCOLINUX
    # ==========================================================

    if Functions.file_check("/etc/pacman.d/arcolinux-mirrorlist"):
        Arcolinuxmirrors_GUI.GUI(self, Gtk, vboxStack16, Functions)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("ArcoLinux Mirrorlist")
        lbl1.set_name("title")
        hbox31.pack_start(lbl1, False, False, 0)

        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)

        lbl2 = Gtk.Label()
        lbl2.set_markup("First install the ArcoLinux Mirrors and ArcoLinux keys\n\
Then you will be able to set the mirrors of ArcoLinux")

        vboxStack16.pack_start(hbox31, False, False, 0)
        vboxStack16.pack_start(hbox41, False, False, 0)
        vboxStack16.pack_start(lbl2, True, False, 0)


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

    Privacy_GUI.GUI(self, Gtk, vboxStack3, Functions)

    # ==========================================================
    #                      SERVICES
    # ==========================================================

    Services_GUI.GUI(self, Gtk, vboxStack14, Functions)


    # ==========================================================
    #                        SHELLS
    # ==========================================================

    Shell_GUI.GUI(self, Gtk, vboxStack23, zsh_theme, fish, base_dir,GdkPixbuf, Functions)

    # ==========================================================
    #                        TEMPLATE
    # ==========================================================

    #Template_GUI.GUI(self, Gtk, vboxStack21, Functions)

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

    Themer_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions, base_dir)

    # # ==========================================================
    # #                USER
    # # ==========================================================

    User_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack18, user, Functions)
    ls = Gtk.Label()
    ls.set_markup("Fill in the fields and create your account")
    vboxStack18.pack_start(ls, True, False, 0)

    # ==========================================================
    #                   ADD TO WINDOW
    # ==========================================================

    stack.add_titled(vboxStack13, "stack13", "Autostart")  # Autostart

    stack.add_titled(vboxStack12, "stack12", "Desktop")  # Desktop installer

    stack.add_titled(vboxStack19, "stack19", "Fixes")  # Fixes

    stack.add_titled(vboxStack4, "stack1", "Grub")  # Grub config

    stack.add_titled(vboxStack22, "stack22", "Login")  # Lightdm config

    stack.add_titled(vboxStack16, "stack16", "Mirrors")  # mirrors

    if not Functions.distr == "xerolinux":
        stack.add_titled(vboxStack8, "stack4", "Neofetch")  # Neofetch config

    stack.add_titled(vboxStack1, "stack6", "Pacman")  # Pacman config

    stack.add_titled(vboxStack3, "stack2", "Privacy")  # Privacy

    if not Functions.distr == "xerolinux":
        stack.add_titled(vboxStack14, "stack14", "Services")  # services

    if not Functions.distr == "xerolinux":
        stack.add_titled(vboxStack23, "stack23", "Shells")  # shell

    #stack.add_titled(vboxStack21, "stack21", "Template")  # template

    stack.add_titled(vboxStack7, "stack8", "Terminals")  # Termite themes

    stack.add_titled(vboxStack20, "stack20", "Terminal Fun") # lolcat and others

    stack.add_titled(vboxStack10, "stack11", "Themes")  # Theme changer

    stack.add_titled(vboxStack18, "stack18", "User")  # user

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
    #               RESTART/QUIT BUTTON
    # =====================================================

    def on_quit(self):
        os.unlink("/tmp/att.lock")
        Gtk.main_quit()
        print("Thanks for using ArchLinux Tweak Tool")
        print("Report issues to make it even better")
        print("---------------------------------------------------------------------------")

    lbl_distro = Gtk.Label(xalign=0)
    lbl_distro.set_markup("Working on\n" + Functions.change_distro_label(distro.id()))
    btnReStartAtt = Gtk.Button(label="Restart ATT")
    btnReStartAtt.set_size_request(100,30)
    btnReStartAtt.connect('clicked', self.on_refresh_att_clicked)
    btnQuitAtt = Gtk.Button(label="Quit ATT")
    btnQuitAtt.set_size_request(100,30)
    btnQuitAtt.connect('clicked', on_quit)

    # =====================================================
    #                      PACKS
    # =====================================================

    #hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

    hbox2.pack_start(lbl_distro, False, False, 0)
    hbox3.pack_start(btnReStartAtt, False, False, 0)
    hbox4.pack_start(btnQuitAtt, False, False, 0)

    #ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)

    ivbox.pack_start(hbox2, False, False, 0)
    ivbox.pack_start(hbox3, False, False, 0)
    ivbox.pack_start(hbox4, False, False, 0)

    vbox1.pack_start(hbox0, False, False, 0)
    vbox1.pack_start(stack, True, True, 0)

    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(vbox1, True, True, 0)

    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
