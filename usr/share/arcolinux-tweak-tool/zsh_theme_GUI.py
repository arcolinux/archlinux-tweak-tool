# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, vboxStack15, zsh_themes):
    # ==========================================================
    #                     TERMITE CONFIG
    # ==========================================================
    label12 = Gtk.Label()
    label12.set_text("Zsh themes")

    self.zsh_themes = Gtk.ComboBoxText()

    termset = Gtk.Button(label="Apply theme")
    termreset = Gtk.Button(label="Reset")

    termset.connect("clicked", self.on_zsh_apply)
    termreset.connect("clicked", self.on_zsh_reset)

    zsh_themes.get_themes(self.zsh_themes)

    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox19.pack_start(label12, False, False, 10)
    hbox19.pack_start(self.zsh_themes, True, True, 10)

    hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)
    
    vboxStack15.pack_start(hbox19, False, False, 0)  #Combobox
    vboxStack15.pack_end(hbox20, False, False, 0)  #Buttons

    if not zsh_themes.check_oh_my():
        termset.set_sensitive(False)