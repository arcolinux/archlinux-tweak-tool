# =================================================================
# =                  Author: Erik Dubois                          =
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
    #                     ZSH THEMES
    # ==========================================================
    
    label12 = Gtk.Label()
    label12.set_text("Zsh themes")
    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox19.pack_start(label12, False, False, 10)
    
    self.zsh_themes = Gtk.ComboBoxText()
    zsh_themes.get_themes(self.zsh_themes)
    hbox19.pack_start(self.zsh_themes, True, True, 10)    
    
    label13 = Gtk.Label()
    label13.set_text("Restart your terminal to apply the new Zsh theme\nIf you switch shell, log-out first")
    label13.set_margin_top(30) 
    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox21.pack_start(label13, True, False, 10)

    tobash = Gtk.Button(label="Apply bash")
    tozsh = Gtk.Button(label="Apply zsh")
    #hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    tobash.connect("clicked", self.tobash_apply)
    tozsh.connect("clicked", self.tozsh_apply)

    termset = Gtk.Button(label="Apply Zsh theme")
    termreset = Gtk.Button(label="Reset ~/.zshrc")

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    hbox20.pack_start(tobash, False, False, 0)
    hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)
    hbox20.pack_end(tozsh, False, False, 0)

    termset.connect("clicked", self.on_zsh_apply)
    termreset.connect("clicked", self.on_zsh_reset)

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/zsh-sample.jpg", 645, 645)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    vboxStack15.pack_start(hbox3, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox4, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox19, False, False, 0)  # Combobox
    vboxStack15.pack_start(image, False, False, 0)  # image
    vboxStack15.pack_start(hbox21, False, False, 0)  # image
    vboxStack15.pack_end(hbox20, False, False, 0)  # Buttons

    if not zsh_themes.check_oh_my():
        termset.set_sensitive(False)
