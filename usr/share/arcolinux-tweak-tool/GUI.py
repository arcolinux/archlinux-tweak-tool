#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

#============Functions============
import Functions
import slim
import Gtk_Functions
import oblogout
import termite
import neofetch
import skelapp
import lightdm

#=============GUI=================
import Termite_GUI
import Neofetch_GUI
import Oblogout_GUI
import Slimlock_GUI
import Grub_GUI
import HBlock_GUI
import Pacman_GUI
import GTK_GUI
import SkelApp_GUI
import Lightdm_GUI

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os):
    #=======================================================
    #                       App Notifications
    #=======================================================
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
    # grid = Gtk.Grid()
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
    vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack11 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ==========================================================
    #                   TAB #0 WELCOME
    # ==========================================================
    # Welcome_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack10, welcome, Functions)
    # ==========================================================
    #                   TAB #1 PACMAN
    # ==========================================================

    Pacman_GUI.GUI(self, Gtk, vboxStack1, Functions)

    # ==========================================================
    #                 TAB #2 GTK THEMES
    # ==========================================================
    # GTK_GUI.GUI(self, Gtk, vboxStack2, Gtk_Functions, Functions)

    # ==========================================================
    #                       HBLOCK
    # ==========================================================
    HBlock_GUI.GUI(self, Gtk, vboxStack3, Functions)

    # ==========================================================
    #                       GRUB
    # ==========================================================
    Grub_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack4, Functions)
    
    # ==========================================================
    #                       TAB #5 SLIMLOCK
    # ==========================================================
    Slimlock_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack5, slim, os)

    # ==========================================================
    #                       TAB #6 OBLOGOUT
    # ==========================================================

    Oblogout_GUI.GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, vboxStack6, oblogout, Functions, os)


    # # ==========================================================
    # #                     TERMITE CONFIG
    # # ==========================================================
    
    Termite_GUI.GUI(self, Gtk, vboxStack7, termite)

    # # ==========================================================
    # #                     NEOFETCH
    # # ==========================================================
    
    Neofetch_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack8, neofetch, Functions)

    # # ==========================================================
    # #                     LIGHTDM
    # # ==========================================================
    
    Lightdm_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack11, lightdm, Functions)

    # # ==========================================================
    # #                     Skelapp
    # # ==========================================================
    
    # SkelApp_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions)
    
    # ==========================================================
    #                     ADD TO WINDOW
    # ==========================================================
    # stack.add_titled(vboxStack10, "stack0", "Welcome")
    #     
    stack.add_titled(vboxStack4, "stack1", "Grub Config")

    stack.add_titled(vboxStack3, "stack2", "HBlock")

    if Functions.file_check(Functions.lightdm_conf):
        stack.add_titled(vboxStack11, "stack3", "Lightdm Config")
    
    if Functions.file_check(Functions.neofetch_config):
        stack.add_titled(vboxStack8, "stack4", "Neofetch Config")

    if Functions.file_check(Functions.oblogout_conf):
        stack.add_titled(vboxStack6, "stack5", "Oblogout Config")
    
    if Functions.file_check(Functions.pacman):
        stack.add_titled(vboxStack1, "stack6", "Pacman Config")

    if Functions.file_check(Functions.slimlock_conf):
        stack.add_titled(vboxStack5, "stack7", "Slimlock")

    if Functions.file_check(Functions.termite_config):
        stack.add_titled(vboxStack7, "stack8", "Termite Themes")
    
    # stack.add_titled(vboxStack2, "stack9", "Theming")

    # stack.add_titled(vboxStack9, "stack10", "Tweak Skel")
    
    

    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_stack(stack)

    # =====================================================
    #                       LOGO
    # =====================================================
    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)


    # =====================================================
#                       VERSION
    # =====================================================
    version = Gtk.Label(xalign=0)
    version.set_markup("<span foreground=\'grey\'>v20.2.39</span>")

    self.lbl_desktop = Gtk.Label(xalign=0)
    self.lbl_desktop.set_markup("<span foreground=\'grey\'>" + self.desktop +"</span>")

    # =====================================================
    #               PATREON LINK
    # =====================================================
    pE = Gtk.EventBox()

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/credits.png'), 58, 58)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pE.add(pimage)

    pE.connect("button_press_event", self.on_social_clicked)
    pE.set_property("has-tooltip", True)

    pE.connect("query-tooltip", self.tooltip_callback, "Support our developers on Patreon")


    # =====================================================
    #                      PACKS
    # =====================================================
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    
    
    hbox1.pack_end(self.lbl_desktop, False, False, 0)

    hbox2.pack_start(pE, False, False, 0)
    hbox2.pack_end(version, False, False, 0)
    
    ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)
    ivbox.pack_start(hbox1, False, False, 0)
    ivbox.pack_start(hbox2, False, False, 0)

    vbox1.pack_start(hbox0, False, False, 0)
    vbox1.pack_start(stack, True, True, 0)
    
    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(vbox1, True, True, 0)
    
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
    