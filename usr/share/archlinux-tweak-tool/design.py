# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

# import os
import functions as fn

# ====================================================================
#                       THEMES FUNCTIONS
# ====================================================================


# themes
def install_themes(self):
    if self.adapta_gtk_theme.get_active():
        fn.install_arco_package(self, "adapta-gtk-theme")
    if self.arc_darkest_theme_git.get_active():
        fn.install_arco_package(self, "arc-darkest-theme-git")
    if self.arc_gtk_theme.get_active():
        fn.install_arco_package(self, "arc-gtk-theme")
    if self.arcolinux_arc_kde.get_active():
        fn.install_arco_package(self, "arcolinux-arc-kde")
    if self.arcolinux_sweet_mars_git.get_active():
        fn.install_arco_package(self, "arcolinux-sweet-mars-git")
    if self.ayu_theme.get_active():
        fn.install_arco_package(self, "ayu-theme")
    if self.breeze.get_active():
        fn.install_arco_package(self, "breeze")
    if self.dracula_gtk_theme.get_active():
        fn.install_arco_package(self, "dracula-gtk-theme")
    if self.fluent_gtk_theme.get_active():
        fn.install_arco_package(self, "fluent-gtk-theme")
    if self.fluent_kde_theme_git.get_active():
        fn.install_arco_package(self, "fluent-kde-theme-git")
    if self.graphite_gtk_theme_git.get_active():
        fn.install_arco_package(self, "graphite-gtk-theme-git")
    if self.kripton_theme_git.get_active():
        fn.install_arco_package(self, "kripton-theme-git")
    if self.kvantum_theme_materia.get_active():
        fn.install_arco_package(self, "kvantum-theme-materia")
    if self.kvantum_theme_qogir_git.get_active():
        fn.install_arco_package(self, "kvantum-theme-qogir-git")
    if self.layan_gtk_theme_git.get_active():
        fn.install_arco_package(self, "layan-gtk-theme-git")
    if self.layan_kde_git.get_active():
        fn.install_arco_package(self, "layan-kde-git")
    if self.materia_gtk_theme.get_active():
        fn.install_arco_package(self, "materia-gtk-theme")
    if self.materia_kde.get_active():
        fn.install_arco_package(self, "materia-kde")
    if self.numix_gtk_theme_git.get_active():
        fn.install_arco_package(self, "numix-gtk-theme-git")
    if self.openbox_themes_pambudi_git.get_active():
        fn.install_arco_package(self, "openbox-themes-pambudi-git")
    if self.orchis_kde_theme_git.get_active():
        fn.install_arco_package(self, "orchis-kde-theme-git")
    if self.orchis_theme_git.get_active():
        fn.install_arco_package(self, "orchis-theme-git")
    if self.qogir_gtk_theme_git.get_active():
        fn.install_arco_package(self, "qogir-gtk-theme-git")
    if self.sweet_theme_git.get_active():
        fn.install_arco_package(self, "sweet-theme-git")
    if self.sweet_gtk_theme_dark.get_active():
        fn.install_arco_package(self, "sweet-gtk-theme-dark")


def remove_themes(self):
    if self.adapta_gtk_theme.get_active():
        fn.remove_package(self, "adapta-gtk-theme")
    if self.arc_darkest_theme_git.get_active():
        fn.remove_package(self, "arc-darkest-theme-git")
    if self.arc_gtk_theme.get_active():
        fn.remove_package(self, "arc-gtk-theme")
    if self.arcolinux_arc_kde.get_active():
        fn.remove_package(self, "arcolinux-arc-kde")
    if self.arcolinux_sweet_mars_git.get_active():
        fn.remove_package(self, "arcolinux-sweet-mars-git")
    if self.ayu_theme.get_active():
        fn.remove_package(self, "ayu-theme")
    if self.breeze.get_active():
        fn.remove_package(self, "breeze")
    if self.dracula_gtk_theme.get_active():
        fn.remove_package(self, "dracula-gtk-theme")
    if self.fluent_gtk_theme.get_active():
        fn.remove_package(self, "fluent-gtk-theme")
    if self.fluent_kde_theme_git.get_active():
        fn.remove_package(self, "fluent-kde-theme-git")
    if self.graphite_gtk_theme_git.get_active():
        fn.remove_package(self, "graphite-gtk-theme-git")
    if self.kripton_theme_git.get_active():
        fn.remove_package(self, "kripton-theme-git")
    if self.kvantum_theme_materia.get_active():
        fn.remove_package(self, "kvantum-theme-materia")
    if self.kvantum_theme_qogir_git.get_active():
        fn.remove_package(self, "kvantum-theme-qogir-git")
    if self.layan_gtk_theme_git.get_active():
        fn.remove_package(self, "layan-gtk-theme-git")
    if self.layan_kde_git.get_active():
        fn.remove_package(self, "layan-kde-git")
    if self.materia_gtk_theme.get_active():
        fn.remove_package(self, "materia-gtk-theme")
    if self.materia_kde.get_active():
        fn.remove_package(self, "materia-kde")
    if self.numix_gtk_theme_git.get_active():
        fn.remove_package(self, "numix-gtk-theme-git")
    if self.openbox_themes_pambudi_git.get_active():
        fn.remove_package(self, "openbox-themes-pambudi-git")
    if self.orchis_kde_theme_git.get_active():
        fn.remove_package(self, "orchis-kde-theme-git")
    if self.orchis_theme_git.get_active():
        fn.remove_package(self, "orchis-theme-git")
    if self.qogir_gtk_theme_git.get_active():
        fn.remove_package(self, "qogir-gtk-theme-git")
    if self.sweet_theme_git.get_active():
        fn.remove_package(self, "sweet-theme-git")
    if self.sweet_gtk_theme_dark.get_active():
        fn.remove_package(self, "sweet-gtk-theme-dark")


