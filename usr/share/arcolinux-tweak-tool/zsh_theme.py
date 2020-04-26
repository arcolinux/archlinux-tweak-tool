import os
import Functions


def check_oh_my():
    if not os.path.isdir("/usr/share/oh-my-zsh/themes"):
        return False
    return True


def get_themes(combo):
    if check_oh_my():
        try:
            lists = [x for x in os.listdir("/usr/share/oh-my-zsh/themes")]
            lists = sorted(lists)
            with open(Functions.zsh_config, "r") as f:
                theme_list = f.readlines()
                f.close()
            pos = Functions._get_position(theme_list, "ZSH_THEME=")
            name = theme_list[pos].split("=")[1].strip()
            active = 0
            combo.append_text("random")
            for x in range(len(lists)):
                if name in lists[x]:
                    active = x
                combo.append_text(lists[x].split(".")[0].strip())
            combo.set_active(active)
        except Exception as e:
            print(e)
    else:
        combo.append_text("oh-my-zsh not installed...")
        combo.set_active(0)


def set_config(self, theme):
    if not os.path.isfile(Functions.zsh_config + ".bak"):
        Functions.shutil.copy(Functions.zsh_config,
                              Functions.zsh_config + ".bak")

    try:
        with open(Functions.zsh_config, "r") as f:
            theme_list = f.readlines()
            f.close()

        pos = Functions._get_position(theme_list, "ZSH_THEME=")

        theme_list[pos] = "ZSH_THEME=\"" + theme + "\"\n"

        with open(Functions.zsh_config, "w") as f:
            f.writelines(theme_list)
            f.close()

        Functions.show_in_app_notification(self,
                                           "Settings Saved Successfully")

    except Exception as e:
        print(e)
        Functions.MessageBox(self,
                             "Error!!",
                             "Something went wrong setting this theme.")