from PySide2.QtWidgets import(
    QAction,
    QWidget,
    QWidget,
    QMainWindow
)
from PySide2.QtGui import QIcon
from .modulo_config import path_file

image_root = path_file()


class MenuFerramenta():
    def menu_ferramenta_service(self):
        """Analise logs sistema, arquivos e services."""
        criar_sair_icon = image_root + r"/lib/icons/system_update_alt_black_18x18.png"
        qaction_Sair = QAction(
            QIcon(criar_sair_icon),
            "Ser&vice",
            self,
            statusTip="Analise logs sistema, arquivos e services."
        )
        qaction_Sair.setShortcut("Ctrl+v")
        qaction_Sair.triggered.connect(self.connect_menu_ferramenta_service)
        self.file_menu.addAction(qaction_Sair)
