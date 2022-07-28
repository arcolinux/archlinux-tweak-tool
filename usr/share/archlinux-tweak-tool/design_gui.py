# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================
# pylint:disable=C0103,


def gui(self, Gtk, vboxstack24, design, fn):
    """create a gui"""
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Design")
    lbl1.set_name("title")
    hbox3.pack_start(lbl1, False, False, 0)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)

    # ==========================================================
    #                     DESIGN
    # ==========================================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxstack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

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
    #                       THEMES TAB
    # ==================================================================

    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10_label = Gtk.Label(xalign=0)
    hbox10_label.set_text(
        "Choose the package you like to install or uninstall and press the button\n\
We obey the dependencies of pacman"
    )
    hbox10.pack_start(hbox10_label, False, False, 10)

    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    self.adapta_gtk_theme = Gtk.CheckButton(label="adapta-gtk-theme")
    self.arc_darkest_theme_git = Gtk.CheckButton(label="arc-darkest-theme-git")
    self.arc_gtk_theme = Gtk.CheckButton(label="arc-gtk-theme")
    self.arcolinux_arc_kde = Gtk.CheckButton(label="arcolinux-arc-kde")
    self.arcolinux_sweet_mars_git = Gtk.CheckButton(label="arcolinux-sweet-mars-git")
    self.ayu_theme = Gtk.CheckButton(label="ayu-theme")
    self.breeze = Gtk.CheckButton(label="breeze")
    self.dracula_gtk_theme = Gtk.CheckButton(label="dracula-gtk-theme")
    self.fluent_gtk_theme = Gtk.CheckButton(label="fluent-gtk-theme")
    self.fluent_kde_theme_git = Gtk.CheckButton(label="fluent-kde-theme-git")
    self.graphite_gtk_theme_git = Gtk.CheckButton(label="graphite-gtk-theme_git")
    self.kripton_theme_git = Gtk.CheckButton(label="kripton-theme-git")
    self.kvantum_theme_materia = Gtk.CheckButton(label="kvantum-theme-materia")
    self.kvantum_theme_qogir_git = Gtk.CheckButton(label="kvantum-theme-qogir-git")
    self.layan_gtk_theme_git = Gtk.CheckButton(label="layan-gtk-theme-git")
    self.layan_kde_git = Gtk.CheckButton(label="layan-kde-git")
    self.materia_gtk_theme = Gtk.CheckButton(label="materia-gtk-theme")
    self.materia_kde = Gtk.CheckButton(label="materia-kde")
    self.numix_gtk_theme_git = Gtk.CheckButton(label="numix-gtk-theme-git")
    self.openbox_themes_pambudi_git = Gtk.CheckButton(
        label="openbox-themes-pambudi-git"
    )
    self.orchis_kde_theme_git = Gtk.CheckButton(label="orchis-kde-theme-git")
    self.orchis_theme_git = Gtk.CheckButton(label="orchis-theme-git")
    self.qogir_gtk_theme_git = Gtk.CheckButton(label="qogir-gtk-theme-git")
    self.sweet_theme_git = Gtk.CheckButton(label="sweet-theme-git")
    self.sweet_gtk_theme_dark = Gtk.CheckButton(label="sweet-gtk-theme-dark")

    flowbox_themes = Gtk.FlowBox()
    flowbox_themes.set_valign(Gtk.Align.START)
    flowbox_themes.set_max_children_per_line(10)
    flowbox_themes.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox_themes.add(self.adapta_gtk_theme)
    flowbox_themes.add(self.arc_darkest_theme_git)
    flowbox_themes.add(self.arc_gtk_theme)
    flowbox_themes.add(self.arcolinux_arc_kde)
    flowbox_themes.add(self.arcolinux_sweet_mars_git)
    flowbox_themes.add(self.ayu_theme)
    flowbox_themes.add(self.breeze)
    flowbox_themes.add(self.dracula_gtk_theme)
    flowbox_themes.add(self.fluent_gtk_theme)
    flowbox_themes.add(self.fluent_kde_theme_git)
    flowbox_themes.add(self.graphite_gtk_theme_git)
    flowbox_themes.add(self.kripton_theme_git)
    flowbox_themes.add(self.kvantum_theme_materia)
    flowbox_themes.add(self.kvantum_theme_qogir_git)
    flowbox_themes.add(self.layan_gtk_theme_git)
    flowbox_themes.add(self.layan_kde_git)
    flowbox_themes.add(self.materia_gtk_theme)
    flowbox_themes.add(self.materia_kde)
    flowbox_themes.add(self.numix_gtk_theme_git)
    flowbox_themes.add(self.openbox_themes_pambudi_git)
    flowbox_themes.add(self.orchis_kde_theme_git)
    flowbox_themes.add(self.orchis_theme_git)
    flowbox_themes.add(self.qogir_gtk_theme_git)
    flowbox_themes.add(self.sweet_theme_git)
    flowbox_themes.add(self.sweet_gtk_theme_dark)

    hbox12.pack_start(flowbox_themes, True, True, 10)

    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_theming_all_selection)
    btn_normal_selection = Gtk.Button(label="Normal")
    btn_normal_selection.connect("clicked", self.on_click_theming_normal_selection)
    btn_small_selection = Gtk.Button(label="Minimal")
    btn_small_selection.connect("clicked", self.on_click_theming_minimal_selection)
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect("clicked", self.on_click_theming_none_selection)
    hbox13.pack_start(label13, False, False, 10)
    hbox13.pack_end(btn_none_selection, False, False, 10)
    hbox13.pack_end(btn_small_selection, False, False, 10)
    hbox13.pack_end(btn_normal_selection, False, False, 10)
    hbox13.pack_end(btn_all_selection, False, False, 10)

    # at bottom
    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_themes = Gtk.Button(label="Install the selected themes")
    button_install_themes.connect("clicked", self.on_install_themes_clicked)
    button_find_themes = Gtk.Button(label="Show the installed themes")
    button_find_themes.connect("clicked", self.on_find_themes_clicked)
    button_remove_themes = Gtk.Button(label="Uninstall the selected themes")
    button_remove_themes.connect("clicked", self.on_remove_themes_clicked)

    hbox19.pack_start(button_remove_themes, False, False, 10)
    hbox19.pack_start(button_find_themes, False, False, 10)
    hbox19.pack_end(button_install_themes, False, False, 10)

    # ==================================================================
    #                       ICONS TAB
    # ==================================================================

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox20_label = Gtk.Label(xalign=0)
    hbox20_label.set_text(
        "Choose the package you like to install or uninstall and press the button\n\
We obey the dependencies of pacman"
    )
    hbox20.pack_start(hbox20_label, False, False, 10)

    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.arc_icon_theme = Gtk.CheckButton(label="arc-icon-theme")
    self.breeze_icons = Gtk.CheckButton(label="breeze-icons")
    self.dracula_icons_git = Gtk.CheckButton(label="dracula-icons-git")
    self.faba_icon_theme_git = Gtk.CheckButton(label="faba-icon-theme-git")
    self.faba_mono_icons_git = Gtk.CheckButton(label="faba-mono-icons-git")
    self.flat_remix_git = Gtk.CheckButton(label="flat-remix-git")
    self.fluent_icon_theme_git = Gtk.CheckButton(label="fluent-icon-theme-git")
    self.halo_icons_git = Gtk.CheckButton(label="halo-icons-git")
    self.la_capitaine_icon_theme_git = Gtk.CheckButton(
        label="la-capitaine-icon-theme-git"
    )
    self.luna_icon_theme_git = Gtk.CheckButton(label="luna-icon-theme-git")
    self.moka_icon_theme_git = Gtk.CheckButton(label="moka-icon-theme-git")
    self.nordzy_icon_theme_git = Gtk.CheckButton(label="nordzy-icon-theme-git")
    self.numix_circle_arc_icons_git = Gtk.CheckButton(
        label="numix-circle-arc-icons-git"
    )
    self.numix_circle_icon_theme_git = Gtk.CheckButton(
        label="numix-circle-icon-theme-git"
    )
    self.obsidian_icon_theme = Gtk.CheckButton(label="obsidian-icon-theme")
    self.oranchelo_icon_theme_git = Gtk.CheckButton(label="oranchelo-icon-theme-git")
    self.paper_icon_theme = Gtk.CheckButton(label="paper-icon-theme")
    self.papirus_folders_git = Gtk.CheckButton(label="papirus-folders-git")
    self.papirus_folders_gui_bin = Gtk.CheckButton(label="papirus-folders-gui-bin")
    self.papirus_folders_nordic = Gtk.CheckButton(label="papirus-folders-nordic")
    self.papirus_icon_theme = Gtk.CheckButton(label="papirus-icon-theme")
    self.papirus_nord = Gtk.CheckButton(label="papirus-nord")
    self.qogir_icon_theme = Gtk.CheckButton(label="qogir-icon-theme")
    self.tela_circle_icon_theme_git = Gtk.CheckButton(
        label="tela-circle-icon-theme-git"
    )
    self.vimix_icon_theme_git = Gtk.CheckButton(label="vimix-icon-theme-git")
    self.we10x_icon_theme_git = Gtk.CheckButton(label="we10x-icon-theme-git")
    self.whitesur_icon_theme_git = Gtk.CheckButton(label="whitesur-icon-theme-git")
    self.zafiro_icon_theme = Gtk.CheckButton(label="zafiro-icon-theme")

    flowbox_icons = Gtk.FlowBox()
    flowbox_icons.set_valign(Gtk.Align.START)
    flowbox_icons.set_max_children_per_line(10)
    flowbox_icons.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox_icons.add(self.arc_icon_theme)
    flowbox_icons.add(self.breeze_icons)
    flowbox_icons.add(self.dracula_icons_git)
    flowbox_icons.add(self.faba_icon_theme_git)
    flowbox_icons.add(self.faba_mono_icons_git)
    flowbox_icons.add(self.flat_remix_git)
    flowbox_icons.add(self.fluent_icon_theme_git)
    flowbox_icons.add(self.halo_icons_git)
    flowbox_icons.add(self.la_capitaine_icon_theme_git)
    flowbox_icons.add(self.luna_icon_theme_git)
    flowbox_icons.add(self.moka_icon_theme_git)
    flowbox_icons.add(self.nordzy_icon_theme_git)
    flowbox_icons.add(self.numix_circle_arc_icons_git)
    flowbox_icons.add(self.numix_circle_icon_theme_git)
    flowbox_icons.add(self.obsidian_icon_theme)
    flowbox_icons.add(self.oranchelo_icon_theme_git)
    flowbox_icons.add(self.paper_icon_theme)
    flowbox_icons.add(self.papirus_folders_git)
    flowbox_icons.add(self.papirus_folders_gui_bin)
    flowbox_icons.add(self.papirus_folders_nordic)
    flowbox_icons.add(self.papirus_icon_theme)
    flowbox_icons.add(self.papirus_nord)
    flowbox_icons.add(self.qogir_icon_theme)
    flowbox_icons.add(self.tela_circle_icon_theme_git)
    flowbox_icons.add(self.vimix_icon_theme_git)
    flowbox_icons.add(self.we10x_icon_theme_git)
    flowbox_icons.add(self.whitesur_icon_theme_git)
    flowbox_icons.add(self.zafiro_icon_theme)

    hbox21.pack_start(flowbox_icons, True, True, 10)

    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_icon_theming_all_selection)
    btn_normal_selection = Gtk.Button(label="Normal")
    btn_normal_selection.connect("clicked", self.on_click_icon_theming_normal_selection)
    btn_small_selection = Gtk.Button(label="Minimal")
    btn_small_selection.connect("clicked", self.on_click_icon_theming_minimal_selection)
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect("clicked", self.on_click_icon_theming_none_selection)
    hbox22.pack_start(label13, False, False, 10)
    hbox22.pack_end(btn_none_selection, False, False, 10)
    hbox22.pack_end(btn_small_selection, False, False, 10)
    hbox22.pack_end(btn_normal_selection, False, False, 10)
    hbox22.pack_end(btn_all_selection, False, False, 10)

    hbox29 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_themes = Gtk.Button(label="Install the selected icon themes")
    button_install_themes.connect("clicked", self.on_install_icon_themes_clicked)
    button_find_themes = Gtk.Button(label="Show the installed icon themes")
    button_find_themes.connect("clicked", self.on_find_icon_themes_clicked)
    button_remove_themes = Gtk.Button(label="Uninstall the selected icon themes")
    button_remove_themes.connect("clicked", self.on_remove_icon_themes_clicked)
    hbox29.pack_start(button_remove_themes, False, False, 10)
    hbox29.pack_start(button_find_themes, False, False, 10)
    hbox29.pack_end(button_install_themes, False, False, 10)

    # ==================================================================
    #                       CURSORS TAB
    # ==================================================================

    hbox30 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox30_label = Gtk.Label(xalign=0)
    hbox30_label.set_text(
        "Choose the package you like to install or uninstall and press the button\n\
We obey the dependencies of pacman - Icon themes provide cursors too"
    )
    hbox30.pack_start(hbox30_label, False, False, 10)

    hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.bibata_cursor_theme_bin = Gtk.CheckButton(label="bibata-cursor-theme-bin")
    self.bibata_cursor_translucent = Gtk.CheckButton(label="bibata-cursor-translucent")
    self.bibata_extra_cursor_theme = Gtk.CheckButton(label="bibata-extra-cursor-theme")
    self.bibata_rainbow_cursor_theme = Gtk.CheckButton(
        label="bibata-rainbow-cursor-theme"
    )
    self.capitaine_cursors = Gtk.CheckButton(label="capitaine-cursors")
    self.catppuccin_cursors_git = Gtk.CheckButton(label="catppuccin-cursors-git")
    self.dracula_cursors_git = Gtk.CheckButton(label="dracula-cursors-git")
    self.layan_cursor_theme_git = Gtk.CheckButton(label="layan-cursor-theme-git")
    self.oxy_neon = Gtk.CheckButton(label="oxy-neon")
    self.sweet_cursor_theme_git = Gtk.CheckButton(label="sweet-cursor-theme-git")
    self.vimix_cursors = Gtk.CheckButton(label="vimix-cursors")
    self.xcursor_arch_cursor_complete = Gtk.CheckButton(
        label="xcursor-arch-cursor-complete"
    )
    self.xcursor_breeze = Gtk.CheckButton(label="xcursor-breeze")
    self.xcursor_comix = Gtk.CheckButton(label="xcursor-comix")
    self.xcursor_flatbed = Gtk.CheckButton(label="xcursor-flatbed")
    self.xcursor_neutral = Gtk.CheckButton(label="xcursor-neutral")
    self.xcursor_premium = Gtk.CheckButton(label="xcursor-premium")
    self.xcursor_simpleandsoft = Gtk.CheckButton(label="xcursor-simpleandsoft")

    flowbox_cursor = Gtk.FlowBox()
    flowbox_cursor.set_valign(Gtk.Align.START)
    flowbox_cursor.set_max_children_per_line(10)
    flowbox_cursor.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox_cursor.add(self.bibata_cursor_theme_bin)
    flowbox_cursor.add(self.bibata_cursor_translucent)
    flowbox_cursor.add(self.bibata_extra_cursor_theme)
    flowbox_cursor.add(self.bibata_rainbow_cursor_theme)
    flowbox_cursor.add(self.capitaine_cursors)
    flowbox_cursor.add(self.catppuccin_cursors_git)
    flowbox_cursor.add(self.dracula_cursors_git)
    flowbox_cursor.add(self.layan_cursor_theme_git)
    flowbox_cursor.add(self.oxy_neon)
    flowbox_cursor.add(self.sweet_cursor_theme_git)
    flowbox_cursor.add(self.vimix_cursors)
    flowbox_cursor.add(self.xcursor_arch_cursor_complete)
    flowbox_cursor.add(self.xcursor_breeze)
    flowbox_cursor.add(self.xcursor_comix)
    flowbox_cursor.add(self.xcursor_flatbed)
    flowbox_cursor.add(self.xcursor_neutral)
    flowbox_cursor.add(self.xcursor_premium)
    flowbox_cursor.add(self.xcursor_simpleandsoft)

    hbox31.pack_start(flowbox_cursor, True, True, 10)

    hbox32 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label32 = Gtk.Label()
    label32.set_text("Choose what to select with a button")
    btn_all_selection_cursors = Gtk.Button(label="All")
    btn_all_selection_cursors.connect(
        "clicked", self.on_click_cursor_theming_all_selection
    )
    btn_normal_selection_cursors = Gtk.Button(label="Normal")
    btn_normal_selection_cursors.connect(
        "clicked", self.on_click_cursor_theming_normal_selection
    )
    btn_small_selection_cursors = Gtk.Button(label="Minimal")
    btn_small_selection_cursors.connect(
        "clicked", self.on_click_cursor_theming_minimal_selection
    )
    btn_none_selection_cursors = Gtk.Button(label="None")
    btn_none_selection_cursors.connect(
        "clicked", self.on_click_cursor_theming_none_selection
    )
    hbox32.pack_start(label32, False, False, 10)
    hbox32.pack_end(btn_none_selection_cursors, False, False, 10)
    hbox32.pack_end(btn_small_selection_cursors, False, False, 10)
    hbox32.pack_end(btn_normal_selection_cursors, False, False, 10)
    hbox32.pack_end(btn_all_selection_cursors, False, False, 10)

    hbox39 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_cursors = Gtk.Button(label="Install the selected cursor themes")
    button_install_cursors.connect("clicked", self.on_install_cursor_themes_clicked)
    button_find_cursors = Gtk.Button(label="Show the installed cursor themes")
    button_find_cursors.connect("clicked", self.on_find_cursor_themes_clicked)
    button_remove_cursors = Gtk.Button(label="Uninstall the selected cursor themes")
    button_remove_cursors.connect("clicked", self.on_remove_cursor_themes_clicked)
    hbox39.pack_start(button_remove_cursors, False, False, 10)
    hbox39.pack_start(button_find_cursors, False, False, 10)
    hbox39.pack_end(button_install_cursors, False, False, 10)

    # ==================================================================
    #                       FONTS TAB
    # ==================================================================

    hbox40 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox40_label = Gtk.Label(xalign=0)
    hbox40_label.set_text(
        "Choose the package you like to install or uninstall and press the button\n\
We obey the dependencies of pacman"
    )
    hbox40.pack_start(hbox40_label, False, False, 10)

    hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.adobe_source_sans_fonts = Gtk.CheckButton(label="adobe-source-sans-fonts")
    self.awesome_terminal_fonts = Gtk.CheckButton(label="awesome-terminal-fonts")
    self.nerd_fonts_source_code_pro = Gtk.CheckButton(
        label="nerd-fonts-source-code-pro"
    )
    self.noto_fonts = Gtk.CheckButton(label="noto-fonts")
    self.ttf_anonymous_pro = Gtk.CheckButton(label="ttf-anonymous-pro")
    self.ttf_bitstream_vera = Gtk.CheckButton(label="ttf-bitstream-vera")
    self.ttf_caladea = Gtk.CheckButton(label="ttf-caladea")
    self.ttf_carlito = Gtk.CheckButton(label="ttf-carlito")
    self.ttf_cascadia_code = Gtk.CheckButton(label="ttf-cascadia-code")
    self.ttf_cormorant = Gtk.CheckButton(label="ttf-cormorant")
    self.ttf_croscore = Gtk.CheckButton(label="ttf-croscore")
    self.ttf_dejavu = Gtk.CheckButton(label="ttf-dejavu")
    self.ttf_droid = Gtk.CheckButton(label="ttf-droid")
    self.ttf_eurof = Gtk.CheckButton(label="ttf-eurof")
    self.ttf_fantasque_sans_mono = Gtk.CheckButton(label="ttf-fantasque-sans-mono")
    self.ttf_fira_code = Gtk.CheckButton(label="ttf-fira-code")
    self.ttf_fira_mono = Gtk.CheckButton(label="ttf-fira-mono")
    self.ttf_fira_sans = Gtk.CheckButton(label="ttf-fira-sans")
    self.ttf_font_awesome = Gtk.CheckButton(label="ttf-font-awesome")
    self.ttf_hack = Gtk.CheckButton(label="ttf-hack")
    self.ttf_hactor = Gtk.CheckButton(label="ttf-hactor")
    self.ttf_hellvetica = Gtk.CheckButton(label="ttf-hellvetica")
    self.ttf_ibm_plex = Gtk.CheckButton(label="ttf-ibm-plex")
    self.ttf_inconsolata = Gtk.CheckButton(label="ttf-inconsolata")
    self.ttf_iosevka_nerd = Gtk.CheckButton(label="ttf-iosevka-nerd")
    self.ttf_jetbrains_mono = Gtk.CheckButton(label="ttf-jetbrains-mono")
    self.ttf_joypixels = Gtk.CheckButton(label="ttf-joypixels")
    self.ttf_lato = Gtk.CheckButton(label="ttf-lato")
    self.ttf_liberation = Gtk.CheckButton(label="ttf-liberation")
    self.ttf_linux_libertine = Gtk.CheckButton(label="ttf-linux-libertine")
    self.ttf_linux_libertine_g = Gtk.CheckButton(label="ttf-linux-libertine-g")
    self.ttf_material_design_iconic_font = Gtk.CheckButton(
        label="ttf-material-design-iconic-font"
    )
    self.ttf_meslo_nerd_font_powerlevel10k = Gtk.CheckButton(
        label="ttf-meslo-nerd-font-powerlevel10k"
    )
    self.ttf_monofur = Gtk.CheckButton(label="ttf-monofur")
    self.ttf_ms_fonts = Gtk.CheckButton(label="ttf-ms-fonts")
    self.ttf_nerd_fonts_symbols = Gtk.CheckButton(label="ttf-nerd-fonts-symbols")
    self.ttf_nerd_fonts_symbols_mono = Gtk.CheckButton(
        label="ttf-nerd-fonts-symbols-mono"
    )
    self.ttf_opensans = Gtk.CheckButton(label="ttf-opensans")
    self.ttf_proggy_clean = Gtk.CheckButton(label="ttf-proggy-clean")
    self.ttf_roboto = Gtk.CheckButton(label="ttf-roboto")
    self.ttf_roboto_mono = Gtk.CheckButton(label="ttf-roboto-mono")
    self.ttf_ubuntu_font_family = Gtk.CheckButton(label="ttf-ubuntu-font-family")

    flowbox_font = Gtk.FlowBox()
    flowbox_font.set_valign(Gtk.Align.START)
    flowbox_font.set_max_children_per_line(10)
    flowbox_font.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox_font.add(self.adobe_source_sans_fonts)
    flowbox_font.add(self.awesome_terminal_fonts)
    flowbox_font.add(self.nerd_fonts_source_code_pro)
    flowbox_font.add(self.noto_fonts)
    flowbox_font.add(self.ttf_anonymous_pro)
    flowbox_font.add(self.ttf_bitstream_vera)
    flowbox_font.add(self.ttf_caladea)
    flowbox_font.add(self.ttf_carlito)
    flowbox_font.add(self.ttf_cascadia_code)
    flowbox_font.add(self.ttf_cormorant)
    flowbox_font.add(self.ttf_croscore)
    flowbox_font.add(self.ttf_dejavu)
    flowbox_font.add(self.ttf_droid)
    flowbox_font.add(self.ttf_eurof)
    flowbox_font.add(self.ttf_fantasque_sans_mono)
    flowbox_font.add(self.ttf_fira_code)
    flowbox_font.add(self.ttf_fira_mono)
    flowbox_font.add(self.ttf_fira_sans)
    flowbox_font.add(self.ttf_font_awesome)
    flowbox_font.add(self.ttf_hack)
    flowbox_font.add(self.ttf_hactor)
    flowbox_font.add(self.ttf_hellvetica)
    flowbox_font.add(self.ttf_ibm_plex)
    flowbox_font.add(self.ttf_inconsolata)
    flowbox_font.add(self.ttf_iosevka_nerd)
    flowbox_font.add(self.ttf_jetbrains_mono)
    flowbox_font.add(self.ttf_joypixels)
    flowbox_font.add(self.ttf_lato)
    flowbox_font.add(self.ttf_liberation)
    flowbox_font.add(self.ttf_linux_libertine)
    flowbox_font.add(self.ttf_linux_libertine_g)
    flowbox_font.add(self.ttf_material_design_iconic_font)
    flowbox_font.add(self.ttf_meslo_nerd_font_powerlevel10k)
    flowbox_font.add(self.ttf_monofur)
    flowbox_font.add(self.ttf_ms_fonts)
    flowbox_font.add(self.ttf_nerd_fonts_symbols)
    flowbox_font.add(self.ttf_nerd_fonts_symbols_mono)
    flowbox_font.add(self.ttf_opensans)
    flowbox_font.add(self.ttf_proggy_clean)
    flowbox_font.add(self.ttf_roboto)
    flowbox_font.add(self.ttf_roboto_mono)
    flowbox_font.add(self.ttf_ubuntu_font_family)

    hbox41.pack_start(flowbox_font, True, True, 10)

    hbox42 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    lbl_hbox42 = Gtk.Label()
    lbl_hbox42.set_text("Choose what to select with a button")
    btn_all_selection_fonts = Gtk.Button(label="All")
    btn_all_selection_fonts.connect("clicked", self.on_click_font_theming_all_selection)
    btn_normal_selection_fonts = Gtk.Button(label="Normal")
    btn_normal_selection_fonts.connect(
        "clicked", self.on_click_font_theming_normal_selection
    )
    btn_small_selection_fonts = Gtk.Button(label="Minimal")
    btn_small_selection_fonts.connect(
        "clicked", self.on_click_font_theming_minimal_selection
    )
    btn_none_selection_fonts = Gtk.Button(label="None")
    btn_none_selection_fonts.connect(
        "clicked", self.on_click_font_theming_none_selection
    )
    hbox42.pack_start(lbl_hbox42, False, False, 10)
    hbox42.pack_end(btn_none_selection_fonts, False, False, 10)
    hbox42.pack_end(btn_small_selection_fonts, False, False, 10)
    hbox42.pack_end(btn_normal_selection_fonts, False, False, 10)
    hbox42.pack_end(btn_all_selection_fonts, False, False, 10)

    hbox49 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_fonts = Gtk.Button(label="Install the selected fonts")
    button_install_fonts.connect("clicked", self.on_install_fonts_clicked)
    button_find_fonts = Gtk.Button(label="Show the installed fonts")
    button_find_fonts.connect("clicked", self.on_find_fonts_clicked)
    button_remove_fonts = Gtk.Button(label="Uninstall the selected fonts")
    button_remove_fonts.connect("clicked", self.on_remove_fonts_clicked)
    hbox49.pack_start(button_remove_fonts, False, False, 10)
    hbox49.pack_start(button_find_fonts, False, False, 10)
    hbox49.pack_end(button_install_fonts, False, False, 10)

    # ====================================================================
    #                       STACK
    # ====================================================================

    # themes
    vboxstack1.pack_start(hbox10, False, False, 10)
    vboxstack1.pack_start(hbox12, False, False, 10)
    vboxstack1.pack_start(hbox13, False, False, 10)
    vboxstack1.pack_start(hbox19, False, False, 0)

    # icons
    vboxstack2.pack_start(hbox20, False, False, 10)
    vboxstack2.pack_start(hbox21, False, False, 10)
    vboxstack2.pack_start(hbox22, False, False, 10)
    vboxstack2.pack_start(hbox29, False, False, 0)

    # cursors
    vboxstack3.pack_start(hbox30, False, False, 10)
    vboxstack3.pack_start(hbox31, False, False, 10)
    vboxstack3.pack_start(hbox32, False, False, 10)
    vboxstack3.pack_start(hbox39, False, False, 0)

    # fonts
    vboxstack4.pack_start(hbox40, False, False, 10)
    vboxstack4.pack_start(hbox41, False, False, 10)
    vboxstack4.pack_start(hbox42, False, False, 10)
    vboxstack4.pack_start(hbox49, False, False, 0)

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================
    stack.add_titled(vboxstack1, "stack1", "Themes")
    stack.add_titled(vboxstack2, "stack2", "Icons")
    stack.add_titled(vboxstack3, "stack3", "Cursors")
    stack.add_titled(vboxstack4, "stack4", "Fonts")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxstack24.pack_start(hbox3, False, False, 0)
    vboxstack24.pack_start(hbox4, False, False, 0)
    vboxstack24.pack_start(vbox, True, True, 0)
