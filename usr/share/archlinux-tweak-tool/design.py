# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

# import os
import functions as fn


# ====================================================================
#                       DESIGN
# ====================================================================


def get_neofetch():
    """get lines from neofetch_config"""
    lines = []
    if fn.path.isfile(fn.neofetch_config):
        with open(fn.neofetch_config, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()

    return lines


def check_backend():
    """see if image is active"""
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for item in enumerate(lines):
            if "image_backend=" in item:
                if not "#" in item:
                    line = item.split("=")[1].replace('"', "").strip()
                    return line
    return "ascii"


def check_ascii():
    """see if ascii is active"""
    line = "auto"
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        for item in enumerate(lines):
            if "ascii_distro=" in item:
                line = item.split("=")[1].replace('"', "").strip()
                return line


def apply_config(self, backend, ascii_size):
    """apply neofetch configuration"""
    if fn.path.isfile(fn.neofetch_config):
        lines = get_neofetch()
        # TODO:enumerate lines
        for i in range(len(lines)):
            if self.os.get_active():
                fn.neofetch_set_value(lines, i, 'info "OS"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "OS"', False)
            if self.host.get_active():
                fn.neofetch_set_value(lines, i, 'info "Host"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Host"', False)
            if self.kernel.get_active():
                fn.neofetch_set_value(lines, i, 'info "Kernel"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Kernel"', False)
            if self.uptime.get_active():
                fn.neofetch_set_value(lines, i, 'info "Uptime"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Uptime"', False)
            if self.packages.get_active():
                fn.neofetch_set_value(lines, i, 'info "Packages"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Packages"', False)
            if self.shell.get_active():
                fn.neofetch_set_value(lines, i, 'info "Shell"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Shell"', False)
            if self.res.get_active():
                fn.neofetch_set_value(lines, i, 'info "Resolution"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Resolution"', False)
            if self.de.get_active():
                fn.neofetch_set_value(lines, i, 'info "DE"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "DE"', False)
            if self.wm.get_active():
                fn.neofetch_set_value(lines, i, 'info "WM"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "WM"', False)
            if self.wmtheme.get_active():
                fn.neofetch_set_value(lines, i, 'info "WM Theme"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "WM Theme"', False)
            if self.themes.get_active():
                fn.neofetch_set_value(lines, i, 'info "Theme"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Theme"', False)
            if self.icons.get_active():
                fn.neofetch_set_value(lines, i, 'info "Icons"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Icons"', False)
            if self.term.get_active():
                fn.neofetch_set_value(lines, i, 'info "Terminal"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Terminal"', False)
            if self.termfont.get_active():
                fn.neofetch_set_value(lines, i, 'info "Terminal Font"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Terminal Font"', False)
            if self.cpu.get_active():
                fn.neofetch_set_value(lines, i, 'info "CPU"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "CPU"', False)
            if self.gpu.get_active():
                fn.neofetch_set_value(lines, i, 'info "GPU"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "GPU"', False)
            if self.mem.get_active():
                fn.neofetch_set_value(lines, i, 'info "Memory"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Memory"', False)
            if self.gpu_driver.get_active():
                fn.neofetch_set_value(lines, i, 'info "GPU Driver"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "GPU Driver"', False)
            if self.cpu_usage.get_active():
                fn.neofetch_set_value(lines, i, 'info "CPU Usage"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "CPU Usage"', False)
            if self.disks.get_active():
                fn.neofetch_set_value(lines, i, 'info "Disk"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Disk"', False)
            if self.font.get_active():
                fn.neofetch_set_value(lines, i, 'info "Font"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Font"', False)
            if self.song.get_active():
                fn.neofetch_set_value(lines, i, 'info "Song"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Song"', False)
            if self.lIP.get_active():
                fn.neofetch_set_value(lines, i, 'info "Local IP"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Local IP"', False)
            if self.PIP.get_active():
                fn.neofetch_set_value(lines, i, 'info "Public IP"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Public IP"', False)
            if self.users.get_active():
                fn.neofetch_set_value(lines, i, 'info "Users"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Users"', False)
            if self.local.get_active():
                fn.neofetch_set_value(lines, i, 'info "Locale"', True)
            else:
                fn.neofetch_set_value(lines, i, 'info "Locale"', False)
            if self.title.get_active():
                fn.neofetch_set_value(lines, i, "info title", True)
                fn.neofetch_set_value(lines, i, "info underline", True)
            else:
                fn.neofetch_set_value(lines, i, "info title", False)
                fn.neofetch_set_value(lines, i, "info underline", False)

            if not backend == "ascii" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "w3m")
                # fn.neofetch_set_backend_value(lines, i, "image_backend=\"ascii\"")
                fn.neofetch_set_value(lines, i, "image_source=", False)
                # fn.neofetch_set_value(lines, i, emblem, True)

            elif not backend == "w3m" and not backend == "off":
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "ascii")
                # fn.neofetch_set_value(lines, i, "image_backend=\"ascii\"", True)
                # fn.neofetch_set_value(lines, i, "image_backend=\"" + backend_val + "\"", False)
                if "ascii_distro=" in lines[i]:
                    lines[i] = 'ascii_distro="' + ascii_size + '"\n'
            else:
                fn.neofetch_set_backend_value(lines, i, 'image_backend="', "off")

            if self.cblocks.get_active():
                fn.neofetch_set_backend_value(lines, i, 'color_blocks="', "on")
            else:
                fn.neofetch_set_backend_value(lines, i, 'color_blocks="', "off")

        with open(fn.neofetch_config, "w", encoding="utf-8") as f:
            f.writelines(lines)
            f.close()
        print("Neofetch settings saved successfully")
        fn.show_in_app_notification(self, "Neofetch settings saved successfully")


