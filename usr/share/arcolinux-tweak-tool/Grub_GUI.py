# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack4, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Grub Themes")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                       GRUB
    # ==========================================================
    label7 = Gtk.Label()
    label7.set_text("Select a wallpaper")

    self.grub_theme_combo = Gtk.ComboBoxText()
    btnremove = Gtk.Button(label="Remove wallpaper")
    btnremove.set_size_request(180, 0)
    btnremove.connect("clicked", self.on_remove_wallpaper)

    wallpaper_list = Functions.get_grub_wallpapers()
    self.pop_themes_grub(self.grub_theme_combo, wallpaper_list, True)

    label8 = Gtk.Label("Import image")
    self.tbimage = Gtk.Entry()
    btnsearch = Gtk.Button(label=". . .")
    btnsearch.connect("clicked", self.on_choose_wallpaper)
    btnimport = Gtk.Button(label="Import selected image")
    btnimport.connect("clicked", self.on_import_wallpaper)

    # self.image_grub = Gtk.Image()

    # try:
    #     pixbuf3 = GdkPixbuf.Pixbuf().new_from_file_at_size('/boot/grub/themes/Vimix/' + self.grub_theme_combo.get_active_text(), 645, 645)
    #     self.image_grub.set_from_pixbuf(pixbuf3)
    # except:
    #     pass
    # frame = Gtk.Frame(label="Preview")
    # frame.add(self.image_grub)
    scrolled = Gtk.ScrolledWindow()
    scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

    self.fb.set_valign(Gtk.Align.START)
    self.fb.set_max_children_per_line(6)
    self.fb.set_selection_mode(Gtk.SelectionMode.SINGLE)
    self.fb.connect("child-activated", self.on_grub_item_clicked)

    scrolled.add(self.fb)

    self.grub_theme_combo.connect("changed", self.on_grub_theme_change)

    grub_apply = Gtk.Button(label="Apply wallpaper")
    grub_apply.connect("clicked", self.on_set_grub_wallpaper)
    grub_reset = Gtk.Button(label="Reset theme")
    grub_reset.connect("clicked", self.on_reset_grub_wallpaper)


    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox101 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    # hbox8.pack_start(label7, False, True, 10)
    # hbox8.pack_start(self.grub_theme_combo, True, True, 10)
    hbox8.pack_end(btnremove, False, False, 10)

    hbox11.pack_start(label8, False, False, 10)
    hbox11.pack_start(self.tbimage, True, True, 10)
    hbox11.pack_start(btnsearch, False, False, 10)

    hbox12.pack_end(btnimport, False, False, 10)

    # hbox101.pack_start(scrolled, True, True, 10)

    hbox9.pack_end(grub_apply, False, False, 0)
    hbox9.pack_end(grub_reset, False, False, 0)

    vboxStack4.pack_start(hbox3, False, False, 0) #Add theme
    vboxStack4.pack_start(hbox4, False, False, 0) #Add theme
    vboxStack4.pack_start(hbox11, False, False, 0) #Add theme
    vboxStack4.pack_start(hbox12, False, False, 0) #btn Import
    vboxStack4.pack_start(scrolled, True, True, 0) #Preview
    vboxStack4.pack_start(hbox8, False, False, 0) #combobox
    vboxStack4.pack_end(hbox9, False, False, 0)# Buttons
