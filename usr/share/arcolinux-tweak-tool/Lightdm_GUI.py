#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, lightdm, Functions):
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label(xalign=0)
    label.set_text("Autologin")
    
    label1 = Gtk.Label(xalign=0)
    label1.set_text("Desktop session")
        
    self.autologin = Gtk.Switch()

    self.sessions = Gtk.ComboBoxText()

    if "#" in lightdm.check_lightdm(lightdm.get_lines(Functions.lightdm_conf),"autologin-user="):
        self.autologin.set_active(False)
    else:
        self.autologin.set_active(True)

    lightdm.pop_box(self, self.sessions)


    apply = Gtk.Button(label="Apply Settings")
    apply.connect("clicked", self.on_click_lightdm_apply)
    reset = Gtk.Button(label="Reset")
    reset.connect("clicked", self.on_click_lightdm_reset)


    hbox.pack_start(label, False, False, 10)
    hbox.pack_end(self.autologin, False, False, 10)

    hbox1.pack_start(label1, False, False, 10)
    hbox1.pack_end(self.sessions, True, True, 10)

    hbox2.pack_end(apply, False, False, 0)
    hbox2.pack_end(reset, False, False, 0)    

    vboxStack10.pack_start(hbox, False, False, 0)
    vboxStack10.pack_start(hbox1, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
