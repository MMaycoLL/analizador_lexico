from modelo.AnalizadorLexico  import AnalizadorLexico

def main():
    codigo_fuente = "{23423}"
    analizador = AnalizadorLexico(codigo_fuente)
    analizador.analizar()

    # Accede a la lista de tokens generada por el analizador léxico
    lista_tokens = analizador.get_lista_tokens()
    for token in lista_tokens:
        print(token)

if __name__ == "__main__":
    main()

