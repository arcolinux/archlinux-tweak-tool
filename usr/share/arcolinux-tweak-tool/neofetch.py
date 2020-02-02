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
            if "image_backend=" in lines[i]:
                if not "#" in lines[i]:
                    line = lines[i].split("=")[1].replace("\"", "").strip()
                    return line
    return "ascii"
def check_ascii():
    line = "auto"
    if os.path.isfile(Functions.neofetch_config):
        lines = get_neofetch()
        for i in range(len(lines)):
            if "ascii_distro=" in lines[i]:
                line = lines[i].split("=")[1].replace("\"", "").strip()
    return line

def apply_config(self, backend, emblem, ascii_size, backend_val):
    if os.path.isfile(Functions.neofetch_config):
        lines = get_neofetch()
        # try:
        for i in range(len(lines)):
            if self.os.get_active():
                Functions.neofetch_set_value(lines, i, "info \"OS\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"OS\"", False)
            if self.host.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Host\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Host\"", False)
            if self.kernel.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Kernel\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Kernel\"", False)
            if self.uptime.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Uptime\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Uptime\"", False)
            if self.packages.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Packages\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Packages\"", False)
            if self.shell.get_active():   
                Functions.neofetch_set_value(lines, i, "info \"Shell\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Shell\"", False)
            if self.res.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Resolution\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Resolution\"", False)
            if self.de.get_active():
                Functions.neofetch_set_value(lines, i, "info \"DE\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"DE\"", False)
            if self.wm.get_active():  
                Functions.neofetch_set_value(lines, i, "info \"WM\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"WM\"", False)
            if self.themes.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Theme\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Theme\"", False)
            if self.icons.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Icons\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Icons\"", False)
            if self.term.get_active():    
                Functions.neofetch_set_value(lines, i, "info \"Terminal\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Terminal\"", False)
            if self.termfont.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Terminal Font\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Terminal Font\"", False)
            if self.cpu.get_active():
                Functions.neofetch_set_value(lines, i, "info \"CPU\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"CPU\"", False)
            if self.gpu.get_active():   
                Functions.neofetch_set_value(lines, i, "info \"GPU\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"GPU\"", False)
            if self.mem.get_active():
                Functions.neofetch_set_value(lines, i, "info \"Memory\"", True)
            else:
                Functions.neofetch_set_value(lines, i, "info \"Memory\"", False)
            
            if not backend == "ascii":            
                Functions.neofetch_set_backend_value(lines, i, "image_backend=\"", backend_val)
                # Functions.neofetch_set_backend_value(lines, i, "image_backend=\"ascii\"")
                Functions.neofetch_set_value(lines, i, "image_source=", False)
                Functions.neofetch_set_value(lines, i, emblem, True)
                
            else:
                Functions.neofetch_set_backend_value(lines, i, "image_backend=\"", "ascii")
                # Functions.neofetch_set_value(lines, i, "image_backend=\"ascii\"", True)
                # Functions.neofetch_set_value(lines, i, "image_backend=\"" + backend_val + "\"", False)
                if "ascii_distro=" in lines[i]:
                    lines[i] = "ascii_distro=\"" + ascii_size + "\"\n"


        with open(Functions.neofetch_config, "w") as f:
            f.writelines(lines)
            f.close()
        Functions.MessageBox("Success!!", "Settings Saved Successfully")
        # except:
        #     pass

def get_state(value):
    lines = get_neofetch()

    for i in range(len(lines)):
        if value in lines[i]:
            if "#" in lines[i]:
                return False
    return True

def get_checkboxes(self):
    
    self.os.set_active(get_state("info \"OS\""))    
    self.host.set_active(get_state("info \"Host\""))
    self.kernel.set_active(get_state("info \"Kernel\""))
    self.uptime.set_active(get_state("info \"Uptime\""))
    self.packages.set_active(get_state("info \"Packages\""))
    self.shell.set_active(get_state("info \"Shell\""))    
    self.res.set_active(get_state("info \"Resolution\""))
    self.de.set_active(get_state("info \"DE\""))
    self.wm.set_active(get_state("info \"WM\""))    
    self.themes.set_active(get_state("info \"Theme\""))
    self.icons.set_active(get_state("info \"Icons\""))
    self.term.set_active(get_state("info \"Terminal\""))    
    self.termfont.set_active(get_state("info \"Terminal Font\""))
    self.cpu.set_active(get_state("info \"CPU\""))
    self.gpu.set_active(get_state("info \"GPU\""))    
    self.mem.set_active(get_state("info \"Memory\""))