def find_themes(self):
    self.adapta_gtk_theme.set_active(False)
    self.arc_darkest_theme_git.set_active(False)
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

    if fn.check_package_installed("adapta-gtk-theme"):
        self.adapta_gtk_theme.set_active(True)
    if fn.check_package_installed("arc-darkest-theme-git"):
        self.arc_darkest_theme_git.set_active(True)
    if fn.check_package_installed("arc-gtk-theme"):
        self.arc_gtk_theme.set_active(True)
    if fn.check_package_installed("arcolinux-arc-kde"):
        self.arcolinux_arc_kde.set_active(True)
    if fn.check_package_installed("arcolinux-sweet-mars-git"):
        self.arcolinux_sweet_mars_git.set_active(True)
    if fn.check_package_installed("ayu-theme"):
        self.ayu_theme.set_active(True)
    if fn.check_package_installed("breeze"):
        self.breeze.set_active(True)
    if fn.check_package_installed("dracula-gtk-theme"):
        self.dracula_gtk_theme.set_active(True)
    if fn.check_package_installed("fluent-gtk-theme"):
        self.fluent_gtk_theme.set_active(True)
    if fn.check_package_installed("fluent-kde-theme-git"):
        self.fluent_kde_theme_git.set_active(True)
    if fn.check_package_installed("graphite-gtk-theme-git"):
        self.graphite_gtk_theme_git.set_active(True)
    if fn.check_package_installed("kripton-theme-git"):
        self.kripton_theme_git.set_active(True)
    if fn.check_package_installed("kvantum-theme-materia"):
        self.kvantum_theme_materia.set_active(True)
    if fn.check_package_installed("kvantum-theme-qogir-git"):
        self.kvantum_theme_qogir_git.set_active(True)
    if fn.check_package_installed("layan-gtk-theme-git"):
        self.layan_gtk_theme_git.set_active(True)
    if fn.check_package_installed("layan-kde-git"):
        self.layan_kde_git.set_active(True)
    if fn.check_package_installed("materia-gtk-theme"):
        self.materia_gtk_theme.set_active(True)
    if fn.check_package_installed("materia-kde"):
        self.materia_kde.set_active(True)
    if fn.check_package_installed("numix-gtk-theme-git"):
        self.numix_gtk_theme_git.set_active(True)
    if fn.check_package_installed("openbox-themes-pambudi-git"):
        self.openbox_themes_pambudi_git.set_active(True)
    if fn.check_package_installed("orchis-kde-theme-git"):
        self.orchis_kde_theme_git.set_active(True)
    if fn.check_package_installed("orchis-theme-git"):
        self.orchis_theme_git.set_active(True)
    if fn.check_package_installed("qogir-gtk-theme-git"):
        self.qogir_gtk_theme_git.set_active(True)
    if fn.check_package_installed("sweet-theme-git"):
        self.sweet_theme_git.set_active(True)
    if fn.check_package_installed("sweet-gtk-theme-dark"):
        self.sweet_gtk_theme_dark.set_active(True)


# icons
def install_icon_themes(self):
    if self.arc_icon_theme.get_active():
        fn.install_arco_package(self, "arc-icon-theme")
    if self.breeze_icons.get_active():
        fn.install_arco_package(self, "breeze-icons")
    if self.dracula_icons_git.get_active():
        fn.install_arco_package(self, "dracula-icons-git")
    if self.faba_icon_theme_git.get_active():
        fn.install_arco_package(self, "faba-icon-theme-git")
    if self.faba_mono_icons_git.get_active():
        fn.install_arco_package(self, "faba-mono-icons-git")
    if self.flat_remix_git.get_active():
        fn.install_arco_package(self, "flat-remix-git")
    if self.fluent_icon_theme_git.get_active():
        fn.install_arco_package(self, "fluent-icon-theme-git")
    if self.halo_icons_git.get_active():
        fn.install_arco_package(self, "halo-icons-git")
    if self.la_capitaine_icon_theme_git.get_active():
        fn.install_arco_package(self, "la-capitaine-icon-theme-git")
    if self.luna_icon_theme_git.get_active():
        fn.install_arco_package(self, "luna-icon-theme-git")
    if self.moka_icon_theme_git.get_active():
        fn.install_arco_package(self, "moka-icon-theme-git")
    if self.nordzy_icon_theme_git.get_active():
        fn.install_arco_package(self, "nordzy-icon-theme-git")
    if self.numix_circle_arc_icons_git.get_active():
        fn.install_arco_package(self, "numix-circle-arc-icons-git")
    if self.numix_circle_icon_theme_git.get_active():
        fn.install_arco_package(self, "numix-circle-icon-theme-git")
    if self.obsidian_icon_theme.get_active():
        fn.install_arco_package(self, "obsidian-icon-theme")
    if self.oranchelo_icon_theme_git.get_active():
        fn.install_arco_package(self, "oranchelo-icon-theme-git")
    if self.paper_icon_theme.get_active():
        fn.install_arco_package(self, "paper-icon-theme")
    if self.papirus_folders_git.get_active():
        fn.install_arco_package(self, "papirus-folders-git")
    if self.papirus_folders_gui_bin.get_active():
        fn.install_arco_package(self, "papirus-folders-gui-bin")
    if self.papirus_folders_nordic.get_active():
        fn.install_arco_package(self, "papirus-folders-nordic")
    if self.papirus_icon_theme.get_active():
        fn.install_arco_package(self, "papirus-icon-theme")
    if self.papirus_nord.get_active():
        fn.install_arco_package(self, "papirus-nord")
    if self.qogir_icon_theme.get_active():
        fn.install_arco_package(self, "qogir-icon-theme")
    if self.tela_circle_icon_theme_git.get_active():
        fn.install_arco_package(self, "tela-circle-icon-theme-git")
    if self.vimix_icon_theme_git.get_active():
        fn.install_arco_package(self, "vimix-icon-theme-git")
    if self.we10x_icon_theme_git.get_active():
        fn.install_arco_package(self, "we10x-icon-theme-git")
    if self.whitesur_icon_theme_git.get_active():
        fn.install_arco_package(self, "whitesur-icon-theme-git")
    if self.zafiro_icon_theme.get_active():
        fn.install_arco_package(self, "zafiro-icon-theme")