def get_state(value):
    """found out what is active and what is not active"""
    lines = get_neofetch()
    # TODO:enumerate lines
    for i in range(len(lines)):
        if value in lines[i]:
            if "#" in lines[i]:
                return False
    return True


def get_checkboxes(self):
    """read the state of the checkbouxes"""
    self.os.set_active(get_state('info "OS"'))
    self.host.set_active(get_state('info "Host"'))
    self.kernel.set_active(get_state('info "Kernel"'))
    self.uptime.set_active(get_state('info "Uptime"'))
    self.packages.set_active(get_state('info "Packages"'))
    self.shell.set_active(get_state('info "Shell"'))
    self.res.set_active(get_state('info "Resolution"'))
    self.de.set_active(get_state('info "DE"'))
    self.wm.set_active(get_state('info "WM"'))
    self.wmtheme.set_active(get_state('info "WM Theme"'))
    self.themes.set_active(get_state('info "Theme"'))
    self.icons.set_active(get_state('info "Icons"'))
    self.term.set_active(get_state('info "Terminal"'))
    self.termfont.set_active(get_state('info "Terminal Font"'))
    self.cpu.set_active(get_state('info "CPU"'))
    self.gpu.set_active(get_state('info "GPU"'))
    self.mem.set_active(get_state('info "Memory"'))
    self.title.set_active(get_state("info title"))

    self.gpu_driver.set_active(get_state('info "GPU Driver"'))
    self.cpu_usage.set_active(get_state('info "CPU Usage"'))
    self.disks.set_active(get_state('info "Disk"'))
    self.font.set_active(get_state('info "Font"'))
    self.song.set_active(get_state('info "Song"'))
    self.lIP.set_active(get_state('info "Local IP"'))
    self.PIP.set_active(get_state('info "Public IP"'))
    self.users.set_active(get_state('info "Users"'))
    self.local.set_active(get_state('info "Locale"'))

    lines = get_neofetch()

    line = [x for x in lines if "color_blocks=" in x]
    if "on" in line[0]:
        self.cblocks.set_active(True)
    else:
        self.cblocks.set_active(False)


#    #====================================================================
#    #                       THEMES
#    #====================================================================


