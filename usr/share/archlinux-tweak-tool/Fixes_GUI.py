#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================
import distro,os

def GUI(self, Gtk, GdkPixbuf, vboxStack19, sddm, Functions):

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_label = Gtk.Label(xalign=0)
    hbox1_label.set_text("Fixes")
    hbox1_label.set_name("title")
    hbox1.pack_start(hbox1_label, False, False, 10)

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox0.pack_start(hseparator, True, True, 0)

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2_label = Gtk.Label(xalign=0)
    hbox2_label.set_text("Reset and reload pacman keys")
    button_Apply_Pacman_Key_Fix = Gtk.Button(label="Fix keys")
    button_Apply_Pacman_Key_Fix.connect ("clicked", self.on_click_fix_pacman_keys)
    hbox2.pack_start(hbox2_label, False, False, 10)
    hbox2.pack_end(button_Apply_Pacman_Key_Fix, False, False, 10)

    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3_label = Gtk.Label(xalign=0)
    hbox3_label.set_text("Set the mainstream servers from ArchLinux")
    button_Apply_Osbeck = Gtk.Button(label="Set mainstream")
    button_Apply_Osbeck.connect ("clicked", self.on_click_fix_mainstream)
    button_reset_mirrorlist = Gtk.Button(label="Reset mirrorlist")
    button_reset_mirrorlist.connect ("clicked", self.on_click_reset_mirrorlist)
    hbox3.pack_start(hbox3_label, False, False, 10)
    hbox3.pack_end(button_reset_mirrorlist, False, False, 10)
    if not Functions.distr == "manjaro":
        hbox3.pack_end(button_Apply_Osbeck, False, False, 10)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4_label = Gtk.Label(xalign=0)
    hbox4_label.set_text("Get the best Arch Linux servers (takes a while)")
    button_Apply_Mirrors = Gtk.Button(label="Get Arch mirrors (reflector)")
    button_Apply_Mirrors.connect ("clicked", self.on_click_get_arch_mirrors)
    button_Apply_Mirrors2 = Gtk.Button(label="Get Arch mirrors (rate-mirrors)")
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

    vboxStack19.pack_start(hbox1, False, False, 0)
    vboxStack19.pack_start(hbox0, False, False, 0)
    vboxStack19.pack_start(hbox10, False, False, 20)
    vboxStack19.pack_start(hbox2, False, False, 0)
    vboxStack19.pack_start(hbox3, False, False, 0)
    if not Functions.distr == "manjaro":
        vboxStack19.pack_start(hbox4, False, False, 0)
    vboxStack19.pack_start(hbox7, False, False, 0)
    vboxStack19.pack_start(hbox8, False, False, 0)
    vboxStack19.pack_start(hbox9, False, False, 20)
    if Functions.distr == "arcolinux":
        vboxStack19.pack_start(hbox5, False, False, 0)
        #vboxStack19.pack_start(hbox6, False, False, 0)
