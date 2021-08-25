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
    
    label25 = Gtk.Label()
    label25.set_text("Termite themes :\n     Use the button to install - select the theme here")
    hbox25 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
    hbox25.pack_start(label25, False, False, 10)   

    label21 = Gtk.Label()
    label21.set_text("Alacritty themes :\n     Use the button to install - Run 'alacritty-themes' in a terminal")
    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
    hbox21.pack_start(label21, False, False, 10)

    label22 = Gtk.Label()
    label22.set_text("Xfce4-terminal themes :\n     Use the button to install  - Change colors in Xfce4-terminal settings")
    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
    hbox22.pack_start(label22, False, False, 10)

    label23 = Gtk.Label()
    label23.set_text("Urxvt themes :\n     Change the settings of ~/.Xresources manually")
    hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
    hbox23.pack_start(label23, False, False, 10)        
    
    btn_alacritty_themes = Gtk.Button(label="Install Alacritty themes")
    btn_alacritty_themes.connect("clicked", self.on_clicked_install_alacritty_themes)
    hbox24 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox24.set_margin_top(30)    
    hbox24.pack_start(btn_alacritty_themes, False, False, 10)    

    btn_xfce4_terminal_themes = Gtk.Button(label="Install Xfce4-terminal themes")
    btn_xfce4_terminal_themes.connect("clicked", self.on_clicked_install_xfce4_themes)    
    hbox24.pack_start(btn_xfce4_terminal_themes, False, False, 10)

    btn_termite_terminal_themes = Gtk.Button(label="Install ArcoLinux Termite themes")
    btn_termite_terminal_themes.connect("clicked", self.on_clicked_install_termite_themes)    
    hbox24.pack_start(btn_termite_terminal_themes, False, False, 10)   
    
    label12 = Gtk.Label()
    label12.set_text("Choose your Termite theme")
    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox19.set_margin_top(30)    
    hbox19.pack_start(label12, False, False, 10)

    self.term_themes = Gtk.ComboBoxText()
    termite.get_themes(self.term_themes)    
    hbox19.pack_start(self.term_themes, True, True, 10)

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
    vboxStack7.pack_start(hbox22, False, False, 0) 
    vboxStack7.pack_start(hbox25, False, False, 0)
    vboxStack7.pack_start(hbox23, False, False, 0)
    vboxStack7.pack_start(hbox24, False, False, 0)
    vboxStack7.pack_start(hbox19, False, False, 0)  # Combobox
 #   vboxStack7.pack_start(image, False, False, 0)  # Image
    vboxStack7.pack_end(hbox20, False, False, 0)  # Buttons
