#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, user, Functions):
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Create User")
    lbl1.set_name("title")
    hbox4.pack_start(lbl1, False, False, 0)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox5.pack_start(hseparator, True, True, 0)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    #hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    #hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10) 

    label_name = Gtk.Label(xalign=0)
    label_name.set_text("Name                       ")
    
    label_username = Gtk.Label(xalign=0)
    label_username.set_text("Username                ")

    label_account_type = Gtk.Label(xalign=0)
    label_account_type.set_text("Account type           ")

    label_password = Gtk.Label(xalign=0)
    label_password.set_text("Password                 ")

    label_confirm_password = Gtk.Label(xalign=0)
    label_confirm_password.set_text("Confirm password  ")

    label_empty1 = Gtk.Label(xalign=0)
    label_empty1.set_text("")
    
    label_empty2 = Gtk.Label(xalign=0)
    label_empty2.set_text("")
    
    label_empty3 = Gtk.Label(xalign=0)
    label_empty3.set_text("")
    
    self.hbox_username = Gtk.Entry()
    self.hbox_name = Gtk.Entry()
    self.hbox_password = Gtk.Entry()
    self.hbox_password.set_visibility(False)
    self.hbox_confirm_password = Gtk.Entry()
    self.hbox_confirm_password.set_visibility(False)

    self.combo_account_type = Gtk.ComboBoxText()
    
    for i in range(len(Functions.account_list)):
            self.combo_account_type.append_text(Functions.account_list[i])
    self.combo_account_type.set_active(1)

    apply_sddm = Gtk.Button(label="Apply settings")
    apply_sddm.connect("clicked", self.on_click_user_apply)
    

    hbox.pack_start(label_name, False, False, 10)
    hbox.pack_end(self.hbox_name, True, True, 10)

    hbox3.pack_start(label_username, False, False, 10)
    hbox3.pack_end(self.hbox_username, True, True, 10)

    hbox8.pack_start(label_account_type, False, False, 10)
    hbox8.pack_end(self.combo_account_type, False, False, 10)

    hbox1.pack_start(label_password, False, False, 10)
    hbox1.pack_end(self.hbox_password, True, True, 10)
    
    hbox6.pack_start(label_confirm_password, False, False, 10)
    hbox6.pack_end(self.hbox_confirm_password, True, True, 10)
    
    hbox7.pack_start(label_empty1, False, False, 10)
    
    hbox8.pack_start(label_empty2, False, False, 10)
    

    hbox2.pack_end(apply_sddm, False, False, 0)

    vboxStack10.pack_start(hbox4, False, False, 0)
    vboxStack10.pack_start(hbox5, False, False, 0)
    vboxStack10.pack_start(hbox3, False, False, 0)
    vboxStack10.pack_start(hbox, False, False, 0)
    #vboxStack10.pack_start(hbox7, False, False, 0)
    #vboxStack10.pack_start(hbox7, False, False, 0)
    vboxStack10.pack_start(hbox8, False, False, 0)
    vboxStack10.pack_start(hbox1, False, False, 0)
    vboxStack10.pack_start(hbox6, False, False, 0)
    vboxStack10.pack_start(hbox9, False, False, 0)
    vboxStack10.pack_start(hbox10, False, False, 0)
    vboxStack10.pack_start(hbox11, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
