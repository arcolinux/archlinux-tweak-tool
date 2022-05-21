#=================================================================
#=                  Author: Brad Heffernan & Erik Dubois         =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, lightdm, Functions):
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Lightdm (inactive)")
    if Functions.check_content("lightdm", "/etc/systemd/system/display-manager.service"):
        lbl1.set_text("Lightdm (active)")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox5.pack_start(hseparator, True, True, 0)
    hbox4.pack_start(lbl1, False, False, 0)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label(xalign=0)
    label.set_text("Autologin")

    label1 = Gtk.Label(xalign=0)
    label1.set_text("Desktop session")

    label_note = Gtk.Label(xalign=0)
    label_note.set_text("Choose the desktop you want to autologin to")

    self.sessions = Gtk.ComboBoxText()
    self.autologin = Gtk.Switch()
    self.autologin.connect("notify::active", self.on_autologin_activated)

    lightdm.pop_box(self, self.sessions)

    enable_lightdm = Gtk.Button(label="Enable Lightdm")
    enable_lightdm.connect("clicked", self.on_click_lightdm_enable)

    enable_slick = Gtk.Button(label="Enable/Disable Lightdm Slickgreeter")
    enable_slick.connect("clicked", self.on_click_lightdm_slick)

    apply = Gtk.Button(label="Apply settings")
    apply.connect("clicked", self.on_click_lightdm_apply)
    reset = Gtk.Button(label="Reset")
    reset.connect("clicked", self.on_click_lightdm_reset)

    hbox.pack_start(label, False, False, 10)
    hbox.pack_end(self.autologin, False, False, 10)

    hbox3.pack_start(label_note, False, False, 10)

    hbox1.pack_start(label1, False, False, 10)
    hbox1.pack_end(self.sessions, True, True, 10)

    hbox2.pack_end(apply, False, False, 0)
    hbox2.pack_end(reset, False, False, 0)
    hbox2.pack_end(enable_slick, False, False, 10)
    hbox2.pack_end(enable_lightdm, False, False, 0)

    vboxStack10.pack_start(hbox4, False, False, 0)
    vboxStack10.pack_start(hbox5, False, False, 0)
    vboxStack10.pack_start(hbox, False, False, 10)
    vboxStack10.pack_start(hbox3, False, False, 0)
    vboxStack10.pack_start(hbox1, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
