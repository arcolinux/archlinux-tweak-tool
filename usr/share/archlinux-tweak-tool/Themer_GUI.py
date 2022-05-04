# =================================================================
# =          Author: Brad Heffernan - Erik Dubois - Cameron Percival
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions, base_dir):  # noqa

    #Image Dimensions. Change once here - apply to ALL the items in this GUI.
    image_width = 645
    image_height = 645
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Theme Switcher")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox7.pack_start(hseparator, True, True, 0)
    hbox6.pack_start(lbl1, False, False, 0)

    if Functions.os.path.isfile(Functions.i3wm_config):
        i3_list = themer.get_list(Functions.i3wm_config)
    if Functions.os.path.isfile(Functions.awesome_config):
        awesome_list = themer.get_list(Functions.awesome_config)
    if Functions.os.path.isfile(Functions.qtile_config):
        qtile_list = themer.get_list(Functions.qtile_config)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)

    # ==================================================================
    #                       I3WM TAB
    # ==================================================================

    label3 = Gtk.Label()
    label3.set_markup("Reload your window manager with <b>Super + Shift + R</b> after you make your changes..\nInstall the desktop with ATT to theme it.")

    label = Gtk.Label("Select theme")
    self.i3_combo = Gtk.ComboBoxText()
    self.i3_combo.set_size_request(280, 0)
    if Functions.os.path.isfile(Functions.i3wm_config):
        themer.get_i3_themes(self.i3_combo, i3_list)

    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox2.pack_start(self.i3_combo, False, False, 0)

    applyi3 = Gtk.Button(label="Apply")
    applyi3.connect("clicked", self.i3wm_apply_clicked)
    reseti3 = Gtk.Button(label="Reset")
    reseti3.connect("clicked", self.i3wm_reset_clicked)

    lbls = Gtk.Label(label="Toggle polybar")
    self.poly = Gtk.Switch()
    if Functions.os.path.isfile(Functions.i3wm_config):
        if themer.check_polybar(themer.get_list(Functions.i3wm_config)):
            self.poly.set_active(True)
    self.poly.connect("notify::active", self.on_polybar_toggle)

    if not Functions.os.path.isfile(Functions.i3wm_config):
        applyi3.set_sensitive(False)
        reseti3.set_sensitive(False)
        self.poly.set_sensitive(False)

    hbox1.pack_start(label, False, False, 10)
    hbox1.pack_end(vbox2, False, False, 10)

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/i3-sample.jpg", image_width, image_height)
    if self.i3_combo.get_active_text() is None:
        pass
    elif Functions.os.path.isfile(base_dir+"/themer_data/i3"+self.i3_combo.get_active_text()+".jpg"):
        pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir+"/themer_data/i3/"+self.i3_combo.get_active_text()+".jpg", image_width, image_height)
    i3_image = Gtk.Image().new_from_pixbuf(pixbuf)

    self.i3_combo.connect("changed", self.update_image, i3_image, "i3", base_dir, image_width, image_height)

    hbox2.pack_end(applyi3, False, False, 0)
    hbox2.pack_end(reseti3, False, False, 0)

    hbox3.pack_end(self.poly, False, False, 0)
    hbox3.pack_end(lbls, False, False, 0)

    vboxStack1.pack_start(hbox1, False, False, 10)
    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_start(i3_image, False, False, 0)
    vboxStack1.pack_start(label3, True, False, 0)
    vboxStack1.pack_end(hbox2, False, False, 0)

    # ==================================================================
    #                       AWESOMEWM TAB
    # ==================================================================

    label4 = Gtk.Label()
    label4.set_markup("Reload your window manager with <b>Super + Shift + R</b> after you make your changes..\nInstall the desktop with ATT to theme it.")

    label2 = Gtk.Label("Select theme")
    self.store = Gtk.ListStore(int, str)
    if Functions.os.path.isfile(Functions.awesome_config):
        try:
            awesome_lines = themer.get_awesome_themes(awesome_list)
            for x in range(len(awesome_lines)):
                self.store.append([x, awesome_lines[x]])
        except:
            pass

    self.awesome_combo = Gtk.ComboBox.new_with_model(self.store)
    self.awesome_combo.set_size_request(180, 0)
    renderer_text = Gtk.CellRendererText()

    if Functions.os.path.isfile(Functions.awesome_config):
        try:
            val = int(themer.get_value(awesome_list, "local chosen_theme =")
                    .replace("themes[", "").replace("]", ""))
            self.awesome_combo.set_active(val-1)
        except:
            pass

    self.awesome_combo.pack_start(renderer_text, False)
    self.awesome_combo.add_attribute(renderer_text, "text", 1)
    #self.awesome_combo.connect("changed", self.on_awesome_change)
    self.awesome_combo.set_entry_text_column(1)

    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox3.pack_start(self.awesome_combo, False, False, 0)
    hbox2.pack_start(label2, False, False, 10)
    hbox2.pack_end(vbox3, False, False, 10)

    frame = Gtk.Frame(label="")
    frmlbl = frame.get_label_widget()
    frmlbl.set_markup("<b>Preview</b>")

    tree_iter = self.awesome_combo.get_active_iter()
    if tree_iter is not None:
        model = self.awesome_combo.get_model()
        row_id, name = model[tree_iter][:2]

    self.image = Gtk.Image()

    image_width = 598
    image_height = 598

    if Functions.os.path.isfile(Functions.awesome_config):
        try:
            pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/themer_data/awesomewm/" + name + ".jpg", image_width, image_height)  # noqa
            self.image.set_from_pixbuf(pimage)
        except:  # noqa
            pass
    else:
            pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/themer_data/awesomewm/multicolor.jpg", image_width, image_height)  # noqa
            self.image.set_from_pixbuf(pimage)

    self.awesome_combo.connect("changed", self.update_image, self.image, "awesome", base_dir, image_width, image_height)

    frame.set_name("awesome")
    frame.add(self.image)

    hbox5.pack_start(frame, True, False, 10)

    apply = Gtk.Button(label="Apply")
    apply.connect("clicked", self.awesome_apply_clicked)
    reset = Gtk.Button(label="Reset")
    reset.connect("clicked", self.awesome_reset_clicked)

    if not Functions.os.path.isfile(Functions.awesome_config):
            apply.set_sensitive(False)
            reset.set_sensitive(False)

    hbox4.pack_end(apply, False, False, 0)
    hbox4.pack_end(reset, False, False, 0)

    vboxStack2.pack_start(hbox2, False, False, 10)
    vboxStack2.pack_start(hbox5, False, False, 10)
    vboxStack2.pack_start(label4, True, False, 10)
    vboxStack2.pack_end(hbox4, False, False, 0)

    # ==================================================================
    #                       Qtile TAB
    # ==================================================================

    label5 = Gtk.Label()
    label5.set_markup("Reload your window manager with <b>Super + Shift + R</b> after you make your changes.\nInstall the desktop with ATT to theme it.")

    labelqt = Gtk.Label("Select theme")
    self.qtile_combo = Gtk.ComboBoxText()
    self.qtile_combo.set_size_request(280, 0)
    if Functions.os.path.isfile(Functions.qtile_config):
        themer.get_qtile_themes(self.qtile_combo, qtile_list)

    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox4.pack_start(self.qtile_combo, False, False, 0)

    applyqtile = Gtk.Button(label="Apply")
    applyqtile.connect("clicked", self.qtile_apply_clicked)
    resetqtile = Gtk.Button(label="Reset")
    resetqtile.connect("clicked", self.qtile_reset_clicked)

    if not Functions.os.path.isfile(Functions.qtile_config):
            applyqtile.set_sensitive(False)
            resetqtile.set_sensitive(False)

