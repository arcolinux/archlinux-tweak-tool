#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import threading

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