def remove_icon_themes(self):
    if self.arc_icon_theme.get_active():
        fn.remove_package(self, "arc-icon-theme")
    if self.breeze_icons.get_active():
        fn.remove_package(self, "breeze-icons")
    if self.dracula_icons_git.get_active():
        fn.remove_package(self, "dracula-icons-git")
    if self.faba_mono_icons_git.get_active():
        fn.remove_package(self, "faba-mono-icons-git")
    if self.faba_icon_theme_git.get_active():
        fn.remove_package(self, "faba-icon-theme-git")
    if self.flat_remix_git.get_active():
        fn.remove_package(self, "flat-remix-git")
    if self.fluent_icon_theme_git.get_active():
        fn.remove_package(self, "fluent-icon-theme-git")
    if self.halo_icons_git.get_active():
        fn.remove_package(self, "halo-icons-git")
    if self.la_capitaine_icon_theme_git.get_active():
        fn.remove_package(self, "la-capitaine-icon-theme-git")
    if self.luna_icon_theme_git.get_active():
        fn.remove_package(self, "luna-icon-theme-git")
    if self.moka_icon_theme_git.get_active():
        fn.remove_package(self, "moka-icon-theme-git")
    if self.nordzy_icon_theme_git.get_active():
        fn.remove_package(self, "nordzy-icon-theme-git")
    if self.numix_circle_arc_icons_git.get_active():
        fn.remove_package(self, "numix-circle-arc-icons-git")
    if self.numix_circle_icon_theme_git.get_active():
        fn.remove_package(self, "numix-circle-icon-theme-git")
    if self.obsidian_icon_theme.get_active():
        fn.remove_package(self, "obsidian-icon-theme")
    if self.oranchelo_icon_theme_git.get_active():
        fn.remove_package(self, "oranchelo-icon-theme-git")
    if self.paper_icon_theme.get_active():
        fn.remove_package(self, "paper-icon-theme")
    if self.papirus_folders_gui_bin.get_active():
        fn.remove_package(self, "papirus-folders-gui-bin")
    if self.papirus_folders_git.get_active():
        fn.remove_package(self, "papirus-folders-git")
    if self.papirus_folders_nordic.get_active():
        fn.remove_package(self, "papirus-folders-nordic")
    if self.papirus_nord.get_active():
        fn.remove_package(self, "papirus-nord")
    if self.papirus_icon_theme.get_active():
        fn.remove_package(self, "papirus-icon-theme")
    if self.qogir_icon_theme.get_active():
        fn.remove_package(self, "qogir-icon-theme")
    if self.tela_circle_icon_theme_git.get_active():
        fn.remove_package(self, "tela-circle-icon-theme-git")
    if self.vimix_icon_theme_git.get_active():
        fn.remove_package(self, "vimix-icon-theme-git")
    if self.we10x_icon_theme_git.get_active():
        fn.remove_package(self, "we10x-icon-theme-git")
    if self.whitesur_icon_theme_git.get_active():
        fn.remove_package(self, "whitesur-icon-theme-git")
    if self.zafiro_icon_theme.get_active():
        fn.remove_package(self, "zafiro-icon-theme")


def find_icon_themes(self):
    self.arc_icon_theme.set_active(False)
    self.breeze_icons.set_active(False)
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
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)

    if fn.check_package_installed("arc-icon-theme"):
        self.arc_icon_theme.set_active(True)
    if fn.check_package_installed("breeze-icons"):
        self.breeze_icons.set_active(True)
    if fn.check_package_installed("dracula-icons-git"):
        self.dracula_icons_git.set_active(True)
    if fn.check_package_installed("faba-icon-theme-git"):
        self.faba_icon_theme_git.set_active(True)
    if fn.check_package_installed("faba-mono-icons-git"):
        self.faba_mono_icons_git.set_active(True)
    if fn.check_package_installed("flat-remix-git"):
        self.flat_remix_git.set_active(True)
    if fn.check_package_installed("fluent-icon-theme-git"):
        self.fluent_icon_theme_git.set_active(True)
    if fn.check_package_installed("halo-icons-git"):
        self.halo_icons_git.set_active(True)
    if fn.check_package_installed("la-capitaine-icon-theme-git"):
        self.la_capitaine_icon_theme_git.set_active(True)
    if fn.check_package_installed("luna-icon-theme-git"):
        self.luna_icon_theme_git.set_active(True)
    if fn.check_package_installed("moka-icon-theme-git"):
        self.moka_icon_theme_git.set_active(True)
    if fn.check_package_installed("nordzy-icon-theme-git"):
        self.nordzy_icon_theme_git.set_active(True)
    if fn.check_package_installed("numix-circle-arc-icons-git"):
        self.numix_circle_arc_icons_git.set_active(True)
    if fn.check_package_installed("numix-circle-icon-theme-git"):
        self.numix_circle_icon_theme_git.set_active(True)
    if fn.check_package_installed("obsidian-icon-theme"):
        self.obsidian_icon_theme.set_active(True)
    if fn.check_package_installed("oranchelo-icon-theme-git"):
        self.oranchelo_icon_theme_git.set_active(True)
    if fn.check_package_installed("paper-icon-theme"):
        self.paper_icon_theme.set_active(True)
    if fn.check_package_installed("papirus-folders-git"):
        self.papirus_folders_git.set_active(True)
    if fn.check_package_installed("papirus-folders-gui-bin"):
        self.papirus_folders_gui_bin.set_active(True)
    if fn.check_package_installed("papirus-folders-nordic"):
        self.papirus_folders_nordic.set_active(True)
    if fn.check_package_installed("papirus-icon-theme"):
        self.papirus_icon_theme.set_active(True)
    if fn.check_package_installed("papirus-nord"):
        self.papirus_nord.set_active(True)
    if fn.check_package_installed("qogir-icon-theme"):
        self.qogir_icon_theme.set_active(True)
    if fn.check_package_installed("tela-circle-icon-theme-git"):
        self.tela_circle_icon_theme_git.set_active(True)
    if fn.check_package_installed("vimix-icon-theme-git"):
        self.vimix_icon_theme_git.set_active(True)
    if fn.check_package_installed("we10x-icon-theme-git"):
        self.we10x_icon_theme_git.set_active(True)
    if fn.check_package_installed("whitesur-icon-theme-git"):
        self.whitesur_icon_theme_git.set_active(True)
    if fn.check_package_installed("zafiro-icon-theme"):
        self.zafiro_icon_theme.set_active(True)


