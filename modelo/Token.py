class Token:
    def __init__(self, palabra, categoria, indice_sgte):
        self.palabra = palabra
        self.categoria = categoria
        self.indice_sgte = indice_sgte

    def __repr__(self):
        return f"Token(palabra='{self.palabra}', categoria='{self.categoria}', indice_sgte={self.indice_sgte})\n"
