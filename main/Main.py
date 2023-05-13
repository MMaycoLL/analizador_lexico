import sys
from PyQt5.QtWidgets import QApplication
from view.ControladorView import ControladorView

def main():
    app = QApplication(sys.argv) # "{Variable} = %hola%;  Private;1~2"
    controlador = ControladorView()
    controlador.mostrar_ventana()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
