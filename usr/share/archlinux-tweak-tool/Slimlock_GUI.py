# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack5, slim, os):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Slimlock Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                       TAB #5 SLIMLOCK
    # ==========================================================
    label9 = Gtk.Label()
    label9.set_text("Slimlock theme")

    self.slimbox = Gtk.ComboBoxText()

    slimset = Gtk.Button(label="Apply theme")
    slimreset = Gtk.Button(label="Reset")
    slimremove = Gtk.Button(label="Remove")

    slimset.connect("clicked", self.on_slim_apply)
    slimreset.connect("clicked", self.on_slim_reset)
    slimremove.connect("clicked", self.on_remove_theme)

    slim.get_slimlock(self.slimbox)

    self.image2 = Gtk.Image()
    self.image5 = Gtk.Image()

    try:
        path = '/usr/share/slim/themes/' + self.slimbox.get_active_text()

        pixbuf4 = GdkPixbuf.Pixbuf().new_from_file_at_size(path + "/background.png", 345, 345)
        self.image2.set_from_pixbuf(pixbuf4)

    except:
        pass

    frame2 = Gtk.Frame(label="Preview")
    frame4 = Gtk.Frame(label="Preview")

    frame2.add(self.image2)
    frame4.add(self.image5)

    self.slimbox.connect("changed", self.on_slim_theme_change, self.image2)

    label12 = Gtk.Label()
    label12.set_markup("Images need to be in <b>.png</b>")

    label10 = Gtk.Label()
    label10.set_text("Select wallpaper")

    label11 = Gtk.Label()
    label11.set_text("Theme name      ")

    self.slimtheme = Gtk.Entry()
    self.slimtext = Gtk.Entry()

    browse2 = Gtk.Button(label=". . .")
    browse2.connect("clicked", self.on_browser_clicked)

    importtheme = Gtk.Button(label="Create theme")
    importtheme.connect("clicked", self.on_create_theme_clicked)


    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox35 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox27 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    hbox13.pack_start(label9, False, False, 10)
    hbox13.pack_start(self.slimbox, True, True, 10)
    hbox13.pack_start(slimremove, False, False, 10)

    hbox35.pack_start(frame2, True, True, 10)

    hbox17.pack_start(label11, False, False, 10)
    hbox17.pack_start(self.slimtheme, True, True, 10)

    hbox27.pack_start(label12, True, False, 10)

    hbox16.pack_start(label10, False, False, 10)
    hbox16.pack_start(self.slimtext, True, True, 10)
    hbox16.pack_start(browse2, False, False, 10)

    hbox26.pack_start(frame4, True, True, 10)

    hbox18.pack_end(importtheme, False, False, 10)

    hbox14.pack_end(slimset, False, False, 0)
    hbox14.pack_end(slimreset, False, False, 0)

    vboxStack5.pack_start(hbox3, False, False, 0)  # combobox
    vboxStack5.pack_start(hbox4, False, False, 0)  # combobox
        
    vboxStack5.pack_start(hbox13, False, False, 0)  # combobox
    vboxStack5.pack_start(hbox35, False, False, 0)  # Preview Theme

    vboxStack5.pack_start(hbox16, False, False, 0)  # Choose Theme Txtbox
    vboxStack5.pack_start(hbox17, False, False, 0)  # Theme Name Text
    vboxStack5.pack_start(hbox27, False, False, 0)  # Info Text
    vboxStack5.pack_start(hbox26, False, False, 0)  # Preview Chosen Image

    vboxStack5.pack_start(hbox18, False, False, 0) #Create Theme
    vboxStack5.pack_end(hbox14, False, False, 0) #Buttons
