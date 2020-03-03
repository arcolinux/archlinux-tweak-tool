# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack13, autostart, Functions, base_dir):
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)

    vbox5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
    vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)


    labelbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    # ==========================================
    #              TREEVIEW
    # ==========================================
    sw = Gtk.ScrolledWindow()
    sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.startups = Gtk.ListStore(str, str)

    self.treeView4 = Gtk.TreeView(self.startups)
    self.create_autostart_columns(self.treeView4)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView4.set_rules_hint(True)
    sw.set_size_request(270, 320)
    sw.add(self.treeView4)

    autostart.get_startups(self)

    # ==========================================
    #              Remove Button
    # ==========================================
    rbutton = Gtk.Button(label="Remove")
    rbutton.set_size_request(140, 0)

    rbutton.connect("clicked", self.on_remove_auto)
    # ==========================================
    #              Button
    # ==========================================
    lbl1 = Gtk.Label("Name")
    lbl2 = Gtk.Label("Command")
    lbl3 = Gtk.Label("Comment")


    self.txtbox1 = Gtk.Entry()  # Name
    self.txtbox2 = Gtk.Entry()  # EXEC
    self.txtbox3 = Gtk.Entry()  # Comment
    self.txtbox1.set_size_request(180, 0)
    self.txtbox2.set_size_request(180, 0)
    self.txtbox3.set_size_request(180, 0)

    bbutton = Gtk.Button(label="...")
    abutton = Gtk.Button(label="Add")
    abutton.set_size_request(140, 0)

    bbutton.connect("clicked", self.on_exec_browse)

    abutton.connect("clicked", self.on_add_autostart)

    vbox2.pack_start(lbl1, False, False, 0)
    vbox2.pack_start(self.txtbox1, False, False, 0)

    vbox3.pack_start(lbl2, False, False, 0)
    vbox3.pack_start(self.txtbox2, False, False, 0)

    vbox4.pack_start(lbl3, False, False, 0)
    vbox4.pack_start(self.txtbox3, False, False, 0)

    vbox5.pack_end(bbutton, False, False, 0)
    vbox6.pack_end(abutton, False, False, 0)

    hbox2.pack_start(vbox2, False, False, 5)
    hbox2.pack_start(vbox3, False, False, 0)
    hbox2.pack_start(vbox5, False, False, 0)
    hbox2.pack_start(vbox4, False, False, 5)
    hbox2.pack_start(vbox6, False, False, 5)

    hbox.pack_start(sw, True, True, 0)
    vbox1.pack_end(rbutton, False, False, 0)
    hbox.pack_start(vbox1, False, False, 0)
    vboxStack13.pack_start(hbox, False, False, 0)
    vboxStack13.pack_start(labelbox, False, False, 0)
    vboxStack13.pack_start(hbox2, False, False, 0)