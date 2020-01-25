#!/usr/bin/env python3
import Settings
import GUI
import Functions
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio
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

        GUI.GUI(self, Gtk, GdkPixbuf, base_dir, os)

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

        if not os.path.isfile(home + "/.config/arcolinux-tweak-tool/att.lock"):
            with open(home + "/.config/arcolinux-tweak-tool/att.lock", "w") as f:
                f.write("")
            
    def on_close(self, widget, data):
        os.unlink(home + "/.config/arcolinux-tweak-tool/att.lock")
        Gtk.main_quit()
    
    
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


    def oblog_changed(self, widget):
        Functions.oblogout_change_theme(widget.get_active_text())


if __name__ == "__main__":
    if not os.path.isfile(home + "/.config/arcolinux-tweak-tool/att.lock"):
        w = Main()
        w.show_all()
        Gtk.main()