def set_checkboxes_theming_all(self):
    """set the state of the checkboxes"""
    self.adapta_gtk_theme.set_active(True)
    self.arc_gtk_theme.set_active(True)
    self.arcolinux_arc_kde.set_active(True)
    self.arcolinux_sweet_mars_git.set_active(True)
    self.ayu_theme.set_active(True)
    self.breeze.set_active(True)
    self.dracula_gtk_theme.set_active(True)
    self.fluent_gtk_theme.set_active(True)
    self.fluent_kde_theme_git.set_active(True)
    self.graphite_gtk_theme_git.set_active(True)
    self.kripton_theme_git.set_active(True)
    self.kvantum_theme_materia.set_active(True)
    self.kvantum_theme_qogir_git.set_active(True)
    self.layan_gtk_theme_git.set_active(True)
    self.layan_kde_git.set_active(True)
    self.materia_gtk_theme.set_active(True)
    self.materia_kde.set_active(True)
    self.numix_gtk_theme_git.set_active(True)
    self.openbox_themes_pambudi_git.set_active(True)
    self.orchis_kde_theme_git.set_active(True)
    self.orchis_theme_git.set_active(True)
    self.qogir_gtk_theme_git.set_active(True)
    self.sweet_theme_git.set_active(True)
    self.sweet_gtk_theme_dark.set_active(True)


def set_checkboxes_theming_normal(self):
    """set the state of the checkboxes"""
    self.adapta_gtk_theme.set_active(False)
    self.arc_gtk_theme.set_active(True)
    self.arcolinux_arc_kde.set_active(True)
    self.arcolinux_sweet_mars_git.set_active(False)
    self.ayu_theme.set_active(False)
    self.breeze.set_active(False)
    self.dracula_gtk_theme.set_active(True)
    self.fluent_gtk_theme.set_active(False)
    self.fluent_kde_theme_git.set_active(False)
    self.graphite_gtk_theme_git.set_active(False)
    self.kripton_theme_git.set_active(False)
    self.kvantum_theme_materia.set_active(False)
    self.kvantum_theme_qogir_git.set_active(False)
    self.layan_gtk_theme_git.set_active(False)
    self.layan_kde_git.set_active(False)
    self.materia_gtk_theme.set_active(False)
    self.materia_kde.set_active(False)
    self.numix_gtk_theme_git.set_active(False)
    self.openbox_themes_pambudi_git.set_active(False)
    self.orchis_kde_theme_git.set_active(False)
    self.orchis_theme_git.set_active(False)
    self.qogir_gtk_theme_git.set_active(False)
    self.sweet_theme_git.set_active(False)
    self.sweet_gtk_theme_dark.set_active(False)


def set_checkboxes_theming_minimal(self):
    """set the state of the checkboxes"""
    self.adapta_gtk_theme.set_active(False)
    self.arc_gtk_theme.set_active(True)
    self.arcolinux_arc_kde.set_active(True)
    self.arcolinux_sweet_mars_git.set_active(False)
    self.ayu_theme.set_active(False)
    self.breeze.set_active(False)
    self.dracula_gtk_theme.set_active(False)
    self.fluent_gtk_theme.set_active(False)
    self.fluent_kde_theme_git.set_active(False)
    self.graphite_gtk_theme_git.set_active(False)
    self.kripton_theme_git.set_active(False)
    self.kvantum_theme_materia.set_active(False)
    self.kvantum_theme_qogir_git.set_active(False)
    self.layan_gtk_theme_git.set_active(False)
    self.layan_kde_git.set_active(False)
    self.materia_gtk_theme.set_active(False)
    self.materia_kde.set_active(False)
    self.numix_gtk_theme_git.set_active(False)
    self.openbox_themes_pambudi_git.set_active(False)
    self.orchis_kde_theme_git.set_active(False)
    self.orchis_theme_git.set_active(False)
    self.qogir_gtk_theme_git.set_active(False)
    self.sweet_theme_git.set_active(False)
    self.sweet_gtk_theme_dark.set_active(False)


