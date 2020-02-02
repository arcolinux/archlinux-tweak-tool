#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import Functions
from Functions import os
#====================================================================
#                       NEOFETCH
#====================================================================

def get_neofetch():
    lines = []
    if os.path.isfile(Functions.neofetch_config):
        with open(Functions.neofetch_config, "r") as f:
            lines = f.readlines()
            f.close()
        
    return lines

def pop_neofetch_box(combo):
    if os.path.isfile(Functions.neofetch_config):
        com = []
        for image in os.listdir(Functions.home + "/.config/neofetch/"):
            if ".png" in image:
                com.append(image)
        
        com.sort()
        active = ""
        lines = get_neofetch()
        
        for i in range(len(lines)):
            if "image_source" in lines[i]:
                if not "#" in lines[i]:
                    line = lines[i].split("=")[1].replace("\"", "")
                    active = os.path.basename(line).strip()
                            
        for i in range(len(com)):
            combo.append_text(com[i])
            if com[i] == active:
                combo.set_active(i)
    
def check_backend():
    if os.path.isfile(Functions.neofetch_config):
        lines = get_neofetch()
        for i in range(len(lines)):
            if "image_backend" in lines[i]:
                if not "#" in lines[i]:
                    line = lines[i].split("=")[1].replace("\"", "").strip()
                    return line
    return "ascii"

def apply_config(backend, emblem):
    if os.path.isfile(Functions.neofetch_config):
        lines = get_neofetch()
        try:
            if backend == "w3m":            
                for i in range(len(lines)):
                    Functions.neofetch_set_value(lines, i, "image_backend=\"w3m\"", True)
                    Functions.neofetch_set_value(lines, i, "image_backend=\"ascii\"", False)
                    Functions.neofetch_set_value(lines, i, "image_source=", False)
                    Functions.neofetch_set_value(lines, i, emblem, True)
                    # if "image_backend=\"w3m\"" in lines[i]:
                    #     if "#" in lines[i]:
                    #         lines[i] = lines[i].replace("#", "")

                    # if "image_backend=\"ascii\"" in lines[i]:
                    #     if not "#" in lines[i]:
                    #         lines[i] = "#" + lines[i]

                    # if "image_source=" in lines[i]:
                    #     if not "#" in lines[i]:
                    #         lines[i] = "#" + lines[i]
                            
                    # if emblem in lines[i]:
                    #     if "#" in lines[i]:
                    #         lines[i] = lines[i].replace("#", "")
            else:
                for i in range(len(lines)):
                    Functions.neofetch_set_value(lines, i, "image_backend=\"ascii\"", True)
                    Functions.neofetch_set_value(lines, i, "image_backend=\"w3m\"", False)
                    # if "image_backend=\"ascii\"" in lines[i]:
                    #     if "#" in lines[i]:
                    #         lines[i] = lines[i].replace("#", "")
                    # if "image_backend=\"w3m\"" in lines[i]:
                    #     if not "#" in lines[i]:
                    #         lines[i] = "#" + lines[i]

                    #ascii_distro="arcolinux_small"

            with open(Functions.neofetch_config, "w") as f:
                f.writelines(lines)
                f.close()
            Functions.MessageBox("Success!!", "Settings Saved Successfully")
        except:
            pass