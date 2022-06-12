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

    self.asci = Gtk.RadioButton(label="Enable ascii backend")
    #self.asci.set_label("Enable ascii backend")
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

    applyneofetch = Gtk.Button(label="Apply your Neofetch configuration")
    resetneofetch = Gtk.Button(label="Reset")
    installneofetch = Gtk.Button(label="Install Neofetch")

    applyneofetch.connect("clicked", self.on_apply_neo)
    resetneofetch.connect("clicked", self.on_reset_neo)
    installneofetch.connect("clicked", self.on_install_neo)

    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox22.set_margin_top(30)
    hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox24 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox25 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox25.set_margin_top(30)
    self.hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox27 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

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
    self.local = Gtk.CheckButton(label="Show locale")

    self.cblocks = Gtk.CheckButton(label="Show blocks")

    self.title = Gtk.CheckButton(label="Show title")

    self.neo_lolcat = Gtk.Switch()
    self.neo_lolcat.connect("notify::active", self.lolcat_toggle, "neofetch")
    lolcat_label = Gtk.Label(xalign=0)
    lolcat_label.set_markup("Use lolcat")
    self.neo_util = Gtk.Switch()
    self.neo_util.connect("notify::active", self.util_toggle, "neofetch")
    neo_util_label = Gtk.Label(xalign=0)
    neo_util_label.set_markup("Neofetch enabled")


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

    #hbox22.pack_start(self.w3m, True, False, 10)
    hbox22.pack_end(self.off, True, False, 10)
    hbox22.pack_end(self.asci, True, False, 10)



    self.hbox26.pack_start(self.big_ascii, True, False, 10)
    self.hbox26.pack_start(self.small_ascii, True, False, 10)

    hbox25.pack_start(flowbox, True, True, 10)

    hbox27.pack_start(neo_util_label, False, False, 10)
    hbox27.pack_start(self.neo_util, False, False, 30)
    hbox27.pack_start(lolcat_label, False, False, 0)
    hbox27.pack_start(self.neo_lolcat, False, False, 30)

    hbox24.pack_end(resetneofetch, False, False, 0)
    hbox24.pack_end(applyneofetch, False, False, 0)
    hbox24.pack_end(installneofetch, False, False, 0)

    vboxStack8.pack_start(hbox3, False, False, 0)
    vboxStack8.pack_start(hbox4, False, False, 0)
    vboxStack8.pack_start(hbox27, False, False, 0)
    vboxStack8.pack_start(hbox22, False, False, 0)
    vboxStack8.pack_start(self.hbox26, False, False, 0)
    vboxStack8.pack_start(hbox23, False, False, 0)
    vboxStack8.pack_start(hbox25, False, False, 0)
    vboxStack8.pack_end(hbox24, False, False, 0)

    if backend == "ascii":
        self.asci.set_active(True)
        self.big_ascii.set_sensitive(True)
        self.small_ascii.set_sensitive(True)
    elif backend == "off":
        self.off.set_active(True)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)
    else:
        #self.w3m.set_active(True)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)

    if asci == "auto":
        self.big_ascii.set_active(True)
    else:
        self.small_ascii.set_active(True)