def set_checkboxes_theming_none(self):
    """set the state of the checkboxes"""
    self.adapta_gtk_theme.set_active(False)
    self.arc_gtk_theme.set_active(False)
    self.arcolinux_arc_kde.set_active(False)
    self.arcolinux_sweet_mars_git.set_active(False)
    self.ayu_theme.set_active(False)
    self.breeze.set_active(False)
    self.dracula_gtk_theme.set_active(False)
    self.fluent_gtk_theme.set_active(False)
    self.fluent_kde_theme_git.set_active(False)
    self.graphite_gtk_theme_git.set_active(False)
    self.kripton_theme_git.set_active(False)
    self.kvantum_theme_materia.set_active(False)
    self.kvantum_theme_qogir_git.set_active(False)
    self.layan_gtk_theme_git.set_active(False)
    self.layan_kde_git.set_active(False)
    self.materia_gtk_theme.set_active(False)
    self.materia_kde.set_active(False)
    self.numix_gtk_theme_git.set_active(False)
    self.openbox_themes_pambudi_git.set_active(False)
    self.orchis_kde_theme_git.set_active(False)
    self.orchis_theme_git.set_active(False)
    self.qogir_gtk_theme_git.set_active(False)
    self.sweet_theme_git.set_active(False)
    self.sweet_gtk_theme_dark.set_active(False)


#    #====================================================================
#    #                       ICONS
#    #====================================================================


