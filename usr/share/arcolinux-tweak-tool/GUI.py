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

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os):
    # ==========================================================
    #                       CONTAINER
    # ==========================================================
    # grid = Gtk.Grid()
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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

    # ==========================================================
    #                   TAB #1 PACMAN
    # ==========================================================

    Pacman_GUI.GUI(self, Gtk, vboxStack1, Functions)

    # ==========================================================
    #                 TAB #2 GTK THEMES
    # ==========================================================
    GTK_GUI.GUI(self, Gtk, vboxStack2, Gtk_Functions, Functions)

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
    # #                     Skelapp
    # # ==========================================================
    
    SkelApp_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions)
    
    # ==========================================================
    #                     ADD TO WINDOW
    # ==========================================================
    if Functions.file_check(Functions.pacman):
        stack.add_titled(vboxStack1, "stack1", "Pacman Config")

    stack.add_titled(vboxStack2, "stack2", "Theming")

    stack.add_titled(vboxStack4, "stack4", "Grub Config")

    if Functions.file_check(Functions.oblogout_conf):
        stack.add_titled(vboxStack6, "stack6", "Oblogout Config")

    stack.add_titled(vboxStack3, "stack3", "HBlock")

    if Functions.file_check(Functions.slimlock_conf):
        stack.add_titled(vboxStack5, "stack5", "Slimlock")

    if Functions.file_check(Functions.termite_config):
        stack.add_titled(vboxStack7, "stack7", "Termite Themes")
    
    if Functions.file_check(Functions.neofetch_config):
        stack.add_titled(vboxStack8, "stack8", "Neofetch Config")
    
    # stack.add_titled(vboxStack9, "stack9", "SkelApp")
    
    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_stack(stack)

    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    version = Gtk.Label(xalign=0)
    version.set_markup("<span foreground=\'grey\'>v20.2.22</span>")

    ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)
    ivbox.pack_start(version, False, False, 0)

    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(stack, True, True, 0)
    
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
    