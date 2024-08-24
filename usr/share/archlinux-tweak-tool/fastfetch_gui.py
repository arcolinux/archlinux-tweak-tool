# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================
# pylint:disable=C0103,
import fastfetch

def gui(self, Gtk, vboxstack8, fastfetch, fn):
    """create a gui"""
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Fastfetch Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                     fastfetch
    # ==========================================================

    hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    warning_label = Gtk.Label(xalign=0)
    warning_label.set_markup(
        "<b>Some distros have their own configuration and/or application, investigate</b>"
    )
    hbox23.pack_start(warning_label, False, False, 10)

    self.asci = Gtk.RadioButton(label="Enable ascii backend")
    self.asci.connect("toggled", self.radio_toggled)

    self.off = Gtk.RadioButton.new_from_widget(self.asci)
    self.off.set_label("No backend")
    self.off.connect("toggled", self.radio_toggled)

    self.distro_ascii = Gtk.ComboBoxText()
    fastfetch.pop_distro_combobox(self, self.distro_ascii)
    # self.distro_ascii.connect("changed", self.on_distro_ascii_changed)
    self.distro_ascii.set_active(0)

    self.big_ascii = Gtk.RadioButton(label="Use normal ascii")

    self.small_ascii = Gtk.RadioButton.new_from_widget(self.big_ascii)
    self.small_ascii.set_label("Use small ascii")

    backend = fastfetch.check_backend()
    asci = fastfetch.check_ascii()

    applyfastfetch = Gtk.Button(label="Apply Fastfetch configuration")
    resetnormalfastfetch = Gtk.Button(label="Reset Fastfetch")
    useattfastfetch = Gtk.Button(label="Use Default config")
    installfastfetch = Gtk.Button(label="Install Fastfetch")

    applyfastfetch.connect("clicked", self.on_apply_fast)
    resetnormalfastfetch.connect("clicked", self.on_reset_fast)
    useattfastfetch.connect("clicked", self.on_reset_fast_att)
    installfastfetch.connect("clicked", self.on_install_fast)

    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox22.set_margin_top(30)
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
    self.display = Gtk.CheckButton(label="Show display")
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
    self.swap = Gtk.CheckButton(label="Show swap")
    self.cursor = Gtk.CheckButton(label="Show cursor")
    self.disks = Gtk.CheckButton(label="Show disk")
    self.font = Gtk.CheckButton(label="Show font")
    self.disks = Gtk.CheckButton(label="Show disks")
    self.lIP = Gtk.CheckButton(label="Show local ip")
    self.PIP = Gtk.CheckButton(label="Show public ip")
    self.local = Gtk.CheckButton(label="Show locale")
    self.batt = Gtk.CheckButton(label="Show battery")
    self.pwr = Gtk.CheckButton(label="Show power adapter")
    self.title = Gtk.CheckButton(label="Show title")
    self.cblocks = Gtk.CheckButton(label="Show color blocks")

    self.fast_lolcat = Gtk.Switch()
    self.fast_lolcat.connect("notify::active", self.lolcat_toggle, "fastfetch")
    lolcat_label = Gtk.Label(xalign=0)
    lolcat_label.set_markup("Use lolcat")
    self.fast_util = Gtk.Switch()
    self.fast_util.connect("notify::active", self.util_toggle, "fastfetch")
    fast_util_label = Gtk.Label(xalign=0)
    fast_util_label.set_markup("Fastfetch enabled")

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.title)
    flowbox.add(self.os)
    flowbox.add(self.host)
    flowbox.add(self.kernel)
    flowbox.add(self.uptime)
    flowbox.add(self.packages)
    flowbox.add(self.shell)
    flowbox.add(self.display)
    flowbox.add(self.de)
    flowbox.add(self.wm)
    flowbox.add(self.wmtheme)
    flowbox.add(self.themes)
    flowbox.add(self.icons)
    flowbox.add(self.font)
    flowbox.add(self.cursor)
    flowbox.add(self.term)
    flowbox.add(self.termfont)
    flowbox.add(self.cpu)
    flowbox.add(self.gpu)
    flowbox.add(self.mem)
    flowbox.add(self.swap)
    flowbox.add(self.disks)
    flowbox.add(self.lIP)
    flowbox.add(self.batt)
    flowbox.add(self.pwr)
    flowbox.add(self.local)
    flowbox.add(self.cblocks)

    fastfetch.get_checkboxes(self)

    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label21 = Gtk.Label()
    label21.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_fastfetch_all_selection)
    btn_normal_selection = Gtk.Button(label="Normal")
    btn_normal_selection.connect("clicked", self.on_click_fastfetch_normal_selection)
    btn_small_selection = Gtk.Button(label="Small")
    btn_small_selection.connect("clicked", self.on_click_fastfetch_small_selection)
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect("clicked", self.on_click_fastfetch_none_selection)
    hbox21.pack_start(label21, False, False, 10)
    hbox21.pack_end(btn_none_selection, False, False, 10)
    hbox21.pack_end(btn_small_selection, False, False, 10)
    hbox21.pack_end(btn_normal_selection, False, False, 10)
    hbox21.pack_end(btn_all_selection, False, False, 10)

    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9_label = Gtk.Label(xalign=0)
    hbox9_label.set_markup(
        "<b>Distro specific:  </b>" + fn.change_distro_label(fn.distr)
    )
    hbox9.pack_start(hbox9_label, False, False, 10)

    hbox28 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label28 = Gtk.Label()
    label28.set_text(
        "AmOS is using a personalized fastfetch application\n\
Switch to the default fastfetch to use this tab"
    )
    hbox28.pack_start(label28, False, False, 10)

    hbox29 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label29 = Gtk.Label()
    label29.set_text(
        "Archcraft is using a personalized fastfetch configuration\n\
Switch to the default fastfetch to use this tab - delete the ~/.config/fastfetch/config.conf"
    )
    hbox29.pack_start(label29, False, False, 10)

    # hbox22.pack_start(self.w3m, True, False, 10)
    hbox22.pack_end(self.off, True, False, 10)
    hbox22.pack_end(self.asci, True, False, 10)

    self.hbox26.pack_start(self.distro_ascii, True, False, 10)
    self.hbox26.pack_start(self.big_ascii, True, False, 10)
    self.hbox26.pack_start(self.small_ascii, True, False, 10)

    hbox25.pack_start(flowbox, True, True, 10)

    hbox27.pack_start(fast_util_label, False, False, 10)
    hbox27.pack_start(self.fast_util, False, False, 30)
    hbox27.pack_start(lolcat_label, False, False, 0)
    hbox27.pack_start(self.fast_lolcat, False, False, 30)

    hbox24.pack_start(installfastfetch, False, False, 0)
    hbox24.pack_start(useattfastfetch, False, False, 0)
    hbox24.pack_end(applyfastfetch, False, False, 0)
    hbox24.pack_end(resetnormalfastfetch, False, False, 0)

    vboxstack8.pack_start(hbox3, False, False, 0)
    vboxstack8.pack_start(hbox4, False, False, 0)
    vboxstack8.pack_start(hbox23, False, False, 0)
    vboxstack8.pack_start(hbox27, False, False, 0)
    vboxstack8.pack_start(hbox22, False, False, 0)
    vboxstack8.pack_start(self.hbox26, False, False, 0)
    vboxstack8.pack_start(hbox25, False, False, 0)
    vboxstack8.pack_start(hbox21, False, False, 0)

    if fn.distr == "amos":
        vboxstack8.pack_start(hbox9, False, False, 0)
        vboxstack8.pack_start(hbox28, False, False, 0)

    if fn.distr == "archcraft":
        vboxstack8.pack_start(hbox9, False, False, 0)
        vboxstack8.pack_start(hbox29, False, False, 0)

    vboxstack8.pack_end(hbox24, False, False, 0)

    if backend == "ascii":
        self.asci.set_active(True)
        self.big_ascii.set_sensitive(True)
        self.small_ascii.set_sensitive(True)
    elif backend == "off":
        self.off.set_active(True)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)
    else:
        # self.w3m.set_active(True)
        self.big_ascii.set_sensitive(False)
        self.small_ascii.set_sensitive(False)

    if asci == "auto":
        self.big_ascii.set_active(True)
