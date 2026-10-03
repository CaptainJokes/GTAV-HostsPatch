from PyQt6.QtWidgets import QApplication, QWidget, Toggle
import os

app = QApplication([])

window = QWidget()
window.setWindowTitle("GTA V Hosts Patch")
window.setGeometry(50,50, 420, 630)
window.show()

app.exec()
