import Functions

def GUI(self, Gtk):
    #==========================================================
    #                       CONTAINER
    #==========================================================
    # grid = Gtk.Grid()        
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    vbox.pack_start(hbox, True, True, 0)
    self.add(vbox)

    #==========================================================
    #                    INITIALIZE STACK
    #==========================================================
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
    stack.set_transition_duration(500)
    
    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    #==========================================================
    #                   TAB #1 PACMAN
    #==========================================================
    
    stack.add_titled(vboxStack1, "stack1", "Pacman Config")
    
    hboxStack1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    self.checkbutton = Gtk.Switch()
    self.checkbutton.connect("notify::active", self.on_pacman_toggle)
    label1 = Gtk.Label(xalign=0)
    label1.set_markup("Enable Arcolinux Test Repo")

    self.checkbutton2 = Gtk.Switch()
    self.checkbutton2.connect("notify::active", self.on_pacman_toggle2)
    label3 = Gtk.Label(xalign=0)
    label3.set_markup("Enable Arch Test Repo")

    self.checkbutton3 = Gtk.Switch()
    self.checkbutton3.connect("notify::active", self.on_pacman_toggle3)
    label4 = Gtk.Label(xalign=0)
    label4.set_markup("Enable Arch Multilib Test Repo")
    
    
    label2 = Gtk.Label(xalign=0)
    label2.set_markup("<b>Add repo to pacman.conf</b>")

    self.textbox1 = Gtk.TextView()
    self.textbox1.set_wrap_mode(Gtk.WrapMode.WORD)
    self.textbox1.set_editable(True)
    self.textbox1.set_cursor_visible(True)   
    self.textbox1.set_border_window_size(Gtk.TextWindowType.LEFT,1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.RIGHT,1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.TOP,1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.BOTTOM,1)

    sw = Gtk.ScrolledWindow()
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    sw.add(self.textbox1)


    self.button1 = Gtk.Button(label="Apply Repo")
    self.button1.connect('clicked', self.button1_clicked)
    
    hboxStack1.pack_start(label1, False, True, 10)
    hboxStack1.pack_end(self.checkbutton, False, True, 10)
    hboxStack5.pack_start(label3, False, True, 10)
    hboxStack5.pack_end(self.checkbutton2, False, True, 10)
    hboxStack6.pack_start(label4, False, True, 10)
    hboxStack6.pack_end(self.checkbutton3, False, True, 10)

    hboxStack2.pack_start(label2, False, True, 10)
    hboxStack3.pack_start(sw, True, True, 0)
    hboxStack4.pack_end(self.button1, False, False, 0)

    

    vboxStack1.pack_start(hboxStack1, False, False, 0)
    vboxStack1.pack_start(hboxStack5, False, False, 0)
    vboxStack1.pack_start(hboxStack6, False, False, 0)
    vboxStack1.pack_start(hboxStack2, False, False, 0)
    vboxStack1.pack_start(hboxStack3, True, True, 0)
    vboxStack1.pack_start(hboxStack4, False, False, 0)
    #==========================================================
    #                 TAB #2 LIGHTDM
    #==========================================================
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    label = Gtk.Label()
    label.set_markup("Gtk Theme:    ")

    label2 = Gtk.Label()
    label2.set_markup("Icon Theme:  ")

    label3 = Gtk.Label()
    label3.set_markup("Cursor Theme:")
    
    themeCombo = Gtk.ComboBoxText()
    iconCombo = Gtk.ComboBoxText()
    cursorCombo = Gtk.ComboBoxText()

    themeCombo.set_size_request(200, 0)
    iconCombo.set_size_request(200, 0)
    cursorCombo.set_size_request(200, 0)

    Functions.get_gtk_themes(self, themeCombo)
    Functions.get_icon_themes(self, iconCombo)
    # Functions.get_cursor_themes(self, cursorCombo)

    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_start(themeCombo, True, True, 0)
    
    hbox2.pack_start(label2, False, False, 0)
    hbox2.pack_start(iconCombo, True, True, 0)
    
    stack.add_titled(vboxStack2, "stack2", "Lightdm Config")

    vboxStack2.pack_start(hbox1, False, False, 0)
    vboxStack2.pack_start(hbox2, False, False, 0)

    #==========================================================
    #                       TAB #3
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #3</big>")
    stack.add_titled(vboxStack3, "stack3", "Skel Config")

    vboxStack3.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #4
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #4</big>")
    stack.add_titled(vboxStack4, "stack4", "Lockscreen")

    vboxStack4.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #5
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #5</big>")
    stack.add_titled(vboxStack5, "stack5", "Grub Config")

    vboxStack5.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #6
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #6</big>")
    stack.add_titled(vboxStack6, "stack6", "Oblogout Themes")

    vboxStack6.pack_start(label, False, False, 0)

    #==========================================================
    #                     ADD TO WINDOW
    #==========================================================
    stack_switcher = Gtk.StackSidebar()
    # stack_switcher.set_orientation(Gtk.Orientation.VERTICAL)
    stack_switcher.set_stack(stack)
    # stack_switcher.set_homogeneous(True)
    # grid.attach(stack_switcher, 0, 0, 1, 10)
    # grid.attach(stack, 1, 0, 2, 10)
    hbox.pack_start(stack_switcher, False, True, 0)
    hbox.pack_start(stack, True, True, 0)