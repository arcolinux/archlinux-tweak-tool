# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

import Functions
from Functions import GLib

def choose_nsswitch(self,widget):
    choice = self.nsswitch_choices.get_active_text()

    #options = ['ArcoLinux', 'Garuda', 'Arch Linux', 'EndeavourOS']
    if choice == "ArcoLinux":
        Functions.copy_nsswitch("arco")
        print("Nsswitch from ArcoLinux")
        GLib.idle_add(Functions.show_in_app_notification, self, "Nsswitch from ArcoLinux")
    elif choice == "Garuda":
        Functions.copy_nsswitch("garuda")
        print("Nsswitch from Garuda")
        GLib.idle_add(Functions.show_in_app_notification, self, "Nsswitch from Garuda")
    elif choice == "Arch Linux":
        Functions.copy_nsswitch("arch")
        print("Nsswitch from Arch Linux")
        GLib.idle_add(Functions.show_in_app_notification, self, "Nsswitch from Arch Linux")
    else:
        Functions.copy_nsswitch("eos")
        print("Nsswitch from EndeavourOS")
        GLib.idle_add(Functions.show_in_app_notification, self, "Nsswitch from EndeavourOS")