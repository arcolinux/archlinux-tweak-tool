import Functions

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os):
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
    label2.set_markup("<b>Add custom repo to pacman.conf</b>")

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


    self.button1 = Gtk.Button(label="Apply Custom Repo")
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
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    label = Gtk.Label()
    label.set_markup("Gtk Theme:       ")

    label2 = Gtk.Label()
    label2.set_markup("Icon Theme:     ")

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
    Functions.get_cursor_themes(self, cursorCombo)

    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_start(themeCombo, True, True, 0)
    
    hbox2.pack_start(label2, False, False, 0)
    hbox2.pack_start(iconCombo, True, True, 0)

    hbox3.pack_start(label3, False, False, 0)
    hbox3.pack_start(cursorCombo, True, True, 0)
    
    
    vboxStack2.pack_start(hbox1, False, False, 0)
    vboxStack2.pack_start(hbox2, False, False, 0)
    vboxStack2.pack_start(hbox3, False, False, 0)

    #==========================================================
    #                       TAB #3
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #3</big>")
    
    vboxStack3.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #4
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #4</big>")
    
    vboxStack4.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #5
    #==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #5</big>")

    vboxStack5.pack_start(label, False, False, 0)

    #==========================================================
    #                       TAB #6
    #==========================================================
    
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    pixbuf2 = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/oblogout.jpg'), 345, 345)
    image2 = Gtk.Image().new_from_pixbuf(pixbuf2)
    hbox6.pack_start(image2, True, True, 0)

    vals = Functions.get_value()
    ad1 = Gtk.Adjustment(vals, 0, 100, 5, 10, 0)

    #==============================================================
    #                   Opacity Slider
    #==============================================================

    label5 = Gtk.Label()
    label5.set_text("Opacity")

    self.hscale = Gtk.Scale(
        orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
    self.hscale.set_digits(0)
    self.hscale.set_hexpand(True)
    self.hscale.set_valign(Gtk.Align.START)
    # self.hscale.connect("value-changed", self.scale_moved)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5.pack_start(label5, False, True, 0)
    hbox5.pack_start(self.hscale, True, True, 0)

    #==============================================================
    #                   Theme Dropdown
    #==============================================================

    label6 = Gtk.Label()
    self.oblog = Gtk.ComboBoxText()
    label6.set_text("Themes")

    # self.oblog.connect("changed", self.oblog_changed)
    Functions.oblog_populate(self.oblog)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4.pack_start(label6, False, False, 0)
    hbox4.pack_start(self.oblog, True, True, 0)

    
    #==============================================================
    #                   Buttons Textbox
    #==============================================================
    label7 = Gtk.Label()
    label7.set_markup("<b>Buttons</b>")

    self.check_shut = Gtk.CheckButton()
    self.check_lock = Gtk.CheckButton()
    self.check_logout = Gtk.CheckButton()
    self.check_restart = Gtk.CheckButton()
    self.check_cancel = Gtk.CheckButton()
    self.check_susp = Gtk.CheckButton()
    self.check_hiber = Gtk.CheckButton()

    self.check_shut.set_label("Show Shutdown")
    self.check_lock.set_label("Show Lock")
    self.check_logout.set_label("Show Logout")
    self.check_restart.set_label("Show Restart")
    self.check_cancel.set_label("Show Cancel")
    self.check_susp.set_label("Show Suspend")
    self.check_hiber.set_label("Show Hibernate")
    
    btnString = Functions.get_buttons()

    if "shutdown" in btnString:
        self.check_shut.set_active(True)
    if "lock" in btnString:
        self.check_lock.set_active(True)
    if "logout" in btnString:
        self.check_logout.set_active(True)
    if "restart" in btnString:
        self.check_restart.set_active(True)
    if "cancel" in btnString:
        self.check_cancel.set_active(True)
    if "suspend" in btnString:
        self.check_susp.set_active(True)
    if "hibernate" in btnString:
        self.check_hiber.set_active(True)

    # SetButtons = Gtk.Button(label="Set Buttons")
    # SetButtons.connect("clicked", self.on_buttons_set)
    
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox7.pack_start(label7, False, False, 0)
    hbox10.pack_start(self.check_shut, False, False, 0)
    hbox10.pack_start(self.check_restart, False, False, 0)
    hbox10.pack_start(self.check_logout, False, False, 0)
    hbox10.pack_start(self.check_lock, False, False, 0)
    hbox11.pack_start(self.check_susp, False, False, 0)
    hbox11.pack_start(self.check_hiber, False, False, 0)
    hbox11.pack_start(self.check_cancel, False, False, 0)
    # hbox12.pack_start(SetButtons, False, False, 0)

    #==========================================================
    #                     Lockscreen Textbox
    #==========================================================

    label8 = Gtk.Label()
    label8.set_text("Lockscreen")

    self.lockBox = Gtk.Entry()
    self.lockBox.set_text(Functions.get_lockscreen())
    # Setlocks = Gtk.Button(label="Set")
    # Setlocks.connect("clicked", self.on_locks_set)

    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8.pack_start(label8, False, False, 0)
    hbox8.pack_start(self.lockBox, True, True, 0)
    # hbox8.pack_start(Setlocks, False, False, 0)

    

    #==========================================================
    #                     COLOR BUTTON
    #==========================================================
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.colorchooser = Gtk.ColorButton()
    # self.colorchooser.connect("color-set", self.on_color_chosen)
    color = Gdk.RGBA()
    color.parse(Functions.get_color())
    self.colorchooser.set_rgba(color)
    label9 = Gtk.Label()
    label9.set_text("Background")    
    
    hbox9.pack_start(label9, False, False, 0)
    hbox9.pack_start(self.colorchooser, True, True, 0)    



    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    save_oblogout = Gtk.Button(label="Save Settings")
    save_oblogout.connect("clicked", self.save_oblogout)
    hbox13.pack_end(save_oblogout, False, False, 0)   

    vboxStack6.pack_start(hbox6, False, False, 0)
    vboxStack6.pack_start(hbox5, False, False, 0)
    vboxStack6.pack_start(hbox4, False, False, 0)
    vboxStack6.pack_start(hbox7, False, False, 0)
    vboxStack6.pack_start(hbox10, False, False, 0)
    vboxStack6.pack_start(hbox11, False, False, 0)
    # vboxStack6.pack_start(hbox12, False, False, 0)
    vboxStack6.pack_start(hbox8, False, False, 0)
    vboxStack6.pack_start(hbox9, False, False, 0)
    vboxStack6.pack_start(hbox13, False, False, 0)

    
    #==========================================================
    #                     ADD TO WINDOW
    #==========================================================
    if Functions.file_check(Functions.pacman):
        stack.add_titled(vboxStack1, "stack1", "Pacman Config")
    if Functions.file_check(Functions.lightdm_conf):
        stack.add_titled(vboxStack2, "stack2", "Lightdm Config")
    # stack.add_titled(vboxStack3, "stack3", "Skel Config")
    # stack.add_titled(vboxStack4, "stack4", "Lockscreen")
    # stack.add_titled(vboxStack5, "stack5", "Grub Config")
    if Functions.file_check(Functions.oblogout_conf):
        stack.add_titled(vboxStack6, "stack6", "Oblogout Themes")


    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_stack(stack)
    
    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)
    
    
    ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)
    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(stack, True, True, 0)
    

    