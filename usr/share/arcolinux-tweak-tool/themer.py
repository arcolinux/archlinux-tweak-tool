# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import Functions as fn
# import numpy as np
# from Functions import os


def get_list(fle):
    with open(fle, "r") as f:
        lines = f.readlines()
        f.close()
    return lines


def set_i3_themes(lines, theme):
    try:
        pos1 = fn._get_position(lines, "##START THEMING")
        pos2 = fn._get_position(lines, "##STOP THEMING")
        name = theme.lower().replace(" ", "-")
        with open(fn.home + "/.config/i3/" + name + ".theme", "r") as f:
            theme_lines = f.readlines()
            f.close()

        lines[pos1:pos2 + 1] = theme_lines

        with open(fn.i3wm_config, "w") as f:
            f.writelines(lines)
            f.close()
    except Exception as e:
        print(e)


def get_i3_themes(combo, lines):
    combo.get_model().clear()
    try:
        menu = [x for x in fn.os.listdir(fn.home + "/.config/i3") if ".theme" in x]

        current_theme = fn._get_position(lines, "Theme name :")
        theme_name = lines[current_theme].split(":")[1].strip().lower().replace(" ", "-")  # noqa
        print(theme_name)
        active = 0
        for i in range(len(menu)):
            if theme_name in menu[i]:
                active = i
            combo.append_text(menu[i].replace(".theme", ""))
        combo.set_active(active)
    except Exception as e:
        print(e)


def get_awesome_themes(lines):

    theme_pos = fn._get_position(lines, "local themes = {")
    end_theme_pos = fn._get_position(lines, "local chosen_theme")

    coms = [x for x in lines[theme_pos:end_theme_pos] if "\"," in x]
    return_list = []
    for x in coms:
        return_list.append(x.split("\"")[1].strip())
    return return_list


def set_awesome_theme(lines, val):
    theme_pos = fn._get_position(lines, "local chosen_theme")
    lst = lines[theme_pos].split("=")[1].replace("themes[",
                                                 "").replace("]",
                                                             "").strip()
    lines[theme_pos] = lines[theme_pos].replace("themes[" + lst + "]",
                                                "themes[" + val + "]")
    with open(fn.awesome_config, "w") as f:
        f.writelines(lines)
        f.close()


def get_value(lists, types):
    try:
        pos = fn._get_position(lists, types)
        color = lists[pos].split("=")[-1].strip()

        return color
    except Exception as e:
        print(e)
