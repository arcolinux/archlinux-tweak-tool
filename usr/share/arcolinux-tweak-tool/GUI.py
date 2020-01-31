import Functions


def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os):
    # ==========================================================
    #                       CONTAINER
    # ==========================================================
    # grid = Gtk.Grid()
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    # swGTK = Gtk.ScrolledWindow()
    # swGTK.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    vbox.pack_start(hbox, True, True, 0)
    self.add(vbox)

    # ==========================================================
    #                    INITIALIZE STACK
    # ==========================================================
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
    stack.set_transition_duration(500)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ==========================================================
    #                   TAB #1 PACMAN
    # ==========================================================

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
    self.textbox1.set_border_window_size(Gtk.TextWindowType.LEFT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.RIGHT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.TOP, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.BOTTOM, 1)

    sw = Gtk.ScrolledWindow()
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    sw.add(self.textbox1)

    self.button1 = Gtk.Button(label="Apply Custom Repo")
    self.button1.connect('clicked', self.button1_clicked)
    reset_pacman = Gtk.Button(label="Reset Pacman")
    reset_pacman.connect("clicked", self.reset_settings, Functions.pacman)

    hboxStack1.pack_start(label1, False, True, 10)
    hboxStack1.pack_end(self.checkbutton, False, False, 10)
    hboxStack5.pack_start(label3, False, True, 10)
    hboxStack5.pack_end(self.checkbutton2, False, False, 10)
    hboxStack6.pack_start(label4, False, True, 10)
    hboxStack6.pack_end(self.checkbutton3, False, False, 10)

    hboxStack2.pack_start(label2, False, True, 10)
    hboxStack3.pack_start(sw, True, True, 10)

    hboxStack4.pack_end(self.button1, False, False, 0)
    hboxStack4.pack_end(reset_pacman, False, False, 0)

    vboxStack1.pack_start(hboxStack1, False, False, 0)
    vboxStack1.pack_start(hboxStack5, False, False, 0)
    vboxStack1.pack_start(hboxStack6, False, False, 0)
    vboxStack1.pack_start(hboxStack2, False, False, 0)
    vboxStack1.pack_start(hboxStack3, True, True, 0)
    vboxStack1.pack_start(hboxStack4, False, False, 0)

    # ==========================================================
    #                 TAB #2 GTK THEMES
    # ==========================================================
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label()
    label.set_markup("Gtk Theme:       ")

    label2 = Gtk.Label()
    label2.set_markup("Icon Theme:     ")

    label3 = Gtk.Label()
    label3.set_markup("Cursor Theme:")

    label5 = Gtk.Label()
    label5.set_markup("Cursor Size: ")

    label6 = Gtk.Label()
    label6.set_markup("Select Font: ")

    self.themeCombo = Gtk.ComboBoxText()
    self.iconCombo = Gtk.ComboBoxText()
    self.cursorCombo = Gtk.ComboBoxText()

    adj1 = Gtk.Adjustment(1.0, 1.0, 42.0, 1.0, 5.0, 0.0)
    self.cursor_size = Gtk.SpinButton()
    self.cursor_size.set_adjustment(adj1)

    self.fonts = Gtk.FontButton()

    self.themeCombo.set_size_request(200, 0)
    self.iconCombo.set_size_request(200, 0)
    self.cursorCombo.set_size_request(200, 0)

    # Set functions
    Functions.get_gtk_themes(self, self.themeCombo)
    Functions.get_icon_themes(self, self.iconCombo)
    Functions.get_cursor_themes(self, self.cursorCombo)

    self.cursor_size.set_value(
        int(Functions.get_gtk_settings("gtk-cursor-theme-size").split(".")[0]))
    self.fonts.set_font_name(Functions.get_gtk_settings("gtk-font-name"))

    save_gtk3_themes = Gtk.Button(label="Save Settings")
    save_gtk3_themes.connect("clicked", self.save_gtk3_settings, self.themeCombo,
                             self.iconCombo, self.cursorCombo, self.cursor_size, self.fonts)

    reset_gtk3_themes = Gtk.Button(label="Reset Defaults")
    reset_gtk3_themes.connect(
        "clicked", self.reset_settings, Functions.gtk3_settings)

    hbox1.pack_start(label, False, False, 10)
    hbox1.pack_start(self.themeCombo, True, True, 10)

    hbox2.pack_start(label2, False, False, 10)
    hbox2.pack_start(self.iconCombo, True, True, 10)

    hbox3.pack_start(label3, False, False, 10)
    hbox3.pack_start(self.cursorCombo, True, True, 10)

    hbox5.pack_start(label5, False, False, 10)
    hbox5.pack_end(self.cursor_size, False, False, 10)

    hbox6.pack_start(label6, False, False, 10)
    hbox6.pack_end(self.fonts, False, False, 10)

    hbox4.pack_end(save_gtk3_themes, False, False, 0)
    hbox4.pack_end(reset_gtk3_themes, False, False, 0)

    vboxStack2.pack_start(hbox1, False, False, 0)  # Gtk Themes
    vboxStack2.pack_start(hbox2, False, False, 0)  # Gtk Icon Themes
    vboxStack2.pack_start(hbox3, False, False, 0)  # Gtk Cursor Themes
    vboxStack2.pack_start(hbox5, False, False, 0)  # Gtk Cursor Size
    vboxStack2.pack_start(hbox6, False, False, 0)  # Gtk Fonts
    vboxStack2.pack_end(hbox4, False, False, 0)  # Save Button

    # ==========================================================
    #                       HBLOCK
    # ==========================================================
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label()
    label.set_text("enable hblock")

    self.label7 = Gtk.Label(xalign=0)
    self.label7.set_text("Idle ....")

    self.progress = Gtk.ProgressBar()
    self.progress.set_pulse_step(0.2)

    self.hbswich = Gtk.Switch()
    self.hbswich.connect("notify::active", self.set_hblock)
    self.hbswich.set_active(Functions.hblock_get_state())

    hbox7.pack_start(label, False, False, 10)
    hbox7.pack_end(self.hbswich, False, False, 10)

    vboxStack3.pack_start(hbox7, False, False, 0)
    vboxStack3.pack_end(self.progress, False, False, 0)
    vboxStack3.pack_end(self.label7, False, False, 0)

    # ==========================================================
    #                       GRUB
    # ==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #4</big>")

    vboxStack4.pack_start(label, False, False, 0)

    # ==========================================================
    #                       TAB #5
    # ==========================================================
    label = Gtk.Label()
    label.set_markup("<big>Label on Tab #5</big>")

    vboxStack5.pack_start(label, False, False, 0)

    # ==========================================================
    #                       TAB #6
    # ==========================================================

    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    pixbuf2 = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/oblogout.jpg'), 345, 345)
    image2 = Gtk.Image().new_from_pixbuf(pixbuf2)
    hbox6.pack_start(image2, True, True, 0)

    # ==============================================================
    #                   Opacity Slider
    # ==============================================================

    try:
        vals = Functions.get_opacity()
        ad1 = Gtk.Adjustment(vals, 0, 100, 5, 10, 0)
    except:
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)

    label5 = Gtk.Label()
    label5.set_text("Opacity")

    self.hscale = Gtk.Scale(
        orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
    self.hscale.set_digits(0)
    self.hscale.set_hexpand(True)
    self.hscale.set_valign(Gtk.Align.START)
    # self.hscale.connect("value-changed", self.scale_moved)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5.pack_start(label5, False, False, 10)
    hbox5.pack_start(self.hscale, True, True, 10)

    # ==============================================================
    #                   Theme Dropdown
    # ==============================================================

    label6 = Gtk.Label()
    self.oblog = Gtk.ComboBoxText()
    label6.set_text("Themes")

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4.pack_start(label6, False, False, 10)
    hbox4.pack_start(self.oblog, True, True, 10)

    # ==============================================================
    #                   Buttons Textbox
    # ==============================================================
    label7 = Gtk.Label()
    label7.set_markup("<b>Buttons</b>")

    self.check_shut = Gtk.CheckButton()
    self.check_lock = Gtk.CheckButton()
    self.check_logout = Gtk.CheckButton()
    self.check_restart = Gtk.CheckButton()
    self.check_cancel = Gtk.CheckButton()
    self.check_susp = Gtk.CheckButton()
    self.check_hiber = Gtk.CheckButton()

    self.check_shut.set_label("Show Shutdown ")
    self.check_lock.set_label("Show Lock     ")
    self.check_logout.set_label("Show Logout   ")
    self.check_restart.set_label("Show Restart     ")
    self.check_cancel.set_label("Show Cancel   ")
    self.check_susp.set_label("Show Suspend   ")
    self.check_hiber.set_label("Show Hibernate")
    self.spacer = Gtk.Label()
    self.spacer.set_text("                             ")

    btnString = Functions.get_buttons()
    Functions.oblog_populate(self.oblog)

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

    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox7.pack_start(label7, False, False, 10)
    hbox10.pack_start(self.check_shut, True, True, 10)
    hbox10.pack_start(self.check_restart, True, True, 10)
    hbox10.pack_start(self.check_logout, True, True, 10)
    hbox11.pack_start(self.check_susp, True, True, 10)
    hbox11.pack_start(self.check_hiber, True, True, 10)
    hbox11.pack_start(self.check_cancel, True, True, 10)
    hbox12.pack_start(self.check_lock, True, True, 10)
    hbox12.pack_start(self.spacer, True, True, 10)
    # hbox12.pack_start(SetButtons, False, False, 0)

    # ==========================================================
    #                     KEYBINDS
    # ==========================================================
    label8 = Gtk.Label()
    label8.set_markup("<b>Keybinds</b>")

    labelcancel = Gtk.Label()
    labelcancel.set_markup("Cancel   ")
    labelshutdown = Gtk.Label()
    labelshutdown.set_markup("Shutdown")
    labelsuspend = Gtk.Label()
    labelsuspend.set_markup("Suspend")
    labelrestart = Gtk.Label()
    labelrestart.set_markup("Restart     ")
    labellogout = Gtk.Label()
    labellogout.set_markup("Logout   ")
    labellock = Gtk.Label()
    labellock.set_markup("Lock")
    labelhibernate = Gtk.Label()
    labelhibernate.set_markup("Hibernate")

    self.tbcancel = Gtk.Entry()
    self.tbcancel.set_max_length(12)
    self.tbcancel.set_width_chars(True)

    self.tbshutdown = Gtk.Entry()
    self.tbshutdown.set_max_length(1)
    self.tbshutdown.set_width_chars(True)

    self.tbsuspend = Gtk.Entry()
    self.tbsuspend.set_max_length(1)
    self.tbsuspend.set_width_chars(True)

    self.tbrestart = Gtk.Entry()
    self.tbrestart.set_max_length(1)
    self.tbrestart.set_width_chars(True)

    self.tblogout = Gtk.Entry()
    self.tblogout.set_max_length(1)
    self.tblogout.set_width_chars(True)

    self.tblock = Gtk.Entry()
    self.tblock.set_max_length(1)
    self.tblock.set_width_chars(True)

    self.tbhibernate = Gtk.Entry()
    self.tbhibernate.set_max_length(1)
    self.tbhibernate.set_width_chars(True)

    hbox14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox14.pack_start(label8, False, False, 10)
    hbox15.pack_start(labelcancel, False, True, 10)
    hbox15.pack_start(self.tbcancel, True, True, 10)

    hbox15.pack_start(labelshutdown, False, True, 10)
    hbox15.pack_start(self.tbshutdown, True, True, 10)

    hbox16.pack_start(labelsuspend, False, True, 10)
    hbox16.pack_start(self.tbsuspend, True, True, 10)

    hbox16.pack_start(labelrestart, False, True, 10)
    hbox16.pack_start(self.tbrestart, True, True, 10)

    hbox17.pack_start(labellogout, False, True, 10)
    hbox17.pack_start(self.tblogout, True, True, 10)

    hbox17.pack_start(labelhibernate, False, True, 10)
    hbox17.pack_start(self.tbhibernate, True, True, 10)

    hbox18.pack_start(labellock, False, True, 10)
    hbox18.pack_start(self.tblock, True, True, 10)

    try:
        self.tbcancel.set_text(Functions.get_shortcut("cancel"))
        self.tbshutdown.set_text(Functions.get_shortcut("shutdown"))
        self.tbsuspend.set_text(Functions.get_shortcut("suspend"))
        self.tbrestart.set_text(Functions.get_shortcut("restart"))
        self.tblogout.set_text(Functions.get_shortcut("logout"))
        self.tbhibernate.set_text(Functions.get_shortcut("hibernate"))
        self.tblock.set_text(Functions.get_shortcut("lock"))
    except:
        pass
    # ==========================================================
    #                     Lockscreen Textbox
    # ==========================================================

    label8 = Gtk.Label()
    label8.set_text("Lockscreen")

    self.lockBox = Gtk.Entry()
    try:
        self.lockBox.set_text(Functions.get_command("lock"))
    except:
        pass
    # Setlocks = Gtk.Button(label="Set")
    # Setlocks.connect("clicked", self.on_locks_set)

    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8.pack_start(label8, False, False, 10)
    hbox8.pack_start(self.lockBox, True, True, 10)
    # hbox8.pack_start(Setlocks, False, False, 0)

    # ==========================================================
    #                     COLOR BUTTON
    # ==========================================================
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.colorchooser = Gtk.ColorButton()
    # self.colorchooser.connect("color-set", self.on_color_chosen)
    color = Gdk.RGBA()
    color.parse(Functions.get_color())
    self.colorchooser.set_rgba(color)
    label9 = Gtk.Label()
    label9.set_text("Background")

    hbox9.pack_start(label9, False, False, 10)
    hbox9.pack_start(self.colorchooser, True, True, 10)

    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    save_oblogout = Gtk.Button(label="Save Settings")
    save_oblogout.connect("clicked", self.save_oblogout)

    reset_oblogout = Gtk.Button(label="Reset Settings")
    reset_oblogout.connect("clicked", self.reset_settings,
                           Functions.oblogout_conf)

    hbox13.pack_end(save_oblogout, False, False, 0)
    hbox13.pack_end(reset_oblogout, False, False, 0)

    # vboxStack6.pack_start(hbox6, False, False, 0)  # image
    vboxStack6.pack_start(hbox5, False, False, 0)  # slider
    vboxStack6.pack_start(hbox4, False, False, 0)  # themes
    vboxStack6.pack_start(hbox7, False, False, 0)  # button label
    vboxStack6.pack_start(hbox10, False, False, 0)  # Buttons row 1
    vboxStack6.pack_start(hbox11, False, False, 0)  # Buttons row 2
    vboxStack6.pack_start(hbox12, False, False, 0)  # Buttons row 3
    vboxStack6.pack_start(hbox14, False, False, 0)  # Keybind Label
    vboxStack6.pack_start(hbox15, False, False, 0)  # keybind row 1
    vboxStack6.pack_start(hbox16, False, False, 0)  # keybind row 2
    vboxStack6.pack_start(hbox17, False, False, 0)  # keybind row 3
    vboxStack6.pack_start(hbox8, False, False, 0)  # lockscreen
    vboxStack6.pack_start(hbox9, False, False, 0)  # Color Button
    vboxStack6.pack_end(hbox13, False, False, 0)  # Save Button

    # ==========================================================
    #                     ADD TO WINDOW
    # ==========================================================
    if Functions.file_check(Functions.pacman):
        stack.add_titled(vboxStack1, "stack1", "Pacman Config")

    stack.add_titled(vboxStack2, "stack2", "Gtk+3 Config")

    # stack.add_titled(vboxStack5, "stack5", "Grub Config")

    if Functions.file_check(Functions.oblogout_conf):
        stack.add_titled(vboxStack6, "stack6", "Oblogout Config")

    stack.add_titled(vboxStack3, "stack3", "HBlock")

    # stack.add_titled(vboxStack4, "stack4", "Grub")

    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_stack(stack)

    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    version = Gtk.Label(xalign=0)
    version.set_markup("<span foreground=\'grey\'>v20.2.16</span>")

    ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)
    ivbox.pack_start(version, False, False, 0)
    hbox.pack_start(ivbox, False, True, 0)
    # swGTK.add(stack)
    hbox.pack_start(stack, True, True, 0)
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
    print(stack.get_hhomogeneous())