# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

# ==========================================================
#                     TERMINALS
# ==========================================================

def GUI(self, Gtk, vboxStack7, termite, GdkPixbuf, base_dir):
   hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
   hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
   lbl1 = Gtk.Label(xalign=0)
   lbl1.set_text("Terminals")
   lbl1.set_name("title")
   hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
   hbox4.pack_start(hseparator, True, True, 0)
   hbox3.pack_start(lbl1, False, False, 0)

   # label25 = Gtk.Label()
   # label25.set_text("Termite themes :\n     Use the button to install - Select the theme here")
   # hbox25 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   # hbox25.pack_start(label25, False, False, 10)

   label21 = Gtk.Label()
   label21.set_text("Use the buttons to install more themes then select your theme")
   hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox21.pack_start(label21, False, False, 10)

   label23 = Gtk.Label()
   label23.set_text("Urxvt themes - Change the settings of ~/.Xresources manually")
   hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox23.pack_start(label23, False, False, 10)

   btn_alacritty_themes = Gtk.Button(label="Install themes for Alacritty")
   btn_alacritty_themes.connect("clicked", self.on_clicked_install_alacritty_themes)
   hbox24 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox24.set_margin_top(30)
   hbox24.pack_start(btn_alacritty_themes, False, False, 10)

   btn_xfce4_terminal_themes = Gtk.Button(label="Install themes for Xfce4-terminal")
   btn_xfce4_terminal_themes.connect("clicked", self.on_clicked_install_xfce4_themes)
   hbox24.pack_start(btn_xfce4_terminal_themes, False, False, 10)

   btn_termite_terminal_themes = Gtk.Button(label="Install themes for Termite")
   btn_termite_terminal_themes.connect("clicked", self.on_clicked_install_termite_themes)
   hbox24.pack_start(btn_termite_terminal_themes, False, False, 10)

   label12 = Gtk.Label()
   label12.set_markup("Choose your <b>Termite</b> theme")
   hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox19.set_margin_top(30)
   hbox19.pack_start(label12, False, False, 10)

   self.term_themes = Gtk.ComboBoxText()
   termite.get_themes(self.term_themes)
   hbox19.pack_start(self.term_themes, True, True, 10)

   #Alacritty
   hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox26.set_margin_top(50)
   label26 = Gtk.Label()
   label26.set_markup("Choose your <b>Alcritty</b> theme - type <b>'alacritty-themes'</b> in the terminal")
   btn_set_arcolinux_alacritty_theme = Gtk.Button(label="Set ArcoLinux alacritty-theme")
   btn_set_arcolinux_alacritty_theme.connect("clicked", self.on_clicked_set_arcolinux_alacritty_theme)
   btn_reset_alacritty = Gtk.Button(label="Reset alacritty theme")
   btn_reset_alacritty.connect("clicked", self.on_clicked_reset_alacritty)
   hbox26.pack_start(label26, False, False, 10)
   hbox26.pack_start(btn_reset_alacritty, False, False, 10)
   hbox26.pack_start(btn_set_arcolinux_alacritty_theme, False, False, 10)

   #Xfce4-terminal
   hbox27 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
   hbox27.set_margin_top(30)
   label27 = Gtk.Label()
   label27.set_markup("Choose your <b>Xfce4-terminal</b> theme in the preferences, colors, presets of Xfce4-terminal")
   btn_choose_xfce4_theme = Gtk.Button(label="Reset xfce4-terminal theme")
   btn_choose_xfce4_theme.connect("clicked", self.on_clicked_reset_xfce4_terminal)
   hbox27.pack_start(label27, False, False, 10)
   hbox27.pack_start(btn_choose_xfce4_theme, False, False, 10)

   btnRefreshAtt = Gtk.Button(label="Refresh the list of the termite themes")
   btnRefreshAtt.connect('clicked', self.on_refresh_att_clicked)

   termreset = Gtk.Button(label="Reset Termite")
   termreset.connect("clicked", self.on_term_reset)

   termset = Gtk.Button(label="Apply Termite theme")
   termset.connect("clicked", self.on_term_apply)

   hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
   hbox20.pack_start(btnRefreshAtt, False, False, 0)
   hbox20.pack_end(termset, False, False, 0)
   hbox20.pack_end(termreset, False, False, 0)

   # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir + "/images/termite-sample.jpg", 645, 645)
   # image = Gtk.Image().new_from_pixbuf(pixbuf)

   vboxStack7.pack_start(hbox3, False, False, 0)  # lbl1
   vboxStack7.pack_start(hbox4, False, False, 0)  # seperator
   vboxStack7.pack_start(hbox21, False, False, 0)
   vboxStack7.pack_start(hbox23, False, False, 0)
   vboxStack7.pack_start(hbox24, False, False, 0)
   vboxStack7.pack_start(hbox26, False, False, 0)
   vboxStack7.pack_start(hbox27, False, False, 0)

   vboxStack7.pack_start(hbox19, False, False, 0)  # Combobox
   vboxStack7.pack_start(hbox20, False, False, 0)  # Buttons
