# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, vboxStack7, termite):
    # ==========================================================
    #                     TERMITE CONFIG
    # ==========================================================
    label12 = Gtk.Label()
    label12.set_text("Termite themes")

    self.term_themes = Gtk.ComboBoxText()

    termset = Gtk.Button(label="Apply Theme")
    termreset = Gtk.Button(label="Reset")

    termset.connect("clicked", self.on_term_apply)
    termreset.connect("clicked", self.on_term_reset)

    termite.get_themes(self.term_themes)

    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox19.pack_start(label12, False, False, 10)
    hbox19.pack_start(self.term_themes, True, True, 10)

    hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)

    vboxStack7.pack_start(hbox19, False, False, 0)  #Combobox
    vboxStack7.pack_end(hbox20, False, False, 0)  #Buttons 