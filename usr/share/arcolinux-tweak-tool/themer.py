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

def get_value(lists, types):
    try:
        pos = Functions._get_position(lists, types)
        color = lists[pos].split("=")[-1].strip()

        return color

            
    except Exception as e:
        print(e)