import gi
from Functions import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class splashScreen():
    def __init__(self):
        super(splashScreen, self).__init__()
        self.window = Gtk.Window(Gtk.WindowType.POPUP)
        self.window.set_decorated(False)
        self.window.set_size_request(400, 150)
        self.window.set_position(Gtk.WindowPosition.CENTER)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        self.window.add(main_vbox)

        self.image = Gtk.Image()
        pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir +
                                                          "/images/splash.png",
                                                          400, 200)
        self.image.set_from_pixbuf(pimage)

        main_vbox.pack_start(self.image, True, True, 0)
        self.window.show_all()
