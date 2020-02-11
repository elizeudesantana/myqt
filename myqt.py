from PySide2.QtWidgets import QApplication, QMainWindow
from ext.modulo_inicial import ModuloInicial
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModuloInicial()
    window.show()
    sys.exit(app.exec_())
