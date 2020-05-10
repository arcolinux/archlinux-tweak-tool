# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, vboxStack3, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("HBlock Addblocker")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                       HBLOCK
    # ==========================================================
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label()
    label.set_text("Enable hblock")

    self.label7 = Gtk.Label(xalign=0)


    self.progress = Gtk.ProgressBar()
    self.progress.set_pulse_step(0.2)

    state = Functions.hblock_get_state(self)

    self.hbswich = Gtk.Switch()
    self.hbswich.connect("notify::active", self.set_hblock)
    self.hbswich.set_active(state)

    if state:
        self.label7.set_text("Hblock active")
    else:
        self.label7.set_text("Hblock inactive")

    label2 = Gtk.Label()
    label2.set_markup("Improve your <b>security</b> and <b>privacy</b> by blocking ads, tracking and malware domains")

    hbox7.pack_start(label, False, False, 10)
    hbox7.pack_end(self.hbswich, False, False, 10)

    vboxStack3.pack_start(hbox3, False, False, 0)
    vboxStack3.pack_start(hbox4, False, False, 0)
    vboxStack3.pack_start(hbox7, False, False, 0)
    vboxStack3.pack_start(label2, True, False, 0)
    vboxStack3.pack_end(self.progress, False, False, 0)
    vboxStack3.pack_end(self.label7, False, False, 0)
