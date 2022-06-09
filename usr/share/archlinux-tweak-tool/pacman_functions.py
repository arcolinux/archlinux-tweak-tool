import Functions

# =================================================================
# =             Author: Cameron Percival    Erik Dubois           =
# =================================================================


def append_repo(self, text):
    with open(Functions.pacman, "a") as myfile:
        myfile.write("\n\n")
        myfile.write(text)

    Functions.show_in_app_notification(self, "Settings Saved Successfully")

    # MessageBox(self, "Success!!", "Settings applied successfully")

def append_mirror(self, text):
    with open(Functions.arcolinux_mirrorlist, "a") as myfile:
        myfile.write("\n\n")
        myfile.write(text)

    Functions.show_in_app_notification(self, "Settings Saved Successfully")


def insert_repo(self, text):
    with open(Functions.pacman, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    pos = Functions._get_position(lines, "[custom]")
    num = pos+3

    lines.insert(num, "\n" + text + "\n")

    with open(Functions.pacman, "w") as f:
        f.writelines(lines)
        f.close()


def check_repo(value):
    with open(Functions.pacman, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            if "#" + value in line:
                return False
            else:
                return True
    return False

def check_mirror(value):
    with open(Functions.arcolinux_mirrorlist, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            if "#" + value in line:
                return False
            else:
                return True
    return False


def repo_exist(value):
    with open(Functions.pacman, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False

def mirror_exist(value):
    with open(Functions.arcolinux_mirrorlist, "r", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            return True
    return False


def pacman_on(repo, lines, i, line):
    if repo in line:
        lines[i] = line.replace("#", "")
        if (i+1) < len(lines):
            lines[i + 1] = lines[i + 1].replace("#", "")
        if (i+2) < len(lines) and "Include" in lines[i+2]:
            lines[i + 2] = lines[i + 2].replace("#", "")

def mirror_on(mirror, lines, i, line):
    if mirror in line:
        lines[i] = line.replace("#", "")
        if (i+1) < len(lines):
            lines[i + 1] = lines[i + 1].replace("#", "")
        if (i+2) < len(lines) and "Include" in lines[i+2]:
            lines[i + 2] = lines[i + 2].replace("#", "")


def pacman_off(repo, lines, i, line):
    if repo in line:
        if "#" not in lines[i]:
            lines[i] = line.replace(lines[i], "#" + lines[i])
        if (i+1) < len(lines):
            if "#" not in lines[i + 1]:
                lines[i + 1] = lines[i + 1].replace(lines[i + 1],
                                                    "#" + lines[i + 1])
        if (i+2) < len(lines) and "Include" in lines[i+2]:
            if "#" not in lines[i + 2]:
                lines[i + 2] = lines[i + 2].replace(lines[i + 2],
                                                    "#" + lines[i + 2])

def mirror_off(mirror, lines, i, line):
    if mirror in line:
        if "#" not in lines[i]:
            lines[i] = line.replace(lines[i], "#" + lines[i])
        # if (i+1) < len(lines):
        #     if "#" not in lines[i + 1]:
        #         lines[i + 1] = lines[i + 1].replace(lines[i + 1],
        #                                             "#" + lines[i + 1])
        # if (i+2) < len(lines) and "Include" in lines[i+2]:
        #     if "#" not in lines[i + 2]:
        #         lines[i + 2] = lines[i + 2].replace(lines[i + 2],
        #                                             "#" + lines[i + 2])

def spin_on(repo, lines, i, line):
    if repo in line:
        lines[i] = line.replace("#", "")
        if (i+1) < len(lines):
            lines[i + 1] = lines[i + 1].replace("#", "")
        if (i+2) < len(lines):
            lines[i + 2] = lines[i + 2].replace("#", "")


def spin_off(repo, lines, i, line):
    if repo in line:
        if "#" not in lines[i]:
            lines[i] = line.replace(lines[i], "#" + lines[i])
        if (i+1) < len(lines):
            if "#" not in lines[i + 1]:
                lines[i + 1] = lines[i + 1].replace(lines[i + 1],
                                                    "#" + lines[i + 1])
        if (i+2) < len(lines):
            if "#" not in lines[i + 2]:
                lines[i + 2] = lines[i + 2].replace(lines[i + 2],
                                                    "#" + lines[i + 2])


def toggle_test_repos(self, state, widget):  # noqa
    if not Functions.os.path.isfile(Functions.pacman + ".bak"):
        Functions.shutil.copy(Functions.pacman, Functions.pacman + ".bak")
    lines = ""
    if state is True:
        with open(Functions.pacman, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "chaotics":
                    spin_on("[chaotic-aur]", lines, i, line)
                if widget == "endeavouros":
                    spin_on("[endeavouros]", lines, i, line)
                if widget == "nemesis":
                    spin_on("[nemesis_repo]", lines, i, line)
                if widget == "xero":
                    spin_on("[xerolinux_repo]", lines, i, line)
                if widget == "xero_xl":
                    spin_on("[xerolinux_repo_xl]", lines, i, line)
                if widget == "xero_nv":
                    spin_on("[xerolinux_nvidia_repo]", lines, i, line)

                if widget == "arco_testing":
                    pacman_on("[arcolinux_repo_testing]", lines, i, line)
                if widget == "arco_base":
                    pacman_on("[arcolinux_repo]", lines, i, line)
                if widget == "arco_a3p":
                    pacman_on("[arcolinux_repo_3party]", lines, i, line)
                if widget == "arco_axl":
                    pacman_on("[arcolinux_repo_xlarge]", lines, i, line)

                if widget == "testing":
                    pacman_on("[testing]", lines, i, line)
                if widget == "core":
                    pacman_on("[core]", lines, i, line)
                if widget == "extra":
                    pacman_on("[extra]", lines, i, line)
                if widget == "community-testing":
                    pacman_on("[community-testing]", lines, i, line)
                if widget == "community":
                    pacman_on("[community]", lines, i, line)
                if widget == "multilib-testing":
                    pacman_on("[multilib-testing]", lines, i, line)
                if widget == "multilib":
                    pacman_on("[multilib]", lines, i, line)

            with open(Functions.pacman, 'w') as f:
                # lines = f.readlines()
                f.writelines(lines)
                f.close()
        except Exception as e:
            print(e)
            Functions.MessageBox(self, "ERROR!!",
                                 "An error has occurred setting this setting \'toggle_test_repos On\'")  # noqa
    else:
        with open(Functions.pacman, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "chaotics":
                    spin_off("[chaotic-aur]", lines, i, line)
                if widget == "endeavouros":
                    spin_off("[endeavouros]", lines, i, line)
                if widget == "nemesis":
                    spin_off("[nemesis_repo]", lines, i, line)
                if widget == "xero":
                    spin_off("[xerolinux_repo]", lines, i, line)
                if widget == "xero_xl":
                    spin_off("[xerolinux_repo_xl]", lines, i, line)
                if widget == "xero_nv":
                    spin_off("[xerolinux_nvidia_repo]", lines, i, line)

                if widget == "arco_testing":
                    pacman_off("[arcolinux_repo_testing]", lines, i, line)
                if widget == "arco_base":
                    pacman_off("[arcolinux_repo]", lines, i, line)
                if widget == "arco_a3p":
                    pacman_off("[arcolinux_repo_3party]", lines, i, line)
                if widget == "arco_axl":
                    pacman_off("[arcolinux_repo_xlarge]", lines, i, line)

                if widget == "testing":
                    pacman_off("[testing]", lines, i, line)
                if widget == "core":
                    pacman_off("[core]", lines, i, line)
                if widget == "extra":
                    pacman_off("[extra]", lines, i, line)
                if widget == "community-testing":
                    pacman_off("[community-testing]", lines, i, line)
                if widget == "community":
                    pacman_off("[community]", lines, i, line)
                if widget == "multilib-testing":
                    pacman_off("[multilib-testing]", lines, i, line)
                if widget == "multilib":
                    pacman_off("[multilib]", lines, i, line)

            with open(Functions.pacman, 'w') as f:
                f.writelines(lines)
                f.close()
        except:  # noqa
            Functions.MessageBox(self, "ERROR!!", "An error has occurred setting this setting \'toggle_test_repos Off\'")  # noqa


def toggle_mirrorlist(self, state, widget):  # noqa
    if not Functions.os.path.isfile(Functions.arcolinux_mirrorlist + ".bak"):
        Functions.shutil.copy(Functions.arcolinux_mirrorlist, Functions.arcolinux_mirrorlist + ".bak")
    lines = ""
    if state is True:
        with open(Functions.arcolinux_mirrorlist, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if widget == "arco_mirror_seed":
                    mirror_on("Server = https://ant.seedhost.eu/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_gitlab":
                    mirror_on("Server = https://gitlab.com/arcolinux/$repo/-/raw/main/$arch", lines, i, line)
                if widget == "arco_mirror_belnet":
                    mirror_on("Server = https://ftp.belnet.be/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_codeberg":
                    mirror_on("Server = https://codeberg.org/arcolinux/$repo/media/branch/main/$arch", lines, i, line)
                if widget == "arco_mirror_funami":
                    mirror_on("Server = https://mirror.funami.tech/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_jingk":
                    mirror_on("Server = https://mirror.jingk.ai/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_github":
                    mirror_on("Server = https://arcolinux.github.io/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_aarnet":
                    mirror_on("Server = https://mirror.aarnet.edu.au/pub/arcolinux/$repo/$arch", lines, i, line)

                # if widget == "arch":
                #     pacman_on("[testing]", lines, i, line)
                # if widget == "multilib":
                #     pacman_on("[multilib-testing]", lines, i, line)
                # if widget == "community":
                #     pacman_on("[community-testing]", lines, i, line)

            with open(Functions.arcolinux_mirrorlist, 'w') as f:
                # lines = f.readlines()
                f.writelines(lines)
                f.close()
        except Exception as e:
            print(e)
            Functions.MessageBox(self, "ERROR!!",
                                 "An error has occurred setting this setting \'toggle_test_repos On\'")  # noqa
    else:
        with open(Functions.arcolinux_mirrorlist, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]

                if widget == "arco_mirror_seed":
                    mirror_off("Server = https://ant.seedhost.eu/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_gitlab":
                    mirror_off("Server = https://gitlab.com/arcolinux/$repo/-/raw/main/$arch", lines, i, line)
                if widget == "arco_mirror_belnet":
                    mirror_off("Server = https://ftp.belnet.be/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_codeberg":
                    mirror_off("Server = https://codeberg.org/arcolinux/$repo/media/branch/main/$arch", lines, i, line)
                if widget == "arco_mirror_funami":
                    mirror_off("Server = https://mirror.funami.tech/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_jingk":
                    mirror_off("Server = https://mirror.jingk.ai/arcolinux/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_github":
                    mirror_off("Server = https://arcolinux.github.io/$repo/$arch", lines, i, line)
                if widget == "arco_mirror_aarnet":
                    mirror_off("Server = https://mirror.aarnet.edu.au/pub/arcolinux/$repo/$arch", lines, i, line)

                # if widget == "arch":
                #     pacman_off("[testing]", lines, i, line)
                # if widget == "multilib":
                #     pacman_off("[multilib-testing]", lines, i, line)
                # if widget == "community":
                #     pacman_off("[community-testing]", lines, i, line)

            with open(Functions.arcolinux_mirrorlist, 'w') as f:
                f.writelines(lines)
                f.close()
        except:  # noqa
            Functions.MessageBox(self, "ERROR!!", "An error has occurred setting this setting \'toggle_test_repos Off\'")  # noqa
