# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, vboxStack15, zsh_themes, base_dir, GdkPixbuf):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("ZSH Themes")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
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

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/zsh-sample.jpg", 645, 645)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)

    vboxStack15.pack_start(hbox3, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox4, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox19, False, False, 0)  # Combobox
    vboxStack15.pack_start(image, False, False, 0)  # image
    vboxStack15.pack_end(hbox20, False, False, 0)  # Buttons

    if not zsh_themes.check_oh_my():
        termset.set_sensitive(False)
