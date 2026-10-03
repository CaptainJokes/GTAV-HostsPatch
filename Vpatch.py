from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import os

app = QApplication([])

def patch_hosts():
    
    os.chdir("C:\windows\system32\drivers\etc")
        with open("test.txt", "a") as file:
         file.write(" \n\n")
         file.write("0.0.0.0 paradise-s1.battleye.com\n")
         file.write("0.0.0.0 test-s1.battleye.com\n")
         file.write("0.0.0.0 paradiseenhanced-s1.battleye.com")
    button.setText("Patched!")

def unpatch_hosts():
    print("Goodbye!")
    os.chdir("C:\windows\system32\drivers\etc")
    with open("hosts", "a") as file:
     file.
    button.setText("Unpatched!")

def test_edit():
    with open("test.txt", "a") as file:
        file.write(" \n\n")
        file.write("0.0.0.0 paradise-s1.battleye.com\n")
        file.write("0.0.0.0 test-s1.battleye.com\n")
        file.write("0.0.0.0 paradiseenhanced-s1.battleye.com")


# Window settings
window = QWidget()
window.setWindowTitle("GTA V Hosts Patch")
window.setGeometry(50,50, 420, 630)

layout = QVBoxLayout(window)


label = QLabel("GTA Hosts Patcher", parent=window)
button = QPushButton("Patch!", parent=window)
button.setCheckable(True)
button.clicked.connect(patch_hosts)
unpatchbutton = QPushButton("Unpatch!", parent=window)
unpatchbutton.setCheckable(True)
unpatchbutton.clicked.connect(unpatch_hosts)
testbutton = QPushButton("Test", parent=window)
testbutton.setCheckable(True)
testbutton.clicked.connect(test_edit)

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(unpatchbutton)
layout.addWidget(testbutton)

window.show()

app.exec()
