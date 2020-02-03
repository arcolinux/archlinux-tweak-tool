#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
def GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions):
    
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    
    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)
    
    #==========================================================
    #                       TAB #1
    #==========================================================
    
    stack.add_titled(vboxStack1, "main_stack", "Main")

    label = Gtk.Label()
    label.set_markup("<big>Under Construction!</big>")

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    
    browse = Gtk.Button(label="ADD")
    browse.connect("clicked", self.on_browse_fixed)

    remove = Gtk.Button(label="REMOVE")
    remove.connect("clicked", self.on_remove_fixed)

    btn2 = Gtk.Button(label="Run Skel")
    btn2.connect("clicked", self.on_button_fetch_clicked)
  
    sw = Gtk.ScrolledWindow()
    sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.store = Gtk.ListStore(str)

    self.treeView = Gtk.TreeView(self.store)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView.set_rules_hint(True)
    sw.set_size_request(270, 120)
    sw.add(self.treeView)
    self.create_columns(self.treeView)

    self.rbutton3 = Gtk.RadioButton(label="File")
    self.rbutton4 = Gtk.RadioButton.new_from_widget(self.rbutton3)
    self.rbutton4.set_label("Folder")

    vbox1.pack_start(browse, False, False, 0)
    vbox1.pack_start(remove, False, False, 10)

    hbox.pack_start(sw, True, True, 10)
    hbox.pack_start(vbox1, False, False, 10)

    hbox1.pack_end(self.rbutton4, False, False, 10)
    hbox1.pack_end(self.rbutton3, False, False, 10)
    
    hbox3.pack_start(label, True, False, 0)

    hbox2.pack_end(btn2, False, False, 0)

    vboxStack1.pack_start(hbox, False, False, 0)
    vboxStack1.pack_start(hbox1, False, False, 0)
    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_end(hbox2, False, False, 0)
    #==========================================================
    #                       TAB #2
    #==========================================================
    
    stack.add_titled(vboxStack2, "backup_stack", "Backups")

    label1 = Gtk.Label()
    label1.set_markup("<big>Under Construction!</big>")

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    hbox2.pack_start(label1, True, False, 10)

    vboxStack2.pack_start(hbox2, False, False, 0)
    vboxStack2.pack_start(hbox3, False, False, 0)


    vboxStack9.pack_start(stack_switcher, False, True, 0)
    vboxStack9.pack_start(stack, True, True, 0)

    # vboxStack9.pack_start(hbox1, False, False, 0)
    # vboxStack9.pack_start(hbox, False, False, 0)