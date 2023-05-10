import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.form import Ui_Widget
from modelo.AnalizadorLexico import AnalizadorLexico


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Instanciar la interfaz y configurarla
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Conectar señales y slots
        self.ui.btnAnalizar.clicked.connect(self.analizar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)

    def analizar(self):
        # Obtener la expresión del QLineEdit
        expresion = self.ui.txtExpresion.text()

        # Crear una instancia del analizador léxico
        analizador = AnalizadorLexico(expresion)
        analizador.analizar()

        # Obtener la lista de tokens generada por el analizador léxico
        lista_tokens = analizador.get_lista_tokens()

        # Mostrar los tokens en el QTextEdit de salida
        self.ui.txtRespuesta.clear()
        for token in lista_tokens:
            self.ui.txtRespuesta.append(str(token))

    def limpiar(self):
        # Limpiar los QLineEdit y el QTextEdit
        self.ui.txtExpresion.clear()
        self.ui.txtRespuesta.clear()


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
