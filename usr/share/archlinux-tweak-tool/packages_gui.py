# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import functions as fn
from packages import Packages


def gui(self, Gtk, vbox_stack, fn):
    """create a gui"""
    try:
        packages_obj = Packages()

        hbox_title = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl_packages_title = Gtk.Label(xalign=0)
        lbl_packages_title.set_name("title")
        lbl_packages_title.set_text("Packages")

        hbox_title_export = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label_export_title = Gtk.Label(xalign=0)
        label_export_title.set_markup("<b> Export Packages</b>")

        label_export_desc = Gtk.Label(xalign=0)
        label_export_desc.set_markup(
            f""
            f" <b>No AUR packages are exported</b>\n"
            f" - Option: All Installed Packages will export all packages currently installed on your system (lots of packages)\n"
            f" - Option: Explicitly Installed Packages (recommended) will export installed packages only found in sync db (less packages)\n"
            f" - Tip: To see packages installed from AUR in the terminal type: pacman -Qqem\n\n"
            f""
            f" A list of installed packages will be exported to <b>{packages_obj.default_export_path}</b>"
        )

        hbox_title_export.pack_start(label_export_title, False, False, 0)

        hbox_desc_export = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        hbox_desc_export.pack_start(label_export_desc, False, False, 0)

        hbox_title.pack_start(lbl_packages_title, False, False, 0)

        hbox_title_install = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label_install_title = Gtk.Label(xalign=0)
        label_install_title.set_markup("<b> Install Packages</b>")

        hbox_title_install.pack_start(label_install_title, False, False, 0)

        hbox_sep = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hsep = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox_sep.pack_start(hsep, True, True, 0)

        button_export_packages = Gtk.Button(label=" Export Packages")

        rb_export_all = Gtk.RadioButton.new_with_label_from_widget(
            None, "All Installed Packages"
        )
        rb_export_all.set_name("rb_packages_export_all")

        rb_export_explicit = Gtk.RadioButton.new_from_widget(rb_export_all)
        rb_export_explicit.set_label("Explicitly Installed Packages")
        rb_export_explicit.set_name("rb_packages_export_explicit")
        rb_export_explicit.set_active(True)

        button_export_packages.connect(
            "clicked",
            self.on_click_export_packages,
            packages_obj,
            rb_export_all,
            rb_export_explicit,
        )
        button_export_packages.set_size_request(100, 30)

        lbl_export_padding1 = Gtk.Label(xalign=0, yalign=0)
        lbl_export_padding1.set_text(" ")
        grid_export = Gtk.Grid()

        grid_export.attach(rb_export_explicit, 0, 2, 1, 1)
        grid_export.attach_next_to(
            lbl_export_padding1, rb_export_explicit, Gtk.PositionType.RIGHT, 1, 1
        )

        grid_export.attach_next_to(
            rb_export_all, lbl_export_padding1, Gtk.PositionType.RIGHT, 1, 1
        )

        hbox_export_button = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox_export_button.pack_start(button_export_packages, False, False, 10)

        hbox_install = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        label_install_desc = Gtk.Label(xalign=0, yalign=0)
        label_install_desc.set_markup(
            f""
            f" <b>WARNING: Proceed with caution this will install packages onto your system!</b>\n"
            f" <b>Packages from the AUR are not supported </b>\n"
            f" <b>This also performs a full system upgrade</b>\n\n"
            f" - A list of packages are sourced from <b>{packages_obj.default_export_path}</b>\n"
            f" - To ignore a package, add a # in front of the package name\n"
            f" - Log file: {packages_obj.logfile}\n"
            f" - A reboot is recommended when core Linux packages are installed"
        )

        label_package_status = Gtk.Label(xalign=0, yalign=0)
        label_package_count = Gtk.Label(xalign=0, yalign=0)

        vbox_pacmanlog = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        textbuffer_pacmanlog = Gtk.TextBuffer()

        textview_pacmanlog = Gtk.TextView()
        textview_pacmanlog.set_property("editable", False)
        textview_pacmanlog.set_property("monospace", True)
        textview_pacmanlog.set_border_width(10)
        textview_pacmanlog.set_vexpand(True)
        textview_pacmanlog.set_hexpand(True)
        textview_pacmanlog.set_name("textview_log")

        textview_pacmanlog.set_buffer(textbuffer_pacmanlog)

        pacmanlog_scrolledwindow = Gtk.ScrolledWindow()
        pacmanlog_scrolledwindow.set_propagate_natural_height(True)
        pacmanlog_scrolledwindow.set_propagate_natural_width(True)
        pacmanlog_scrolledwindow.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC
        )
        pacmanlog_scrolledwindow.add(textview_pacmanlog)

        button_install_packages = Gtk.Button(label="Install Packages")

        gui_parts = (
            vbox_stack,
            label_package_status,
            vbox_pacmanlog,
            textbuffer_pacmanlog,
            textview_pacmanlog,
            label_package_count,
        )

        button_install_packages.connect(
            "clicked",
            self.on_click_install_packages,
            packages_obj,
            gui_parts,
        )
        button_install_packages.set_size_request(100, 30)

        hbox_install_button = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox_install_button.pack_start(button_install_packages, False, False, 10)

        vbox_pacmanlog.pack_start(pacmanlog_scrolledwindow, False, False, 0)

        hbox_install.pack_start(label_install_desc, False, False, 0)

        vbox_stack.pack_start(hbox_title, False, False, 0)
        vbox_stack.pack_start(hbox_sep, False, False, 0)
        vbox_stack.pack_start(hbox_title_export, False, False, 0)
        vbox_stack.pack_start(hbox_desc_export, False, False, 0)

        vbox_stack.pack_start(grid_export, False, False, 0)
        vbox_stack.pack_start(hbox_export_button, False, False, 0)

        vbox_stack.pack_start(hbox_title_install, False, False, 0)
        vbox_stack.pack_start(hbox_install, False, False, 0)
        vbox_stack.pack_start(hbox_install_button, False, False, 0)

    except Exception as e:
        fn.logger.error("Exception in packages_gui.gui(): %s" % e)
