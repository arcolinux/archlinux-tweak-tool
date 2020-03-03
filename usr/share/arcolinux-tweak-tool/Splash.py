import gi
from Functions import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class splashScreen(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, Gtk.WindowType.POPUP, title='')
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_size_request(500, 250)
        self.set_position(Gtk.WindowPosition.CENTER)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        self.add(main_vbox)

        self.image = Gtk.Image()
        pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir +
                                                          "/images/splash.png",
                                                          500, 250)
        self.image.set_from_pixbuf(pimage)

        main_vbox.pack_start(self.image, True, True, 0)

        self.show_all()
