# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

def GUI(self, Gtk, vboxStack1, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("ArcoLinux Mirrorlist")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                   GLOBALS
    # ==========================================================

    hboxStack1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack17 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    # ========================================================
    #               ARCO REPOS
    # ========================================================

    frame3 = Gtk.Frame(label="")
    frame3lbl = frame3.get_label_widget()
    frame3lbl.set_markup("<b>ArcoLinux Mirrorlist</b>")

    # seedhost
    self.aseed_button = Gtk.Switch()
    self.aseed_button.connect("notify::active", self.on_mirror_seed_repo_toggle)
    label5 = Gtk.Label(xalign=0)
    label5.set_markup("Enable Seedhost repo - Do not enable it and save us bandwidth and money - paid - Netherlands - Always up-to-date")
    seedhost_sync = Gtk.Label(xalign=0)
    hboxStack7.pack_start(label5, False, True, 10)
    hboxStack7.pack_end(self.aseed_button, False, False, 20)
    hboxStack7.pack_start(seedhost_sync, False, True, 10)

    # gitlab
    self.agitlab_button = Gtk.Switch()
    self.agitlab_button.connect("notify::active", self.on_mirror_gitlab_repo_toggle)
    labelGitlab = Gtk.Label(xalign=0)
    labelGitlab.set_markup("Enable Gitlab repo - free bandwidth - United States - Always up-to-date")
    gitlab_sync = Gtk.Label(xalign=0)
    hboxStack16.pack_start(labelGitlab, False, True, 10)
    hboxStack16.pack_end(self.agitlab_button, False, False, 20)
    hboxStack16.pack_start(gitlab_sync, False, True, 10)

    # belnet
    self.abelnet_button = Gtk.Switch()
    self.abelnet_button.connect("notify::active", self.on_mirror_belnet_repo_toggle)
    label6 = Gtk.Label(xalign=0)
    label6.set_markup("Enable Belnet repo - free bandwidth - Belgium - Belnet syncs twice per day")
    belnet_sync = Gtk.Label(xalign=0)
    hboxStack14.pack_start(label6, False, True, 10)
    hboxStack14.pack_end(self.abelnet_button, False, False, 20)
    hboxStack14.pack_start(belnet_sync, False, True, 10)

    # funami
    self.afunami_button = Gtk.Switch()
    self.afunami_button.connect("notify::active", self.on_mirror_funami_repo_toggle)
    labelfunami = Gtk.Label(xalign=0)
    labelfunami.set_markup("Enable Funami repo - free bandwidth - South Korea - Funami syncs once per day")
    funami_sync = Gtk.Label(xalign=0)
    hboxStack18.pack_start(labelfunami, False, True, 10)
    hboxStack18.pack_end(self.afunami_button, False, False, 20)
    hboxStack18.pack_start(funami_sync, False, True, 10)

    # jingk
    self.ajingk_button = Gtk.Switch()
    self.ajingk_button.connect("notify::active", self.on_mirror_jingk_repo_toggle)
    labeljingk = Gtk.Label(xalign=0)
    labeljingk.set_markup("Enable Jingk repo - free bandwidth - Singapore - Jingk syncs twice per day")
    jingk_sync = Gtk.Label(xalign=0)
    hboxStack19.pack_start(labeljingk, False, True, 10)
    hboxStack19.pack_end(self.ajingk_button, False, False, 20)
    hboxStack19.pack_start(jingk_sync, False, True, 10)

    # codeberg
    self.acodeberg_button = Gtk.Switch()
    self.acodeberg_button.connect("notify::active", self.on_mirror_codeberg_repo_toggle)
    labelacodeberg = Gtk.Label(xalign=0)
    labelacodeberg.set_markup("Enable Codeberg repo - free bandwidth - Germany - Always up-to-date")
    codeberg_sync = Gtk.Label(xalign=0)
    hboxStack17.pack_start(labelacodeberg, False, True, 10)
    hboxStack17.pack_end(self.acodeberg_button, False, False, 20)
    hboxStack17.pack_start(codeberg_sync, False, True, 10)

    # github - always there as fallback - no extra large repo on github
    # self.agithub_button = Gtk.Switch()
    # self.agithub_button.connect("notify::active", self.on_mirror_github_repo_toggle)
    # label7 = Gtk.Label(xalign=0)
    # label7.set_markup("Enable Github repo - free bandwidth")
    # hboxStack9.pack_start(label7, False, True, 10)
    # hboxStack9.pack_end(self.agithub_button, False, False, 20)

    # aarnet
    self.aarnet_button = Gtk.Switch()
    self.aarnet_button.connect("notify::active", self.on_mirror_aarnet_repo_toggle)
    label8 = Gtk.Label(xalign=0)
    label8.set_markup("Enable Aarnet repo - free bandwidth - Australia - Aarnet syncs daily")
    aarnet_sync = Gtk.Label(xalign=0)
    #aarnet_sync.set_markup("     Aarnet syncs once per day")
    hboxStack10.pack_start(label8, False, True, 10)
    hboxStack10.pack_end(self.aarnet_button, False, False, 20)
    hboxStack10.pack_start(aarnet_sync, False, True, 10)

    warning = Gtk.Label(xalign=0)
    warning.set_markup("If you disable all these mirrors you will no longer have access to the ArcoLinux Xlarge repository.")
    warning2 = Gtk.Label(xalign=0)
    warning2.set_markup("Change your /etc/pacman.conf accordingly.")
    hboxStack11.pack_start(warning, False, False, 10)
    hboxStack12.pack_start(warning2, False, False, 10)

    frame4 = Gtk.Frame(label="")
    frame4.set_margin_top(10)
    frame4lbl = frame4.get_label_widget()
    frame4lbl.set_markup("<b>Other mirrorlists</b>")

    pace_label = Gtk.Label(xalign=0)
    pace_label.set_margin_top(0)
    pace_label.set_markup("We use the <b>pace</b> application to set the mirrors of other repositories.\nYou save the settings in pace by clicking on preview and save. Pace will change the orginal layout.")
    launch_pace_btn = Gtk.Button(label="Install/launch pace")
    launch_pace_btn.connect("clicked", self.on_click_launch_pace)

    hboxStack15.pack_start(pace_label, False, False, 10)
    hboxStack15.pack_start(launch_pace_btn, False, False, 10)

    # ========================================================
    #               FOOTER
    # ========================================================

    reset_mirror = Gtk.Button(label="Reset ArcoLinux Mirrorlist")
    reset_mirror.connect("clicked", self.on_click_reset_arcolinux_mirrorlist)
    hboxStack4.pack_end(reset_mirror, False, False, 0)

    # ========================================================
    #               VBOX - FRAME
    # ========================================================

    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #message
    vbox3.pack_start(hboxStack11, False, False, 0)
    vbox3.pack_start(hboxStack12, False, False, 0)
    #gitlab
    vbox3.pack_start(hboxStack16, False, False, 0)
    #codeberg
    #vbox3.pack_start(hboxStack17, False, False, 0)
    #belnet
    vbox3.pack_start(hboxStack14, False, False, 0)
    # aarnet
    vbox3.pack_start(hboxStack10, False, False, 0)
    #funami
    vbox3.pack_start(hboxStack18, False, False, 0)
    #jingk
    vbox3.pack_start(hboxStack19, False, False, 0)
    #seedhost
    vbox3.pack_start(hboxStack7, False, False, 0)

    frame3.add(vbox3)


    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #message
    vbox4.pack_start(hboxStack15, False, False, 0)
    frame4.add(vbox4)

    # ========================================================
    #               PACK TO WINDOW
    # ========================================================

    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_start(hbox4, False, False, 0)
    vboxStack1.pack_start(frame3, False, False, 10)
    vboxStack1.pack_start(frame4, False, False, 10)
    vboxStack1.pack_end(hboxStack4, False, False, 0)
