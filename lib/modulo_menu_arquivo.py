from PySide2.QtWidgets import(
    QAction,
    QWidget,
    QWidget,
    QMainWindow
)
from PySide2.QtGui import QIcon
from .modulo_config import path_file

image_root = path_file()


class MenuArquivo():
    def menu_arquivo_sair(self):
        """Sair do aplicativo."""
        criar_sair_icon = image_root + r"/lib/icons/exit18x18.png"
        qaction_Sair = QAction(
            QIcon(criar_sair_icon),
            "&Sair",
            self,
            statusTip="Sair do aplicativo."
        )
        qaction_Sair.setShortcut("Ctrl+S")
        qaction_Sair.triggered.connect(self.connect_menu_arquivo_sair)
        self.file_menu.addAction(qaction_Sair)