# cursors
def install_cursor_themes(self):
    if self.bibata_cursor_theme_bin.get_active():
        fn.install_arco_package(self, "bibata-cursor-theme-bin")
    if self.bibata_cursor_translucent.get_active():
        fn.install_arco_package(self, "bibata-cursor-translucent")
    if self.bibata_extra_cursor_theme.get_active():
        fn.install_arco_package(self, "bibata-extra-cursor-theme")
    if self.bibata_rainbow_cursor_theme.get_active():
        fn.install_arco_package(self, "bibata-rainbow-cursor-theme")
    if self.capitaine_cursors.get_active():
        fn.install_arco_package(self, "capitaine-cursors")
    if self.catppuccin_cursors_git.get_active():
        fn.install_arco_package(self, "catppuccin-cursors-git")
    if self.dracula_cursors_git.get_active():
        fn.install_arco_package(self, "dracula-cursors-git")
    if self.layan_cursor_theme_git.get_active():
        fn.install_arco_package(self, "layan-cursor-theme-git")
    if self.oxy_neon.get_active():
        fn.install_arco_package(self, "oxy-neon")
    if self.sweet_cursor_theme_git.get_active():
        fn.install_arco_package(self, "sweet-cursor-theme-git")
    if self.vimix_cursors.get_active():
        fn.install_arco_package(self, "vimix-cursors")
    if self.xcursor_arch_cursor_complete.get_active():
        fn.install_arco_package(self, "xcursor-arch-cursor-complete")
    if self.xcursor_breeze.get_active():
        fn.install_arco_package(self, "xcursor-breeze")
    if self.xcursor_comix.get_active():
        fn.install_arco_package(self, "xcursor-comix")
    if self.xcursor_flatbed.get_active():
        fn.install_arco_package(self, "xcursor-flatbed")
    if self.xcursor_neutral.get_active():
        fn.install_arco_package(self, "xcursor-neutral")
    if self.xcursor_premium.get_active():
        fn.install_arco_package(self, "xcursor-premium")
    if self.xcursor_simpleandsoft.get_active():
        fn.install_arco_package(self, "xcursor-simpleandsoft")


def remove_cursor_themes(self):
    if self.bibata_cursor_theme_bin.get_active():
        fn.remove_package(self, "bibata-cursor-theme-bin")
    if self.bibata_cursor_translucent.get_active():
        fn.remove_package(self, "bibata-cursor-translucent")
    if self.bibata_extra_cursor_theme.get_active():
        fn.remove_package(self, "bibata-extra-cursor-theme")
    if self.bibata_rainbow_cursor_theme.get_active():
        fn.remove_package(self, "bibata-rainbow-cursor-theme")
    if self.capitaine_cursors.get_active():
        fn.remove_package(self, "capitaine-cursors")
    if self.catppuccin_cursors_git.get_active():
        fn.remove_package(self, "catppuccin-cursors-git")
    if self.dracula_cursors_git.get_active():
        fn.remove_package(self, "dracula-cursors-git")
    if self.layan_cursor_theme_git.get_active():
        fn.remove_package(self, "layan-cursor-theme-git")
    if self.oxy_neon.get_active():
        fn.remove_package(self, "oxy-neon")
    if self.sweet_cursor_theme_git.get_active():
        fn.remove_package(self, "sweet-cursor-theme-git")
    if self.vimix_cursors.get_active():
        fn.remove_package(self, "vimix-cursors")
    if self.xcursor_arch_cursor_complete.get_active():
        fn.remove_package(self, "xcursor-arch-cursor-complete")
    if self.xcursor_breeze.get_active():
        fn.remove_package(self, "xcursor-breeze")
    if self.xcursor_comix.get_active():
        fn.remove_package(self, "xcursor-comix")
    if self.xcursor_flatbed.get_active():
        fn.remove_package(self, "xcursor-flatbed")
    if self.xcursor_neutral.get_active():
        fn.remove_package(self, "xcursor-neutral")
    if self.xcursor_premium.get_active():
        fn.remove_package(self, "xcursor-premium")
    if self.xcursor_simpleandsoft.get_active():
        fn.remove_package(self, "xcursor-simpleandsoft")


def find_cursor_themes(self):
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

    if fn.check_package_installed("bibata-cursor-theme-bin"):
        self.bibata_cursor_theme_bin.set_active(True)
    if fn.check_package_installed("bibata-cursor-translucent"):
        self.bibata_cursor_translucent.set_active(True)
    if fn.check_package_installed("bibata-extra-cursor-theme"):
        self.bibata_extra_cursor_theme.set_active(True)
    if fn.check_package_installed("bibata-rainbow-cursor-theme"):
        self.bibata_rainbow_cursor_theme.set_active(True)
    if fn.check_package_installed("capitaine-cursors"):
        self.capitaine_cursors.set_active(True)
    if fn.check_package_installed("catppuccin-cursors-git"):
        self.catppuccin_cursors_git.set_active(True)
    if fn.check_package_installed("dracula-cursors-git"):
        self.dracula_cursors_git.set_active(True)
    if fn.check_package_installed("layan-cursor-theme-git"):
        self.layan_cursor_theme_git.set_active(True)
    if fn.check_package_installed("oxy-neon"):
        self.oxy_neon.set_active(True)
    if fn.check_package_installed("sweet-cursor-theme-git"):
        self.sweet_cursor_theme_git.set_active(True)
    if fn.check_package_installed("vimix-cursors"):
        self.vimix_cursors.set_active(True)
    if fn.check_package_installed("xcursor-arch-cursor-complete"):
        self.xcursor_arch_cursor_complete.set_active(True)
    if fn.check_package_installed("xcursor-breeze"):
        self.xcursor_breeze.set_active(True)
    if fn.check_package_installed("xcursor-comix"):
        self.xcursor_comix.set_active(True)
    if fn.check_package_installed("xcursor-flatbed"):
        self.xcursor_flatbed.set_active(True)
    if fn.check_package_installed("xcursor-neutral"):
        self.xcursor_neutral.set_active(True)
    if fn.check_package_installed("xcursor-premium"):
        self.xcursor_premium.set_active(True)
    if fn.check_package_installed("xcursor-simpleandsoft"):
        self.xcursor_simpleandsoft.set_active(True)


