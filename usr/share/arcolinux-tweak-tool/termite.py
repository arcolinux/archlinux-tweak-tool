#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import Functions
import numpy as np 

from Functions import os
#====================================================================
#                       TERMITE
#====================================================================
def get_themes(combo):
    themes = os.listdir(Functions.home + "/.config/termite/themes/")
    
    with open(Functions.termite_config, "r") as f:
        lines = f.readlines()
        f.close()
    
    theme_line = lines[Functions._get_position(lines, "[colors]") + 1]
    active = ""
    coms = []
    for theme in themes:
        if ".config" in theme:
            print(theme.replace("base16-", "").replace(".config", ""))
            if theme.replace("base16-", "").replace(".config", "").capitalize() in theme_line:
                active = theme.replace(".config", "")
            coms.append(theme.replace(".config", ""))
    
    coms.sort()

    for i in range(len(coms)):
        combo.append_text(coms[i])
        if active == coms[i]:
            combo.set_active(i)

    # print(lines[Functions._get_position(lines, "[colors]") + 1])

def get_config():
    with open(Functions.termite_config, "r") as f:
        lists = f.readlines()
        f.close()
    target_element = "[colors]\n"
    try:
        target_index = lists.index(target_element)
    except:
        return lists

    return lists[:target_index]


def set_config(theme):
    if not os.path.isfile(Functions.termite_config + ".bak"):
        Functions.shutil.copy(Functions.termite_config, Functions.termite_config + ".bak")

    try:
        config = get_config()

        with open(Functions.home + "/.config/termite/themes/" + theme + ".config", "r") as f:
            theme_list = f.readlines()
            f.close()

        
        config = list(np.append(config, theme_list))

        with open(Functions.termite_config, "w") as f:
            f.writelines(config)
            f.close()

        Functions.MessageBox("Success!!", "Settings Saved Successfully")
    except:
        Functions.MessageBox("Error!!", "Something went wrong setting this theme.")


