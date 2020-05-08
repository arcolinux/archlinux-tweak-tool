# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack8, neofetch, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Neofetch Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                     NEOFETCH
    # ==========================================================
    label13 = Gtk.Label()
    label13.set_text("Select image")

    self.w3m = Gtk.RadioButton(label="Enable image backend")
    self.w3m.connect("toggled", self.radio_toggled)

    self.asci = Gtk.RadioButton.new_from_widget(self.w3m)
    self.asci.set_label("Enable ascii backend")
    self.asci.connect("toggled", self.radio_toggled)

    self.off = Gtk.RadioButton.new_from_widget(self.asci)
    self.off.set_label("No backend")
    self.off.connect("toggled", self.radio_toggled)

    self.big_ascii = Gtk.RadioButton(label="Use normal ascii")

    self.small_ascii = Gtk.RadioButton.new_from_widget(self.big_ascii)
    self.small_ascii.set_label("Use small ascii")

    backend = neofetch.check_backend()
    asci = neofetch.check_ascii()

    self.emblem = Gtk.ComboBoxText()
    neofetch.pop_neofetch_box(self.emblem)
    self.emblem.connect("changed", self.on_elmblem_changed)

    applyneofetch = Gtk.Button(label="Apply")
    resetneofetch = Gtk.Button(label="Reset")

    applyneofetch.connect("clicked", self.on_apply_neo)
    resetneofetch.connect("clicked", self.on_reset_neo)

    self.image4 = Gtk.Image()

    try:
        path = Functions.home + "/.config/neofetch/" + self.emblem.get_active_text()

        pixbuf6 = GdkPixbuf.Pixbuf().new_from_file_at_size(path, 145, 145)
        self.image4.set_from_pixbuf(pixbuf6)
    except:
        pass

    self.frame3 = Gtk.Frame(label="Preview")
    self.frame3.set_no_show_all(True)
    self.frame3.add(self.image4)

    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox24 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox25 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    self.hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    self.os = Gtk.CheckButton(label="Show os")
    self.host = Gtk.CheckButton(label="Show hostname")
    self.kernel = Gtk.CheckButton(label="Show kernel")

    self.uptime = Gtk.CheckButton(label="Show uptime")
    self.packages = Gtk.CheckButton(label="Show packages")
    self.shell = Gtk.CheckButton(label="Show shell")

    self.res = Gtk.CheckButton(label="Show resolution")
    self.de = Gtk.CheckButton(label="Show de")
    self.wm = Gtk.CheckButton(label="Show wm")
    self.wmtheme = Gtk.CheckButton(label="Show wm theme")

    self.themes = Gtk.CheckButton(label="Show theme")
    self.icons = Gtk.CheckButton(label="Show icons")
    self.term = Gtk.CheckButton(label="Show terminal")

    self.termfont = Gtk.CheckButton(label="Show terminal font")
    self.cpu = Gtk.CheckButton(label="Show cpu")
    self.gpu = Gtk.CheckButton(label="Show gpu")

    self.mem = Gtk.CheckButton(label="Show memory")

    self.gpu_driver = Gtk.CheckButton(label="Show gpu driver")
    self.cpu_usage = Gtk.CheckButton(label="Show cpu usage")
    self.disks = Gtk.CheckButton(label="Show disk")
    self.font = Gtk.CheckButton(label="Show font")
    self.song = Gtk.CheckButton(label="Show song")
    self.lIP = Gtk.CheckButton(label="Show local ip")
    self.PIP = Gtk.CheckButton(label="Show public ip")
    self.users = Gtk.CheckButton(label="Show users")
    self.local = Gtk.CheckButton(label="Show local")

    self.cblocks = Gtk.CheckButton(label="Show blocks")

    self.title = Gtk.CheckButton(label="Show title")

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.os)
    flowbox.add(self.host)
    flowbox.add(self.kernel)
    flowbox.add(self.uptime)
    flowbox.add(self.packages)
    flowbox.add(self.shell)
    flowbox.add(self.res)
    flowbox.add(self.de)
    flowbox.add(self.wm)
    flowbox.add(self.wmtheme)
    flowbox.add(self.themes)
    flowbox.add(self.icons)
    flowbox.add(self.term)
    flowbox.add(self.termfont)
    flowbox.add(self.cpu)
    flowbox.add(self.gpu)
    flowbox.add(self.mem)
    flowbox.add(self.gpu_driver)
    flowbox.add(self.cpu_usage)
    flowbox.add(self.disks)
    flowbox.add(self.font)
    flowbox.add(self.song)
    flowbox.add(self.lIP)
    flowbox.add(self.PIP)
    flowbox.add(self.users)
    flowbox.add(self.local)
    flowbox.add(self.cblocks)
    flowbox.add(self.title)

    neofetch.get_checkboxes(self)

    label14 = Gtk.Label(xalign=0)
    label14.set_markup("<b>Tip:</b> We use w3m to display an image.")

    hbox22.pack_start(self.w3m, True, False, 10)
    hbox22.pack_end(self.off, True, False, 10)
    hbox22.pack_end(self.asci, True, False, 10)



    self.hbox26.pack_start(self.big_ascii, True, False, 10)
    self.hbox26.pack_start(self.small_ascii, True, False, 10)

    hbox23.pack_start(label13, False, False, 10)
    hbox23.pack_start(self.emblem, True, True, 10)

    hbox25.pack_start(self.frame3, False, False, 10)
    hbox25.pack_start(flowbox, True, True, 10)

    hbox24.pack_end(applyneofetch, False, False, 0)
    hbox24.pack_end(resetneofetch, False, False, 0)

    vboxStack8.pack_start(hbox3, False, False, 0) #Backend RadioButtons
    vboxStack8.pack_start(hbox4, False, False, 0) #Backend RadioButtons
    vboxStack8.pack_start(hbox22, False, False, 0) #Backend RadioButtons
    vboxStack8.pack_start(self.hbox26, False, False, 0) #Ascii RadioButtons
    vboxStack8.pack_start(hbox23, False, False, 0) #ComboBox
    vboxStack8.pack_start(hbox25, False, False, 0) #Preview / Options
    vboxStack8.pack_end(hbox24, False, False, 0) #Buttons
    vboxStack8.pack_end(label14, False, False, 0) #Buttons




    if backend == "ascii":
        self.asci.set_active(True)
        self.emblem.set_sensitive(False)
        self.big_ascii.set_sensitive(True)
        self.small_ascii.set_sensitive(True)
        self.frame3.hide()
    elif backend == "off":
        self.off.set_active(True)
        self.emblem.set_sensitive(False)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)
        self.frame3.hide()
    else:
        self.w3m.set_active(True)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)
        self.frame3.show()
        self.image4.show()

    if asci == "auto":
        self.big_ascii.set_active(True)
    else:
        self.small_ascii.set_active(True)
