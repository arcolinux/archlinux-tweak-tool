#      #============================================================
#      #=        Authors: Erik Dubois - Cameron Percival           =
#      #============================================================

def GUI(self, Gtk, vboxStack2, fish, base_dir, GdkPixbuf):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Fish")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                     FISH
    # ==========================================================

    label01 = Gtk.Label()
    label01.set_text("Install fish")
    hbox01 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox01.pack_start(label01, False, False, 10)

    self.fish = Gtk.Switch()
    hbox01.pack_end(self.fish, False, False, 10)
    self.fish.connect("notify::active", self.on_fish_toggle)

    # ==========================================================
    #                     FISH OH-MY-FISh
    # ==========================================================

    label02 = Gtk.Label()
    label02.set_text("Install oh-my-fish")
    hbox02 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox02.pack_start(label02, False, False, 10)

    self.ohmyfish = Gtk.Switch()
    hbox02.pack_end(self.ohmyfish, False, False, 10)
    self.ohmyfish.connect("notify::active", self.on_ohmyfish_toggle)

    # ==========================================================
    #                     BUTTONS
    # ==========================================================

    label13 = Gtk.Label()
    label13.set_text("Restart your terminal to apply the new Fish theme\nIf you switch shell, log-out first")
    label13.set_margin_top(30)
    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox21.pack_start(label13, False, False, 10)

    tobash = Gtk.Button(label="Apply bash")
    tofish = Gtk.Button(label="Apply ArcoLinux fish")
    #hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    tobash.connect("clicked", self.tobash_apply)
    tofish.connect("clicked", self.tofish_apply)

    termset = Gtk.Button(label="Apply Fish theme")
    termreset = Gtk.Button(label="Reset fish")

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox20.pack_start(tobash, False, False, 0)
    #hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)
    hbox20.pack_end(tofish, False, False, 0)

    #termset.connect("clicked", self.on_fish_apply)
    termreset.connect("clicked", self.on_fish_reset)

    # ==========================================================
    #                     VBOXSTACK
    # ==========================================================

    vboxStack2.pack_start(hbox3, False, False, 0)  # Combobox
    vboxStack2.pack_start(hbox4, False, False, 0)  # Combobox
    vboxStack2.pack_start(hbox01, False, False, 0)  # fish
    #vboxStack2.pack_start(hbox02, False, False, 0)  # oh-my-fish

    vboxStack2.pack_start(hbox21, False, False, 0)  # image
    vboxStack2.pack_end(hbox20, False, False, 0)  # Buttons