# fonts
def install_fonts(self):
    if self.adobe_source_sans_fonts.get_active():
        fn.install_arco_package(self, "adobe-source-sans-fonts")
    if self.awesome_terminal_fonts.get_active():
        fn.install_arco_package(self, "awesome-terminal-fonts")
    if self.nerd_fonts_source_code_pro.get_active():
        fn.install_arco_package(self, "nerd-fonts-source-code-pro")
    if self.noto_fonts.get_active():
        fn.install_arco_package(self, "noto-fonts")
    if self.ttf_anonymous_pro.get_active():
        fn.install_arco_package(self, "ttf-anonymous-pro")
    if self.ttf_bitstream_vera.get_active():
        fn.install_arco_package(self, "ttf-bitstream-vera")
    if self.ttf_caladea.get_active():
        fn.install_arco_package(self, "ttf-caladea")
    if self.ttf_carlito.get_active():
        fn.install_arco_package(self, "ttf-carlito")
    if self.ttf_cascadia_code.get_active():
        fn.install_arco_package(self, "ttf-cascadia-code")
    if self.ttf_cormorant.get_active():
        fn.install_arco_package(self, "ttf-cormorant")
    if self.ttf_croscore.get_active():
        fn.install_arco_package(self, "ttf-croscore")
    if self.ttf_dejavu.get_active():
        fn.install_arco_package(self, "ttf-dejavu")
    if self.ttf_droid.get_active():
        fn.install_arco_package(self, "ttf-droid")
    if self.ttf_eurof.get_active():
        fn.install_arco_package(self, "ttf-eurof")
    if self.ttf_fantasque_sans_mono.get_active():
        fn.install_arco_package(self, "ttf-fantasque-sans-mono")
    if self.ttf_fira_code.get_active():
        fn.install_arco_package(self, "ttf-fira-code")
    if self.ttf_fira_mono.get_active():
        fn.install_arco_package(self, "ttf-fira-mono")
    if self.ttf_fira_sans.get_active():
        fn.install_arco_package(self, "ttf-fira-sans")
    if self.ttf_font_awesome.get_active():
        fn.install_arco_package(self, "ttf-font-awesome")
    if self.ttf_hack.get_active():
        fn.install_arco_package(self, "ttf-hack")
    if self.ttf_hactor.get_active():
        fn.install_arco_package(self, "ttf-hactor")
    if self.ttf_hellvetica.get_active():
        fn.install_arco_package(self, "ttf-hellvetica")
    if self.ttf_ibm_plex.get_active():
        fn.install_arco_package(self, "ttf-ibm-plex")
    if self.ttf_inconsolata.get_active():
        fn.install_arco_package(self, "ttf-inconsolata")
    if self.ttf_iosevka_nerd.get_active():
        fn.install_arco_package(self, "ttf-iosevka-nerd")
    if self.ttf_jetbrains_mono.get_active():
        fn.install_arco_package(self, "ttf-jetbrains-mono")
    if self.ttf_joypixels.get_active():
        fn.install_arco_package(self, "ttf-joypixels")
    if self.ttf_lato.get_active():
        fn.install_arco_package(self, "ttf-lato")
    if self.ttf_liberation.get_active():
        fn.install_arco_package(self, "ttf-liberation")
    if self.ttf_linux_libertine.get_active():
        fn.install_arco_package(self, "ttf-linux-libertine")
    if self.ttf_linux_libertine_g.get_active():
        fn.install_arco_package(self, "ttf-linux-libertine-g")
    if self.ttf_material_design_iconic_font.get_active():
        fn.install_arco_package(self, "ttf-material-design-iconic-font")
    if self.ttf_meslo_nerd_font_powerlevel10k.get_active():
        fn.install_arco_package(self, "ttf-meslo-nerd-font-powerlevel10k")
    if self.ttf_monofur.get_active():
        fn.install_arco_package(self, "ttf-monofur")
    if self.ttf_ms_fonts.get_active():
        fn.install_arco_package(self, "ttf-ms-fonts")
    if self.ttf_nerd_fonts_symbols.get_active():
        fn.install_arco_package(self, "ttf-nerd-fonts-symbols")
    if self.ttf_nerd_fonts_symbols_mono.get_active():
        fn.install_arco_package(self, "ttf-nerd-fonts-symbols-mono")
    if self.ttf_opensans.get_active():
        fn.install_arco_package(self, "ttf-opensans")
    if self.ttf_proggy_clean.get_active():
        fn.install_arco_package(self, "ttf-proggy-clean")
    if self.ttf_roboto.get_active():
        fn.install_arco_package(self, "ttf-roboto")
    if self.ttf_roboto_mono.get_active():
        fn.install_arco_package(self, "ttf-roboto-mono")
    if self.ttf_ubuntu_font_family.get_active():
        fn.install_arco_package(self, "ttf-ubuntu-font-family")


