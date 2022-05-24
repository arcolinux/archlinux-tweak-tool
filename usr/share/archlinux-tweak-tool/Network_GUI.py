#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================
import distro,os

def GUI(self, Gtk, vboxStack14, Functions):

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_label = Gtk.Label(xalign=0)
    hbox1_label.set_text("Network")
    hbox1_label.set_name("title")
    hbox1.pack_start(hbox1_label, False, False, 10)

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox0.pack_start(hseparator, True, True, 0)

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2_label = Gtk.Label(xalign=0)
    hbox2_label.set_text("Discover other computers in your network")
    button_Apply_Pacman_Key_Fix = Gtk.Button(label="Install discovery")
    button_Apply_Pacman_Key_Fix.connect ("clicked", self.on_click_fix_pacman_keys)
    button_Apply_Pacman_Key_Fixu = Gtk.Button(label="Uninstall discovery")
    button_Apply_Pacman_Key_Fixu.connect ("clicked", self.on_click_fix_pacman_keys)
    hbox2.pack_start(hbox2_label, False, False, 10)
    hbox2.pack_end(button_Apply_Pacman_Key_Fixu, False, False, 10)
    hbox2.pack_end(button_Apply_Pacman_Key_Fix, False, False, 10)

    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3_label = Gtk.Label(xalign=0)
    hbox3_label.set_text("Change the /etc/nsswitch.conf to connect to computers/NAS")
    nsswitch_choices = Gtk.ComboBoxText()
    options = ['ArcoLinux', 'Garuda', 'Arch Linux', 'EndeavourOS']
    for option in options:
        nsswitch_choices.append_text(option)
    nsswitch_choices.set_active(0)
    button_Apply_Osbeck = Gtk.Button(label="Apply selected nsswitch")
    button_Apply_Osbeck.connect ("clicked", self.on_click_fix_mainstream)
    button_Apply_Osbeckr = Gtk.Button(label="Reset to default nsswitch")
    button_Apply_Osbeckr.connect ("clicked", self.on_click_fix_mainstream)
    hbox3.pack_start(hbox3_label, False, False, 10)

    hbox3.pack_end(button_Apply_Osbeckr, False, False, 10)
    hbox3.pack_end(button_Apply_Osbeck, False, False, 10)
    hbox3.pack_end(nsswitch_choices, False, False, 10)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4_label = Gtk.Label(xalign=0)
    hbox4_label.set_text("Install the samba server - sharing with other computers")
    button_Apply_Mirrors = Gtk.Button(label="Uninstall Samba")
    button_Apply_Mirrors.connect ("clicked", self.on_click_get_arch_mirrors)
    button_Apply_Mirrors2 = Gtk.Button(label="Install Samba")
    button_Apply_Mirrors2.connect ("clicked", self.on_click_get_arch_mirrors2)
    hbox4.pack_start(hbox4_label, False, False, 10)
    hbox4.pack_end(button_Apply_Mirrors, False, False, 10)
    hbox4.pack_end(button_Apply_Mirrors2, False, False, 10)

    if not os.path.exists("/usr/bin/reflector"):
        button_Apply_Mirrors.set_sensitive(False)
    if not os.path.exists("/usr/bin/rate-mirrors"):
        button_Apply_Mirrors2.set_sensitive(False)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5_label = Gtk.Label(xalign=0)
    hbox5_label.set_text("Get the original ArcoLinux /etc/sddm.conf and /etc/sddm.conf.d/kde_settings.conf")
    button_Apply_Mirrors = Gtk.Button(label="Reset sddm.conf")
    button_Apply_Mirrors.connect ("clicked", self.on_click_fix_sddm_conf)
    hbox5.pack_start(hbox5_label, False, False, 10)
    hbox5.pack_end(button_Apply_Mirrors, False, False, 10)

    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6_label = Gtk.Label(xalign=0)
    hbox6_label.set_text("Get the original ArcoLinux /etc/pacman.conf")
    button_Apply_Pacman_Conf = Gtk.Button(label="Reset pacman.conf")
    button_Apply_Pacman_Conf.connect ("clicked", self.on_click_fix_pacman_conf)
    hbox6.pack_start(hbox6_label, False, False, 10)
    hbox6.pack_end(button_Apply_Pacman_Conf, False, False, 10)

    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7_label = Gtk.Label(xalign=0)
    hbox7_label.set_text("Get the best keyservers for /etc/pacman.d/gnupg/gpg.conf")
    button_Apply_Pacman_Gpg_Conf = Gtk.Button(label="Backup and reset gpg.conf")
    button_Apply_Pacman_Gpg_Conf.connect ("clicked", self.on_click_fix_pacman_gpg_conf)
    hbox7.pack_start(hbox7_label, False, False, 10)
    hbox7.pack_end(button_Apply_Pacman_Gpg_Conf, False, False, 10)

    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8_label = Gtk.Label(xalign=0)
    hbox8_label.set_text("Get the best keyservers for ~/.gnupg/gpg.conf")
    button_Apply_Pacman_Gpg_Conf_Local = Gtk.Button(label="Backup and reset gpg.conf")
    button_Apply_Pacman_Gpg_Conf_Local.connect ("clicked", self.on_click_fix_pacman_gpg_conf_local)
    hbox8.pack_start(hbox8_label, False, False, 10)
    hbox8.pack_end(button_Apply_Pacman_Gpg_Conf_Local, False, False, 10)

    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9_label = Gtk.Label(xalign=0)
    hbox9_label.set_markup("<b>Distro specific:  </b>" + Functions.change_distro_label(distro.id()))
    hbox9.pack_start(hbox9_label, False, False, 10)

    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10_label = Gtk.Label(xalign=0)
    hbox10_label.set_markup("<b>For any Arch Linux based system</b>")
    hbox10.pack_start(hbox10_label, False, False, 10)

    # ======================================================================
    #                       VBOX STACK
    # ======================================================================

    vboxStack14.pack_start(hbox1, False, False, 0)
    vboxStack14.pack_start(hbox0, False, False, 0)
    vboxStack14.pack_start(hbox10, False, False, 20) # title for any arch linux based system
    vboxStack14.pack_start(hbox2, False, False, 0)
    vboxStack14.pack_start(hbox3, False, False, 0)
    vboxStack14.pack_start(hbox4, False, False, 0)
    #vboxStack14.pack_start(hbox7, False, False, 0)
    #vboxStack14.pack_start(hbox8, False, False, 0)
    #vboxStack14.pack_start(hbox9, False, False, 20)
    #if Functions.distr == "arcolinux":
    #    vboxStack14.pack_start(hbox5, False, False, 0)
        #vboxStack19.pack_start(hbox6, False, False, 0)