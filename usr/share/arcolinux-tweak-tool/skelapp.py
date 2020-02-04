#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import Functions
import threading
import datetime

from Functions import os, GLib

def setMessage(self, message):
    self.label_info.set_markup("<i>" + message + "</i>")


def setProgress(self, value):
    self.progressbar.set_fraction(value)

def skel_run(self, Functions):
    passes = True
    text = self.treeView.get_model()
    if len(text) >= 1:
        for item in text:
            if not "/etc/skel" in item[0]:
                passes = False
        if passes == True:
            
            # Functions.setMessage(self, "Running Backup")
            t1 = threading.Thread(target=run_backup,
                                    args=(self, text,))
            t1.daemon = True
            t1.start()
        else:
            Functions.MessageBox("Failed!!", "It looks like your out of the /etc/skel directory")

def run_backup(self, text):
    print("NICE NICE NICE")

# ===========================================
#		DELETE BACKUP FUNCTION
# ===========================================
def Delete_Backup(self):
    count = os.listdir(Functions.home + "/" + Functions.bd).__len__()

    if count > 0:
        GLib.idle_add(setMessage,self, "Removing ...")
        GLib.idle_add(setProgress, self, 0.3)
        for filename in os.listdir(Functions.home + "/" + Functions.bd):
            if filename == self.backs.get_active_text():
                Functions.shutil.rmtree(Functions.home + "/" + Functions.bd + "/" + filename)
        GLib.idle_add(refresh, self)
        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self, 1)
        GLib.idle_add(Functions.MessageBox,"Success!!","Config backups cleaned.")
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self, "Idle ...")
    GLib.idle_add(setProgress, self, 0)


def Delete_Inner_Backup(self):
    count = os.listdir(Functions.home + "/" + Functions.bd).__len__()

    if count > 0:
        GLib.idle_add(setMessage,self, "Removing ...")
        GLib.idle_add(setProgress, self, 0.3)
        treeselect = self.treeView2.get_selection()
        
        for filename in os.listdir(Functions.home + "/" + Functions.bd + "/" + self.backs.get_active_text()):
            (model, pathlist) = treeselect.get_selected_rows()
            for path in pathlist :
                tree_iter = model.get_iter(path)
                value = model.get_value(tree_iter,0)
                if filename == value:
                    # print(value)
                    if os.path.isdir(Functions.home + "/" + Functions.bd + "/" + self.backs.get_active_text() + "/" + filename):
                        Functions.shutil.rmtree(Functions.home + "/" + Functions.bd + "/" + self.backs.get_active_text() + "/" + filename)
                    elif os.path.isfile(Functions.home + "/" + Functions.bd + "/" + self.backs.get_active_text() + "/" + filename):
                        os.unlink(Functions.home + "/" + Functions.bd + "/" + self.backs.get_active_text() + "/" + filename)
            
        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self, 1)
        GLib.idle_add(Functions.MessageBox,"Success!!", "Config backups cleaned.")
        GLib.idle_add(setMessage,self, "Idle ...")
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setProgress, self, 0)

def Flush_All(self):
    count = os.listdir(Functions.home + "/" + Functions.bd).__len__()

    if count > 0:
        count = ((count/count)/count)
        GLib.idle_add(setMessage,self, "Deleting Backup")
        for filename in os.listdir(Functions.home + "/" + Functions.bd):                
            if os.path.isdir(Functions.home + "/" + Functions.bd + "/" + filename):
                GLib.idle_add(setProgress, self, self.progressbar.get_fraction() + count)
                Functions.shutil.rmtree(Functions.home + "/" + Functions.bd + "/" + filename)            
                

        GLib.idle_add(Functions.MessageBox,"Success!!", ".ATT_Backups directory has been cleaned.")
        GLib.idle_add(refresh, self)
        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self, 0)
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self, "Idle ...")
# ===========================================
#		REFRESH FUNCTION
# ===========================================
def refresh(self):
    if not os.path.exists(Functions.home + "/" + Functions.bd):
        os.makedirs(Functions.home + "/" + Functions.bd)

    self.backs.get_model().clear()
    BACKUPS_CATS = []
    
    for filename in os.listdir(Functions.home + "/" + Functions.bd):
        if os.path.isdir(Functions.home + "/" + Functions.bd + "/" + filename):
            BACKUPS_CATS.append(filename)
    
    for item in BACKUPS_CATS:
        self.backs.append_text(item)

    self.backs.set_active(0)


