# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import functions as fn


def find_slick_greeter_label(label):
    if fn.check_package_installed("lightdm-slick-greeter"):
        label.set_text("Install lightdm slick greeter (installed)")
        if fn.check_content("slick-greeter", "/etc/lightdm/lightdm.conf"):
            label.set_text("Install lightdm slick greeter (installed and active)")
    else:
        label.set_text("Install lightdm slick greeter")
