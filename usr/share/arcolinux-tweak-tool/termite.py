#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import Functions
import numpy as np 
import Settings
from Functions import os
#====================================================================
#                       TERMITE
#====================================================================
def get_themes(combo):
    if os.path.isdir(Functions.home + "/.config/termite/themes/"):
        themes = os.listdir(Functions.home + "/.config/termite/themes/")
        
        with open(Functions.termite_config, "r") as f:
            lines = f.readlines()
            f.close()
        
        theme_line = lines[Functions._get_position(lines, "[colors]") + 1]
        active = ""
        coms = []
        for theme in themes:
            if ".config" in theme:
                # print(theme.replace("base16-", "").replace(".config", ""))
                if theme.replace("base16-", "").replace(".config", "").capitalize() in theme_line:
                    active = theme.replace(".config", "")
                coms.append(theme.replace(".config", ""))
        
        coms.sort()

        if Functions.os.path.isfile(Functions.config):
            themes = Settings.read_settings("TERMITE", "theme")
            if len(themes) > 1:
                active = themes

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if active == coms[i]:
                combo.set_active(i)

    # print(lines[Functions._get_position(lines, "[colors]") + 1])

def get_config():
    if os.path.isfile(Functions.termite_config):
        with open(Functions.termite_config, "r") as f:
            lists = f.readlines()
            f.close()
        target_element = "[colors]\n"
        try:
            target_index = lists.index(target_element)
        except:
            return lists

        return lists[:target_index]
    return []

def set_config(theme):
    if not os.path.isfile(Functions.termite_config + ".bak"):
        Functions.shutil.copy(Functions.termite_config, Functions.termite_config + ".bak")

    try:
        config = get_config()

        with open(Functions.home + "/.config/termite/themes/" + theme + ".config", "r") as f:
            theme_list = f.readlines()
            f.close()

        configs = list(np.append(config, theme_list))

        if not configs == None:
            with open(Functions.termite_config, "w") as f:
                f.writelines(list(configs))
                f.close()

            Functions.MessageBox("Success!!", "Settings Saved Successfully")
        if Functions.os.path.isfile(Functions.config):
            Settings.write_settings("TERMITE", "theme", theme)

    except:
        Functions.MessageBox("Error!!", "Something went wrong setting this theme.")


