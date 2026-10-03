from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import os

app = QApplication([])

def patch_hosts():
    print("Hello world!")
    button.setText("Patched!")

def unpatch_hosts():
    print("Goodbye!")
    button.setText("Unpatched!")

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

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(unpatchbutton)

window.show()

app.exec()
