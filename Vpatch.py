from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import os

app = QApplication([])

# Checks if GTA V is open

def patch_hosts():
    
    os.chdir("C:\\windows\system32\drivers\etc")
    with open("hosts", "a") as file:
     file.write(" \n\n")
     file.write("0.0.0.0 paradise-s1.battleye.com\n")
     file.write("0.0.0.0 test-s1.battleye.com\n")
     file.write("0.0.0.0 paradiseenhanced-s1.battleye.com")
    button.setText("Patched!")
    print("patched")
    

def unpatch_hosts():
    os.chdir("C:\\windows\system32\drivers\etc")
    with open("hosts", "w") as file:
        file.write ("#127.0.0.1 localhost")
     
    button.setText("Unpatched!")
    print("unpatched")


# Window settings
window = QWidget()
window.setWindowTitle("GTA V Hosts Patch")
window.setGeometry(50,50, 420, 630)

layout = QVBoxLayout(window)

# this is what it displays in the window
label = QLabel("GTA Hosts Patcher", parent=window)
button = QPushButton("Patch!", parent=window)
button.setCheckable(True)
button.clicked.connect(patch_hosts)
unpatchbutton = QPushButton("Unpatch!", parent=window)
unpatchbutton.setCheckable(True)
unpatchbutton.clicked.connect(unpatch_hosts)
warnlabel = QLabel ("CLOSE GTA V BEFORE PATCHING/UNPATCHING!!!!!", parent=window)

layout.addWidget(label)
layout.addWidget(warnlabel)
layout.addWidget(button)
layout.addWidget(unpatchbutton)

window.show()

app.exec()