def remove_fonts(self):
    if self.adobe_source_sans_fonts.get_active():
        fn.remove_package(self, "adobe-source-sans-fonts")
    if self.awesome_terminal_fonts.get_active():
        fn.remove_package(self, "awesome-terminal-fonts")
    if self.nerd_fonts_source_code_pro.get_active():
        fn.remove_package(self, "nerd-fonts-source-code-pro")
    if self.noto_fonts.get_active():
        fn.remove_package(self, "noto-fonts")
    if self.ttf_anonymous_pro.get_active():
        fn.remove_package(self, "ttf-anonymous-pro")
    if self.ttf_bitstream_vera.get_active():
        fn.remove_package(self, "ttf-bitstream-vera")
    if self.ttf_caladea.get_active():
        fn.remove_package(self, "ttf-caladea")
    if self.ttf_carlito.get_active():
        fn.remove_package(self, "ttf-carlito")
    if self.ttf_cascadia_code.get_active():
        fn.remove_package(self, "ttf-cascadia-code")
    if self.ttf_cormorant.get_active():
        fn.remove_package(self, "ttf-cormorant")
    if self.ttf_croscore.get_active():
        fn.remove_package(self, "ttf-croscore")
    if self.ttf_dejavu.get_active():
        fn.remove_package(self, "ttf-dejavu")
    if self.ttf_droid.get_active():
        fn.remove_package(self, "ttf-droid")
    if self.ttf_eurof.get_active():
        fn.remove_package(self, "ttf-eurof")
    if self.ttf_fantasque_sans_mono.get_active():
        fn.remove_package(self, "ttf-fantasque-sans-mono")
    if self.ttf_fira_code.get_active():
        fn.remove_package(self, "ttf-fira-code")
    if self.ttf_fira_mono.get_active():
        fn.remove_package(self, "ttf-fira-mono")
    if self.ttf_fira_sans.get_active():
        fn.remove_package(self, "ttf-fira-sans")
    if self.ttf_font_awesome.get_active():
        fn.remove_package(self, "ttf-font-awesome")
    if self.ttf_hack.get_active():
        fn.remove_package(self, "ttf-hack")
    if self.ttf_hactor.get_active():
        fn.remove_package(self, "ttf-hactor")
    if self.ttf_hellvetica.get_active():
        fn.remove_package(self, "ttf-hellvetica")
    if self.ttf_ibm_plex.get_active():
        fn.remove_package(self, "ttf-ibm-plex")
    if self.ttf_inconsolata.get_active():
        fn.remove_package(self, "ttf-inconsolata")
    if self.ttf_iosevka_nerd.get_active():
        fn.remove_package(self, "ttf-iosevka-nerd")
    if self.ttf_jetbrains_mono.get_active():
        fn.remove_package(self, "ttf-jetbrains-mono")
    if self.ttf_joypixels.get_active():
        fn.remove_package(self, "ttf-joypixels")
    if self.ttf_lato.get_active():
        fn.remove_package(self, "ttf-lato")
    if self.ttf_liberation.get_active():
        fn.remove_package(self, "ttf-liberation")
    if self.ttf_linux_libertine.get_active():
        fn.remove_package(self, "ttf-linux-libertine")
    if self.ttf_linux_libertine_g.get_active():
        fn.remove_package(self, "ttf-linux-libertine-g")
    if self.ttf_material_design_iconic_font.get_active():
        fn.remove_package(self, "ttf-material-design-iconic-font")
    if self.ttf_meslo_nerd_font_powerlevel10k.get_active():
        fn.remove_package(self, "ttf-meslo-nerd-font-powerlevel10k")
    if self.ttf_monofur.get_active():
        fn.remove_package(self, "ttf-monofur")
    if self.ttf_ms_fonts.get_active():
        fn.remove_package(self, "ttf-ms-fonts")
    if self.ttf_nerd_fonts_symbols.get_active():
        fn.remove_package(self, "ttf-nerd-fonts-symbols")
    if self.ttf_nerd_fonts_symbols_mono.get_active():
        fn.remove_package(self, "ttf-nerd-fonts-symbols-mono")
    if self.ttf_opensans.get_active():
        fn.remove_package(self, "ttf-opensans")
    if self.ttf_proggy_clean.get_active():
        fn.remove_package(self, "ttf-proggy-clean")
    if self.ttf_roboto.get_active():
        fn.remove_package(self, "ttf-roboto")
    if self.ttf_roboto_mono.get_active():
        fn.remove_package(self, "ttf-roboto-mono")
    if self.ttf_ubuntu_font_family.get_active():
        fn.remove_package(self, "ttf-ubuntu-font-family")


