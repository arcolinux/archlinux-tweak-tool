# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

# ============Functions============
import Functions
import slim
# import Gtk_Functions
import oblogout
import termite
import neofetch
import skelapp
import lightdm
import themer
import desktopr
import autostart
import polybar
import zsh_theme

# =============GUI=================
import Termite_GUI
import Neofetch_GUI
import Oblogout_GUI
import Slimlock_GUI
import Grub_GUI
import HBlock_GUI
import Pacman_GUI
# import GTK_GUI
import SkelApp_GUI
import Lightdm_GUI
import Themer_GUI
import desktopr_GUI
import autostart_GUI
import polybar_GUI
import zsh_theme_GUI


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
    # vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack11 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack12 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack13 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack14 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack15 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ==========================================================
    #                   TAB #1 PACMAN
    # ==========================================================
    if Functions.file_check(Functions.pacman):
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
    # if Functions.file_check(Functions.slimlock_conf):
    #     Slimlock_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack5, slim, os)

    # ==========================================================
    #                       TAB #6 OBLOGOUT
    # ==========================================================
    # if Functions.file_check(Functions.oblogout_conf):
    #     Oblogout_GUI.GUI(self, Gtk, Gdk, GdkPixbuf,
    #                      base_dir, vboxStack6, oblogout, Functions, os)

    # # ==========================================================
    # #                     TERMITE CONFIG
    # # ==========================================================
    if Functions.file_check(Functions.termite_config):
        Termite_GUI.GUI(self, Gtk, vboxStack7, termite, GdkPixbuf, base_dir)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox42 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox41 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Termite Themes")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack7.pack_start(hbox31, False, False, 0)
        vboxStack7.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("If you install <b>ArcoLinux Termite themes</b> you can choose the theme")
        self.ls2 = Gtk.Label()
        self.ls2.set_markup("")
        self.btn_term = Gtk.Button(label="Install Termite themes")
        self.btn_term.connect("clicked", self.on_install_termite_themes)
        vbox41.pack_start(ls, False, False, 0)
        hbox42.pack_start(self.btn_term, True, False, 0)
        vbox41.pack_start(hbox42, False, False, 0)
        vbox41.pack_start(self.ls2, False, False, 0)
        vboxStack7.pack_start(vbox41, True, False, 0)
    # # ==========================================================
    # #                     NEOFETCH
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
    # # ==========================================================
    # #                     LIGHTDM
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
        ls.set_markup("If you install <b>lightdm</b> you can toggle autologin and set your default desktop session")
        vboxStack11.pack_start(ls, True, False, 0)
    # # ==========================================================
    # #                     Skelapp
    # # ==========================================================

    # SkelApp_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions)

    # ==========================================================
    #                       Themer
    # ==========================================================
    if "awesome" in self.desktop.lower() or "i3" in self.desktop.lower():
        Themer_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions, base_dir)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Theme Switcher")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack10.pack_start(hbox31, False, False, 0)
        vboxStack10.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("Change your themes on <b>I3</b> or <b>Awesome</b>")
        vboxStack10.pack_start(ls, True, False, 0)
    # ==========================================================
    #                       Themer
    # ==========================================================
    desktopr_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack12, desktopr,
                     Functions, base_dir, Pango)

    # ==========================================================
    #                       Autostart
    # ==========================================================
    autostart_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack13, autostart,
                      Functions, base_dir)

    # ==========================================================
    #                       Polybar
    # ==========================================================
    # if Functions.path_check(Functions.polybar):
    #     polybar_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack14, polybar,
    #                     Functions, base_dir)

    # ==========================================================
    #                       Autostart
    # ==========================================================
    if output == "/bin/zsh":
        zsh_theme_GUI.GUI(self, Gtk, vboxStack15, zsh_theme, base_dir, GdkPixbuf)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("ZSH Themes")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack15.pack_start(hbox31, False, False, 0)
        vboxStack15.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("If you switch to <b>Zsh</b> you can change the theme (use tozsh and tobash)")
        vboxStack15.pack_start(ls, True, False, 0)
    # ==========================================================
    #                     ADD TO WINDOW
    # ==========================================================
    # stack.add_titled(vboxStack10, "stack0", "Welcome")
    #
    stack.add_titled(vboxStack13, "stack13", "")  # Autostart
    # prop.set_property("has-tooltip", True)
    # prop.connect("query-tooltip", self.tooltip_callback, "Support BradHeff on Patreon")

    stack.add_titled(vboxStack12, "stack12", "")  # Desktop installer

    stack.add_titled(vboxStack4, "stack1", "")  # Grub config

    stack.add_titled(vboxStack3, "stack2", "")  # Hblock

    # if Functions.file_check(Functions.lightdm_conf):
    stack.add_titled(vboxStack11, "stack3", "")  # Lightdm config

    # if Functions.file_check(Functions.neofetch_config):
    stack.add_titled(vboxStack8, "stack4", "")  # Neofetch config

    # if Functions.file_check(Functions.oblogout_conf):
    #     stack.add_titled(vboxStack6, "stack5", "") # Oblogout config

    # if Functions.file_check(Functions.pacman):
    stack.add_titled(vboxStack1, "stack6", "")  # Pacman config

    # if Functions.path_check(Functions.polybar):
    #     stack.add_titled(vboxStack14, "stack14", "Polybar changer")

    # if Functions.file_check(Functions.slimlock_conf):
    #     stack.add_titled(vboxStack5, "stack7", "") # Slimlock

    # if Functions.file_check(Functions.termite_config):
    stack.add_titled(vboxStack7, "stack8", "")  # Termite themes

    # stack.add_titled(vboxStack2, "stack9", "Theming")

    # stack.add_titled(vboxStack9, "stack10", "Tweak skel")

    # if "awesome" in self.desktop.lower() or "i3" in self.desktop.lower():
    stack.add_titled(vboxStack10, "stack11", "")  # Theme changer

    # if output == "/bin/zsh":
    stack.add_titled(vboxStack15, "stack15", "")  # Zsh themes

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
    #                       VERSION
    # =====================================================
    version = Gtk.Label(xalign=0)
    version.set_markup("<span foreground=\'grey\'>v21.02-1</span>")

    # self.lbl_desktop = Gtk.Label(xalign=0)
    # self.lbl_desktop.set_markup("<span foreground=\'grey\'>" +
    #                             self.desktop + "</span>")

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

    pE.connect("query-tooltip", self.tooltip_callback,
               "Support our developers on Patreon")

    # =====================================================
    #                      PACKS
    # =====================================================
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

    # hbox1.pack_start(self.lbl_desktop, False, False, 0)

    hbox3.pack_start(pE, False, False, 0)
    hbox2.pack_start(version, False, False, 0)

    ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)
    # ivbox.pack_start(hbox1, False, False, 0)
    ivbox.pack_start(hbox2, False, False, 0)
    ivbox.pack_start(hbox3, False, False, 0)

    vbox1.pack_start(hbox0, False, False, 0)
    vbox1.pack_start(stack, True, True, 0)

    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(vbox1, True, True, 0)

    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
