#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
def GUI(self, Gtk, vboxStack3, Functions):
    # ==========================================================
    #                       HBLOCK
    # ==========================================================
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label()
    label.set_text("enable hblock")

    self.label7 = Gtk.Label(xalign=0)
    self.label7.set_text("Idle ....")

    self.progress = Gtk.ProgressBar()
    self.progress.set_pulse_step(0.2)

    self.hbswich = Gtk.Switch()
    self.hbswich.connect("notify::active", self.set_hblock)
    self.hbswich.set_active(Functions.hblock_get_state(self))

    hbox7.pack_start(label, False, False, 10)
    hbox7.pack_end(self.hbswich, False, False, 10)

    vboxStack3.pack_start(hbox7, False, False, 0)
    vboxStack3.pack_end(self.progress, False, False, 0)
    vboxStack3.pack_end(self.label7, False, False, 0)