#   Commented out for now. TODO: implement theming for polybar under Qtile
#   lbls = Gtk.Label(label="Toggle polybar")
#   self.poly = Gtk.Switch()
#   if Functions.os.path.isfile(Functions.i3wm_config):
#       if themer.check_polybar(themer.get_list(Functions.i3wm_config)):
#           self.poly.set_active(True)
#   self.poly.connect("notify::active", self.on_polybar_toggle)

    hbox8.pack_start(labelqt, False, False, 10)
    hbox8.pack_end(vbox4, False, False, 10)

    qtile_pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/qtile-sample.jpg", image_width, image_height)
    if self.qtile_combo.get_active_text() is None:
        pass
    elif Functions.os.path.isfile(base_dir+"/themer_data/qtile/"+self.qtile_combo.get_active_text()+".jpg"):
        qtile_pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir+"/themer_data/qtile/"+self.qtile_combo.get_active_text()+".jpg", image_width, image_height)
    qtile_image = Gtk.Image().new_from_pixbuf(qtile_pixbuf)

    self.qtile_combo.connect("changed", self.update_image, qtile_image, "qtile", base_dir, image_width, image_height)

    hbox9.pack_end(applyqtile, False, False, 0)
    hbox9.pack_end(resetqtile, False, False, 0)

    vboxStack3.pack_start(hbox8, False, False, 0)
    vboxStack3.pack_start(hbox10, False, False, 0)
    vboxStack3.pack_start(qtile_image, False, False, 0)
    vboxStack3.pack_start(label5, True, False, 0)
    vboxStack3.pack_end(hbox9, False, False, 0)

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================

    stack.add_titled(vboxStack1, "stack1", "I3WM")
    stack.add_titled(vboxStack2, "stack2", "AwesomeWM")
    stack.add_titled(vboxStack3, "stack3", "Qtile")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack10.pack_start(hbox6, False, False, 0)
    vboxStack10.pack_start(hbox7, False, False, 0)
    vboxStack10.pack_start(vbox, True, True, 0)
