# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, vboxStack2, Gtk_Functions, Functions):
    # ==========================================================
    #                 TAB #2 GTK THEMES
    # ==========================================================
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label()
    label.set_markup("Gtk Theme:       ")

    label2 = Gtk.Label()
    label2.set_markup("Icon Theme:     ")

    label3 = Gtk.Label()
    label3.set_markup("Cursor Theme:")

    label5 = Gtk.Label()
    label5.set_markup("Cursor Size: ")

    label6 = Gtk.Label()
    label6.set_markup("Select Font: ")

    label7 = Gtk.Label()
    label7.set_markup("Select Monospace Font: ")

    self.themeCombo = Gtk.ComboBoxText()
    self.iconCombo = Gtk.ComboBoxText()
    self.cursorCombo = Gtk.ComboBoxText()

    adj1 = Gtk.Adjustment(28.0, 10.0, 100.0, 1.0, 5.0, 0.0)
    self.cursor_size = Gtk.SpinButton()
    self.cursor_size.set_adjustment(adj1)


    # self.fonts = Gtk.FontButton()
    # self.monofonts = Gtk.FontButton()

    self.themeCombo.set_size_request(200, 0)
    self.iconCombo.set_size_request(200, 0)
    self.cursorCombo.set_size_request(200, 0)

    # Set functions
    Gtk_Functions.get_gtk_themes(self, self.themeCombo)
    Gtk_Functions.get_icon_themes(self, self.iconCombo)
    Gtk_Functions.get_cursor_themes(self, self.cursorCombo)

    self.cursor_size.set_value(
        int(Gtk_Functions.get_gtk_settings("gtk-cursor-theme-size").split(".")[0]))
    # self.fonts.set_font(Gtk_Functions.get_gtk_settings("gtk-font-name"))
    # self.monofonts.set_font(Gtk_Functions.get_mono_font("MonospaceFontName"))

    save_gtk3_themes = Gtk.Button(label="Save Settings")
    # save_gtk3_themes.connect("clicked", self.save_gtk3_settings, self.themeCombo,self.iconCombo, self.cursorCombo, self.cursor_size, self.fonts, self.monofonts)
    save_gtk3_themes.connect("clicked", self.save_gtk3_settings, self.themeCombo,self.iconCombo, self.cursorCombo, self.cursor_size)

    reset_gtk3_themes = Gtk.Button(label="Reset/Reload Defaults")
    reset_gtk3_themes.connect(
        "clicked", self.reset_settings, Functions.gtk3_settings)

    hbox1.pack_start(label, False, False, 10)
    hbox1.pack_start(self.themeCombo, True, True, 10)

    hbox2.pack_start(label2, False, False, 10)
    hbox2.pack_start(self.iconCombo, True, True, 10)

    hbox3.pack_start(label3, False, False, 10)
    hbox3.pack_start(self.cursorCombo, True, True, 10)

    hbox5.pack_start(label5, False, False, 10)
    hbox5.pack_end(self.cursor_size, False, False, 10)

    # hbox6.pack_start(label6, False, False, 10)
    # hbox6.pack_end(self.fonts, False, False, 10)

    # hbox7.pack_start(label7, False, False, 10)
    # hbox7.pack_end(self.monofonts, False, False, 10)

    hbox4.pack_end(save_gtk3_themes, False, False, 0)
    hbox4.pack_end(reset_gtk3_themes, False, False, 0)

    vboxStack2.pack_start(hbox1, False, False, 0)  # Gtk Themes
    vboxStack2.pack_start(hbox2, False, False, 0)  # Gtk Icon Themes
    vboxStack2.pack_start(hbox3, False, False, 0)  # Gtk Cursor Themes
    vboxStack2.pack_start(hbox5, False, False, 0)  # Gtk Cursor Size
    vboxStack2.pack_start(hbox6, False, False, 0)  # Gtk Fonts
    vboxStack2.pack_start(hbox7, False, False, 0)  # Gtk Mono Fonts
    vboxStack2.pack_end(hbox4, False, False, 0)  # Save Button