def find_fonts(self):
    self.adobe_source_sans_fonts.set_active(False)
    self.awesome_terminal_fonts.set_active(False)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.noto_fonts.set_active(False)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_dejavu.set_active(False)
    self.ttf_droid.set_active(False)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hack.set_active(False)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_iosevka_nerd.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_material_design_iconic_font.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(False)
    self.ttf_opensans.set_active(False)
    self.ttf_proggy_clean.set_active(False)
    self.ttf_roboto.set_active(False)
    self.ttf_roboto_mono.set_active(False)
    self.ttf_ubuntu_font_family.set_active(False)

    if fn.check_package_installed("adapta-gtk-theme"):
        self.adapta_gtk_theme.set_active(True)

    if fn.check_package_installed("adobe-source-sans-fonts"):
        self.adobe_source_sans_fonts.set_active(True)
    if fn.check_package_installed("awesome-terminal-fonts"):
        self.awesome_terminal_fonts.set_active(True)
    if fn.check_package_installed("nerd-fonts-source-code-pro"):
        self.nerd_fonts_source_code_pro.set_active(True)
    if fn.check_package_installed("noto-fonts"):
        self.noto_fonts.set_active(True)
    if fn.check_package_installed("ttf-anonymous-pro"):
        self.ttf_anonymous_pro.set_active(True)
    if fn.check_package_installed("ttf-bitstream-vera"):
        self.ttf_bitstream_vera.set_active(True)
    if fn.check_package_installed("ttf-caladea"):
        self.ttf_caladea.set_active(True)
    if fn.check_package_installed("ttf-carlito"):
        self.ttf_carlito.set_active(True)
    if fn.check_package_installed("ttf-cascadia-code"):
        self.ttf_cascadia_code.set_active(True)
    if fn.check_package_installed("ttf-cormorant"):
        self.ttf_cormorant.set_active(True)
    if fn.check_package_installed("ttf-croscore"):
        self.ttf_croscore.set_active(True)
    if fn.check_package_installed("ttf-dejavu"):
        self.ttf_dejavu.set_active(True)
    if fn.check_package_installed("ttf-droid"):
        self.ttf_droid.set_active(True)
    if fn.check_package_installed("ttf-eurof"):
        self.ttf_eurof.set_active(True)
    if fn.check_package_installed("ttf-fantasque-sans-mono"):
        self.ttf_fantasque_sans_mono.set_active(True)
    if fn.check_package_installed("ttf-fira-code"):
        self.ttf_fira_code.set_active(True)
    if fn.check_package_installed("ttf-fira-mono"):
        self.ttf_fira_mono.set_active(True)
    if fn.check_package_installed("ttf-fira-sans"):
        self.ttf_fira_sans.set_active(True)
    if fn.check_package_installed("ttf-font-awesome"):
        self.ttf_font_awesome.set_active(True)
    if fn.check_package_installed("ttf-hack"):
        self.ttf_hack.set_active(True)
    if fn.check_package_installed("ttf-hactor"):
        self.ttf_hactor.set_active(True)
    if fn.check_package_installed("ttf-hellvetica"):
        self.ttf_hellvetica.set_active(True)
    if fn.check_package_installed("ttf-ibm-plex"):
        self.ttf_ibm_plex.set_active(True)
    if fn.check_package_installed("ttf-inconsolata"):
        self.ttf_inconsolata.set_active(True)
    if fn.check_package_installed("ttf-iosevka-nerd"):
        self.ttf_iosevka_nerd.set_active(True)
    if fn.check_package_installed("ttf-jetbrains-mono"):
        self.ttf_jetbrains_mono.set_active(True)
    if fn.check_package_installed("ttf-joypixels"):
        self.ttf_joypixels.set_active(True)
    if fn.check_package_installed("ttf-lato"):
        self.ttf_lato.set_active(True)
    if fn.check_package_installed("ttf-liberation"):
        self.ttf_liberation.set_active(True)
    if fn.check_package_installed("ttf-linux-libertine"):
        self.ttf_linux_libertine.set_active(True)
    if fn.check_package_installed("ttf-linux-libertine-g"):
        self.ttf_linux_libertine_g.set_active(True)
    if fn.check_package_installed("ttf-material-design-iconic-font"):
        self.ttf_material_design_iconic_font.set_active(True)
    if fn.check_package_installed("ttf-meslo-nerd-font-powerlevel10k"):
        self.ttf_meslo_nerd_font_powerlevel10k.set_active(True)
    if fn.check_package_installed("ttf-monofur"):
        self.ttf_monofur.set_active(True)
    if fn.check_package_installed("ttf-ms-fonts"):
        self.ttf_ms_fonts.set_active(True)
    if fn.check_package_installed("ttf-nerd-fonts-symbols"):
        self.ttf_nerd_fonts_symbols.set_active(True)
    if fn.check_package_installed("ttf-nerd-fonts-symbols-mono"):
        self.ttf_nerd_fonts_symbols_mono.set_active(True)
    if fn.check_package_installed("ttf-opensans"):
        self.ttf_opensans.set_active(True)
    if fn.check_package_installed("ttf-proggy-clean"):
        self.ttf_proggy_clean.set_active(True)
    if fn.check_package_installed("ttf-roboto"):
        self.ttf_roboto.set_active(True)
    if fn.check_package_installed("ttf-roboto-mono"):
        self.ttf_roboto_mono.set_active(True)
    if fn.check_package_installed("ttf-ubuntu-font-family"):
        self.ttf_ubuntu_font_family.set_active(True)


# ====================================================================
#                       THEMES SELECTION
# ====================================================================


def set_checkboxes_theming_all(self):
    """set the state of the checkboxes"""
    self.adapta_gtk_theme.set_active(True)
    self.arc_darkest_theme_git.set_active(True)
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
    self.arc_darkest_theme_git.set_active(True)
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
    self.arc_darkest_theme_git.set_active(False)
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
    self.arc_darkest_theme_git.set_active(False)
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
    self.breeze_icons.set_active(True)
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
    self.tela_circle_icon_theme_git.set_active(True)
    self.vimix_icon_theme_git.set_active(True)
    self.we10x_icon_theme_git.set_active(True)
    self.whitesur_icon_theme_git.set_active(True)
    self.zafiro_icon_theme.set_active(True)


def set_checkboxes_theming_icons_normal(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.breeze_icons.set_active(False)
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
    self.paper_icon_theme.set_active(True)
    self.papirus_folders_git.set_active(False)
    self.papirus_folders_gui_bin.set_active(False)
    self.papirus_folders_nordic.set_active(False)
    self.papirus_icon_theme.set_active(True)
    self.papirus_nord.set_active(False)
    self.qogir_icon_theme.set_active(False)
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)


