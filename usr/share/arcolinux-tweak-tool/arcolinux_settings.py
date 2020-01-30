#!/usr/bin/env python3

import gi
from gi.repository import GLib


import dbus
import dbus.service
import dbus.mainloop.glib
import subprocess


class ArcoLinux(dbus.service.Object):

    def __init__(self, conn=None, object_path=None, bus_name=None):
        dbus.service.Object.__init__(self, conn, object_path, bus_name)

    # Write file.

    @dbus.service.method("org.arcolinux.ObInterface", in_signature='', out_signature='')
    def save_file(self, filename, list):
        with open(filename, 'w') as f:
            for item in list:
                f.write(item)

    # Run command.

    @dbus.service.method("org.arcolinux.ObInterface", in_signature='', out_signature='')
    def shell_commands(self, command):
        subprocess.call([command], shell=True)

    @dbus.service.method("org.arcolinux.ObInterface", in_signature='', out_signature='')
    def Exit(self):
        mainloop.quit()


if __name__ == "__main__":
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    name = dbus.service.BusName("org.arcolinux.ObService", bus)
    object = ArcoLinux(bus, "/ArcoLinux")

    mainloop = GLib.MainLoop()
    print("Running example service.")
    mainloop.run()
