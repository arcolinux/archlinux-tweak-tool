#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================
import distro,os

def GUI(self, Gtk, vboxStack14, Functions):

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_label = Gtk.Label(xalign=0)
    hbox1_label.set_text("Services")
    hbox1_label.set_name("title")
    hbox1.pack_start(hbox1_label, False, False, 10)

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox0.pack_start(hseparator, True, True, 0)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)

    # ==================================================================
    #                       SAMBA TAB
    # ==================================================================

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2_label = Gtk.Label(xalign=0)
    hbox2_label.set_text("Discover other computers in your network (to access other computers)")
    button_install_discovery = Gtk.Button(label="Install network discovery")
    button_install_discovery.connect ("clicked", self.on_install_discovery_clicked)
    button_remove_discovery = Gtk.Button(label="Uninstall network discovery")
    button_remove_discovery.connect ("clicked", self.on_remove_discovery_clicked)
    hbox2.pack_start(hbox2_label, False, False, 10)
    hbox2.pack_end(button_remove_discovery, False, False, 10)
    hbox2.pack_end(button_install_discovery, False, False, 10)

    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3_label = Gtk.Label(xalign=0)
    hbox3_label.set_text("Change the /etc/nsswitch.conf to connect to computers/NAS")
    self.nsswitch_choices = Gtk.ComboBoxText()
    options = ['ArcoLinux', 'Garuda', 'Arch Linux', 'EndeavourOS']
    for option in options:
        self.nsswitch_choices.append_text(option)
    self.nsswitch_choices.set_active(0)
    button_apply_nsswitch = Gtk.Button(label="Apply selected nsswitch.conf")
    button_apply_nsswitch.connect ("clicked", self.on_click_apply_nsswitch)
    button_reset_nsswitch = Gtk.Button(label="Reset to default nsswitch")
    button_reset_nsswitch.connect ("clicked", self.on_click_reset_nsswitch)
    hbox3.pack_start(hbox3_label, False, False, 10)

    hbox3.pack_end(button_reset_nsswitch, False, False, 10)
    hbox3.pack_end(button_apply_nsswitch, False, False, 10)
    hbox3.pack_end(self.nsswitch_choices, False, False, 10)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4_label = Gtk.Label(xalign=0)
    hbox4_label.set_text("Install the samba server - sharing with other computers")
    self.samba_choices = Gtk.ComboBoxText()
    options_samba = ['ArcoLinux', 'Example', 'Original']
    for option in options_samba:
        self.samba_choices.append_text(option)
    self.samba_choices.set_active(0)
    button_apply_samba = Gtk.Button(label="Apply selected samba.conf")
    button_apply_samba.connect ("clicked", self.on_click_apply_samba)
    button_reset_samba = Gtk.Button(label="Reset to default samba.conf")
    button_reset_samba.connect ("clicked", self.on_click_reset_samba)
    button_uninstall_samba = Gtk.Button(label="Uninstall Samba")
    button_uninstall_samba.connect ("clicked", self.on_click_uninstall_samba)
    button_install_samba = Gtk.Button(label="Install Samba")
    button_install_samba.connect ("clicked", self.on_click_install_samba)
    hbox4.pack_start(hbox4_label, False, False, 10)
    hbox4.pack_start(self.samba_choices, True, False,10)
    hbox4.pack_start(button_apply_samba, True, False, 10)
    hbox4.pack_end(button_reset_samba, False, False, 10)
    hbox4.pack_end(button_uninstall_samba, False, False, 10)
    hbox4.pack_end(button_install_samba, False, False, 10)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5_label = Gtk.Label(xalign=0)
    hbox5_label.set_text("After installing Samba you need to create an account to be able to access the Samba server")
    hbox5.pack_start(hbox5_label, False, False, 10)

    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6_label = Gtk.Label(xalign=0)
    hbox6_label.set_text("Fill in the username and password")
    self.entry_username = Gtk.Entry()
    self.entry_password = Gtk.Entry()
    self.entry_password.set_visibility(False)
    button_create_samba_user = Gtk.Button(label="Create Samba user")
    button_create_samba_user.connect ("clicked", self.on_click_create_samba_user)
    hbox6.pack_start(hbox6_label, False, False, 10)
    hbox6.pack_start(self.entry_username, False, False, 10)
    hbox6.pack_start(self.entry_password, False, False, 10)
    hbox6.pack_end(button_create_samba_user, False, False, 10)

    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7_label = Gtk.Label(xalign=0)
    hbox7_label.set_text("A terminal will open upon creating a new Samba user\nNow type the password the user will need to access Samba")
    hbox7.pack_start(hbox7_label, False, False, 10)

    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8_label = Gtk.Label(xalign=0)
    hbox8_label.set_text("Remove the selected Samba user")
    button_delete_samba_user = Gtk.Button(label="Remove the selected user from Samba")
    button_delete_samba_user.connect ("clicked", self.on_click_delete_samba_user)
    button_delete_user = Gtk.Button(label="Remove the selected user completely")
    button_delete_user.connect ("clicked", self.on_click_delete_user)
    self.samba_users = Gtk.ComboBoxText()
    samba_users= []
    samba_users = Functions.list_users("/etc/passwd")
    for user in samba_users:
        self.samba_users.append_text(user)
    self.samba_users.set_active(0)
    hbox8.pack_start(hbox8_label, False, False, 10)
    hbox8.pack_start(self.samba_users, False, False, 10)
    hbox8.pack_end(button_delete_user, False, False, 10)
    hbox8.pack_end(button_delete_samba_user, False, False, 10)

    # hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox9_label = Gtk.Label(xalign=0)
    # hbox9_label.set_markup("<b>Distro specific:  </b>" + Functions.change_distro_label(distro.id()))
    # hbox9.pack_start(hbox9_label, False, False, 10)

    # hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox10_label = Gtk.Label(xalign=0)
    # hbox10_label.set_markup("<b>For any Arch Linux based system</b>")
    # hbox10.pack_start(hbox10_label, False, False, 10)

    hbox91 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox91_label = Gtk.Label(xalign=0)
    hbox91_label.set_text("With the Avahi daemon (network discovery) running on both the server and client,\nthe file manager on the client should automatically find the server- Beware of firewalls")
    hbox91.pack_start(hbox91_label, False, False,10)

    hbox92 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox92_label = Gtk.Label(xalign=0)
    hbox92_label.set_markup("<span foreground=\"red\" size=\"large\">We found a firewall on your system</span>")
    hbox92.pack_start(hbox92_label, False, False,10)

    hbox93 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox93_label = Gtk.Label(xalign=0)

    status1 = Functions.check_service("smb")
    if status1 == True:
        status1 = "active"
    else:
        status1 = "inactive"

    status2 = Functions.check_service("nmb")
    if status2 == True:
        status2 = "active"
    else:
        status2 = "inactive"

    status3 = Functions.check_service("avahi-daemon")
    if status3 == True:
        status3 = "active"
    else:
        status3 = "inactive"

    hbox93_label.set_text("Samba : " + status1 + "   Nmb : " + status2 + "   Avahi : " + status3)
    hbox93.pack_start(hbox93_label, False, False,10)

    vboxStack1.pack_start(hbox2, False, False, 10)
    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_start(hbox4, False, False, 0)
    vboxStack1.pack_start(hbox5, False, False, 0)
    vboxStack1.pack_start(hbox6, False, False, 0)
    vboxStack1.pack_start(hbox7, False, False, 0)
    vboxStack1.pack_start(hbox8, False, False, 0)
    vboxStack1.pack_end(hbox91, False, False, 10)
    vboxStack1.pack_end(hbox93, False, False, 10)
    if Functions.check_service("firewalld"):
        vboxStack1.pack_end(hbox92, False, False, 10)



    # ==================================================================
    #                       PRINTING TAB
    # ==================================================================

    # ==================================================================
    #                       BLUETOOTH TAB
    # ==================================================================

    # ==================================================================
    #                       AUDIO TAB
    # ==================================================================

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================

    stack.add_titled(vboxStack1, "stack1", "Samba")
    stack.add_titled(vboxStack2, "stack2", "Printing")
    stack.add_titled(vboxStack3, "stack3", "Bluetooth")
    stack.add_titled(vboxStack4, "stack4", "Audio")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack14.pack_start(hbox1, False, False, 0)
    vboxStack14.pack_start(hbox0, False, False, 0)
    vboxStack14.pack_start(vbox, True, True, 0)

    # ======================================================================
    #                       VBOX STACK
    # ======================================================================

    # vboxStack14.pack_start(hbox1, False, False, 0)
    # vboxStack14.pack_start(hbox0, False, False, 0)
    # vboxStack14.pack_start(hbox10, False, False, 20) # title for any arch linux based system
    # vboxStack14.pack_start(hbox2, False, False, 0)
    # vboxStack14.pack_start(hbox3, False, False, 0)
    # vboxStack14.pack_start(hbox4, False, False, 0)

    #vboxStack14.pack_start(hbox7, False, False, 0)
    #vboxStack14.pack_start(hbox8, False, False, 0)
    #vboxStack14.pack_start(hbox9, False, False, 20)
    #if Functions.distr == "arcolinux":
    #    vboxStack14.pack_start(hbox5, False, False, 0)
        #vboxStack19.pack_start(hbox6, False, False, 0)
