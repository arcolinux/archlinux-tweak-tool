#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack19, sddm, Functions):
         
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_label = Gtk.Label(xalign=0)
    hbox1_label.set_text("ArcoLinux Fixes")
    hbox1_label.set_name("title")
    hbox1.pack_start(hbox1_label, False, False, 10)

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2_label = Gtk.Label(xalign=0)
    hbox2_label.set_text("ArcoLinux fix pacman keys")   
    button_Apply_Pacman_Key_Fix = Gtk.Button(label="Fix keys")
    button_Apply_Pacman_Key_Fix.connect ("clicked", self.on_click_fix_pacman_keys)
    hbox2.pack_start(hbox2_label, False, False, 10)
    hbox2.pack_end(button_Apply_Pacman_Key_Fix, False, False, 10)
           
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3_label = Gtk.Label(xalign=0)
    hbox3_label.set_text("Set Osbeck as the only Arch Linux server")   
    button_Apply_Osbeck = Gtk.Button(label="Set Osbeck")
    button_Apply_Osbeck.connect ("clicked", self.on_click_fix_osbeck)
    hbox3.pack_start(hbox3_label, False, False, 10)
    hbox3.pack_end(button_Apply_Osbeck, False, False, 10)    
    
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4_label = Gtk.Label(xalign=0)
    hbox4_label.set_text("Get the best Arch Linux servers (takes a while)")   
    button_Apply_Mirrors = Gtk.Button(label="Get Arch mirrors")
    button_Apply_Mirrors.connect ("clicked", self.on_click_fix_mirrors)
    hbox4.pack_start(hbox4_label, False, False, 10)
    hbox4.pack_end(button_Apply_Mirrors, False, False, 10)        
    
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5_label = Gtk.Label(xalign=0)
    hbox5_label.set_text("Get the original ArcoLinux /etc/sddm.conf")   
    button_Apply_Mirrors = Gtk.Button(label="Reset the sddm.conf")
    button_Apply_Mirrors.connect ("clicked", self.on_click_fix_sddm_conf)
    hbox5.pack_start(hbox5_label, False, False, 10)
    hbox5.pack_end(button_Apply_Mirrors, False, False, 10) 
    
    # hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
     
    # hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    
    # hbox99 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # apply_sddm = Gtk.Button(label="Apply settings")
    # apply_sddm.connect("clicked", self.on_click_sddm_apply)
    
    # reset_sddm = Gtk.Button(label="Reset")
    # reset_sddm.connect("clicked", self.on_click_sddm_reset)    

    # hbox99.pack_end(apply_sddm, False, False, 0)
    # hbox99.pack_end(reset_sddm, False, False, 0)

    
    # ======================================================================
    #                       VBOX STACK 
    # ======================================================================
    vboxStack19.pack_start(hbox1, False, False, 0)
    vboxStack19.pack_start(hbox2, False, False, 0)
    vboxStack19.pack_start(hbox3, False, False, 0)
    vboxStack19.pack_start(hbox4, False, False, 0)
    vboxStack19.pack_start(hbox5, False, False, 0)
#    vboxStack19.pack_start(hbox6, False, False, 0)
#    vboxStack19.pack_start(hbox7, False, False, 0)
#    vboxStack19.pack_start(hbox8, False, False, 0)
#    vboxStack19.pack_start(hbox9, False, False, 0)
#    vboxStack19.pack_start(hbox10, False, False, 0)
#    vboxStack19.pack_start(hbox11, False, False, 0)
#    vboxStack19.pack_start(hbox12, False, False, 0)
#    vboxStack19.pack_start(hbox13, False, False, 0)
#    vboxStack19.pack_end(hbox99, False, False, 0)
