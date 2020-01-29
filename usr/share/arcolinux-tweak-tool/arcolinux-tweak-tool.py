#!/usr/bin/env python3
import Settings
import GUI
import Functions
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio, Gdk
from Settings import settings, configparser
from Functions import os, home, pacman

base_dir = os.path.dirname(os.path.realpath(__file__))

class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="ArcoLinux Tweak Tool")
        self.set_border_width(10)
        self.connect("delete-event", self.on_close)        
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file(os.path.join(base_dir, 'images/arcolinux.png'))
        self.set_size_request(700, 500)

        self.opened = True

        GUI.GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os)

        if not os.path.exists(home + "/.config/arcolinux-tweak-tool"):
            os.mkdir(home + "/.config/arcolinux-tweak-tool")

        if not os.path.isfile(settings):
            key = {
                'arco-testing-repo': 'False',
                'arch-testing-repo': 'False',
                'multilib-testing-repo': 'False'
            }
            Settings.make_file('Pacman', key)
            self.opened = False
        else:
            try:
                arco = Settings.read_settings('Pacman', 'arco-testing-repo')
                arch = Settings.read_settings('Pacman', 'arch-testing-repo')
                multi = Settings.read_settings('Pacman', 'multilib-testing-repo')

                self.checkbutton.set_active(eval(arco))
                self.checkbutton2.set_active(eval(arch))
                self.checkbutton3.set_active(eval(multi))
            except:
                pass

            self.opened = False

        if not os.path.isfile("/tmp/att.lock"):
            with open("/tmp/att.lock", "w") as f:
                f.write("")
            
    def on_close(self, widget, data):
        os.unlink("/tmp/att.lock")
        Gtk.main_quit()
    
    #=====================================================
    #               PACMAN FUNCTIONS
    #=====================================================

    def on_pacman_toggle(self, widget, active):
        if self.opened == False:
            key = {
                'arco-testing-repo': str(self.checkbutton.get_active()),
                'arch-testing-repo': str(self.checkbutton2.get_active()),
                'multilib-testing-repo': str(self.checkbutton3.get_active())
            }
            Settings.write_settings("Pacman", key)
            Functions.toggle_test_repos(widget.get_active(), "arco")

    def on_pacman_toggle2(self, widget, active):
        if self.opened == False:
            print("WRITE")
            key = {
                'arco-testing-repo': str(self.checkbutton.get_active()),
                'arch-testing-repo': str(self.checkbutton2.get_active()),
                'multilib-testing-repo': str(self.checkbutton3.get_active())
            }
            Settings.write_settings("Pacman", key)
            Functions.toggle_test_repos(widget.get_active(), "arch")

    def on_pacman_toggle3(self, widget, active):
        if self.opened == False:
            print("WRITE")
            key = {
                'arco-testing-repo': str(self.checkbutton.get_active()),
                'arch-testing-repo': str(self.checkbutton2.get_active()),
                'multilib-testing-repo': str(self.checkbutton3.get_active())
            }
            Settings.write_settings("Pacman", key)
            Functions.toggle_test_repos(widget.get_active(), "multilib")


    def button1_clicked(self, widget):
        self.text = self.textbox1.get_buffer()
        startiter, enditer = self.text.get_bounds()
        Functions.append_repo(self, self.text.get_text(startiter, enditer, True))


    #=====================================================
    #               OBLOGOUT FUNCTIONS
    #=====================================================
    
    def save_oblogout(self, widget):
        if not os.path.isfile(Functions.oblogout_conf + ".bak"):
            Functions.shutil.copy(Functions.oblogout_conf, Functions.oblogout_conf + ".bak")

        string = ""
        if self.check_shut.get_active():
            string += "shutdown "
        if self.check_restart.get_active():
            string += "restart "
        if self.check_logout.get_active():
            string += "logout "
        if self.check_cancel.get_active():
            string += "cancel "
        if self.check_susp.get_active():
            string += "suspend "
        if self.check_hiber.get_active():
            string += "hibernate "
        if self.check_lock.get_active():
            string += "lock "

        
        Functions.set_buttons(string.rstrip().lstrip().replace(" ", ", "))
        Functions.oblogout_change_theme(self.oblog.get_active_text())
        Functions.set_value(self.hscale.get_value())
        Functions.set_lockscreen(self.lockBox.get_text())
        Functions.oblogout_change_keybinds(self)
        hex = Functions.rgb_to_hex(self.colorchooser.get_rgba().to_string())
        Functions.set_color(hex)


    # def oblog_changed(self, widget):
    #     Functions.oblogout_change_theme(widget.get_active_text())

    # def scale_moved(self, widget):
    #     Functions.set_value(widget.get_value())

    # def on_buttons_set(self, widget):
    #     string = ""
    #     if self.check_shut.get_active():
    #         string += "shutdown "
    #     if self.check_restart.get_active():
    #         string += "restart "
    #     if self.check_logout.get_active():
    #         string += "logout "
    #     if self.check_cancel.get_active():
    #         string += "cancel "
    #     if self.check_susp.get_active():
    #         string += "suspend "
    #     if self.check_hiber.get_active():
    #         string += "hibernate "
    #     if self.check_lock.get_active():
    #         string += "lock "

        
    #     Functions.set_buttons(string.rstrip().replace(" ", ", "))

    # def on_locks_set(self, widget):
    #     Functions.set_lockscreen(self.lockBox.get_text())

    # def on_color_chosen(self, widget):
    #     print(widget.get_rgba().to_string())
    #     hex = Functions.rgb_to_hex(widget.get_rgba().to_string())
    #     Functions.set_color(hex)
    
    def save_gtk3_settings(self, widget, themeCombo, iconCombo, cursorCombo, cursor_size, fonts):
        Functions.gtk3_save_settings(themeCombo.get_active_text(), "gtk-theme-name")
        Functions.gtk3_save_settings(iconCombo.get_active_text(), "gtk-icon-theme-name")
        Functions.gtk3_save_settings(cursorCombo.get_active_text(), "gtk-cursor-theme-name")
        Functions.gtk3_save_settings(cursor_size.get_value(), "gtk-cursor-theme-size")
        Functions.gtk3_save_settings(fonts.get_font_name(), "gtk-font-name")

    def reset_settings(self, widget, filez):
        print(filez)
        if os.path.isfile(filez + ".bak"):
            Functions.shutil.copy(filez + ".bak", filez)
        if filez == Functions.gtk3_settings:
            Functions.get_gtk_themes(self, self.themeCombo)
            Functions.get_icon_themes(self, self.iconCombo)
            Functions.get_cursor_themes(self, self.cursorCombo)

            self.cursor_size.set_value(float(Functions.get_gtk_settings(self, "gtk-cursor-theme-size")))
            self.fonts.set_font_name(Functions.get_gtk_settings(self, "gtk-font-name"))
        
        elif filez == Functions.oblogout_conf:
            self.oblog.get_model().clear()
            vals = Functions.get_value()
            self.hscale.set_value(vals)
            Functions.keybinds_populate(self)
            self.lockBox.set_text(Functions.get_lockscreen())
            color = Gdk.RGBA()
            color.parse(Functions.get_color())
            self.colorchooser.set_rgba(color)
            btnString = Functions.get_buttons()
            Functions.oblog_populate(self.oblog)
            
            
            if "shutdown" in btnString:
                self.check_shut.set_active(True)
            if "lock" in btnString:
                self.check_lock.set_active(True)
            if "logout" in btnString:
                self.check_logout.set_active(True)
            if "restart" in btnString:
                self.check_restart.set_active(True)
            if "cancel" in btnString:
                self.check_cancel.set_active(True)
            if "suspend" in btnString:
                self.check_susp.set_active(True)
            if "hibernate" in btnString:
                self.check_hiber.set_active(True)


if __name__ == "__main__":
    if not os.path.isfile("/tmp/att.lock"):
        with open("/tmp/att.pid", "w") as f:
            f.write(str(os.getpid()))
            f.close()
        w = Main()
        w.show_all()
        Gtk.main()
    else:
        md = Gtk.MessageDialog(parent=Main(), flags=0, message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.YES_NO, text="Lock File Found")
        md.format_secondary_markup(
            "The lock file has been found. This indicates there is already an instance of <b>Arcolinux Tweak tool</b> running.\n\
click yes to remove the lock file and try running again")

        result = md.run()
        md.destroy()

        if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
            pid = ""
            with open("/tmp/att.pid", "r") as f:
                line = f.read()
                pid = line.rstrip().lstrip()
                print(pid)
                f.close()

            if Functions.checkIfProcessRunning(int(pid)):
                md2 = Gtk.MessageDialog(parent=Main(), flags=0, message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK, text="Application Running!")
                md2.format_secondary_markup(
                    "You first need to close the existing application")

                result = md2.run()
                md2.destroy()
            else:
                os.unlink("/tmp/att.lock")
