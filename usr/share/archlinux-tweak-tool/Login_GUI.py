#=================================================================
#=                  Author: Erik Dubois                          =
#=================================================================

def GUI(self, Gtk, GdkPixbuf, vboxStack22, sddm, lightdm, os, Functions):

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_lbl = Gtk.Label(xalign=0)
    hbox1_lbl.set_markup("Login Managers")
    hbox1_lbl.set_name("title")
    hbox1.pack_start(hbox1_lbl, False, False, 10)

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox0.pack_start(hseparator, True, True, 0)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)

    if Functions.check_package_installed("sddm"):

        # ==================================================================
        #                       SDDM
        # ==================================================================

        hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox4_lbl = Gtk.Label(xalign=0)
        hbox4_lbl.set_text("Sddm (inactive)")
        if Functions.check_content("sddm", "/etc/systemd/system/display-manager.service"):
            hbox4_lbl.set_text("Sddm (active)")
        hbox4_lbl.set_name("title")
        hbox4_lbl.set_name("title")
        hbox4.pack_start(hbox4_lbl, False, False, 0)

        hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox5.pack_start(hseparator, True, True, 0)

        # ==================================================================

        hbox14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label_sddm_config = Gtk.Label(xalign=0)
        label_sddm_config.set_text("We recommend to use the default sddm configuration setup\nSddm configuration \
split into two files : /etc/sddm.conf and /etc/sddm.conf.d/kde_settings.conf\n\
We will backup your files")
        hbox14.pack_start(label_sddm_config, False, False, 10)

        hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        reset_sddm_original_att = Gtk.Button(label="Apply the Sddm configuration from ATT - autoreboot")
        reset_sddm_original_att.set_size_request(100,60)
        reset_sddm_original_att.connect("clicked", self.on_click_sddm_reset_original_att)
        reset_sddm_original = Gtk.Button(label="Apply your original Sddm configuration - autoreboot")
        reset_sddm_original.set_size_request(100,60)
        reset_sddm_original.connect("clicked", self.on_click_sddm_reset_original)
        hbox13.pack_start(reset_sddm_original_att, False, False, 10)
        hbox13.pack_start(reset_sddm_original, False, False, 10)

        hbox05 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox05.pack_start(hseparator, True, True, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox_lbl = Gtk.Label(xalign=0)
        hbox_lbl.set_markup("Autologin")
        self.autologin_sddm = Gtk.Switch()
        self.autologin_sddm.connect("notify::active", self.on_autologin_sddm_activated)
        hbox.pack_start(hbox_lbl, False, False, 10)
        hbox.pack_end(self.autologin_sddm, False, False, 10)

        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox3_lbl = Gtk.Label(xalign=0)
        hbox3_lbl.set_text("Choose the desktop you want to autologin to")
        hbox3.pack_start(hbox3_lbl, False, False, 10)

        hbox18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox18_lbl = Gtk.Label(xalign=0)
        hbox18_lbl.set_markup("Desktop session")
        self.sessions_sddm = Gtk.ComboBoxText()
        sddm.pop_box(self, self.sessions_sddm)
        hbox18.pack_start(hbox18_lbl, False, False, 10)
        hbox18.pack_end(self.sessions_sddm, False, False, 10)

        hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox9_lbl = Gtk.Label(xalign=0)
        hbox9_lbl.set_text("Theme")
        self.theme_sddm = Gtk.ComboBoxText()
        sddm.pop_theme_box(self, self.theme_sddm)
        hbox9.pack_start(hbox9_lbl, False, False, 10)
        hbox9.pack_end(self.theme_sddm, False, False, 10)

        hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        install_sddm_themes = Gtk.Button(label="Install missing ArcoLinux Sddm Themes")
        install_sddm_themes.connect("clicked", self.on_click_install_sddm_themes)
        remove_sddm_themes = Gtk.Button(label="Remove the ArcoLinux Sddm Themes")
        remove_sddm_themes.connect("clicked", self.on_click_remove_sddm_themes)
        hbox11.pack_start(install_sddm_themes, False, False, 10)
        hbox11.pack_end(remove_sddm_themes, False, False, 10)

        hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        install_bibata_cursor = Gtk.Button(label="Install Bibata cursor")
        install_bibata_cursor.connect("clicked", self.on_click_install_bibata_cursor)
        remove_bibata_cursor = Gtk.Button(label="Remove Bibata cursor")
        remove_bibata_cursor.connect("clicked", self.on_click_remove_bibata_cursor)
        hbox16.pack_start(install_bibata_cursor, False, False, 10)
        hbox16.pack_end(remove_bibata_cursor, False, False, 10)

        hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox12_lbl = Gtk.Label(xalign=0)
        hbox12_lbl.set_text("Keep the default ArcoLinux theme")
        self.keep_default_theme = Gtk.Switch()
        hbox12.pack_end(self.keep_default_theme, False, False, 10)
        hbox12.pack_end(hbox12_lbl, False, False, 10)

        hbox17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox17_lbl = Gtk.Label(xalign=0)
        hbox17_lbl.set_text("Type your cursor theme for the login screen e.g. Bibata-Modern-Ice")
        hbox17.pack_start(hbox17_lbl, False, False, 10)

        hbox15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox15_lbl = Gtk.Label(xalign=0)
        hbox15_lbl.set_text("Cursor theme")
        self.cbt_cursor_themes = Gtk.ComboBoxText()
        sddm.pop_cursor_box(self, self.cbt_cursor_themes)
        hbox15.pack_start(hbox15_lbl, False, False, 10)
        hbox15.pack_start(self.cbt_cursor_themes, True, True, 10)

        #reset_sddm = Gtk.Button(label="Apply your backup of sddm.conf")
        #reset_sddm.connect("clicked", self.on_click_sddm_reset)

        # ======================================================================
        #                              BOTTOM
        # ======================================================================

        hbox90 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        enable_sddm = Gtk.Button(label="Enable Sddm")
        enable_sddm.connect("clicked", self.on_click_sddm_enable)
        btnRefreshAtt = Gtk.Button(label="Refresh the list of Sddm themes")
        btnRefreshAtt.connect('clicked', self.on_refresh_att_clicked)
        apply_sddm_settings = Gtk.Button(label="Apply settings")
        apply_sddm_settings.connect("clicked", self.on_click_sddm_apply)
        hbox90.pack_end(apply_sddm_settings, False, False, 0)
        hbox90.pack_end(btnRefreshAtt, False, False, 0)
        hbox90.pack_start(enable_sddm, False, False, 10)

        # ======================================================================
        #                              PACK TO STACK
        # ======================================================================

        vboxStack1.pack_start(hbox4, False, False, 0)
        vboxStack1.pack_start(hbox5, False, False, 0)
        vboxStack1.pack_start(hbox14, False, False, 0)
        vboxStack1.pack_start(hbox13, False, False, 0)
        vboxStack1.pack_start(hbox05, False, False, 0)

        if Functions.os.path.isfile(Functions.sddm_default_d2):
            vboxStack1.pack_start(hbox, False, False, 0)
            vboxStack1.pack_start(hbox3, False, False, 0)
            vboxStack1.pack_start(hbox18, False, False, 0)
            vboxStack1.pack_start(hbox9, False, False, 0)
            vboxStack1.pack_start(hbox11, False, False, 0)
            vboxStack1.pack_start(hbox12, False, False, 0)
            vboxStack1.pack_start(hbox16, False, False, 0)
            vboxStack1.pack_start(hbox17, False, False, 0)
            vboxStack1.pack_start(hbox15, False, False, 0)
            vboxStack1.pack_end(hbox90, False, False, 0)

    else:
        #no sddm installed
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox31_lbl = Gtk.Label(xalign=0)
        hbox31_lbl.set_text("Sddm is not installed")
        hbox31_lbl.set_name("title")
        hbox31.pack_start(hbox31_lbl, False, False, 0)

        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)

        ls = Gtk.Label()
        ls.set_markup("<b>Sddm does not seem to be installed</b>")
        install_sddm = Gtk.Button(label="Install Sddm - autoreboot - do not forget to enable it")
        install_sddm.connect("clicked", self.on_click_att_sddm_clicked)

        vboxStack1.pack_start(hbox31, False, False, 0)
        vboxStack1.pack_start(hbox41, False, False, 0)
        vboxStack1.pack_start(ls, False, False, 0)
        vboxStack1.pack_start(install_sddm, False, False, 0)

    # ==================================================================
    #                       LIGHTDM
    # ==================================================================

    if Functions.check_package_installed("lightdm"):

        hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox19_lbl = Gtk.Label(xalign=0)
        hbox19_lbl.set_text("Lightdm (inactive)")
        if Functions.check_content("lightdm", "/etc/systemd/system/display-manager.service"):
            hbox19_lbl.set_text("Lightdm (active)")
        if Functions.check_content("lightdm", "/etc/systemd/system/display-manager.service") and \
            Functions.check_content("slick-greeter", "/etc/lightdm/lightdm.conf"):
            hbox19_lbl.set_text("Lightdm + slick-greeter (active)")
        hbox19_lbl.set_name("title")
        hbox19.pack_start(hbox19_lbl, False, False, 0)

        hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox20.pack_start(hseparator, True, True, 0)

        hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox21_lbl = Gtk.Label(xalign=0)
        hbox21_lbl.set_text("Autologin")
        self.autologin = Gtk.Switch()
        self.autologin.connect("notify::active", self.on_autologin_activated)
        hbox21.pack_start(hbox21_lbl, False, False, 10)
        hbox21.pack_end(self.autologin, False, False, 10)

        hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox22_lbl = Gtk.Label(xalign=0)
        hbox22_lbl.set_text("Choose the desktop you want to autologin to")
        hbox22.pack_start(hbox22_lbl, False, False, 10)

        hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox23_lbl = Gtk.Label(xalign=0)
        hbox23_lbl.set_text("Use the ATT lightdm-gtk-greeter config")
        btn_install_arco_lightdm_greeter = Gtk.Button(label="Set ATT config")
        btn_install_arco_lightdm_greeter.connect ("clicked", self.on_click_install_arco_lightdmgreeter)
        btn_reset_lightdm_greeter = Gtk.Button(label="Reset back to original config")
        btn_reset_lightdm_greeter.connect ("clicked", self.on_click_reset_lightdm_greeter)
        hbox23.pack_start(hbox23_lbl, False, False, 10)
        hbox23.pack_end(btn_reset_lightdm_greeter, False, False, 10)
        hbox23.pack_end(btn_install_arco_lightdm_greeter, False, False, 10)

        hbox27 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox27_lbl = Gtk.Label(xalign=0)
        hbox27_lbl.set_text("Desktop session")
        self.sessions = Gtk.ComboBoxText()
        lightdm.pop_box(self, self.sessions)
        hbox27.pack_start(hbox27_lbl, False, False, 10)
        hbox27.pack_end(self.sessions, True, True, 10)

        hbox24 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox24_lbl = Gtk.Label(xalign=0)
        hbox24_lbl.set_text("You can change more settings with the lightdm-gtk-greeter-settings app")
        hbox24.pack_start(hbox24_lbl, False, False, 10)

        hbox25 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox25_label = Gtk.Label(xalign=0)
        if Functions.check_content("slick-greeter", "/etc/lightdm/lightdm.conf"):
            hbox25_label.set_text("Slickgreeter is active")
        else:
            hbox25_label.set_text("Slickgreeter is inactive")
        hbox25.pack_start(hbox25_label, False, False, 10)

        hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        enable_lightdm = Gtk.Button(label="Enable Lightdm")
        enable_lightdm.connect("clicked", self.on_click_lightdm_enable)
        enable_slick = Gtk.Button(label="Install and Enable or Disable Lightdm Slickgreeter")
        enable_slick.connect("clicked", self.on_click_lightdm_slick)
        apply = Gtk.Button(label="Apply settings")
        apply.connect("clicked", self.on_click_lightdm_apply)
        reset = Gtk.Button(label="Reset lightdm.conf")
        reset.connect("clicked", self.on_click_lightdm_reset)
        hbox26.pack_end(apply, False, False, 0)
        hbox26.pack_end(reset, False, False, 0)
        hbox26.pack_end(enable_slick, False, False, 10)
        hbox26.pack_start(enable_lightdm, False, False, 0)

        vboxStack2.pack_start(hbox19, False, False, 0)
        vboxStack2.pack_start(hbox20, False, False, 0)
        vboxStack2.pack_start(hbox22, False, False, 0)
        vboxStack2.pack_start(hbox21, False, False, 0)
        vboxStack2.pack_start(hbox27, False, False, 0)
        vboxStack2.pack_start(hbox23, False, False, 0)
        vboxStack2.pack_start(hbox24, False, False, 0)
        vboxStack2.pack_start(hbox25, False, False, 0)
        vboxStack2.pack_end(hbox26, False, False, 0)

    else:
       #no lightdm installed
        hbox32 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox32_lbl = Gtk.Label(xalign=0)
        hbox32_lbl.set_text("Lightdm is not installed")
        hbox32_lbl.set_name("title")
        hbox32.pack_start(hbox32_lbl, False, False, 0)

        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)

        vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vboxStack2.pack_start(hbox32, False, False, 0)
        vboxStack2.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("<b>Lightdm does not seem to be installed</b>")

        install_lightdm = Gtk.Button(label="Install Lightdm and enable it - autoreboot")
        install_lightdm.connect("clicked", self.on_click_att_lightdm_clicked)

        vboxStack2.pack_start(ls, False, False, 0)
        vboxStack2.pack_start(install_lightdm, False, False, 0)

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================
    if not Functions.distr == "manjaro":
        stack.add_titled(vboxStack1, "stack1", "SDDM")
    stack.add_titled(vboxStack2, "stack2", "LIGHTDM")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack22.pack_start(hbox1, False, False, 0)
    vboxStack22.pack_start(hbox0, False, False, 0)
    vboxStack22.pack_start(vbox, True, True, 0)
