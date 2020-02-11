from PySide2.QtWidgets import(
    QAction,
    QToolBar,
    QWidget,
    QMainWindow
)
from PySide2.QtGui import QIcon
import unittest
from .modulo_config import path_file

image_root = path_file()

class BarraFerramentaInicial():
    def botoes_barra_inicial(self):
        """ Icones Barra Ferramenta Inicial"""
        criar_sair_icon = image_root + r"/lib/icons/exit18x18.png"
        self.sairAction = QAction(QIcon(criar_sair_icon),"Sair",self)
        self.sairAction.setShortcut("Ctrl+S")
        self.sairAction.setStatusTip("Sair do aplicativo.")
        self.sairAction.triggered.connect(self.connect_menu_arquivo_sair)

        self.toolbar = self.addToolBar("Inicial")

        self.toolbar.addAction(self.sairAction)

        self.addToolBarBreak()
