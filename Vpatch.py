from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import os

app = QApplication([])

def patch_hosts():
    
    os.chdir("C:\\windows\system32\drivers\etc")
    with open("hosts", "w") as file:
     file.write("0.0.0.0 paradise-s1.battleye.com\n0.0.0.0 test-s1.battleye.com\n0.0.0.0 paradiseenhanced-s1.battleye.com")
    button.setText("Patched!")
    print("patched")
    

def unpatch_hosts():
    os.chdir("C:\\windows\system32\drivers\etc")
    with open("hosts", "w") as file:
        file.write ("#127.0.0.1 localhost")
     
    unpatchbutton.setText("Unpatched!")
    print("unpatched")


# Window settings
window = QWidget()
window.setWindowTitle("VPatch 1.0.2")
window.setGeometry(50,50, 500, 500)

layout = QVBoxLayout(window)

# this is what it displays in the window
label = QLabel("<h1>VPatch</h1>", parent=window)
button = QPushButton("Patch!", parent=window)
button.setCheckable(True)
button.clicked.connect(patch_hosts)
unpatchbutton = QPushButton("Unpatch!", parent=window)
unpatchbutton.setCheckable(True)
unpatchbutton.clicked.connect(unpatch_hosts)
warnlabel = QLabel("<h1>CLOSE GTA V BEFORE PATCHING/UNPATCHING!</h1>", parent=window)
warlabel2 = QLabel("<h1>DO NOT PRESS PATCH MULTIPLE TIMES!</h1>")

layout.addWidget(label)
layout.addWidget(warnlabel)
layout.addWidget(warlabel2)
layout.addWidget(button)
layout.addWidget(unpatchbutton)

window.show()

app.exec()
