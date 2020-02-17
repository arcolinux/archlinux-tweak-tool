# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import Functions
from Functions import os
# ====================================================================
#                       OBLOGOUT FUNCTIONS
# ====================================================================


def get_shortcut(value):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, "r") as f:
            lines = f.readlines()
            f.close()
        shortcu = Functions.check_value(lines[Functions.get_shortcuts(lines):Functions.get_commands(lines)], value)
        if not shortcu:
            shortcut = [value, '']            
        else:
            shortcut = [shortcu[0].lstrip().rstrip().replace(" ", "")][0].split("=")
        return shortcut[1]


def set_shorcut(self, value, value_sk):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            shortcuts_pos = Functions._get_position(lines, "[shortcuts]")
            commandss_pos = Functions._get_position(lines, "[commands]")
            data1_shortcut = Functions.check_value(lines[shortcuts_pos:commandss_pos], value)

            if not data1_shortcut:

                pos = shortcuts_pos + 5
                lines.insert(pos, value + ' = ' + str(value_sk) + '\n')
            else:
                pos = int(Functions._get_position(lines[shortcuts_pos:commandss_pos], value))
                lines[shortcuts_pos + pos] = value + ' = ' + str(value_sk) + '\n'
            
            with open(Functions.oblogout_conf, 'w') as f:            
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'set_shorcut\'")


def oblog_populate(combo):
    if os.path.isfile(Functions.oblogout_conf):
        coms = []
        active = ""
        with open(Functions.oblogout_conf, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "buttontheme" in line:
                    
                    value = line.split("=")
                    val = value[1].lstrip().rstrip()
                    coms.append(val)
                    
                    if not "#" in line:
                        active = val
        
        coms.sort()

        for i in range(len(coms)):
            combo.append_text(coms[i])
            if(coms[i] == active):
                combo.set_active(i)


def oblogout_change_theme(self, theme):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
                lines = f.readlines()
                f.close()

        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttontheme" in line:
                    if not "#" in lines[i]:
                        lines[i] = line.replace(lines[i], "#" + lines[i])
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttontheme" in line:
                    
                    if theme == lines[i].split("=")[1].lstrip().rstrip():
                        lines[i] = line.replace("#","")

            with open(Functions.oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'oblogout_change_theme\'")


def get_opacity():
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()

        data = Functions.check_value(lines, "opacity")
        if not data:
            opacity = 80
        else:
            opacity = Functions._get_variable(lines, "opacity")
        return int(opacity[1].split(".")[0])


def set_opacity(self, value):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            data = Functions.check_value(lines, 'opacity')
            if not data:
                pos = int(Functions._get_position(lines, "[looks]")) + 1
                lines.insert(pos, 'opacity = ' + str(int(value.split(".")[0])) + '\n')
            else:
                pos = int(Functions._get_position(lines, 'opacity'))
                lines[pos] = 'opacity = ' + str(value).split(".")[0] + '\n'

            with open(Functions.oblogout_conf, 'w') as f:            
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'set_opacity\'")


def set_buttons(self, value):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if "buttons =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, value)

            with open(Functions.oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'set_buttons\'")


def get_buttons():
    buttons = "You do not have oblogout.conf"
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()

            for i in range(0, len(lines)):
                line = lines[i]
                if "buttons =" in line:
                    nline = line.split("=")
                    buttons = nline[1].lstrip().rstrip()
                    
            f.close()
            return buttons
    else:
        return buttons


def get_command(value):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        comman = Functions.check_value(lines[Functions.get_commands(lines):], value)
        if not comman:
            command = ['', '']
            command[0] = value
        else:
            command = [comman[0].strip('\n')][0].split("=")
            command[0] = command[0].replace(' ', '').replace('#', '')
            command[1] = command[1][:1].replace(' ', '') + command[1][1:]
        # command[1] = command1[:1].replace(' ', '')
        return command[1]


def set_command(self, value, value_sk):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            commandss_pos = Functions._get_position(lines, "[commands]")
            data_command = Functions.check_value(lines[commandss_pos:], value)
            if not data_command:
                pos = data_command + 4
                lines.insert(pos, value + ' = ' + str(value_sk) + '\n')
            else:
                pos = int(Functions._get_position(lines[commandss_pos:], value))
                lines[commandss_pos + pos] = value + ' = ' + str(value_sk) + '\n'
            
            with open(Functions.oblogout_conf, 'w') as f:            
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'set_command\'")


def get_color():
    color = ""
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "bgcolor =" in line:
                    color = line.split("=")[1].lstrip().rstrip()
            f.close()
    return color


def set_color(self, color):
    if os.path.isfile(Functions.oblogout_conf):
        with open(Functions.oblogout_conf, 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            for i in range(0, len(lines)):
                line = lines[i]
                if "bgcolor =" in line:
                    nline = line.split("=")
                    val = nline[1].lstrip().rstrip()
                    lines[i] = line.replace(val, color)

            with open(Functions.oblogout_conf, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox(self, "ERROR!!", "An error has occured setting this setting \'set_color\'")