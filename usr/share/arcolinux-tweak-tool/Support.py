import gi
import Functions
from Functions import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

base_dir = os.path.dirname(os.path.realpath(__file__))

class Support(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Credits - Support Development", parent, 0)
        # self.add_buttons(Gtk.STOCK_OK,Gtk.ResponseType.OK)
        
        self.set_default_size(550, 200)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        box = self.get_content_area()
        box.pack_start(vbox, False, False, 0)
        
        label = Gtk.Label()
        label.set_line_wrap(True)
        label.set_markup("Big thank you to our developers for there work on this project.\n\
Brad Heffernan is the driving force aka developer behind the ArcoLinux Tweak Tool. \n\
with Krisztian Veress and Erik Dubois")

        label2 = Gtk.Label()
        label2.set_markup("Support Brad on patreon")
        # =====================================================
        #               PATREON LINK
        # =====================================================
        pE = Gtk.EventBox()
        ppE = Gtk.EventBox()

        pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/patreon.png'), 30, 30)
        pimage = Gtk.Image().new_from_pixbuf(pbp)

        logo = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/arcolinux-red.png'), 100, 100)
        logo_image = Gtk.Image().new_from_pixbuf(logo)

        pE.add(pimage)

        pE.connect("button_press_event", self.on_support_click, "https://www.patreon.com/hefftor")
        pE.set_property("has-tooltip", True)

        pE.connect("query-tooltip", self.tooltip_callback, "Support BradHeff on Patreon")

        

        pbpp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/paypal.png'), 30, 30)
        ppimage = Gtk.Image().new_from_pixbuf(pbpp)

        ppE.add(ppimage)

        ppE.connect("button_press_event", self.on_support_click, "https://PayPal.Me/heffserver")
        ppE.set_property("has-tooltip", True)

        ppE.connect("query-tooltip", self.tooltip_callback, "Buy BradHeff a coffee")

        hbox.pack_start(label, True, True, 10)
        
        # https://www.paypal.com/paypalme/my/profile
        hbox1.pack_start(label2, False, False, 10)
        hbox1.pack_start(pE, False, False, 0)
        hbox1.pack_start(ppE, False, False, 0)
        
        vbox.pack_start(logo_image, False, False, 10)
        vbox.pack_start(hbox, True, True, 10)
        # vbox.pack_start(spacer, True, True, 0)
        vbox.pack_end(hbox1, False, False, 0)

        self.show_all()



    def on_support_click(self, widget, event, link):
        t = Functions.threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()
        # print("CLICKED")
        # self.weblink(link)


    def weblink(self, link):
        Functions.subprocess.call(["sudo", "-H", "-u", Functions.sudo_username, "bash", "-c", "exo-open --launch webbrowser " + link], shell=False)
        # webbrowser.open_new_tab(link)

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True