# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

def GUI(self, Gtk, vboxStack1, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("ArcoLinux Mirrorlist")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    
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
    hboxStack10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    # ========================================================
    #               ARCO REPOS
    # ========================================================
    
    frame3 = Gtk.Frame(label="")
    frame3lbl = frame3.get_label_widget()
    frame3lbl.set_markup("<b>ArcoLinux Mirrorlist</b>")

    self.aseed_button = Gtk.Switch()
    self.aseed_button.connect("notify::active", self.on_mirror_seed_repo_toggle)
    label5 = Gtk.Label(xalign=0)
    label5.set_markup("Enable Seedhost repo - Do not enable it and save us bandwidth")
    hboxStack7.pack_start(label5, False, True, 10)
    hboxStack7.pack_end(self.aseed_button, False, False, 20)    

    # self.abelnet_button = Gtk.Switch()
    # self.abelnet_button.connect("notify::active", self.on_mirror_belnet_repo_toggle)
    # label6 = Gtk.Label(xalign=0)
    # label6.set_markup("Enable Belnet repo - free bandwidth")
    # hboxStack8.pack_start(label6, False, True, 10)
    # hboxStack8.pack_end(self.abelnet_button, False, False, 20)

    # self.agithub_button = Gtk.Switch()
    # self.agithub_button.connect("notify::active", self.on_mirror_github_repo_toggle)
    # label7 = Gtk.Label(xalign=0)
    # label7.set_markup("Enable Github repo - free bandwidth")
    # hboxStack9.pack_start(label7, False, True, 10)
    # hboxStack9.pack_end(self.agithub_button, False, False, 20)
    
    # ========================================================
    #               FOOTER
    # ========================================================

    reset_mirror = Gtk.Button(label="Reset ArcoLinux Mirrorlist")
    reset_mirror.connect("clicked", self.on_click_reset_arcolinux_mirrorlist)
    hboxStack4.pack_end(reset_mirror, False, False, 0)

    # ========================================================
    #               ARCOLINUX MIRRORS
    # ========================================================

    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox3.pack_start(hboxStack7, False, False, 10)
    #vbox3.pack_start(hboxStack8, False, False, 10)
    #vbox3.pack_start(hboxStack9, False, False, 10)
    frame3.add(vbox3)
    
    # ========================================================
    #               PACK TO WINDOW
    # ========================================================

    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_start(hbox4, False, False, 0)
    vboxStack1.pack_start(frame3, False, False, 10)
    vboxStack1.pack_end(hboxStack4, False, False, 0)
