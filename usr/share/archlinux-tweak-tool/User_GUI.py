#=================================================================
#=         Author: Erik Dubois and Cameron Percival              =
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

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    sep_text = "                       "

    label_name = Gtk.Label(xalign=0)
    label_name.set_text("    Name")
    name_sep = Gtk.Label(xalign=0)
    name_sep.set_text(sep_text)

    label_username = Gtk.Label(xalign=0)
    label_username.set_text("    Username")
    uname_sep = Gtk.Label(xalign=0)
    uname_sep.set_text(sep_text)

    label_account_type = Gtk.Label(xalign=0)
    label_account_type.set_text("    Account type")
    account_sep = Gtk.Label(xalign=0)
    account_sep.set_text(sep_text)

    label_password = Gtk.Label(xalign=0)
    label_password.set_text("    Password")
    pwd_sep = Gtk.Label(xalign=0)
    pwd_sep.set_text(sep_text)

    label_confirm_password = Gtk.Label(xalign=0)
    label_confirm_password.set_text("    Confirm password")
    conf_pwd_sep = Gtk.Label(xalign=0)
    conf_pwd_sep.set_text(sep_text)

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

    grid = Gtk.Grid()
    grid.attach(label_username, 0, 0, 2, 1)
    grid.attach_next_to(uname_sep, label_username, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach_next_to(self.hbox_username, uname_sep, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach(label_name, 0, 2, 2, 1)
    grid.attach_next_to(name_sep, label_name, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach_next_to(self.hbox_name, name_sep, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach(label_account_type, 0 , 4, 2, 1)
    grid.attach_next_to(account_sep, label_account_type, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach_next_to(self.combo_account_type, account_sep, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach(label_password, 0, 6, 2, 1)
    grid.attach_next_to(pwd_sep, label_password, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach_next_to(self.hbox_password, pwd_sep, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach(label_confirm_password, 0, 8, 2, 1)
    grid.attach_next_to(conf_pwd_sep, label_confirm_password, Gtk.PositionType.RIGHT, 1, 1)
    grid.attach_next_to(self.hbox_confirm_password, conf_pwd_sep, Gtk.PositionType.RIGHT, 1, 1)

    hbox2.pack_end(apply_sddm, False, False, 0)

    vboxStack10.pack_start(hbox4, False, False, 0)
    vboxStack10.pack_start(hbox5, False, False, 0)
    vboxStack10.pack_start(grid, False, False, 0)
    vboxStack10.pack_start(hbox9, False, False, 0)
    vboxStack10.pack_start(hbox10, False, False, 0)
    vboxStack10.pack_start(hbox11, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
