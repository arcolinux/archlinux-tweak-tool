# =================================================================
# =          Authors: Erik Dubois - Cameron Percival
# =================================================================

import Functions as fn

def get_list(fle):
    with open(fle, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    return lines

def get_value(lists, types):
    try:
        pos = fn._get_position(lists, types)
        color = lists[pos].split("=")[-1].strip()

        return color
    except Exception as e:
        print(e)

def move_file(self, state):
    if state:
        if fn.os.path.isfile(fn.home + "/.config/i3/config-polybar"):
            fn.subprocess.run(["mv", fn.home + "/.config/i3/config", fn.home + "/.config/i3/config-bar"])
            fn.subprocess.run(["mv", fn.home + "/.config/i3/config-polybar", fn.home + "/.config/i3/config"])
        else:
            fn.MessageBox(self, "OOPS!", "you dont seem to have <b>config-polybar</b> file in your <i>~/.config/i3</i> directory. So we can not enable this feature.")
            self.poly.set_active(False)
    else:
        fn.subprocess.run(["mv", fn.home + "/.config/i3/config", fn.home + "/.config/i3/config-polybar"])
        fn.subprocess.run(["mv", fn.home + "/.config/i3/config-bar", fn.home + "/.config/i3/config"])

def toggle_polybar(self, lines, state):
    if state:
        if not check_polybar(lines):
            move_file(self, True)
    else:
        if check_polybar(lines):
            move_file(self, False)

def check_polybar(lines):
    try:
        pos = fn._get_position(lines, "~/.config/polybar/launch.sh")
        if "#" in lines[pos]:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        return False

# =================================================================
# =                  I3WM
# =================================================================

def get_i3_themes(combo, lines):
    combo.get_model().clear()
    try:
        menu = [x for x in fn.os.listdir(fn.home + "/.config/i3") if ".theme" in x]

        current_theme = fn._get_position(lines, "Theme name :")
        theme_name = lines[current_theme].split(":")[1].strip().lower().replace(" ", "-")  # noqa
        #print(theme_name)
        active = 0
        sorted_menu = sorted(menu)
        for i in range(len(sorted_menu)):
            if theme_name in sorted_menu[i]:
                active = i
            combo.append_text(sorted_menu[i].replace(".theme", ""))
        combo.set_active(active)
    except Exception as e:
        print(e)

def set_i3_themes(lines, theme):
    try:
        pos1 = fn._get_position(lines, "##START THEMING WM")
        pos2 = fn._get_position(lines, "##STOP THEMING WM")
        name = theme.lower().replace(" ", "-")
        with open(fn.home + "/.config/i3/" + name + ".theme", "r", encoding="utf-8") as f:
            theme_lines = f.readlines()
            f.close()
        pos3 = fn._get_position(theme_lines, "##START THEMING WM")
        pos4 = fn._get_position(theme_lines, "##STOP THEMING WM")
        lines[pos1:pos2 + 1] = theme_lines[pos3:pos4 + 1]
        with open(fn.i3wm_config, "w") as f:
            f.writelines(lines)
            f.close()
    except Exception as e:
        print(e)


def set_i3_themes_bar(lines, theme):
    try:
        pos1 = fn._get_position(lines, "##START THEMING BAR")
        pos2 = fn._get_position(lines, "##STOP THEMING BAR")
        name = theme.lower().replace(" ", "-")
        with open(fn.home + "/.config/i3/" + name + ".theme", "r", encoding="utf-8") as f:
            theme_lines = f.readlines()
            f.close()

        pos3 = fn._get_position(theme_lines, "##START THEMING BAR")
        pos4 = fn._get_position(theme_lines, "##STOP THEMING BAR")

        lines[pos1:pos2 + 1] = theme_lines[pos3:pos4 + 1]

        with open(fn.i3wm_config, "w") as f:
            f.writelines(lines)
            f.close()
    except Exception as e:
        print(e)

# =================================================================
# =                  AWESOME
# =================================================================

def get_awesome_themes(lines):
    theme_pos = fn._get_position(lines, "local themes = {")
    end_theme_pos = fn._get_position(lines, "local chosen_theme")

    coms = [x for x in lines[theme_pos:end_theme_pos] if "\"," in x]
    list = []
    for x in coms:
        list.append(x.split("\"")[1].strip())
    return_list = sorted(list)
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

# =================================================================
# =                  QTILE
# =================================================================

def get_qtile_themes(combo, lines):
    combo.get_model().clear()
    try:
        menu = [x for x in fn.os.listdir(fn.home + "/.config/qtile/themes/") if ".theme" in x]

        current_theme = fn._get_position(lines, "Theme name :")
        theme_name = lines[current_theme].split(":")[1].strip().lower().replace(" ", "-")  # noqa
        active = 0
        sorted_menu = sorted(menu)
        for i in range(len(sorted_menu)):
            if theme_name in sorted_menu[i]:
                active = i
            combo.append_text(sorted_menu[i].replace(".theme", ""))
        combo.set_active(active)
    except Exception as e:
        print(e)

def set_qtile_themes(lines, theme):
    try:
        pos1 = fn._get_position(lines, "# COLORS FOR THE BAR")
        pos2 = fn._get_position(lines, "colors = init_colors()")
        name = theme.lower().replace(" ", "-")
        with open(fn.home + "/.config/qtile/themes/" + name + ".theme", "r", encoding="utf-8") as f:
            theme_lines = f.readlines()
            f.close()
        pos3 = fn._get_position(theme_lines, "# COLORS FOR THE BAR")
        pos4 = fn._get_position(theme_lines, "colors = init_colors()")

        lines[pos1:pos2 + 1] = theme_lines[pos3:pos4 + 1]

        with open(fn.qtile_config, "w") as f:
            f.writelines(lines)
            f.close()
    except Exception as e:
        print(e)
