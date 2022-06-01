#      #============================================================
#      #= Authors: Brad Heffernan - Erik Dubois - Cameron Percival =
#      #============================================================
import os
import Functions

def GUI(self, Gtk, vboxStack15, zsh_themes, base_dir, GdkPixbuf):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("ZSH Themes")

    if Functions.get_shell() == "zsh":
        lbl1.set_text("ZSH THEMES (Zsh active)")
    else:
        lbl1.set_text("ZSH THEMES (Zsh not active)")

    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                     ZSH THEMES
    # ==========================================================

    label12 = Gtk.Label()
    label12.set_text("Zsh themes")
    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox19.pack_start(label12, False, False, 10)

    self.zsh_themes = Gtk.ComboBoxText()
    zsh_themes.get_themes(self.zsh_themes)
    hbox19.pack_start(self.zsh_themes, True, True, 10)

    label13 = Gtk.Label()
    label13.set_text("Restart your terminal to apply the new Zsh theme\nIf you switch shell, log-out first")
    label13.set_margin_top(30)
    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox21.pack_start(label13, False, False, 10)

    tobash = Gtk.Button(label="Apply bash")
    tozsh = Gtk.Button(label="Apply zsh")
    tofish = Gtk.Button(label="Apply fish")
    install_oh_my_zsh = Gtk.Button(label="Install oh-my-zsh")
    #hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    tobash.connect("clicked", self.tobash_apply)
    tozsh.connect("clicked", self.tozsh_apply)
    tofish.connect("clicked", self.tofish_apply)
    install_oh_my_zsh.connect("clicked", self.install_oh_my_zsh)

    termset = Gtk.Button(label="Apply Zsh theme")
    termreset = Gtk.Button(label="Reset or create ~/.zshrc")

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox20.pack_start(tozsh, False, False, 0)
    hbox20.pack_start(tobash, False, False, 0)
    hbox20.pack_start(tofish, False, False, 0)
    hbox20.pack_end(termset, False, False, 0)
    hbox20.pack_end(termreset, False, False, 0)
    hbox20.pack_end(install_oh_my_zsh, False, False, 0)

    termset.connect("clicked", self.on_zsh_apply_theme)
    termreset.connect("clicked", self.on_zsh_reset)

    if not zsh_themes.check_oh_my():
        termset.set_sensitive(False)

    #image dimensions - this will (in time) allow the image changing function to be re-usable by other parts of the app
    image_width = 600
    image_height = 480
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/zsh-sample.jpg", image_width, image_height)
    if self.zsh_themes.get_active_text() is None:
        pass
    elif Functions.os.path.isfile(base_dir+"/images/zsh_previews/"+self.zsh_themes.get_active_text()+".jpg"):
        pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/zsh_previews/"+self.zsh_themes.get_active_text()+".jpg", image_width, image_height)
    image = Gtk.Image().new_from_pixbuf(pixbuf)
    image.set_margin_top(30)

    self.zsh_themes.connect("changed", self.update_image, image, "zsh", base_dir, image_width, image_height)

    vboxStack15.pack_start(hbox3, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox4, False, False, 0)  # Combobox
    vboxStack15.pack_start(hbox19, False, False, 0)  # Combobox
    vboxStack15.pack_start(image, False, False, 0)  # image
    vboxStack15.pack_start(hbox21, False, False, 0)  # image
    vboxStack15.pack_end(hbox20, False, False, 0)  # Buttons

    if not zsh_themes.check_oh_my() or not os.path.isfile(Functions.zsh_config):
        termset.set_sensitive(False)
        termreset.set_sensitive(False)
    if not os.path.isfile(Functions.zsh_config):
        termreset.set_sensitive(True)
