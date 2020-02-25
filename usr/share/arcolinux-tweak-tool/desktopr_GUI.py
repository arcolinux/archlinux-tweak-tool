# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack12, desktopr, Functions, base_dir):

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    dropbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)

    # =======================================
    #               DROPDOWN
    # =======================================
    label = Gtk.Label(xalign=0)
    label.set_text("Select a desktop")
    self.d_combo = Gtk.ComboBoxText()
    self.d_combo.set_size_request(180, 0)
    self.d_combo.connect("changed", self.on_d_combo_changed)
    for x in desktopr.desktops:
        self.d_combo.append_text(x)
    self.d_combo.set_active(0)

    dropbox.pack_start(label, False, False, 0)
    dropbox.pack_start(self.d_combo, False, False, 0)

    # =======================================
    #               BUTTONS
    # =======================================
    button_install = Gtk.Button(label="Install")
    button_uninstall = Gtk.Button(label="Uninstall")

    buttonbox.pack_start(button_install, True, True, 0)
    buttonbox.pack_start(button_uninstall, True, True, 0)

    # =======================================
    #               FRAME PREVIEW
    # =======================================
    self.image_DE = Gtk.Image()

    try:
        pixbuf3 = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir +
                                                           "/desktop_data/" +
                                                           self.d_combo.get_active_text() + ".png",  # noqa
                                                           345,
                                                           345)
        self.image_DE.set_from_pixbuf(pixbuf3)
    except:  # noqa
        pass
    frame = Gtk.Frame(label="Preview")
    frame.add(self.image_DE)

    # =======================================
    #               PACK TO BOXES
    # =======================================
    vbox.pack_start(dropbox, False, False, 0)
    vbox.pack_start(buttonbox, False, False, 0)

    hbox.pack_start(vbox, True, True, 10)
    hbox.pack_start(frame, True, True, 10)

    # =======================================
    #               PACK TO WINDOW
    # =======================================
    vboxStack12.pack_start(hbox, False, False, 0)
