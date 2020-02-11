from PySide2.QtWidgets import (
    QMainWindow,
    QAction,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
    QPlainTextEdit
)
from PySide2.QtGui import QIcon
from PySide2.QtCore import qApp, Slot
import sys



class ModuloInicial(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.settings()

    def settings(self):
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)
        self.setWindowTitle("Bob - EliSoftWare")

        self.setStyleSheet("QWidget {background-image: url(imagem/bg2.jpg)}")
    
        # InitToolbar.initToolbar(self)
        # Clima.atualiza(self)

        self.status = self.statusBar()
        self.status.showMessage("Seja bem vindo - Bob - EliSoftWare")