def refresh_inner(self):
    count = os.listdir(Functions.home + "/" + Functions.bd).__len__()
    active_text = "".join([str(self.backs.get_active_text()), ""])

    if count > 0:
        if os.path.isdir(Functions.home + "/" + Functions.bd + "/" + active_text):
            self.store2.clear()
            
            for filename in os.listdir(Functions.home + "/" + Functions.bd + "/" + active_text):
                self.store2.append([filename])
            
    else:
        self.store2.clear()


def button_toggles(self, state):
    self.btn2.set_sensitive(state)
    self.btn5.set_sensitive(state)
    self.btn9.set_sensitive(state)
    self.btn4.set_sensitive(state)
    self.btn10.set_sensitive(state)
    self.btn11.set_sensitive(state)
    self.btn12.set_sensitive(state)
    self.browse.set_sensitive(state)
    self.remove.set_sensitive(state)

def do_pulse(data, self):
    self.progressbar.pulse()
    return True

def processing(self, active_text):
    now = datetime.datetime.now()
    

    GLib.idle_add(setProgress, self, 0.1)

    GLib.idle_add(self.progressbar.set_pulse_step, 0.2)
    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self)

    # ============================
    #       CONFIG
    # ============================
    GLib.idle_add(setMessage,self, "Backing up .config")
    Functions.copytree(self, Functions.home + '/.config', Functions.home + '/' + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.config-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)

    # GLib.idle_add(setProgress, self, 0.3)

    # ============================
    #       LOACAL
    # ============================
    GLib.idle_add(setMessage,self, "Backing up .local")
    Functions.copytree(self, Functions.home + '/.local', Functions.home + '/' + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.local-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)
    
    GLib.source_remove(timeout_id)
    timeout_id = None
    
    GLib.idle_add(setProgress, self, 0.5)

    # ============================
    #       BASH
    # ============================

    if os.path.isfile(Functions.home + '/.bashrc'):
        GLib.idle_add(setMessage,self, "Backing up .bashrc")
        Functions.shutil.copy(
            Functions.home + '/.bashrc', Functions.home + "/" + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.bashrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
    
    GLib.idle_add(setProgress, self, 0.6)
    # ============================
    #       ZSH
    # ============================
    if os.path.isfile(Functions.home + '/.zshrc'):
        GLib.idle_add(setMessage,self, "Backing up .zshrc")
        Functions.shutil.copy(
            Functions.home + '/.zshrc', Functions.home + "/" + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.zshrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setProgress, self, 0.7)

    # ============================
    #       CONKY
    # ============================
    if os.path.exists(Functions.home + '/.lua'):
        GLib.idle_add(setMessage,self, "Backing up .lua")
        Functions.copytree(self, Functions.home + '/.lua', Functions.home + '/' + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.lua-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)

    if os.path.isfile(Functions.home + '/.conkyrc'):
        GLib.idle_add(setMessage,self, "Backing up .cokyrc")
        Functions.shutil.copy(
            Functions.home + '/.conkyrc', Functions.home + "/" + Functions.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.conkyrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setProgress, self, 0.8)

    GLib.idle_add(setMessage, self, "Done")

    
    if not active_text == "BACKUP":
        pass    
    #     GLib.idle_add(setMessage, self, "Running Skel")
        
    #     GLib.idle_add(run, self, active_text)
    else:
        GLib.idle_add(setProgress, self, 1)
        GLib.idle_add(button_toggles,self,True)
        GLib.idle_add(setMessage,self, "Idle...")
        GLib.idle_add(setProgress,self,0)
        

    GLib.idle_add(refresh, self)
    GLib.idle_add(refresh_inner, self)