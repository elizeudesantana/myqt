from PySide2.QtWidgets import(
    QAction,
    QToolBar,
    QWidget,
    QMainWindow
)
from PySide2.QtGui import QIcon
from .modulo_config import path_file

image_root = path_file()

class BarraFerramentaEdicao():
    def botoes_barra_edicao(self):
        """Icones Barra Ferramenta Edição"""
        invert_color_icon = image_root + r"/lib/icons/invert_colors36x36.png"
        self.sairAction = QAction(QIcon(invert_color_icon),"Cores",self)
        self.sairAction.setShortcut("Ctrl+C")
        self.sairAction.setStatusTip("Definir cores do background.")
        self.sairAction.triggered.connect(self.connect_menu_ferramenta_service)

        self.toolbar = self.addToolBar("Edicao")

        self.toolbar.addAction(self.sairAction)

        self.addToolBarBreak()
