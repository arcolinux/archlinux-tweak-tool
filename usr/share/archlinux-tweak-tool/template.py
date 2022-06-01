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

def choose_smb_conf(self,widget):
    choice = self.samba_choices.get_active_text()

    #options_samba = ['ArcoLinux', 'Example', 'Original']
    if choice == "ArcoLinux":
        Functions.copy_samba("arco")
        print("smb.conf from ArcoLinux")
        GLib.idle_add(Functions.show_in_app_notification, self, "Smb.conf from ArcoLinux")
    elif choice == "Easy":
        Functions.copy_samba("example")
        GLib.idle_add(Functions.show_in_app_notification, self, "Smb.conf easy configuration applied")
    elif choice == "Usershares":
        Functions.copy_samba("usershares")
        GLib.idle_add(Functions.show_in_app_notification, self, "Smb.conf usershares configuration applied")
    elif choice == "Windows":
        Functions.copy_samba("windows")
        GLib.idle_add(Functions.show_in_app_notification, self, "Smb.conf windows configuration applied")
    elif choice == "Original":
        Functions.copy_samba("original")
        print("Smb.conf from gitlab of Samba")
        GLib.idle_add(Functions.show_in_app_notification, self, "Smb.conf from gitlab of Samba")

def create_samba_user(self,widget):

    username = Functions.sudo_username
    #password = self.entry_password.get_text()

    if username:
        #user_password = "echo " + username + ":" + password

        # com = Functions.subprocess.run(["sh", "-c", "su - " + Functions.sudo_username + " -c groups"], shell=False, stdout=Functions.subprocess.PIPE)
        # groups = com.stdout.decode().strip().split(" ")
        # # print(groups)
        # if "sambashare" not in groups:
        #     Functions.subprocess.run(["gpasswd", "-a", Functions.sudo_username, "sambashare"], shell=False)

        # useradd ='useradd -m -G autologin,audio,video,network,storage,rfkill,wheel,sambashare -c "'  + username + '" -s /bin/bash ' + username
        # Functions.os.system(useradd)
        # Functions.os.system(user_password + " | " + "chpasswd -c SHA512")

        Functions.install_alacritty(self)
        print("Type in your password for the Sambashare")
        print("Although the user name is shared with Linux system, Samba uses a password")
        print("separate from that of the Linux user accounts.")
        try:
            Functions.subprocess.call("alacritty -e /usr/bin/smbpasswd -a " + username,
                            shell=True,
                            stdout=Functions.subprocess.PIPE,
                            stderr=Functions.subprocess.STDOUT)
            print("Created a password for the current user")
            GLib.idle_add(Functions.show_in_app_notification, self, "Created a password for the current user")
        except Exception as e:
           print(e)
    else:
        print("First fill in your username")
        GLib.idle_add(Functions.show_in_app_notification, self, "First fill in your username")

def delete_samba_user(self,widget):

    username = self.samba_users.get_active_text()

    if username:
        Functions.install_alacritty(self)
        Functions.subprocess.call("alacritty -e /usr/bin/smbpasswd -x " + username,
                        shell=True,
                        stdout=Functions.subprocess.PIPE,
                        stderr=Functions.subprocess.STDOUT)
        print("Deleting the selected user from Samba...")
        GLib.idle_add(Functions.show_in_app_notification, self, "Deleting the selected user from Samba...")
    else:
        print("Make a selection")
        GLib.idle_add(Functions.show_in_app_notification, self, "Make a selection")

def delete_user(self,widget):

    username = self.samba_users.get_active_text()

    if username:
        userdel ='userdel ' + username
        Functions.os.system(userdel)
        print("The user " + username + " has been completely deleted from your system")
        GLib.idle_add(Functions.show_in_app_notification, self, "User deleted from system")
    else:
        print("Something went wrong")

def restart_smb(self,widget):

    if Functions.check_service("smb"):
        restart ='systemctl restart smb'
        Functions.os.system(restart)
        print("Restarting smb service...")
        GLib.idle_add(Functions.show_in_app_notification, self, "Restarting smb service...")
    else:
        print("Did you install samba - check for errors")
        print("Type in a terminal")
        print("   sudo systemctl status smb")
        GLib.idle_add(Functions.show_in_app_notification, self, "Did you install samba - check for errors")
