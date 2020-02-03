#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
def GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions):
    
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    
    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)
    
    
    #=======================TAB #1=============================
    
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
    
    #=======================TAB #2=============================
    
    stack.add_titled(vboxStack2, "backup_stack", "Backups")

    label1 = Gtk.Label()
    label1.set_markup("<big>Under Construction!</big>")

    
    hbox4 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox5 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    vbox9 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox10 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox11 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox12 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox13 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox14 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    vbox11 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)
    
    # ListRow 1 Elements
    self.backs = Gtk.ComboBoxText()
    
    # skelapp.refresh(self)

    self.backs.set_active(0)
    self.backs.set_size_request(170, 0)
    btn4 = Gtk.Button(label="Refresh")
    btn5 = Gtk.Button(label="Delete")
    btn12 = Gtk.Button(label="Run Full Backup")
    btn9 = Gtk.Button(label="Delete All Backups")
    

    sw2 = Gtk.ScrolledWindow()
    sw2.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw2.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.store2 = Gtk.ListStore(str)

    self.treeView2 = Gtk.TreeView(self.store2)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView2.set_rules_hint(True)
    sw2.set_size_request(270, 120)
    sw2.add(self.treeView2)
    self.create_columns(self.treeView2)

    
    # skelapp.refresh_inner(self)
    
    btn10 = Gtk.Button(label="Delete")
    btn11 = Gtk.Button(label="Restore")

    btn4.connect("clicked", self.on_refresh_clicked)
    btn5.connect("clicked", self.on_delete_clicked)
    # btn9.connect("clicked", self.on_flush_clicked)
    btn12.connect("clicked", self.on_backup_clicked)
    btn10.connect("clicked", self.on_delete_inner_clicked)
    # btn11.connect("clicked", self.on_restore_inner_clicked)

    label4 = Gtk.Label(xalign=0)
    label4.set_markup("<b>Delete Backups</b>")

    self.progressbar = Gtk.ProgressBar()
    self.label_info = Gtk.Label("Idle ...")

    hbox5.pack_start(label4, True, True, 10)

    hbox4.pack_start(self.backs, True, True, 10)
    hbox4.pack_start(btn4, False, False, 0)
    hbox4.pack_end(btn5, True, True, 10)

    # hbox11.pack_start(self.backs_inner, True, True, 0)

    vbox11.pack_start(btn10, False, False, 0)
    vbox11.pack_start(btn11, False, False, 10)

    hbox10.pack_start(sw2, True, True, 10)
    hbox10.pack_start(vbox11, False, False, 10)
    
    vbox9.pack_start(btn9, True, True, 5)
    vbox9.pack_start(btn12, True, True, 5)
        
    hbox12.pack_start(label1, True, True, 5)

    hbox13.pack_start(self.label_info, False, False, 5)
    hbox14.pack_start(self.progressbar, True, True, 5)

    vboxStack2.pack_start(hbox5, False, False, 0)
    vboxStack2.pack_start(hbox4, False, False, 0)
    vboxStack2.pack_start(hbox10, False, False, 0)
    vboxStack2.pack_start(vbox9, False, False, 0) #
    vboxStack2.pack_start(hbox12, False, False, 0)

    vboxStack2.pack_end(hbox14, False, False, 0)
    vboxStack2.pack_end(hbox13, False, False, 0)

    self.backs.connect("changed", self.backs_changed)

    #=======================ADD STACKS=============================

    vboxStack9.pack_start(stack_switcher, False, True, 0)
    vboxStack9.pack_start(stack, True, True, 0)

    # vboxStack9.pack_start(hbox1, False, False, 0)
    # vboxStack9.pack_start(hbox, False, False, 0)