def set_checkboxes_theming_icons_minimal(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.breeze_icons.set_active(False)
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
    self.numix_circle_arc_icons_git.set_active(True)
    self.numix_circle_icon_theme_git.set_active(True)
    self.obsidian_icon_theme.set_active(False)
    self.oranchelo_icon_theme_git.set_active(False)
    self.paper_icon_theme.set_active(False)
    self.papirus_folders_git.set_active(False)
    self.papirus_folders_gui_bin.set_active(False)
    self.papirus_folders_nordic.set_active(False)
    self.papirus_icon_theme.set_active(False)
    self.papirus_nord.set_active(False)
    self.qogir_icon_theme.set_active(False)
    self.tela_circle_icon_theme_git.set_active(False)
    self.vimix_icon_theme_git.set_active(False)
    self.we10x_icon_theme_git.set_active(False)
    self.whitesur_icon_theme_git.set_active(False)
    self.zafiro_icon_theme.set_active(False)


def set_checkboxes_theming_icons_none(self):
    """set the state of the checkboxes"""
    self.arc_icon_theme.set_active(False)
    self.breeze_icons.set_active(False)
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
    self.capitaine_cursors.set_active(True)
    self.catppuccin_cursors_git.set_active(True)
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
    self.adobe_source_sans_fonts.set_active(True)
    self.awesome_terminal_fonts.set_active(True)
    self.nerd_fonts_source_code_pro.set_active(True)
    self.noto_fonts.set_active(True)
    self.ttf_anonymous_pro.set_active(True)
    self.ttf_bitstream_vera.set_active(True)
    self.ttf_caladea.set_active(True)
    self.ttf_carlito.set_active(True)
    self.ttf_cascadia_code.set_active(True)
    self.ttf_cormorant.set_active(True)
    self.ttf_croscore.set_active(True)
    self.ttf_dejavu.set_active(True)
    self.ttf_droid.set_active(True)
    self.ttf_eurof.set_active(True)
    self.ttf_fantasque_sans_mono.set_active(True)
    self.ttf_fira_code.set_active(True)
    self.ttf_fira_mono.set_active(True)
    self.ttf_fira_sans.set_active(True)
    self.ttf_font_awesome.set_active(True)
    self.ttf_hack.set_active(True)
    self.ttf_hactor.set_active(True)
    self.ttf_hellvetica.set_active(True)
    self.ttf_ibm_plex.set_active(True)
    self.ttf_inconsolata.set_active(True)
    self.ttf_iosevka_nerd.set_active(True)
    self.ttf_jetbrains_mono.set_active(True)
    self.ttf_joypixels.set_active(True)
    self.ttf_lato.set_active(True)
    self.ttf_liberation.set_active(True)
    self.ttf_linux_libertine.set_active(True)
    self.ttf_linux_libertine_g.set_active(True)
    self.ttf_material_design_iconic_font.set_active(True)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(True)
    self.ttf_monofur.set_active(True)
    self.ttf_ms_fonts.set_active(True)
    self.ttf_nerd_fonts_symbols.set_active(True)
    self.ttf_nerd_fonts_symbols_mono.set_active(True)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(True)
    self.ttf_roboto.set_active(True)
    self.ttf_roboto_mono.set_active(True)
    self.ttf_ubuntu_font_family.set_active(True)


def set_checkboxes_fonts_normal(self):
    """set the state of the checkboxes"""
    self.adobe_source_sans_fonts.set_active(True)
    self.awesome_terminal_fonts.set_active(True)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.noto_fonts.set_active(True)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_dejavu.set_active(True)
    self.ttf_droid.set_active(True)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hack.set_active(True)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_iosevka_nerd.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_material_design_iconic_font.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(True)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(False)
    self.ttf_roboto.set_active(False)
    self.ttf_roboto_mono.set_active(False)
    self.ttf_ubuntu_font_family.set_active(False)


def set_checkboxes_fonts_minimal(self):
    """set the state of the checkboxes"""
    self.adobe_source_sans_fonts.set_active(False)
    self.awesome_terminal_fonts.set_active(False)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.noto_fonts.set_active(True)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_dejavu.set_active(True)
    self.ttf_droid.set_active(True)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hack.set_active(True)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_iosevka_nerd.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_material_design_iconic_font.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(False)
    self.ttf_opensans.set_active(True)
    self.ttf_proggy_clean.set_active(False)
    self.ttf_roboto.set_active(False)
    self.ttf_roboto_mono.set_active(False)
    self.ttf_ubuntu_font_family.set_active(False)


def set_checkboxes_fonts_none(self):
    """set the state of the checkboxes"""
    self.adobe_source_sans_fonts.set_active(False)
    self.awesome_terminal_fonts.set_active(False)
    self.nerd_fonts_source_code_pro.set_active(False)
    self.noto_fonts.set_active(False)
    self.ttf_anonymous_pro.set_active(False)
    self.ttf_bitstream_vera.set_active(False)
    self.ttf_caladea.set_active(False)
    self.ttf_carlito.set_active(False)
    self.ttf_cascadia_code.set_active(False)
    self.ttf_cormorant.set_active(False)
    self.ttf_croscore.set_active(False)
    self.ttf_dejavu.set_active(False)
    self.ttf_droid.set_active(False)
    self.ttf_eurof.set_active(False)
    self.ttf_fantasque_sans_mono.set_active(False)
    self.ttf_fira_code.set_active(False)
    self.ttf_fira_mono.set_active(False)
    self.ttf_fira_sans.set_active(False)
    self.ttf_font_awesome.set_active(False)
    self.ttf_hack.set_active(False)
    self.ttf_hactor.set_active(False)
    self.ttf_hellvetica.set_active(False)
    self.ttf_ibm_plex.set_active(False)
    self.ttf_inconsolata.set_active(False)
    self.ttf_iosevka_nerd.set_active(False)
    self.ttf_jetbrains_mono.set_active(False)
    self.ttf_joypixels.set_active(False)
    self.ttf_lato.set_active(False)
    self.ttf_liberation.set_active(False)
    self.ttf_linux_libertine.set_active(False)
    self.ttf_linux_libertine_g.set_active(False)
    self.ttf_material_design_iconic_font.set_active(False)
    self.ttf_meslo_nerd_font_powerlevel10k.set_active(False)
    self.ttf_monofur.set_active(False)
    self.ttf_ms_fonts.set_active(False)
    self.ttf_nerd_fonts_symbols.set_active(False)
    self.ttf_nerd_fonts_symbols_mono.set_active(False)
    self.ttf_opensans.set_active(False)
    self.ttf_proggy_clean.set_active(False)
    self.ttf_roboto.set_active(False)
    self.ttf_roboto_mono.set_active(False)
    self.ttf_ubuntu_font_family.set_active(False)
