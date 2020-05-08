# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions, base_dir):  # noqa
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

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

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
    label3.set_markup("Reload your window manager with <b>Super + Shift + R</b> after you make your changes.")

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

    hbox1.pack_start(label, False, False, 10)
    hbox1.pack_end(vbox2, False, False, 10)

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/i3-sample.jpg", 645, 645)
    i3_image = Gtk.Image().new_from_pixbuf(pixbuf)

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
    label4.set_markup("Reload your window manager with <b>Super + Shift + R</b> after you make your changes.")

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
    self.awesome_combo.connect("changed", self.on_awsome_change)
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

    if Functions.os.path.isfile(Functions.awesome_config):
        try:
            pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/themer_data/awesomewm/" + name + ".jpg", 598, 598)  # noqa
            self.image.set_from_pixbuf(pimage)
        except:  # noqa
            pass
    frame.set_name("awesome")
    frame.add(self.image)

    hbox5.pack_start(frame, True, False, 10)

    apply = Gtk.Button(label="Apply")
    apply.connect("clicked", self.awesome_apply_clicked)
    reset = Gtk.Button(label="Reset")
    reset.connect("clicked", self.awesome_reset_clicked)

    hbox4.pack_end(apply, False, False, 0)
    hbox4.pack_end(reset, False, False, 0)

    vboxStack2.pack_start(hbox2, False, False, 10)
    vboxStack2.pack_start(hbox5, False, False, 10)
    vboxStack2.pack_start(label4, True, False, 10)
    vboxStack2.pack_end(hbox4, False, False, 0)

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================

    if Functions.os.path.isfile(Functions.i3wm_config):
        stack.add_titled(vboxStack1, "stack1", "I3WM")
    if Functions.os.path.isfile(Functions.awesome_config):
        stack.add_titled(vboxStack2, "stack2", "AwesomeWM")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack10.pack_start(hbox6, False, False, 0)
    vboxStack10.pack_start(hbox7, False, False, 0)
    vboxStack10.pack_start(vbox, True, True, 0)
