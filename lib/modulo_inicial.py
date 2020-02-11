from PySide2.QtWidgets import (
    QMainWindow,
    QAction,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
    QPlainTextEdit,
    QMenu
)
from PySide2.QtGui import QIcon
from PySide2.QtCore import qApp, Slot

from .modulo_menu_inicial import MenuInicial
from .modulo_barraferramenta_inicial import BarraFerramentaInicial
from .modulo_barraferramenta_edicao import BarraFerramentaEdicao
import sys

class PopupMenu():
    def new_cluster(self):
        print("New Cluster")

    def rename_cluster(self):
        print ("Rename cluster")

    def delete_cluster(self):
        print ("Delete cluster")

    def create_popup_menu(self, parent=None):
        from .modulo_config import path_file

        image_root = path_file()

        self.popup_menu = QMenu(parent)

        criar_sair_icon = image_root + r"/ext/icons/exit18x18.png"
        new_cluster = QAction(
            QIcon(criar_sair_icon),
            "&Sair",
            self,
            statusTip="Sair do aplicativo."
        )
        new_cluster.setShortcut("Ctrl+S")
        new_cluster.triggered.connect(self.connect_menu_arquivo_sair)
        self.popup_menu.addAction(new_cluster)

        #self.popup_menu.addAction("New", self.new_cluster)
        #self.popup_menu.addAction("Rename", self.rename_cluster)
        #self.popup_menu.addSeparator()
        #self.popup_menu.addAction("Delete", self.delete_cluster)

    def on_context_menu(self, pos):
        node = self.treeWidget.mapToGlobal(pos)
        self.popup_menu.exec_(self.treeWidget.mapToGlobal(pos))


class ModuloInicial(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.settings()
        # self.create_popup_menu(self, parent)

    def settings(self):
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)
        self.setWindowTitle("Bob - EliSoftWare")

        self.setStyleSheet("QWidget {background-image: url(imagem/bg2.jpg)}")

        # adicona barra de menus.
        MenuInicial.adicionar(self)
        PopupMenu.create_popup_menu(self, parent=None)

        # configura barra de ferramentas.
        BarraFerramentaInicial.botoes_barra_inicial(self)
        BarraFerramentaEdicao.botoes_barra_edicao(self)


        # Clima.atualiza(self)

        self.status = self.statusBar()
        self.status.showMessage("Seja bem vindo - Bob - EliSoftWare")

    @Slot()
    def connect_menu_arquivo_sair(self, checked):
        """
            Dependentes:
                modulo_menu_arquivo
                modulo_barraferramenta_inicial
        """
        sys.exit()

    @Slot()
    def connect_menu_ferramenta_service(self, checked):
        ...
