#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, sddm, Functions):
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Sddm Configuration")
    lbl1.set_name("title")
    hbox4.pack_start(lbl1, False, False, 0)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox5.pack_start(hseparator, True, True, 0)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label(xalign=0)
    label.set_text("Autologin")

    label1 = Gtk.Label(xalign=0)
    label1.set_text("Desktop session")

    label_note = Gtk.Label(xalign=0)
    label_note.set_text("Choose the desktop you want to autologin to")

    self.autologin_sddm = Gtk.Switch()
    self.autologin_sddm.connect("notify::active", self.on_autologin_sddm_activated)

    label_theme = Gtk.Label(xalign=0)
    label_theme.set_text("Choose the Sddm theme")

    label_cursor = Gtk.Label(xalign=0)
    label_cursor.set_text("Type your cursor theme for the login screen")

    label_cursor_ex = Gtk.Label(xalign=0)
    label_cursor_ex.set_text("Cursor theme")

    label2 = Gtk.Label(xalign=0)
    label2.set_text("Theme")

    label_sddm_config = Gtk.Label(xalign=0)
    label_sddm_config.set_text("Set our sddm configuration back\n(/etc/sddm.conf and /etc/sddm.conf.d/kde_settings.conf")

    label_empty1 = Gtk.Label(xalign=0)
    label_empty1.set_text("")

    label_empty2 = Gtk.Label(xalign=0)
    label_empty2.set_text("")

    label_empty3 = Gtk.Label(xalign=0)
    label_empty3.set_text("")

    label_empty4 = Gtk.Label(xalign=0)
    label_empty4.set_text("")

    self.entry_cursor_name = Gtk.Entry()

    self.sessions_sddm = Gtk.ComboBoxText()
    sddm.pop_box(self, self.sessions_sddm)

    self.theme_sddm = Gtk.ComboBoxText()
    sddm.pop_theme_box(self, self.theme_sddm)

    self.keep_default_theme = Gtk.Switch()
    #self.keep_default_theme.connect("notify::active", self.on_keep_default_theme_activated)

    install_sddm_themes = Gtk.Button(label="Install Missing ArcoLinux Sddm Themes")
    install_sddm_themes.connect("clicked", self.on_click_install_sddm_themes)

    remove_sddm_themes = Gtk.Button(label="Remove the ArcoLinux Sddm Themes")
    remove_sddm_themes.connect("clicked", self.on_click_remove_sddm_themes)

    label_keep_default = Gtk.Label(xalign=0)
    label_keep_default.set_text("Keep the default ArcoLinux theme")

    apply_sddm = Gtk.Button(label="Apply settings")
    apply_sddm.connect("clicked", self.on_click_sddm_apply)

    reset_sddm_original = Gtk.Button(label="Apply the sddm configuration from ArcoLinux")
    reset_sddm_original.connect("clicked", self.on_click_sddm_reset_original)

    enable_sddm = Gtk.Button(label="Enable Sddm")
    enable_sddm.connect("clicked", self.on_click_sddm_enable)

    #reset_sddm = Gtk.Button(label="Apply your backup of sddm.conf")
    #reset_sddm.connect("clicked", self.on_click_sddm_reset)

    hbox.pack_start(label, False, False, 10)
    hbox.pack_end(self.autologin_sddm, False, False, 10)

    hbox3.pack_start(label_note, False, False, 10)

    hbox1.pack_start(label1, False, False, 10)
    hbox1.pack_end(self.sessions_sddm, True, True, 10)

    hbox15.pack_start(label_cursor_ex, False, False, 10)
    hbox15.pack_start(self.entry_cursor_name, True, True, 10)

    hbox17.pack_start(label_cursor, False, False, 10)

    hbox7.pack_start(label_empty1, False, False, 10)

    hbox8.pack_start(label_empty2, False, False, 10)

    hbox10.pack_start(label_empty3, False, False, 10)

    hbox16.pack_start(label_empty4, False, False, 10)

    hbox11.pack_start(install_sddm_themes, False, False, 10)
    hbox11.pack_end(remove_sddm_themes, False, False, 10)

    hbox12.pack_end(self.keep_default_theme, False, False, 10)
    hbox12.pack_end(label_keep_default, False, False, 10)

    # ======================================================================
    #                       REFRESH THEMES
    # ======================================================================
    btnRefreshAtt = Gtk.Button(label="Refresh the list of Sddm themes")
    btnRefreshAtt.connect('clicked', self.on_refresh_att_clicked)


    hbox9.pack_start(label2, False, False, 10)
    hbox9.pack_end(self.theme_sddm, True, True, 10)

    hbox14.pack_start(label_sddm_config, False, False, 10)

    hbox13.pack_start(reset_sddm_original, False, False, 10)

    hbox2.pack_end(apply_sddm, False, False, 0)
    hbox2.pack_end(btnRefreshAtt, False, False, 0)
    hbox2.pack_end(enable_sddm, False, False, 10)

    vboxStack10.pack_start(hbox4, False, False, 0)
    vboxStack10.pack_start(hbox5, False, False, 0)
    vboxStack10.pack_start(hbox, False, False, 0)
    vboxStack10.pack_start(hbox3, False, False, 0)
    vboxStack10.pack_start(hbox1, False, False, 0)
    vboxStack10.pack_start(hbox8, False, False, 0)
    vboxStack10.pack_start(hbox6, False, False, 0)
    vboxStack10.pack_start(hbox9, False, False, 0)
    vboxStack10.pack_start(hbox16, False, False, 0)
    vboxStack10.pack_start(hbox17, False, False, 0)
    vboxStack10.pack_start(hbox15, False, False, 0)
    vboxStack10.pack_start(hbox10, False, False, 0)
    vboxStack10.pack_start(hbox11, False, False, 0)
    vboxStack10.pack_start(hbox12, False, False, 0)
    vboxStack10.pack_start(hbox7, False, False, 0)
    vboxStack10.pack_start(hbox14, False, False, 0)
    vboxStack10.pack_start(hbox13, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
