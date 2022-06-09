# =================================================================
# =            Author: Brad Heffernan - Erik Dubois
# =================================================================

def GUI(self, Gtk, vboxStack1, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Pacman Config Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ========================================================
    #               FOOTER
    # ========================================================

    self.button1 = Gtk.Button(label="Apply custom repo")
    self.button1.connect('clicked', self.button1_clicked)
    reset_pacman_local = Gtk.Button(label="Reset pacman local")
    reset_pacman_local.connect("clicked", self.reset_pacman_local)
    reset_pacman_online = Gtk.Button(label="Reset pacman online")
    reset_pacman_online.connect("clicked", self.reset_pacman_online)
    blank_pacman = Gtk.Button(label="Blank pacman (autoreboot) and select")
    blank_pacman.connect("clicked", self.blank_pacman)
    label_backup = Gtk.Label(xalign=0)
    label_backup.set_text("You can find the backup at /etc/pacman.conf.bak")

    # ==========================================================
    #                   GLOBALS
    # ==========================================================

    hboxStack1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    #hboxStack10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    # ========================================================
    #               ARCO REPOS
    # ========================================================

    frame3 = Gtk.Frame(label="")
    frame3lbl = frame3.get_label_widget()
    frame3lbl.set_markup("<b>ArcoLinux repos</b>")

    self.atestrepo_button = Gtk.Switch()
    self.atestrepo_button.connect("notify::active", self.on_pacman_atestrepo_toggle)
    label1 = Gtk.Label(xalign=0)
    label1.set_markup("# Enable ArcoLinux testing repo")

    self.arcolinux_button = Gtk.Button(label="Install keys and mirrors")
    self.arcolinux_button.connect("clicked", self.on_arcolinux_clicked)

    self.arepo_button = Gtk.Switch()
    self.arepo_button.connect("notify::active", self.on_pacman_arepo_toggle)
    label5 = Gtk.Label(xalign=0)
    label5.set_markup("Enable ArcoLinux repo")

    self.a3prepo_button = Gtk.Switch()
    self.a3prepo_button.connect("notify::active", self.on_pacman_a3p_toggle)
    label6 = Gtk.Label(xalign=0)
    label6.set_markup("Enable ArcoLinux 3rd-party repo")

    self.axlrepo_button = Gtk.Switch()
    self.axlrepo_button.connect("notify::active", self.on_pacman_axl_toggle)
    label7 = Gtk.Label(xalign=0)
    label7.set_markup("Enable ArcoLinux x-large repo")

    # ========================================================
    #               ARCHLINUX REPOS
    # ========================================================

    frame = Gtk.Frame(label="")
    framelbl = frame.get_label_widget()
    framelbl.set_markup("<b>Arch Linux repos</b>")

    self.checkbutton2 = Gtk.Switch()
    self.checkbutton2.connect("notify::active", self.on_pacman_toggle1)
    label3 = Gtk.Label(xalign=0)
    label3.set_markup("# Enable Arch Linux testing repo")

    self.checkbutton6 = Gtk.Switch()
    self.checkbutton6.connect("notify::active", self.on_pacman_toggle2)
    label13 = Gtk.Label(xalign=0)
    label13.set_markup("Enable Arch Linux core repo")

    self.checkbutton7 = Gtk.Switch()
    self.checkbutton7.connect("notify::active", self.on_pacman_toggle3)
    label14 = Gtk.Label(xalign=0)
    label14.set_markup("Enable Arch Linux extra repo")

    self.checkbutton4 = Gtk.Switch()
    self.checkbutton4.connect("notify::active", self.on_pacman_toggle4)
    label10 = Gtk.Label(xalign=0)
    label10.set_markup("# Enable Arch Linux community testing repo")

    self.checkbutton5 = Gtk.Switch()
    self.checkbutton5.connect("notify::active", self.on_pacman_toggle5)
    label12 = Gtk.Label(xalign=0)
    label12.set_markup("Enable Arch Linux community repo")

    self.checkbutton3 = Gtk.Switch()
    self.checkbutton3.connect("notify::active", self.on_pacman_toggle6)
    label4 = Gtk.Label(xalign=0)
    label4.set_markup("# Enable Arch Linux multilib testing repo")

    self.checkbutton8 = Gtk.Switch()
    self.checkbutton8.connect("notify::active", self.on_pacman_toggle7)
    label15 = Gtk.Label(xalign=0)
    label15.set_markup("Enable Arch Linux multilib repo")

    # ========================================================
    #               OTHER REPOS
    # ========================================================

    frame2 = Gtk.Frame(label="")
    frame2lbl = frame2.get_label_widget()
    frame2lbl.set_markup("<b>Other repos</b>")

    self.endeavouros_button = Gtk.Button(label="Install keys and mirrors")
    self.endeavouros_button.connect("clicked", self.on_endeavouros_clicked)
    self.endeavouros_switch = Gtk.Switch()
    self.endeavouros_switch.connect("notify::active", self.on_endeavouros_toggle)
    label16 = Gtk.Label(xalign=0)
    label16.set_markup("Enable Endeavour repo")

    self.nemesis_switch = Gtk.Switch()
    self.nemesis_switch.connect("notify::active", self.on_nemesis_toggle)
    label11 = Gtk.Label(xalign=0)
    label11.set_markup("Enable Nemesis repo")

    self.xerolinux_button = Gtk.Button(label="Install mirrors")
    self.xerolinux_button.connect("clicked", self.on_xerolinux_clicked)

    self.xerolinux_switch = Gtk.Switch()
    self.xerolinux_switch.connect("notify::active", self.on_xero_toggle)
    label17 = Gtk.Label(xalign=0)
    label17.set_markup("Enable Xerolinux repo")

    self.xerolinux_xl_switch = Gtk.Switch()
    self.xerolinux_xl_switch.connect("notify::active", self.on_xero_xl_toggle)
    label18 = Gtk.Label(xalign=0)
    label18.set_markup("Enable Xerolinux XL repo")

    self.xerolinux_nv_switch = Gtk.Switch()
    self.xerolinux_nv_switch.connect("notify::active", self.on_xero_nv_toggle)
    label19 = Gtk.Label(xalign=0)
    label19.set_markup("Enable Xerolinux Nvidia repo")

    self.chaotics_button = Gtk.Button(label="Install keys and mirrors")
    self.chaotics_button.connect("clicked", self.on_chaotics_clicked)
    self.chaotics_switch = Gtk.Switch()
    self.chaotics_switch.connect("notify::active", self.on_chaotics_toggle)
    label9 = Gtk.Label(xalign=0)
    label9.set_markup("Enable Chaotics repo - set as last repo")

    # ========================================================
    #               CUSTOM REPOS
    # ========================================================

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

    # ========================================================
    #               ARCO REPOS PACKING
    # ========================================================
    if not Functions.check_package_installed("arcolinux-keyring"):
        hboxStack7.pack_start(label5, False, True, 10)
        hboxStack7.pack_end(self.arcolinux_button, False, True, 10)

    if Functions.check_package_installed("arcolinux-keyring"):
        hboxStack18.pack_start(label1, False, True, 10)
        hboxStack18.pack_end(self.atestrepo_button, False, False, 10)
        hboxStack7.pack_start(label5, False, True, 10)
        hboxStack7.pack_end(self.arepo_button, False, False, 10)
        hboxStack8.pack_start(label6, False, True, 10)
        hboxStack8.pack_end(self.a3prepo_button, False, False, 10)
        hboxStack9.pack_start(label7, False, True, 10)
        hboxStack9.pack_end(self.axlrepo_button, False, False, 10)

    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vboxStack2.pack_start(hboxStack1, False, False, 10)

    # ========================================================
    #               TESTING REPOS PACKING
    # ========================================================

    hboxStack5.pack_start(label3, False, True, 10)
    hboxStack5.pack_end(self.checkbutton2, False, False, 10)
    hboxStack15.pack_start(label13, False, True, 10)
    hboxStack15.pack_end(self.checkbutton6, False, False, 10)
    hboxStack16.pack_start(label14, False, True, 10)
    hboxStack16.pack_end(self.checkbutton7, False, False, 10)
    hboxStack12.pack_start(label10, False, True, 10)
    hboxStack12.pack_end(self.checkbutton4, False, False, 10)
    hboxStack14.pack_start(label12, False, True, 10)
    hboxStack14.pack_end(self.checkbutton5, False, False, 10)
    hboxStack6.pack_start(label4, False, True, 10)
    hboxStack6.pack_end(self.checkbutton3, False, False, 10)
    hboxStack17.pack_start(label15, False, True, 10)
    hboxStack17.pack_end(self.checkbutton8, False, False, 10)

    # ========================================================
    #               OTHER REPOS PACKING
    # ========================================================

    if not Functions.check_package_installed("endeavouros-keyring"):
        hboxStack19.pack_start(label16, False, True, 10)
        hboxStack19.pack_end(self.endeavouros_button, False, False, 10)

    if Functions.check_package_installed("endeavouros-keyring"):
        hboxStack19.pack_start(label16, False, True, 10)
        hboxStack19.pack_end(self.endeavouros_switch, False, False, 10)

    hboxStack13.pack_start(label11, False, True, 10)
    hboxStack13.pack_end(self.nemesis_switch, False, False, 10)

    if not Functions.check_package_installed("xerolinux-mirrorlist"):
        hboxStack20.pack_start(label17, False, True, 10)
        hboxStack20.pack_end(self.xerolinux_button, False, True, 10)

    if Functions.check_package_installed("xerolinux-mirrorlist"):
        hboxStack20.pack_start(label17, False, True, 10)
        hboxStack20.pack_end(self.xerolinux_switch, False, False, 10)

        hboxStack21.pack_start(label18, False, True, 10)
        hboxStack21.pack_end(self.xerolinux_xl_switch, False, False, 10)

        hboxStack22.pack_start(label19, False, True, 10)
        hboxStack22.pack_end(self.xerolinux_nv_switch, False, False, 10)

    if not Functions.check_package_installed("chaotic-keyring"):
        hboxStack11.pack_start(label9, False, True, 10)
        hboxStack11.pack_end(self.chaotics_button, False, False, 10)

    if Functions.check_package_installed("chaotic-keyring"):
        hboxStack11.pack_start(label9, False, True, 10)
        hboxStack11.pack_end(self.chaotics_switch, False, False, 10)

    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vboxStack4.pack_start(hboxStack13, False, False, 10)
    vboxStack4.pack_start(hboxStack19, False, False, 10)
    vboxStack4.pack_start(hboxStack20, False, False, 10)
    if Functions.check_package_installed("xerolinux-mirrorlist"):
        vboxStack4.pack_start(hboxStack21, False, False, 10)
        vboxStack4.pack_start(hboxStack22, False, False, 10)
    vboxStack4.pack_start(hboxStack11, False, False, 10)

    # ========================================================
    #               CUSTOM REPOS PACKING
    # ========================================================

    hboxStack2.pack_start(label2, False, True, 10)
    hboxStack3.pack_start(sw, True, True, 10)

    # ========================================================
    #               BUTTONS PACKING
    # ========================================================

    #hboxStack4.pack_end(self.button1, False, False, 0)
    hboxStack4.pack_end(reset_pacman_local, False, False, 0)
    hboxStack4.pack_end(reset_pacman_online, False, False, 0)
    hboxStack4.pack_end(blank_pacman, False, False, 0)
    #hboxStack4.pack_start(label_backup, False, False, 0)

    # ========================================================
    #               TESTING REPOS PACKING TO FRAME
    # ========================================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.pack_start(hboxStack5, False, False, 0)
    vbox.pack_start(hboxStack15, False, False, 0)
    vbox.pack_start(hboxStack16, False, False, 0)
    vbox.pack_start(hboxStack12, False, False, 0)
    vbox.pack_start(hboxStack14, False, False, 0)
    vbox.pack_start(hboxStack6, False, False,0)
    vbox.pack_start(hboxStack17, False, False,0)
    frame.add(vbox)

    # ========================================================
    #               OTHER REPOS PACKING TO FRAME
    # ========================================================

    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vbox2.pack_start(hboxStack10, False, False, 0)
    vbox2.pack_start(vboxStack4, False, False, 0)
    frame2.add(vbox2)

    # ========================================================
    #               OTHER REPOS PACKING TO FRAME
    # ========================================================

    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox3.pack_start(hboxStack18, False, False, 0)
    vbox3.pack_start(hboxStack7, False, False, 0)
    vbox3.pack_start(hboxStack8, False, False, 0)
    vbox3.pack_start(hboxStack9, False, False, 0)

    frame3.add(vbox3)
    # ========================================================
    #               PACK TO WINDOW
    # ========================================================

    # =================ARCO REPO========================

    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_start(hbox4, False, False, 0)
    vboxStack1.pack_start(frame3, False, False, 5)

    # =================TESTING REPO========================

    vboxStack1.pack_start(frame, False, False, 0)

    # =================OTHER REPO========================

    vboxStack1.pack_start(frame2, False, False, 0)

    # =================CUSTOM REPO========================

    #vboxStack1.pack_start(hboxStack2, False, False, 0)
    #vboxStack1.pack_start(hboxStack3, True, True, 0)

    # =================FOOTER========================

    vboxStack1.pack_end(hboxStack4, False, False, 0)
