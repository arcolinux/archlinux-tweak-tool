# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, vboxStack6, oblogout, Functions, os):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Oblogout Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox8.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                       TAB #6 OBLOGOUT
    # ==========================================================

    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    pixbuf2 = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/oblogout.jpg'), 345, 345)
    image2 = Gtk.Image().new_from_pixbuf(pixbuf2)
    hbox6.pack_start(image2, True, True, 0)


    # ==================Opacity Slider==============================

    try:
        vals = oblogout.get_opacity()
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

    # ==================Theme Dropdown==============================

    label6 = Gtk.Label()
    self.oblog = Gtk.ComboBoxText()
    label6.set_text("Themes")

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4.pack_start(label6, False, False, 10)
    hbox4.pack_start(self.oblog, True, True, 10)

    # ==================Buttons Textbox=============================

    label7 = Gtk.Label()
    label7.set_markup("<b>Buttons</b>")

    self.check_shut = Gtk.CheckButton()
    self.check_lock = Gtk.CheckButton()
    self.check_logout = Gtk.CheckButton()
    self.check_restart = Gtk.CheckButton()
    self.check_cancel = Gtk.CheckButton()
    self.check_susp = Gtk.CheckButton()
    self.check_hiber = Gtk.CheckButton()

    self.check_shut.set_label("Show shutdown ")
    self.check_lock.set_label("Show lock     ")
    self.check_logout.set_label("Show logout   ")
    self.check_restart.set_label("Show restart     ")
    self.check_cancel.set_label("Show cancel   ")
    self.check_susp.set_label("Show suspend   ")
    self.check_hiber.set_label("Show hibernate")
    self.spacer = Gtk.Label()
    self.spacer.set_text("                             ")

    btnString = oblogout.get_buttons()
    oblogout.oblog_populate(self.oblog)

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

    # ====================KEYBINDS==============================

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
        self.tbcancel.set_text(oblogout.get_shortcut("cancel"))
        self.tbshutdown.set_text(oblogout.get_shortcut("shutdown"))
        self.tbsuspend.set_text(oblogout.get_shortcut("suspend"))
        self.tbrestart.set_text(oblogout.get_shortcut("restart"))
        self.tblogout.set_text(oblogout.get_shortcut("logout"))
        self.tbhibernate.set_text(oblogout.get_shortcut("hibernate"))
        self.tblock.set_text(oblogout.get_shortcut("lock"))
    except:
        pass

    # ====================Lockscreen Textbox====================

    # label8 = Gtk.Label()
    # label8.set_text("Lockscreen")

    # self.lockBox = Gtk.Entry()
    # try:
    #     self.lockBox.set_text(oblogout.get_command("lock"))
    # except:
    #     pass

    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8.pack_start(label8, False, False, 10)
    # hbox8.pack_start(self.lockBox, True, True, 10)

    # ====================COLOR BUTTON==========================

    # hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # self.colorchooser = Gtk.ColorButton()
    # color = Gdk.RGBA()
    # color.parse(oblogout.get_color())
    # self.colorchooser.set_rgba(color)
    # label9 = Gtk.Label()
    # label9.set_text("Background")

    # hbox9.pack_start(label9, False, False, 10)
    # hbox9.pack_start(self.colorchooser, True, True, 10)

    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    save_oblogout = Gtk.Button(label="Save settings")
    save_oblogout.connect("clicked", self.save_oblogout)

    reset_oblogout = Gtk.Button(label="Reset settings")
    reset_oblogout.connect("clicked", self.reset_settings,
                           Functions.oblogout_conf)

    hbox21.pack_end(save_oblogout, False, False, 0)
    hbox21.pack_end(reset_oblogout, False, False, 0)

    # vboxStack6.pack_start(hbox6, False, False, 0)  # image
    vboxStack6.pack_start(hbox3, False, False, 0)  # slider
    vboxStack6.pack_start(hbox8, False, False, 0)  # slider
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
    # vboxStack6.pack_start(hbox8, False, False, 0)  # lockscreen
    # vboxStack6.pack_start(hbox9, False, False, 0)  # Color Button
    vboxStack6.pack_end(hbox21, False, False, 0)  # Save Button
