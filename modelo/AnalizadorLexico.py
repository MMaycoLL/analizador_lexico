from modelo.Token import Token
from modelo.Categoria import Categoria
from modelo.PalabrasReservadas import PalabrasReservadas


class AnalizadorLexico:
    def __init__(self, codigo_fuente):
        # Inicializa el objeto AnalizadorLexico con el código fuente proporcionado
        self.codigo_fuente = codigo_fuente
        self.lista_tokens = []  # Crea una lista vacía para almacenar los tokens

    def analizar(self):
        i = 0
        while i < len(self.codigo_fuente):
            if self.codigo_fuente[i].isspace():
                i += 1
                continue  # Ignora los espacios en blanco y pasa al siguiente carácter

            token = self.extraer_sgte_token(i)
            self.lista_tokens.append(token)
            i = token.indice_sgte

    def extraer_sgte_token(self, indice):

        token = self.extraer_numeros_naturales(indice)
        if token is not None:
            return token

        token = self.extraer_numeros_reales(indice)
        if token is not None:
            return token

        token = self.extraer_identificador(indice)
        if token is not None:
            return token

        token = self.extraer_palabra_reservada(indice)
        if token is not None:
            return token

        token = self.extraer_operador_aritmetico(indice)
        if token is not None:
            return token

        token = self.extraer_operador_relacional(indice)
        if token is not None:
            return token

        token = self.extraer_operador_logico(indice)
        if token is not None:
            return token

        token = self.extraer_operador_asignacion(indice)
        if token is not None:
            return token

        token = self.extraer_operador_incremento_decremento(indice)
        if token is not None:
            return token

        token = self.extraer_parentesis(indice)
        if token is not None:
            return token

        token = self.extraer_llaves(indice)
        if token is not None:
            return token

        token = self.extraer_terminal(indice)
        if token is not None:
            return token

        token = self.extraer_separador(indice)
        if token is not None:
            return token

        token = self.extraer_hexadecimal(indice)
        if token is not None:
            return token

        token = self.extraer_cadena_caracteres(indice)
        if token is not None:
            return token

        token = self.extraer_comentario(indice)
        if token is not None:
            return token

        token = self.extraer_identificador(indice)
        if token is not None:
            return token

        token = self.extraer_no_reconocido(indice)
        return token

    # Metodo que extrae los numeros naturales
    def extraer_numeros_naturales(self, indice):
        if indice < len(self.codigo_fuente) and (
                self.codigo_fuente[indice].isdigit() or self.codigo_fuente[indice] == '~'):
            posicion = indice
            has_decimal = False
            while indice < len(self.codigo_fuente) and (
                    self.codigo_fuente[indice].isdigit() or (self.codigo_fuente[indice] == '~' and not has_decimal)):
                if self.codigo_fuente[indice] == '~':
                    has_decimal = True
                indice += 1
                '''
                Verifica si hay un separador decimal y llama al método extraer_numeros_reales
                si es el caso, o crea un objeto Token con el fragmento de código extraído y la categoría NATURAL
                '''
            if has_decimal:
                return self.extraer_numeros_reales(posicion)
            return Token(self.codigo_fuente[posicion:indice], Categoria.NATURAL, indice)
        return None

    ''' Metodo que extrae los numeros reales, en este caso en particular se 
    define "~" como el separador decimal'''

    def extraer_numeros_reales(self, indice):
        if indice < len(self.codigo_fuente) and self.codigo_fuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigo_fuente) and (
                    self.codigo_fuente[indice].isdigit() or self.codigo_fuente[indice] == '~'):
                indice += 1
            return Token(self.codigo_fuente[posicion:indice], Categoria.REAL, indice)
        return None

    def extraer_identificador(self, indice):
        if self.codigo_fuente[indice] == "{":
            inicio = indice + 1
            fin = self.codigo_fuente.find("}", inicio)
            if fin != -1:  # Verifica si se encontró el cierre de la llave
                identificador = self.codigo_fuente[inicio:fin]
                if len(identificador) <= 10 and identificador.isalnum():
                    return Token("{" + identificador + "}", Categoria.IDENTIFICADOR, fin + 1)
                else:
                    # Error: identificador no cumple con los requisitos
                    error = self.codigo_fuente[indice:fin + 1]
                    return Token(error, Categoria.ERROR_LEXICO, fin + 1)
            else:
                # Error: falta el cierre de la llave
                error = self.codigo_fuente[indice:]
                return Token(error, Categoria.ERROR_LEXICO, len(self.codigo_fuente))
        elif self.codigo_fuente[indice] == "}":
            # Error: falta la apertura de la llave
            error = self.codigo_fuente[indice:]
            return Token(error, Categoria.ERROR_LEXICO, len(self.codigo_fuente))
        else:
            return None

    def extraer_palabra_reservada(self, indice):  # Metodo que extrae las palabras reservadas
        for palabra in PalabrasReservadas:  # Recorre la lista de palabras reservadas
            if self.codigo_fuente.startswith(palabra, indice):  # Verifica si la palabra reservada se encuentra
                return Token(palabra, Categoria.PALABRA_RESERVADA, indice + len(palabra))
        return None

    def extraer_operador_aritmetico(self, indice):
        operadores_aritmeticos = ["+", "-", "*", "/"]
        for operador in operadores_aritmeticos:
            if self.codigo_fuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_ARITMETICO, indice + len(operador))
        return None

    def extraer_operador_relacional(self, indice):
        operadores_relacionales = ["==", "!=", "<", ">", "<=", ">="]
        for operador in operadores_relacionales:
            if self.codigo_fuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_RELACIONAL, indice + len(operador))
        return None

    def extraer_operador_logico(self, indice):
        operadores_logicos = ["&&", "||", "!"]
        for operador in operadores_logicos:
            if self.codigo_fuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_LOGICO, indice + len(operador))
        return None

    def extraer_operador_asignacion(self, indice):
        operadores_asignacion = ["=", "+=", "-=", "*=", "/="]
        for operador in operadores_asignacion:
            if self.codigo_fuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_ASIGNACION, indice + len(operador))
        return None

    def extraer_operador_incremento_decremento(self, indice):
        operadores_incremento_decremento = ["++", "--"]
        for operador in operadores_incremento_decremento:
            if self.codigo_fuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_INCREMENTO_DECREMENTO, indice + len(operador))
        return None

    def extraer_parentesis(self, indice):
        if self.codigo_fuente[indice] == "(":
            return Token("(", Categoria.PARENTESIS_APERTURA, indice + 1)
        elif self.codigo_fuente[indice] == ")":
            return Token(")", Categoria.PARENTESIS_CIERRE, indice + 1)
        return None

    def extraer_llaves(self, indice):
        if self.codigo_fuente[indice] == "[":
            return Token("{", Categoria.LLAVE_APERTURA, indice + 1)
        elif self.codigo_fuente[indice] == "]":
            return Token("}", Categoria.LLAVE_CIERRE, indice + 1)
        return None

    def extraer_terminal(self, indice):
        if self.codigo_fuente[indice] == ";":
            return Token(";", Categoria.TERMINAL, indice + 1)
        return None

    def extraer_separador(self, indice):
        if self.codigo_fuente[indice] == ",":
            return Token(",", Categoria.SEPARADOR, indice + 1)
        return None

    def extraer_hexadecimal(self, indice):
        if indice < len(self.codigo_fuente) and self.codigo_fuente[indice] in "0123456789ABCDEFabcdef":
            posicion = indice
            while indice < len(self.codigo_fuente) and self.codigo_fuente[indice] in "0123456789ABCDEFabcdef":
                indice += 1
            return Token(self.codigo_fuente[posicion:indice], Categoria.HEXADECIMAL, indice)
        return None

    def extraer_cadena_caracteres(self, indice):
        if indice < len(self.codigo_fuente) and self.codigo_fuente[indice] == "$":
            posicion = indice + 1
            indice += 1
            while indice < len(self.codigo_fuente) and self.codigo_fuente[indice] != "$":
                indice += 1
            if indice < len(self.codigo_fuente) and self.codigo_fuente[indice] == "$":
                return Token(self.codigo_fuente[posicion:indice], Categoria.CADENA_CARACTERES, indice + 1)
            else:
                # No se encontró el cierre de la cadena
                return Token(self.codigo_fuente[posicion:], Categoria.ERROR_LEXICO, indice + 1)
        return None

    def extraer_comentario(self, indice):
        if indice < len(self.codigo_fuente) and self.codigo_fuente[indice] == "#":
            posicion = indice
            while indice < len(self.codigo_fuente) and self.codigo_fuente[indice] != "\n":
                indice += 1
            return Token(self.codigo_fuente[posicion:indice], Categoria.COMENTARIO, indice)
        return None

    def extraer_no_reconocido(self, indice):
        lexema = self.codigo_fuente[indice]
        return Token(lexema, Categoria.NO_RECONOCIDO, indice + 1)

    def get_lista_tokens(self):
        return self.lista_tokens
