#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, Functions):
    
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    
    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)

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
    themer.get_i3_themes(self.i3_combo)

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
    self.awesome_combo = Gtk.ComboBoxText()
    self.awesome_combo.set_size_request(180, 0)
    themer.get_awesome_themes(self.awesome_combo)

    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox3.pack_start(self.awesome_combo, False, False, 0)

    hbox2.pack_start(label2, False, False, 10)
    hbox2.pack_end(vbox3, False, False, 10)

    vboxStack2.pack_start(hbox2, False, False, 10)


    if Functions.os.path.isfile(Functions.i3wm_config):
        stack.add_titled(vboxStack1, "stack1", "I3WM")
    if Functions.os.path.isfile(Functions.awesome_config):
        stack.add_titled(vboxStack2, "stack2", "AwesomeWM")


    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack10.pack_start(vbox, False, False, 0)
