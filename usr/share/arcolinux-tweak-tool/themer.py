#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

import Functions
import numpy as np
from Functions import os

def get_list(fle):
    with open(fle, "r") as f:
        lines = f.readlines()
        f.close()
    return lines

def get_i3_themes(combo):
    pass

def get_awesome_themes(lines):
    
    theme_pos = Functions._get_position(lines, "local themes = {")
    end_theme_pos = Functions._get_position(lines, "local chosen_theme")
    
    coms = [x for x in lines[theme_pos:end_theme_pos] if "\"," in x]
    return_list = []
    for x in coms:
        return_list.append(x.split("\"")[1].strip())
    return return_list

def set_awesome_theme(lines, val):
    theme_pos = Functions._get_position(lines, "local chosen_theme")
    lst = lines[theme_pos].split("=")[1].replace("themes[", "").replace("]", "").strip()
    lines[theme_pos] = lines[theme_pos].replace("themes[" + lst + "]", "themes[" + val + "]")
    with open(Functions.awesome_config, "w") as f:
        f.writelines(lines)
        f.close()

def reload_awesome():
    Functions.subprocess.run(["sh", "-c", "echo 'awesome.restart()' | awesome-client"], shell=False)

def get_value(lists, types):
    try:
        pos = Functions._get_position(lists, types)
        color = lists[pos].split("=")[-1].strip()

        return color

            
    except Exception as e:
        print(e)