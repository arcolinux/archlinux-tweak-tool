# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions):  # noqa

    # ============================================
    #                   STACKS
    # ============================================

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)

    # =======================TAB #1=============================

    stack.add_titled(vboxStack1, "main_stack", "Main")

    label = Gtk.Label(xalign=0)
    label.set_markup("<big>Exclude file/folder from above selections</big>")

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

    # ============================================
    #                   TREE VIEW
    # ============================================

    self.browse = Gtk.Button(label="Add")
    self.browse.connect("clicked", self.on_browse_fixed)

    self.remove = Gtk.Button(label="Remove")
    self.remove.connect("clicked", self.on_remove_fixed)

    sw = Gtk.ScrolledWindow()
    sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.stores = Gtk.ListStore(str)

    self.treeView = Gtk.TreeView(self.stores)
    self.create_columns(self.treeView)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView.set_rules_hint(True)
    sw.set_size_request(270, 120)
    sw.add(self.treeView)

    # ============================================
    #              RADIO BUTTONS
    # ============================================

    self.rbutton3 = Gtk.RadioButton(label="File")
    self.rbutton4 = Gtk.RadioButton.new_from_widget(self.rbutton3)
    self.rbutton4.set_label("Folder")

    # ============================================
    #              BASHRC BUTTONS
    # ============================================

    self.bashrc = Gtk.Button(label="Upgrade .bashrc")
    self.bashrc.set_size_request(0, 50)
    self.bashrc.connect("clicked", self.on_bashrc_upgrade)

    # ============================================
    #                   FOOTER
    # ============================================

    labelBacks = Gtk.Label(xalign=0)
    labelBacks.set_markup("<b>Run backup before skel</b>")

    self.switch = Gtk.Switch()
    self.switch.set_active(True)

    self.btn2 = Gtk.Button(label="Run skel")
    self.btn2.connect("clicked", self.on_button_fetch_clicked)

    self.progressbar1 = Gtk.ProgressBar()
    self.label_info1 = Gtk.Label("Idle ...")

    # ==================TREEVIEW==================

    vbox1.pack_start(self.browse, False, False, 0)
    vbox1.pack_start(self.remove, False, False, 10)

    hbox.pack_start(sw, True, True, 10)
    hbox.pack_start(vbox1, False, False, 10)

    # ==================LABEL==================
    hbox3.pack_start(label, False, False, 0)

    # ==================RADIO BUTTONS==================

    hbox1.pack_end(self.rbutton4, False, False, 10)
    hbox1.pack_end(self.rbutton3, False, False, 10)

    # ==================BASHRC BUTTON==================

    hbox5.pack_start(self.bashrc, True, True, 10)

    # ==================FOOTER==================

    hbox2.pack_start(self.label_info1, False, False, 0)
    hbox2.pack_end(self.btn2, False, False, 0)

    hbox4.pack_start(labelBacks, False, False, 0)
    hbox4.pack_end(self.switch, False, False, 0)

    # ============================================
    #                   ADD TO WINDOW
    # ============================================
    vboxStack1.pack_start(hbox, False, False, 0)  # Treeview
    vboxStack1.pack_start(hbox1, False, False, 0)  # Radio Buttons

    # vboxStack1.pack_start(hbox3, False, False, 0)  # Label Under Construction

    vboxStack1.pack_start(hbox5, False, False, 0)  # Bashrc Button

    vboxStack1.pack_end(self.progressbar1, False, False, 0)  # Progressbar
    vboxStack1.pack_end(hbox2, False, False, 0)  # Skel button
    vboxStack1.pack_end(hbox4, False, False, 10)  # Backup Toggle

    # =======================TAB #2=============================

    stack.add_titled(vboxStack2, "backup_stack", "Backups")

    label1 = Gtk.Label()
    label1.set_markup("<big>Under construction!</big>")

    # ============================================
    #               PACKING BOXES
    # ============================================
    hbox4 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox5 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    vbox9 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox10 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    # hbox11 = Gtk.Box(
    #     orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox12 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox13 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox14 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    vbox11 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)

    # ============================================
    #                BACKUPS COMBOBOX
    # ============================================
    # ListRow 1 Elements
    self.backs = Gtk.ComboBoxText()

    skelapp.refresh(self)

    self.backs.set_active(0)
    self.backs.set_size_request(170, 0)
    self.btn4 = Gtk.Button(label="Refresh")
    self.btn5 = Gtk.Button(label="Delete")

    # ============================================
    #               SECOND ROW BUTTONS
    # ============================================
    self.btn12 = Gtk.Button(label="Run full backup")
    self.btn12.set_size_request(0, 80)
    self.btn9 = Gtk.Button(label="Delete all backups")

    # ============================================
    #               TREEVIEW
    # ============================================
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

    skelapp.refresh_inner(self)

    self.btn10 = Gtk.Button(label="Delete")
    self.btn11 = Gtk.Button(label="Restore")

    # ============================================
    #               BUTTONS CLICK EVENT
    # ============================================
    self.btn4.connect("clicked", self.on_refresh_clicked)  # Refresh Button
    self.btn5.connect("clicked", self.on_delete_clicked)  # Delete Combo Button
    self.btn9.connect("clicked", self.on_flush_clicked)  # Delete all Button
    self.btn12.connect("clicked", self.on_backup_clicked)  # RUN BACKUP Button
    self.btn10.connect("clicked", self.on_delete_inner_clicked)  # Delete Treeview Item Button # noqa
    self.btn11.connect("clicked", self.on_restore_inner_clicked)  # Restore Item button # noqa

    label4 = Gtk.Label(xalign=0)
    label4.set_markup("<b>Delete backups</b>")

    # ============================================
    #                FOOTER
    # ============================================
    self.progressbar = Gtk.ProgressBar()
    self.label_info = Gtk.Label("Idle ...")

    hbox5.pack_start(label4, True, True, 10)  # Delete Backups Label

    # =====================COMBO ROW==========================

    hbox4.pack_start(self.backs, True, True, 10)  # Backups Combobox
    hbox4.pack_start(self.btn4, False, False, 0)  # Refresh button
    hbox4.pack_end(self.btn5, True, True, 10)  # Delete Button

    # hbox11.pack_start(self.backs_inner, True, True, 0)

    # =====================TREEVIEW ROW==========================

    vbox11.pack_start(self.btn10, False, False, 0)  # Delete Treeview Item Button # noqa
    vbox11.pack_start(self.btn11, False, False, 10)  # Restore Item button

    hbox10.pack_start(sw2, True, True, 10)
    hbox10.pack_start(vbox11, False, False, 10)

    # =====================Buttons ROW==========================

    vbox9.pack_start(self.btn12, True, True, 0)  # RUN BACKUP Button
    vbox9.pack_start(self.btn9, True, True, 10)  # Delete all Button

    hbox12.pack_start(label1, True, True, 5)  # Under Construction Label

    # =====================FOOTER ROW==========================

    hbox13.pack_start(self.label_info, False, False, 5)
    hbox14.pack_start(self.progressbar, True, True, 5)

    # ============================================
    #                   ADD TO WINDOW
    # ============================================
    vboxStack2.pack_start(hbox5, False, False, 0)
    vboxStack2.pack_start(hbox4, False, False, 0)
    vboxStack2.pack_start(hbox10, False, False, 0)
    vboxStack2.pack_start(vbox9, False, False, 0)
    vboxStack2.pack_start(hbox12, False, False, 0)

    vboxStack2.pack_end(hbox14, False, False, 0)
    vboxStack2.pack_end(hbox13, False, False, 0)

    self.backs.connect("changed", self.backs_changed)

    # =======================ADD STACKS=============================

    vboxStack9.pack_start(stack_switcher, False, True, 0)
    vboxStack9.pack_start(stack, True, True, 0)

    # vboxStack9.pack_start(hbox1, False, False, 0)
    # vboxStack9.pack_start(hbox, False, False, 0)
