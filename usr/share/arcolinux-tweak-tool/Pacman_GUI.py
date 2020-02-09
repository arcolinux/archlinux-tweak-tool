#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
def GUI(self, Gtk, vboxStack1, Functions):
    # ==========================================================
    #                   TAB #1 PACMAN
    # ==========================================================

    hboxStack1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    self.checkbutton = Gtk.Switch()
    self.checkbutton.connect("notify::active", self.on_pacman_toggle)
    label1 = Gtk.Label(xalign=0)
    label1.set_markup("Enable ArcoLinux test repo")

    self.checkbutton2 = Gtk.Switch()
    self.checkbutton2.connect("notify::active", self.on_pacman_toggle2)
    label3 = Gtk.Label(xalign=0)
    label3.set_markup("Enable Arch test repo")

    self.checkbutton3 = Gtk.Switch()
    self.checkbutton3.connect("notify::active", self.on_pacman_toggle3)
    label4 = Gtk.Label(xalign=0)
    label4.set_markup("Enable Arch multilib test repo")

    label2 = Gtk.Label(xalign=0)
    label2.set_markup("<b>Add custom repo to pacman.conf</b>")

    self.textbox1 = Gtk.TextView()
    self.textbox1.set_wrap_mode(Gtk.WrapMode.WORD)
    self.textbox1.set_editable(True)
    self.textbox1.set_cursor_visible(True)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.LEFT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.RIGHT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.TOP, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.BOTTOM, 1)

    sw = Gtk.ScrolledWindow()
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    sw.add(self.textbox1)

    self.button1 = Gtk.Button(label="Apply Custom Repo")
    self.button1.connect('clicked', self.button1_clicked)
    reset_pacman = Gtk.Button(label="Reset Pacman")
    reset_pacman.connect("clicked", self.reset_settings, Functions.pacman)

    hboxStack1.pack_start(label1, False, True, 10)
    hboxStack1.pack_end(self.checkbutton, False, False, 10)
    hboxStack5.pack_start(label3, False, True, 10)
    hboxStack5.pack_end(self.checkbutton2, False, False, 10)
    hboxStack6.pack_start(label4, False, True, 10)
    hboxStack6.pack_end(self.checkbutton3, False, False, 10)

    hboxStack2.pack_start(label2, False, True, 10)
    hboxStack3.pack_start(sw, True, True, 10)

    hboxStack4.pack_end(self.button1, False, False, 0)
    hboxStack4.pack_end(reset_pacman, False, False, 0)

    vboxStack1.pack_start(hboxStack1, False, False, 0)
    vboxStack1.pack_start(hboxStack5, False, False, 0)
    vboxStack1.pack_start(hboxStack6, False, False, 0)
    vboxStack1.pack_start(hboxStack2, False, False, 0)
    vboxStack1.pack_start(hboxStack3, True, True, 0)
    vboxStack1.pack_start(hboxStack4, False, False, 0)