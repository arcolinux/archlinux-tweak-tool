# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================
# pylint:disable=C0301,W0104

import Functions as fn

# from types import FunctionType
# import crypt
from Functions import GLib


def create_user(self):
    username = self.hbox_username.get_text()
    name = self.hbox_name.get_text()
    atype = self.combo_account_type.get_active_text()
    password = self.hbox_password.get_text()
    confirm_password = self.hbox_confirm_password.get_text()
    user_password = "echo " + username + ":" + password

    try:
        command = "groupadd -r sambashare"
        fn.subprocess.call(
            command.split(" "),
            shell=False,
            stdout=fn.subprocess.PIPE,
            stderr=fn.subprocess.STDOUT,
        )
    except Exception as e:
        print(e)

    if password == confirm_password:
        if atype == "Administrator":
            useradd = 'useradd -m -G audio,video,network,storage,rfkill,wheel,autologin,sambashare -c "'
            +name + '" -s /bin/bash ' + username
            fn.system(useradd)
            fn.system(user_password + " | " + "chpasswd -c SHA512")
        else:
            useradd = 'useradd -m -G audio,video,network,storage,rfkill,autologin,sambashare -c "'
            +name + '" -s /bin/bash ' + username
            fn.system(useradd)
            fn.system(user_password + " | " + "chpasswd -c SHA512")
        print("User has been created")
        GLib.idle_add(fn.show_in_app_notification, self, "User has been created")
    else:
        GLib.idle_add(fn.show_in_app_notification, self, "Passwords are not the same")
        fn.MessageBox(self, "Message", "Passwords are not the same")


def on_click_delete_user(self):
    username = self.cbt_users.get_active_text()
    userdel = "userdel " + username

    fn.system(userdel)
    print("User has been deleted - home folder has not been deleted")
    GLib.idle_add(fn.show_in_app_notification, self, "User has been deleted")


def on_click_delete_all_user(self):
    username = self.cbt_users.get_active_text()
    userdel = "userdel -r -f " + username

    fn.system(userdel)
    print("User has been deleted - home folder has been deleted")
    GLib.idle_add(
        fn.show_in_app_notification, self, "User and home folder has been deleted"
    )


def pop_cbt_users(self, combo):
    combo.get_model().clear()
    users = fn.list_users("/etc/passwd")
    for user in users:
        self.cbt_users.append_text(user)
        self.cbt_users.set_active(0)
