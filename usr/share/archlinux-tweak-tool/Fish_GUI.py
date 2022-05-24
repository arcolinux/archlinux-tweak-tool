#      #============================================================
#      #=        Authors: Erik Dubois - Cameron Percival           =
#      #============================================================

def GUI(self, Gtk, vboxStack2, fish, base_dir, GdkPixbuf,Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    if Functions.get_shell() == "fish":

        lbl1.set_text("Fish (active)")
    else:
        lbl1.set_text("Fish (not active)")

    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                     FISH
    # ==========================================================

    label01 = Gtk.Label()
    if Functions.check_package_installed("fish"):
        label01.set_text("Install Fish (already installed)")
    else:
        label01.set_text("Install Fish (not installed)")
    hbox01 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox01.pack_start(label01, False, False, 10)

    self.fish = Gtk.Button("Install Fish")
    hbox01.pack_end(self.fish, False, False, 10)
    self.fish.connect("clicked", self.on_install_fish_clicked)

    # ==========================================================
    #                     FISH OH-MY-FISh
    # ==========================================================

    label02 = Gtk.Label()
    if Functions.check_package_installed("arcolinux-fish-git"):
        label02.set_text("ArcoLinux fish incl. oh-my-fish, themes and plugins (already installed)")
    else:
        label02.set_text("ArcoLinux fish incl. oh-my-fish, themes and plugins (not installed)")

    hbox02 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox02.pack_start(label02, False, False, 10)

    self.arcolinux_fish = Gtk.Button("Install the ArcoLinux Fish configuration")
    hbox02.pack_end(self.arcolinux_fish, False, False, 10)
    self.arcolinux_fish.connect("clicked", self.on_arcolinux_fish_clicked)

    # ==========================================================
    #                     BUTTONS
    # ==========================================================

    label13 = Gtk.Label()
    label13.set_text("If you just switched shell, log-out first.\nRestart your terminal to apply the new Fish theme\n\
\nYou will find scripts in your ~/.config/fish \
folder to install oh-my-fish, theme and plugins\n\
if you installed the ArcoLinux Fish configuration")
    label13.set_margin_top(30)
    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox21.pack_start(label13, False, False, 10)

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    tobash = Gtk.Button(label="Apply bash")
    tobash.connect("clicked", self.tobash_apply)
    tozsh = Gtk.Button(label="Apply zsh")
    tozsh.connect("clicked", self.tozsh_apply)
    tofish = Gtk.Button(label="Apply fish")
    tofish.connect("clicked", self.tofish_apply)
    removefish = Gtk.Button(label="Remove all Fish related packages")
    removefish.connect("clicked", self.on_remove_fish)
    termreset = Gtk.Button(label="Reset fish")
    termreset.connect("clicked", self.on_fish_reset)

    hbox20.pack_start(tofish, False, False, 0)
    hbox20.pack_start(tobash, False, False, 0)
    hbox20.pack_start(tozsh, False, False, 0)
    hbox20.pack_end(removefish, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)

    # ==========================================================
    #                     VBOXSTACK
    # ==========================================================

    vboxStack2.pack_start(hbox3, False, False, 0)  # Combobox
    vboxStack2.pack_start(hbox4, False, False, 0)  # Combobox
    vboxStack2.pack_start(hbox01, False, False, 0)  # fish
    vboxStack2.pack_start(hbox02, False, False, 0)  # oh-my-fish

    vboxStack2.pack_start(hbox21, False, False, 0)  # image
    vboxStack2.pack_end(hbox20, False, False, 0)  # Buttons

