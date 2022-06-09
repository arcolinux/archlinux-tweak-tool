# =================================================================
# =          Authors: Erik Dubois - Cameron Percival
# =================================================================

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
            lists_sorted = sorted(lists)
            with open(Functions.zsh_config, "r", encoding="utf-8", errors="ignore") as f:
                theme_list = f.readlines()
                f.close()
            pos = Functions._get_position(theme_list, "ZSH_THEME=")
            #stripping whitespace, and quotation marks
            name = theme_list[pos].split("=")[1].strip().strip('"')
            active = 0
            combo.append_text("random")
            for x in range(len(lists_sorted)):
                if name in lists_sorted[x].replace(".zsh-theme", ""):
                    active = x+1 #remember; arrays start at ZERO
                combo.append_text(lists_sorted[x].split(".")[0].strip())
            combo.set_active(active)
        except OSError:
            print("ATT was unable to locate your ~/.zshrc file. We have placed a working ~/.zshrc in your base home directory (~/.zshrc)")
            print("You may need to reload ATT to set the options in the zsh tab")
        except Exception as e:
            print(e)
    else:
        combo.append_text("oh-my-zsh-git is not installed...install it first")
        combo.set_active(0)

def set_config(self, theme):
    if not os.path.isfile(Functions.zsh_config + ".bak"):
        Functions.shutil.copy(Functions.zsh_config,
                              Functions.zsh_config + ".bak")

    try:
        with open(Functions.zsh_config, "r", encoding="utf-8", errors="ignore") as f:
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
