def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Se está ejecutando el decorador antes de la función original")
        funcion_original()
        print("Se está ejecutando el decorador después de la función original")
    return nueva_funcion

@mi_decorador
def mi_funcion():
    print("Esta es la función original")

# Llamamos a la función decorada
mi_funcion()
