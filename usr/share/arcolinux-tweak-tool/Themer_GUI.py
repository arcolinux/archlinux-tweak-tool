#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions):
    
    i3_list = themer.get_list(Functions.i3wm_config)
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


    #==================================================================
    #                       I3WM TAB
    #==================================================================
    label = Gtk.Label("Select theme")
    self.i3_combo = Gtk.ComboBoxText()
    self.i3_combo.set_size_request(180, 0)
    themer.get_i3_themes(i3_list)

    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox2.pack_start(self.i3_combo, False, False, 0)

    hbox1.pack_start(label, False, False, 10)
    hbox1.pack_end(vbox2, False, False, 10)

    vboxStack1.pack_start(hbox1, False, False, 10)
    #==================================================================
    #                       AWESOMEWM TAB
    #==================================================================
    label2 = Gtk.Label("Select theme")
    self.store = Gtk.ListStore(int, str)
    awesome_lines = themer.get_awesome_themes(awesome_list)
    for x in range(len(awesome_lines)):
        self.store.append([x, awesome_lines[x]])
    
    self.awesome_combo = Gtk.ComboBox.new_with_model(self.store)
    self.awesome_combo.set_size_request(180, 0)
    renderer_text = Gtk.CellRendererText()

    val = int(themer.get_value(awesome_list, "local chosen_theme =").replace("themes[", "").replace("]", ""))
    self.awesome_combo.set_active(val-1)
    

    self.awesome_combo.pack_start(renderer_text, False)
    self.awesome_combo.add_attribute(renderer_text, "text", 1)
    self.awesome_combo.set_entry_text_column(1)
    
    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox3.pack_start(self.awesome_combo, False, False, 0)

    hbox2.pack_start(label2, False, False, 10)
    hbox2.pack_end(vbox3, False, False, 10)

    apply = Gtk.Button(label="Apply")
    apply.connect("clicked", self.awesome_apply_clicked)
    reset = Gtk.Button(label="Reset")
    reset.connect("clicked", self.awesome_reset_clicked)

    hbox4.pack_end(apply, False, False, 0)
    hbox4.pack_end(reset, False, False, 0)

    vboxStack2.pack_start(hbox2, False, False, 10)
    vboxStack2.pack_end(hbox4, False, False, 0)


    if Functions.os.path.isfile(Functions.i3wm_config):
        stack.add_titled(vboxStack1, "stack1", "I3WM")
    if Functions.os.path.isfile(Functions.awesome_config):
        stack.add_titled(vboxStack2, "stack2", "AwesomeWM")


    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack10.pack_start(vbox, True, True, 0)
