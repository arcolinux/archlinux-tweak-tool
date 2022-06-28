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
        install_bibata_cursor = Gtk.Button(label="Install Bibata cursors")
        install_bibata_cursor.connect("clicked", self.on_click_install_bibata_cursor)
        remove_bibata_cursor = Gtk.Button(label="Remove Bibata cursors")
        remove_bibata_cursor.connect("clicked", self.on_click_remove_bibata_cursor)
        hbox16.pack_start(install_bibata_cursor, False, False, 10)
        hbox16.pack_end(remove_bibata_cursor, False, False, 10)

        hbox28 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        install_bibata_cursorr = Gtk.Button(label="Install Bibata extra cursors")
        install_bibata_cursorr.connect("clicked", self.on_click_install_bibatar_cursor)
        remove_bibata_cursorr = Gtk.Button(label="Remove Bibata extra cursors")
        remove_bibata_cursorr.connect("clicked", self.on_click_remove_bibatar_cursor)
        hbox28.pack_start(install_bibata_cursorr, False, False, 10)
        hbox28.pack_end(remove_bibata_cursorr, False, False, 10)

        hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox12_lbl = Gtk.Label(xalign=0)
        hbox12_lbl.set_text("Keep the default ArcoLinux theme")
        self.keep_default_theme = Gtk.Switch()
        hbox12.pack_end(self.keep_default_theme, False, False, 10)
        hbox12.pack_end(hbox12_lbl, False, False, 10)

        hbox17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox17_lbl = Gtk.Label(xalign=0)
        hbox17_lbl.set_text("Select your cursor theme for the login screen e.g. Bibata-Modern-Ice")
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
            vboxStack1.pack_start(hbox28, False, False, 0)
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

        install_lightdm = Gtk.Button(label="Install Lightdm - autoreboot - do not forget to enable it")
        install_lightdm.connect("clicked", self.on_click_att_lightdm_clicked)

        vboxStack2.pack_start(ls, False, False, 0)
        vboxStack2.pack_start(install_lightdm, False, False, 0)

    # ==================================================================
    #                       LXDM
    # ==================================================================

    if Functions.check_package_installed("lxdm") or Functions.check_package_installed("lxdm-gtk3"):

        hbox50 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox50_lbl = Gtk.Label(xalign=0)
        hbox50_lbl.set_text("Lxdm (inactive)")
        if Functions.check_content("lxdm", "/etc/systemd/system/display-manager.service"):
            hbox50_lbl.set_text("Lxdm (active)")
        hbox50_lbl.set_name("title")
        hbox50.pack_start(hbox50_lbl, False, False, 0)

        hbox51 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox51.pack_start(hseparator, True, True, 0)

        # hbox52 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox52_lbl = Gtk.Label(xalign=0)
        # hbox52_lbl.set_text("Autologin")
        # self.autologin = Gtk.Switch()
        # self.autologin.connect("notify::active", self.on_autologin_activated)
        # hbox52.pack_start(hbox52_lbl, False, False, 10)
        # hbox52.pack_end(self.autologin, False, False, 10)

        # hbox53 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox53_lbl = Gtk.Label(xalign=0)
        # hbox53_lbl.set_text("Choose the desktop you want to autologin to")
        # hbox53.pack_start(hbox53_lbl, False, False, 10)

        # hbox54 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox54_lbl = Gtk.Label(xalign=0)
        # hbox54_lbl.set_text("Use the ATT lightdm-gtk-greeter config")
        # btn_install_arco_lightdm_greeter = Gtk.Button(label="Set ATT config")
        # btn_install_arco_lightdm_greeter.connect ("clicked", self.on_click_install_arco_lightdmgreeter)
        # btn_reset_lightdm_greeter = Gtk.Button(label="Reset back to original config")
        # btn_reset_lightdm_greeter.connect ("clicked", self.on_click_reset_lightdm_greeter)
        # hbox54.pack_start(hbox54_lbl, False, False, 10)
        # hbox54.pack_end(btn_reset_lightdm_greeter, False, False, 10)
        # hbox54.pack_end(btn_install_arco_lightdm_greeter, False, False, 10)

        # hbox55 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox55_lbl = Gtk.Label(xalign=0)
        # hbox55_lbl.set_text("Desktop session")
        # self.sessions = Gtk.ComboBoxText()
        # lightdm.pop_box(self, self.sessions)
        # hbox55.pack_start(hbox55_lbl, False, False, 10)
        # hbox55.pack_end(self.sessions, True, True, 10)

        # hbox56 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox56_lbl = Gtk.Label(xalign=0)
        # hbox56_lbl.set_text("You can change more settings with the lightdm-gtk-greeter-settings app")
        # hbox56.pack_start(hbox56_lbl, False, False, 10)

        # hbox57 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # hbox57_label = Gtk.Label(xalign=0)
        # if Functions.check_content("slick-greeter", "/etc/lightdm/lightdm.conf"):
        #     hbox57_label.set_text("Slickgreeter is active")
        # else:
        #     hbox57_label.set_text("Slickgreeter is inactive")
        # hbox57.pack_start(hbox57_label, False, False, 10)

        hbox58 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        enable_lxdm = Gtk.Button(label="Enable Lxdm")
        enable_lxdm.connect("clicked", self.on_click_lxdm_enable)
        # enable_slick = Gtk.Button(label="Install and Enable or Disable Lightdm Slickgreeter")
        # enable_slick.connect("clicked", self.on_click_lightdm_slick)
        # apply = Gtk.Button(label="Apply settings")
        # apply.connect("clicked", self.on_click_lightdm_apply)
        # reset = Gtk.Button(label="Reset lxdm.conf")
        # reset.connect("clicked", self.on_click_lightdm_reset)
        #hbox58.pack_end(apply, False, False, 0)
        #hbox58.pack_end(reset, False, False, 0)
        #hbox58.pack_end(enable_slick, False, False, 10)
        hbox58.pack_start(enable_lxdm, False, False, 0)

        vboxStack3.pack_start(hbox50, False, False, 0)
        vboxStack3.pack_start(hbox51, False, False, 0)
        # vboxStack3.pack_start(hbox52, False, False, 0)
        # vboxStack3.pack_start(hbox53, False, False, 0)
        # vboxStack3.pack_start(hbox55, False, False, 0)
        # vboxStack3.pack_start(hbox54, False, False, 0)
        # vboxStack3.pack_start(hbox56, False, False, 0)
        # vboxStack3.pack_start(hbox57, False, False, 0)
        vboxStack3.pack_end(hbox58, False, False, 0)

    else:
       #no lxdm installed
        hbox60 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox60_lbl = Gtk.Label(xalign=0)
        hbox60_lbl.set_text("Lxdm is not installed")
        hbox60_lbl.set_name("title")
        hbox60.pack_start(hbox60_lbl, False, False, 0)

        hbox61 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox61.pack_start(hseparator, True, True, 0)

        vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vboxStack3.pack_start(hbox60, False, False, 0)
        vboxStack3.pack_start(hbox61, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("<b>Lxdm does not seem to be installed</b>")

        install_lxdm = Gtk.Button(label="Install Lxdm - autoreboot - do not forget to enable it")
        install_lxdm.connect("clicked", self.on_click_install_lxdm)

        vboxStack3.pack_start(ls, False, False, 0)
        vboxStack3.pack_start(install_lxdm, False, False, 0)

    # ==================================================================
    #                       WALL
    # ==================================================================

    if Functions.check_package_installed("sddm"):

        hbox70 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox70_lbl = Gtk.Label(xalign=0)
        hbox70_lbl.set_text("Choose the background of your login manager")
        hbox70_lbl.set_name("title")
        hbox70.pack_start(hbox70_lbl, False, False, 0)

        hbox71 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox71.pack_start(hseparator, True, True, 0)

        hbox72 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox72_lbl = Gtk.Label(xalign=0)
        hbox72_lbl.set_text("Choose the login manager you want to change")
        hbox72.pack_start(hbox72_lbl, False, False, 10)

        hbox73 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox73_lbl = Gtk.Label(xalign=0)
        hbox73_lbl.set_text("Desktop session")
        self.login_managers_combo = Gtk.ComboBoxText()
        options = ['sddm', 'lightdm', 'lxdm']
        for option in options:
            self.login_managers_combo.append_text(option)
        self.login_managers_combo.set_active(0)
        hbox73.pack_start(hbox73_lbl, False, False, 10)
        hbox73.pack_end(self.login_managers_combo, True, True, 10)

        hbox111 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        label111 = Gtk.Label("Import image")
        self.login_image = Gtk.Entry()
        btnsearch = Gtk.Button(label=". . .")
        btnsearch.connect("clicked", self.on_choose_login_wallpaper)
        hbox111.pack_start(label111, False, False, 10)
        hbox111.pack_start(self.login_image, True, True, 10)
        hbox111.pack_start(btnsearch, False, False, 10)

        hbox113 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        label113 = Gtk.Label()
        if Functions.check_package_installed("archlinux-login-backgrounds-git"):
            label113.set_text("Install our selection of wallpapers (installed)")
        else:
            label113.set_text("Install our selection of wallpapers")
        btn_att_install = Gtk.Button(label="Install ATT backgrounds")
        btn_att_install.connect("clicked", self.on_install_att_backgrounds)
        btn_att_remove = Gtk.Button(label="Remove ATT backgrounds")
        btn_att_remove.connect("clicked", self.on_remove_att_backgrounds)
        hbox113.pack_end(btn_att_remove, False, False, 10)
        hbox113.pack_end(btn_att_install, False, False, 10)
        hbox113.pack_start(label113, False, True, 10)

        hbox112 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        btn_login_import = Gtk.Button(label="Import selected image")
        btn_login_import.connect("clicked", self.on_import_login_wallpaper)
        btn_remove_import = Gtk.Button(label="Remove selected image")
        btn_remove_import.connect("clicked", self.on_import_remove_login_wallpaper)
        hbox112.pack_end(btn_remove_import, False, False, 10)
        hbox112.pack_end(btn_login_import, False, False, 10)

        hbox115 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox115.pack_start(hseparator, True, True, 0)

        hbox114 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        label114 = Gtk.Label()
        label114.set_text("Select a wallpaper and apply")
        hbox114.pack_start(label114, False, True, 10)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        wallpaper_list = Functions.get_login_wallpapers()
        self.login_wallpapers_combo = Gtk.ComboBoxText()
        self.pop_login_wallpapers(self.login_wallpapers_combo, wallpaper_list, True)
        self.flowbox_wall.set_valign(Gtk.Align.START)
        self.flowbox_wall.set_max_children_per_line(6)
        self.flowbox_wall.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.flowbox_wall.connect("child-activated", self.on_login_wallpaper_clicked)
        scrolled.add(self.flowbox_wall)
        self.login_wallpapers_combo.connect("changed", self.on_login_wallpaper_change)


        hbox119 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        login_apply = Gtk.Button(label="Select and apply background")
        login_apply.connect("clicked", self.on_set_login_wallpaper)
        login_reset = Gtk.Button(label="Reset to the original background")
        login_reset.connect("clicked", self.on_reset_login_wallpaper)

        hbox119.pack_end(login_reset, False, False, 0)
        hbox119.pack_end(login_apply, False, False, 0)

        vboxStack4.pack_start(hbox70, False, False, 0)
        vboxStack4.pack_start(hbox71, False, False, 0)
        vboxStack4.pack_start(hbox113, False, False, 0)
        vboxStack4.pack_start(hbox72, False, False, 0)
        vboxStack4.pack_start(hbox73, False, False, 0)
        vboxStack4.pack_start(hbox111, False, False, 0)
        vboxStack4.pack_start(hbox112, False, False, 0)
        vboxStack4.pack_start(hbox114, False, False, 0)
        vboxStack4.pack_start(hbox115, False, False, 0)
        vboxStack4.pack_start(scrolled, True, True, 0)
        vboxStack4.pack_end(hbox119, False, False, 0)














    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================
    if not Functions.distr == "manjaro":
        stack.add_titled(vboxStack1, "stack1", "SDDM")
    stack.add_titled(vboxStack2, "stack2", "LIGHTDM")
    stack.add_titled(vboxStack3, "stack3", "LXDM")
    stack.add_titled(vboxStack4, "stack4", "WALL")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxStack22.pack_start(hbox1, False, False, 0)
    vboxStack22.pack_start(hbox0, False, False, 0)
    vboxStack22.pack_start(vbox, True, True, 0)