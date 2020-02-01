#!/usr/bin/env python3

#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================


import gi
import Functions
import slim
import Gtk_Functions
import oblogout
import GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio, Gdk
from Functions import os, pacman
from Settings import settings, configparser

base_dir = os.path.dirname(os.path.realpath(__file__))


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="ArcoLinux Tweak Tool")
        self.set_border_width(10)
        self.connect("delete-event", self.on_close)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file(os.path.join(base_dir, 'images/arcolinux.png'))
        self.set_default_size(800, 550)

        self.opened = True
        self.firstrun = True
        
        GUI.GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os)

        arco_testing = Functions.check_repo("[arcolinux_repo_testing]")
        multi_testing = Functions.check_repo("[multilib-testing]")
        arch_testing = Functions.check_repo("[testing]")

        self.checkbutton.set_active(arco_testing)
        self.checkbutton2.set_active(arch_testing)
        self.checkbutton3.set_active(multi_testing)
        self.opened = False

        if not os.path.isfile("/tmp/att.lock"):
            with open("/tmp/att.lock", "w") as f:
                f.write("")

    def on_close(self, widget, data):
        os.unlink("/tmp/att.lock")
        Gtk.main_quit()

    # =====================================================
    #               PACMAN FUNCTIONS
    # =====================================================

    def on_pacman_toggle(self, widget, active):
        if self.opened == False:
            Functions.toggle_test_repos(widget.get_active(), "arco")

    def on_pacman_toggle2(self, widget, active):
        if self.opened == False:
            Functions.toggle_test_repos(widget.get_active(), "arch")

    def on_pacman_toggle3(self, widget, active):
        if self.opened == False:
            Functions.toggle_test_repos(widget.get_active(), "multilib")

    def button1_clicked(self, widget):
        self.text = self.textbox1.get_buffer()
        startiter, enditer = self.text.get_bounds()
        Functions.append_repo(
            self, self.text.get_text(startiter, enditer, True))

    # =====================================================
    #               OBLOGOUT FUNCTIONS
    # =====================================================

    def save_oblogout(self, widget):
        widget.set_sensitive(False)
        if not os.path.isfile(Functions.oblogout_conf + ".bak"):
            Functions.shutil.copy(Functions.oblogout_conf,
                                  Functions.oblogout_conf + ".bak")
        try:
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

            oblogout.set_buttons(string.rstrip().lstrip().replace(" ", ", "))
            oblogout.oblogout_change_theme(self.oblog.get_active_text())
            oblogout.set_opacity(self.hscale.get_value())
            oblogout.set_command("lock", self.lockBox.get_text())
            oblogout.set_shorcut(
                "shutdown", self.tbshutdown.get_text().capitalize())
            oblogout.set_shorcut(
                "restart", self.tbrestart.get_text().capitalize())
            oblogout.set_shorcut(
                "suspend", self.tbsuspend.get_text().capitalize())
            oblogout.set_shorcut(
                "logout", self.tblogout.get_text().capitalize())
            oblogout.set_shorcut(
                "cancel", self.tbcancel.get_text().capitalize())
            oblogout.set_shorcut(
                "hibernate", self.tbhibernate.get_text().capitalize())
            oblogout.set_shorcut("lock", self.tblock.get_text().capitalize())
            hex = Functions.rgb_to_hex(
                self.colorchooser.get_rgba().to_string())
            oblogout.set_color(hex)

            Functions.MessageBox("Success!!", "Settings Saved Successfully")
            widget.set_sensitive(True)
        except:
            pass
    
    # =====================================================
    #               Gtk FUNCTIONS
    # =====================================================
    def save_gtk3_settings(self, widget, themeCombo, iconCombo, cursorCombo, cursor_size, fonts):
        # try:
        widget.set_sensitive(False)
        # Functions.gtk3_save_settings(
        #     themeCombo.get_active_text(), "gtk-theme-name")
        # Functions.gtk3_save_settings(
        #     iconCombo.get_active_text(), "gtk-icon-theme-name")
        # Functions.gtk3_save_settings(
        #     cursorCombo.get_active_text(), "gtk-cursor-theme-name")
        # Functions.gtk3_save_settings(
        #     int(str(cursor_size.get_value()).split(".")[0]), "gtk-cursor-theme-size")
        # Functions.gtk3_save_settings(
        #     fonts.get_font_name(), "gtk-font-name")

        # Functions.set_xfce_settings(themeCombo.get_active_text(), iconCombo.get_active_text(), cursorCombo.get_active_text(), int(str(cursor_size.get_value()).split(".")[0]))
        # Functions.update_index_theme(cursorCombo.get_active_text())

        t = Functions.threading.Thread(target=Gtk_Functions.gtk_settings_saved, args=(themeCombo.get_active_text(),iconCombo.get_active_text(),cursorCombo.get_active_text(),int(str(cursor_size.get_value()).split(".")[0]),fonts.get_font()))
        t.daemon = True
        t.start()
        # subprocess.call(["xsetroot -xcf /usr/share/icons/" + self.cursorCombo.get_active_text(
        # ) + "/cursors/left_ptr " + str(self.cursor_size.get_value())], shell=True)
        # Functions.MessageBox("Success!!", "Settings Saved Successfully")
        
        widget.set_sensitive(True)
        Functions.MessageBox("Success!!", "Settings Saved Successfully")
        # except:
        #     pass

    def reset_settings(self, widget, filez):
        if os.path.isfile(filez + ".bak"):
            Functions.shutil.copy(filez + ".bak", filez)
        
        if filez == Functions.gtk3_settings:
            
            if os.path.isfile(Functions.gtk2_settings + ".bak"):
                Functions.shutil.copy(Functions.gtk2_settings + ".bak", Functions.gtk2_settings)

            Gtk_Functions.get_gtk_themes(self, self.themeCombo)
            Gtk_Functions.get_icon_themes(self, self.iconCombo)
            Gtk_Functions.get_cursor_themes(self, self.cursorCombo)

            self.cursor_size.set_value(
                float(Functions.get_gtk_settings("gtk-cursor-theme-size")))
            self.fonts.set_font(
                Functions.get_gtk_settings("gtk-font-name"))
            Functions.subprocess.call(["xsetroot -xcf /usr/share/icons/" + self.cursorCombo.get_active_text(
            ) + "/cursors/left_ptr " + str(self.cursor_size.get_value())], shell=True)

        elif filez == Functions.oblogout_conf:
            self.oblog.get_model().clear()
            vals = oblogout.get_opacity()
            self.hscale.set_value(vals)
            try:
                self.tbcancel.set_text(oblogout.get_shortcut("cancel"))
                self.tbshutdown.set_text(oblogout.get_shortcut("shutdown"))
                self.tbsuspend.set_text(oblogout.get_shortcut("suspend"))
                self.tbrestart.set_text(oblogout.get_shortcut("restart"))
                self.tblogout.set_text(oblogout.get_shortcut("logout"))
                self.tbhibernate.set_text(oblogout.get_shortcut("hibernate"))
                self.tblock.set_text(oblogout.get_shortcut("lock"))
            except:
                pass
            self.lockBox.set_text(oblogout.get_command("lock"))
            color = Gdk.RGBA()
            color.parse(oblogout.get_color())
            self.colorchooser.set_rgba(color)
            btnString = oblogout.get_buttons()
            oblogout.oblog_populate(self.oblog)

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

    
    #====================================================================
    #                       HBlock
    #====================================================================
    def set_hblock(self, widget, state):
        if not self.firstrun == True:
            t = Functions.threading.Thread(target=Functions.set_hblock, args=(
                self, widget, widget.get_active()))
            # t.daemon = True
            t.start()
            # Functions.set_hblock(self, widget, widget.get_active())
        else:
            self.firstrun = False
    
    #====================================================================
    #                       GRUB
    #====================================================================
    def on_set_grub_wallpaper(self, widget):
        Functions.set_grub_wallpaper(self.grub_theme_combo.get_active_text())

    def on_reset_grub_wallpaper(self, widget):
        if os.path.isfile(Functions.grub_theme_conf + ".bak"):
            Functions.shutil.copy(Functions.grub_theme_conf + ".bak", Functions.grub_theme_conf)
        self.pop_themes_grub(self.grub_theme_combo, Functions.get_grub_wallpapers())

    def pop_themes_grub(self, combo, lists, start):
        if os.path.isfile(Functions.grub_theme_conf):
            combo.get_model().clear()
            with open(Functions.grub_theme_conf, "r") as f:
                listss = f.readlines()
                f.close()

            val = Functions._get_position(listss, "desktop-image: ")
            bg_image = listss[val].split(" ")[1].replace("\"", "").lstrip().rstrip()

            for i in range(len(lists)):
                combo.append_text(lists[i])
                if start == True:
                    if(lists[i] == bg_image):
                        combo.set_active(i)
                else:
                    if(lists[i] == os.path.basename(self.tbimage.get_text())):
                        combo.set_active(i)
                    

    def on_grub_theme_change(self, widget, image):
        try:
            pixbuf3 = GdkPixbuf.Pixbuf().new_from_file_at_size('/boot/grub/themes/Vimix/' + widget.get_active_text(), 345, 345)
            self.image.set_from_pixbuf(pixbuf3)
        except:
            pass
    def on_import_wallpaper(self, widget):
        text = self.tbimage.get_text()
        if len(text) > 1:
            print(os.path.basename(text))
            Functions.shutil.copy(text, '/boot/grub/themes/Vimix/' + os.path.basename(text))
            self.pop_themes_grub(self.grub_theme_combo, Functions.get_grub_wallpapers(), False)

    def on_remove_wallpaper(self, widget):
        widget.set_sensitive(False)
        if os.path.isfile('/boot/grub/themes/Vimix/' + self.grub_theme_combo.get_active_text()):
            os.unlink('/boot/grub/themes/Vimix/' + self.grub_theme_combo.get_active_text())
            self.pop_themes_grub(self.grub_theme_combo, Functions.get_grub_wallpapers(), True)
        widget.set_sensitive(True)

    def on_choose_wallpaper(self, widget):
        dialog = Gtk.FileChooserDialog(
				title="Please choose a file",
				action=Gtk.FileChooserAction.OPEN,)
        filter = Gtk.FileFilter()
        filter.set_name("IMAGE Files")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpg")
        filter.add_mime_type("image/jpeg")
        dialog.set_filter(filter)
        dialog.set_current_folder(Functions.home)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Open", Gtk.ResponseType.OK)
        dialog.connect("response", self.open_response_cb)
 
        dialog.show()

        
    def open_response_cb(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            self.tbimage.set_text(dialog.get_filename())
            dialog.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()


    
    #====================================================================
    #                       SLIMLOCK
    #====================================================================
    
    def on_slim_apply(self, widget):
        if not os.path.isfile(Functions.slimlock_conf + ".bak"):
            Functions.shutil.copy(Functions.slimlock_conf, Functions.slimlock_conf + ".bak")
        slim.set_slimlock(self.slimbox.get_active_text())
        


    def on_slim_reset(self, widget):
        if os.path.isfile(Functions.slimlock_conf + ".bak"):
            Functions.shutil.copy(Functions.slimlock_conf + ".bak", Functions.slimlock_conf)
        slim.get_slimlock(self.slimbox)
 
    def on_slim_theme_change(self, widget, image):
        try:
            path = '/usr/share/slim/themes/' + widget.get_active_text()
            pixbuf4 = GdkPixbuf.Pixbuf().new_from_file_at_size(path + "/background.png", 345, 345)
            self.image2.set_from_pixbuf(pixbuf4)

            pixbuf5 = GdkPixbuf.Pixbuf().new_from_file_at_size(path + "/panel.png", 345, 345)
            self.image3.set_from_pixbuf(pixbuf5)
        except:
            pass

    def on_browser_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
				title="Please choose a file",
				action=Gtk.FileChooserAction.OPEN,)
        filter = Gtk.FileFilter()
        filter.set_name("IMAGE Files")
        filter.add_mime_type("image/png")
        dialog.set_filter(filter)
        dialog.set_current_folder(Functions.home)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Open", Gtk.ResponseType.OK)
        dialog.connect("response", self.open_response_slim)
 
        dialog.show()

        
    def open_response_slim(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            self.slimtext.set_text(dialog.get_filename())
            dialog.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

    def on_create_theme_clicked(self, widget):
        path = "/usr/share/slim/themes/"
        if os.path.isdir(path):
            if len(self.slimtheme.get_text()) >= 3 and len(self.slimtext.get_text()) > 3:
                try:
                    os.mkdir(path + self.slimtheme.get_text())
                except:
                    pass

                Functions.shutil.copy(base_dir + "/slim_data/info.txt",  path + self.slimtheme.get_text() + "/info.txt")
                Functions.shutil.copy(base_dir + "/slim_data/panel.png",  path + self.slimtheme.get_text() + "/panel.png")
                Functions.shutil.copy(base_dir + "/slim_data/slim.theme",  path + self.slimtheme.get_text() + "/slim.theme")
                Functions.shutil.copy(self.slimtext.get_text(), path + self.slimtheme.get_text() + "/background.png")

                slim.reload_import(self.slimbox, self.slimtheme.get_text())

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
                f.close()

            if Functions.checkIfProcessRunning(int(pid)):
                Functions.MessageBox("Application Running!", "You first need to close the existing application")
            else:
                os.unlink("/tmp/att.lock")