def set_checkboxes_theming_icons_all(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(True)
    self.arcolinux_candy_beauty_git.set_active(True)
    self.breeze.set_active(True)
    self.dracula_icons_git.set_active(True)
    self.faba_icon_theme_git.set_active(True)
    self.faba_mono_icons_git.set_active(True)
    self.flat_remix_git.set_active(True)
    self.fluent_icon_theme_git.set_active(True)
    self.halo_icons_git.set_active(True)
    self.la_capitaine_icon_theme_git.set_active(True)
    self.luna_icon_theme_git.set_active(True)
    self.moka_icon_theme_git.set_active(True)
    self.nordzy_icon_theme_git.set_active(True)
    self.numix_circle_arc_icons_git.set_active(True)
    self.numix_circle_icon_theme_git.set_active(True)
    self.obsidian_icon_theme.set_active(True)
    self.oranchelo_icon_theme_git.set_active(True)
    self.paper_icon_theme.set_active(True)
    self.papirus_folders_git.set_active(True)
    self.papirus_folders_gui_bin.set_active(True)
    self.papirus_folders_nordic.set_active(True)
    self.papirus_icon_theme.set_active(True)
    self.papirus_nord.set_active(True)
    self.qogir_icon_theme.set_active(True)
    self.sardi_icons.set_active(True)
    self.surfn_icons_git.set_active(True)
    self.tela_circle_icon_theme_git.set_active(True)
    self.vimix_icon_theme_git.set_active(True)
    self.we10x_icon_theme_git.set_active(True)
    self.whitesur_icon_theme_git.set_active(True)
    self.zafiro_icon_theme.set_active(True)


def set_checkboxes_theming_icons_normal(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.arcolinux_candy_beauty_git.set_active(True)
    self.breeze.set_active(False)
    self.dracula_icons_git.set_active(True)
    self.faba_icon_theme_git.set_active(False)
    self.faba_mono_icons_git.set_active(False)
    self.flat_remix_git.set_active(False)
    self.fluent_icon_theme_git.set_active(False)
    self.halo_icons_git.set_active(False)
    self.la_capitaine_icon_theme_git.set_active(False)
    self.luna_icon_theme_git.set_active(False)
    self.moka_icon_theme_git.set_active(False)
    self.nordzy_icon_theme_git.set_active(False)
    self.numix_circle_arc_icons_git.set_active(True)
    self.numix_circle_icon_theme_git.set_active(True)
    self.obsidian_icon_theme.set_active(False)
    self.oranchelo_icon_theme_git.set_active(False)
    self.paper_icon_theme.set_active(False)
    self.papirus_folders_git.set_active(False)
    self.papirus_folders_gui_bin.set_active(False)
    self.papirus_folders_nordic.set_active(False)
    self.papirus_icon_theme.set_active(True)
    self.papirus_nord.set_active(False)
    self.qogir_icon_theme.set_active(False)
    self.sardi_icons.set_active(True)
    self.surfn_icons_git.set_active(True)
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)


def set_checkboxes_theming_icons_minimal(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.arcolinux_candy_beauty_git.set_active(False)
    self.breeze.set_active(False)
    self.dracula_icons_git.set_active(False)
    self.faba_icon_theme_git.set_active(False)
    self.faba_mono_icons_git.set_active(False)
    self.flat_remix_git.set_active(False)
    self.fluent_icon_theme_git.set_active(False)
    self.halo_icons_git.set_active(False)
    self.la_capitaine_icon_theme_git.set_active(False)
    self.luna_icon_theme_git.set_active(False)
    self.moka_icon_theme_git.set_active(False)
    self.nordzy_icon_theme_git.set_active(False)
    self.numix_circle_arc_icons_git.set_active(False)
    self.numix_circle_icon_theme_git.set_active(False)
    self.obsidian_icon_theme.set_active(False)
    self.oranchelo_icon_theme_git.set_active(False)
    self.paper_icon_theme.set_active(False)
    self.papirus_folders_git.set_active(False)
    self.papirus_folders_gui_bin.set_active(False)
    self.papirus_folders_nordic.set_active(False)
    self.papirus_icon_theme.set_active(False)
    self.papirus_nord.set_active(False)
    self.qogir_icon_theme.set_active(False)
    self.sardi_icons.set_active(True)
    self.surfn_icons_git.set_active(True)
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)


def set_checkboxes_theming_icons_none(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.arcolinux_candy_beauty_git.set_active(False)
    self.breeze.set_active(False)
    self.dracula_icons_git.set_active(False)
    self.faba_icon_theme_git.set_active(False)
    self.faba_mono_icons_git.set_active(False)
    self.flat_remix_git.set_active(False)
    self.fluent_icon_theme_git.set_active(False)
    self.halo_icons_git.set_active(False)
    self.la_capitaine_icon_theme_git.set_active(False)
    self.luna_icon_theme_git.set_active(False)
    self.moka_icon_theme_git.set_active(False)
    self.nordzy_icon_theme_git.set_active(False)
    self.numix_circle_arc_icons_git.set_active(False)
    self.numix_circle_icon_theme_git.set_active(False)
    self.obsidian_icon_theme.set_active(False)
    self.oranchelo_icon_theme_git.set_active(False)
    self.paper_icon_theme.set_active(False)
    self.papirus_folders_git.set_active(False)
    self.papirus_folders_gui_bin.set_active(False)
    self.papirus_folders_nordic.set_active(False)
    self.papirus_icon_theme.set_active(False)
    self.papirus_nord.set_active(False)
    self.qogir_icon_theme.set_active(False)
    self.sardi_icons.set_active(False)
    self.surfn_icons_git.set_active(False)
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)


#    #====================================================================
#    #                       CURSORS
#    #====================================================================


def set_checkboxes_theming_cursors_all(self):
    """set the state of the checkboxes"""
    self.bibata_cursor_theme_bin.set_active(True)
    self.bibata_cursor_translucent.set_active(True)
    self.bibata_extra_cursor_theme.set_active(True)
    self.bibata_rainbow_cursor_theme.set_active(True)
    self.capitaine_cursors.set_active(True)
    self.catppuccin_cursors_git.set_active(True)
    self.dracula_cursors_git.set_active(True)
    self.layan_cursor_theme_git.set_active(True)
    self.oxy_neon.set_active(True)
    self.sweet_cursor_theme_git.set_active(True)
    self.vimix_cursors.set_active(True)
    self.xcursor_arch_cursor_complete.set_active(True)
    self.xcursor_breeze.set_active(True)
    self.xcursor_comix.set_active(True)
    self.xcursor_flatbed.set_active(True)
    self.xcursor_neutral.set_active(True)
    self.xcursor_premium.set_active(True)
    self.xcursor_simpleandsoft.set_active(True)


def set_checkboxes_theming_cursors_normal(self):
    """set the state of the checkboxes"""
    self.bibata_cursor_theme_bin.set_active(True)
    self.bibata_cursor_translucent.set_active(False)
    self.bibata_extra_cursor_theme.set_active(False)
    self.bibata_rainbow_cursor_theme.set_active(False)
    self.capitaine_cursors.set_active(False)
    self.catppuccin_cursors_git.set_active(False)
    self.dracula_cursors_git.set_active(True)
    self.layan_cursor_theme_git.set_active(False)
    self.oxy_neon.set_active(False)
    self.sweet_cursor_theme_git.set_active(False)
    self.vimix_cursors.set_active(True)
    self.xcursor_arch_cursor_complete.set_active(False)
    self.xcursor_breeze.set_active(False)
    self.xcursor_comix.set_active(False)
    self.xcursor_flatbed.set_active(False)
    self.xcursor_neutral.set_active(False)
    self.xcursor_premium.set_active(False)
    self.xcursor_simpleandsoft.set_active(False)


def set_checkboxes_theming_cursors_minimal(self):
    """set the state of the checkboxes"""
    self.bibata_cursor_theme_bin.set_active(True)
    self.bibata_cursor_translucent.set_active(False)
    self.bibata_extra_cursor_theme.set_active(False)
    self.bibata_rainbow_cursor_theme.set_active(False)
    self.capitaine_cursors.set_active(False)
    self.catppuccin_cursors_git.set_active(False)
    self.dracula_cursors_git.set_active(False)
    self.layan_cursor_theme_git.set_active(False)
    self.oxy_neon.set_active(False)
    self.sweet_cursor_theme_git.set_active(False)
    self.vimix_cursors.set_active(True)
    self.xcursor_arch_cursor_complete.set_active(False)
    self.xcursor_breeze.set_active(False)
    self.xcursor_comix.set_active(False)
    self.xcursor_flatbed.set_active(False)
    self.xcursor_neutral.set_active(False)
    self.xcursor_premium.set_active(False)
    self.xcursor_simpleandsoft.set_active(False)


def set_checkboxes_theming_cursors_none(self):
    """set the state of the checkboxes"""
    self.bibata_cursor_theme_bin.set_active(False)
    self.bibata_cursor_translucent.set_active(False)
    self.bibata_extra_cursor_theme.set_active(False)
    self.bibata_rainbow_cursor_theme.set_active(False)
    self.capitaine_cursors.set_active(False)
    self.catppuccin_cursors_git.set_active(False)
    self.dracula_cursors_git.set_active(False)
    self.layan_cursor_theme_git.set_active(False)
    self.oxy_neon.set_active(False)
    self.sweet_cursor_theme_git.set_active(False)
    self.vimix_cursors.set_active(False)
    self.xcursor_arch_cursor_complete.set_active(False)
    self.xcursor_breeze.set_active(False)
    self.xcursor_comix.set_active(False)
    self.xcursor_flatbed.set_active(False)
    self.xcursor_neutral.set_active(False)
    self.xcursor_premium.set_active(False)
    self.xcursor_simpleandsoft.set_active(False)


#    #====================================================================
#    #                       FONTS
#    #====================================================================


def set_checkboxes_fonts_all(self):
    """set the state of the checkboxes"""
    self.awesome_terminal_fonts.set_active(True)
    self.nerd_fonts_source_code_pro.set_active(True)
    self.ttf_anonymous_pro.set_active(True)
    self.ttf_bitstream_vera.set_active(True)
    self.ttf_caladea.set_active(True)
    self.ttf_carlito.set_active(True)
    self.ttf_cascadia_code.set_active(True)
    self.ttf_cormorant.set_active(True)
    self.ttf_croscore.set_active(True)
    self.ttf_eurof.set_active(True)
    self.ttf_fantasque_sans_mono.set_active(True)
    self.ttf_fira_code.set_active(True)
    self.ttf_fira_mono.set_active(True)
    self.ttf_fira_sans.set_active(True)
    self.ttf_font_awesome.set_active(True)
    self.ttf_hactor.set_active(True)
    self.ttf_hellvetica.set_active(True)
    self.ttf_ibm_plex.set_active(True)
    self.ttf_inconsolata.set_active(True)
    self.ttf_jetbrains_mono.set_active(True)
    self.ttf_joypixels.set_active(True)
    self.ttf_lato.set_active(True)
    self.ttf_liberation.set_active(True)
    self.ttf_linux_libertine.set_active(True)
    self.ttf_linux_libertine_g.set_active(True)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(True)
    self.ttf_monofur.set_active(True)
    self.ttf_ms_fonts.set_active(True)
    self.ttf_nerd_fonts_symbols.set_active(True)
    self.ttf_nerd_fonts_symbols_mono.set_active(True)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(True)


def set_checkboxes_fonts_normal(self):
    """set the state of the checkboxes"""
    self.awesome_terminal_fonts.set_active(True)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(True)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_jetbrains_mono.set_active(True)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(True)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(True)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(False)


def set_checkboxes_fonts_minimal(self):
    """set the state of the checkboxes"""
    self.awesome_terminal_fonts.set_active(False)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(False)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(False)


def set_checkboxes_fonts_none(self):
    """set the state of the checkboxes"""
    self.awesome_terminal_fonts.set_active(False)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(False)
    self.ttf_opensans.set_active(False)
    self.ttf_proggy_clean.set_active(False)


# def pop_distro_combobox(self, combo):
#     """populate distro box"""
#     coms = []
#     combo.get_model().clear()
#     list_distros = [
#         "auto",
#         "Antergos",
#         "Anarchy",
#         "Android",
#         "Antergos",
#         "antiX",
#         "ArcoLinux",
#         "ArchBox",
#         "ARCHlabs",
#         "ArchStrike",
#         "Arch",
#         "Artix",
#         "Arya",
#         "Bedrock",
#         "BlackArch",
#         "BSD",
#         "BunsenLabs",
#         "CentOS",
#         "Chakra",
#         "ClearOS",
#         "Debian",
#         "Deepin",
#         "Elementary",
#         "EndeavourOS",
#         "Fedora",
#         "Feren",
#         "FreeBSD",
#         "Frugalware",
#         "Funtoo",
#         "Garuda",
#         "Gentoo",
#         "GNOME",
#         "GNU",
#         "Kali",
#         "KaOS",
#         "KDE_neon",
#         "Kubuntu",
#         "LMDE",
#         "Lubuntu",
#         "macos",
#         "Mageia",
#         "MagpieOS",
#         "Mandriva",
#         "Manjaro",
#         "Maui",
#         "LinuxMint",
#         "MX_Linux",
#         "Namib",
#         "NetBSD",
#         "Netrunner",
#         "Nitrux",
#         "NixOS",
#         "OBRevenge",
#         "OpenBSD",
#         "OpenMandriva",
#         "Oracle",
#         "PCLinuxOS",
#         "Peppermint",
#         "popos",
#         "Puppy",
#         "PureOS",
#         "Raspbian",
#         "Reborn_OS",
#         "Redcore",
#         "Redhat,SalentOS",
#         "Slackware",
#         "Solus",
#         "SteamOS",
#         "SunOS",
#         "openSUSE_Leap",
#         "openSUSE_Tumbleweed",
#         "openSUSE",
#         "SwagArch",
#         "Ubuntu-Budgie",
#         "Ubuntu-GNOME",
#         "Ubuntu-MATE",
#         "Ubuntu-Studio",
#         "Ubuntu",
#         "Venom",
#         "Void",
#         "windows10",
#         "Windows7",
#         "Xubuntu",
#         "Zorin",
#     ]

#     for items in list_distros:
#         coms.append(items)

#     # try:
#     #     name = fn.get_position(fn.neofetch_config, "ascii_distro=").split("=")[1]
#     # except IndexError:
#     #     name = ""

#     # coms.sort()
#     for i, item in enumerate(coms):
#         combo.append_text(item)
#         # if name.lower() == item.lower():
#         #     combo.set_active(i)
