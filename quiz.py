"""
Quiz interactivo por consola
-----------------------------
Programa que hace preguntas de opción múltiple, organizadas por
categorías, lleva el puntaje del jugador y muestra un resumen final.

Autora: Sabrina Soledad Roa
"""

import random

# ---------------------------------------------------------
# 1. Datos: preguntas organizadas por categoría
# ---------------------------------------------------------
# Cada pregunta es un diccionario con:
#   - "pregunta": el texto de la pregunta
#   - "opciones": lista de posibles respuestas
#   - "correcta": el índice (0, 1, 2...) de la opción correcta

PREGUNTAS = {
    "Matemática": [
        {
            "pregunta": "¿Cuánto es 7 x 8?",
            "opciones": ["54", "56", "64", "48"],
            "correcta": 1,
        },
        {
            "pregunta": "¿Cuál es el resultado de 15 - 9?",
            "opciones": ["4", "5", "6", "7"],
            "correcta": 2,
        },
        {
            "pregunta": "¿Cuánto es la raíz cuadrada de 81?",
            "opciones": ["7", "8", "9", "10"],
            "correcta": 2,
        },
    ],
    "Programación": [
        {
            "pregunta": "¿Qué palabra clave se usa en Python para crear una función?",
            "opciones": ["function", "def", "func", "lambda"],
            "correcta": 1,
        },
        {
            "pregunta": "¿Cómo se llama una lista de pares clave-valor en Python?",
            "opciones": ["Lista", "Tupla", "Diccionario", "Conjunto"],
            "correcta": 2,
        },
        {
            "pregunta": "¿Qué símbolo se usa para comentar una línea en Python?",
            "opciones": ["//", "#", "<!-- -->", "/*"],
            "correcta": 1,
        },
    ],
}


# ---------------------------------------------------------
# 2. Funciones principales
# ---------------------------------------------------------

def elegir_categoria():
    """Muestra las categorías disponibles y devuelve la elegida por el usuario."""
    categorias = list(PREGUNTAS.keys())

    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"  {i}. {categoria}")

    while True:
        eleccion = input("\nElegí una categoría (número): ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(categorias):
            return categorias[int(eleccion) - 1]
        print("Opción inválida, probá de nuevo.")


def hacer_pregunta(pregunta_data):
    """Muestra una pregunta con sus opciones y devuelve True si la respuesta es correcta."""
    print("\n" + pregunta_data["pregunta"])
    for i, opcion in enumerate(pregunta_data["opciones"], start=1):
        print(f"  {i}. {opcion}")

    while True:
        respuesta = input("Tu respuesta (número): ").strip()
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta_data["opciones"]):
            return (int(respuesta) - 1) == pregunta_data["correcta"]
        print("Opción inválida, probá de nuevo.")


def jugar_quiz(categoria):
    """Recorre todas las preguntas de una categoría y devuelve el puntaje final."""
    preguntas = PREGUNTAS[categoria].copy()
    random.shuffle(preguntas)  # para que no salgan siempre en el mismo orden

    puntaje = 0
    for pregunta_data in preguntas:
        if hacer_pregunta(pregunta_data):
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            opcion_correcta = pregunta_data["opciones"][pregunta_data["correcta"]]
            print(f"❌ Incorrecto. La respuesta correcta era: {opcion_correcta}")

    return puntaje, len(preguntas)


def mostrar_resultado(puntaje, total):
    """Muestra un mensaje final según el desempeño del jugador."""
    print("\n" + "=" * 40)
    print(f"Resultado final: {puntaje} de {total} correctas")

    porcentaje = (puntaje / total) * 100
    if porcentaje == 100:
        print("🏆 ¡Perfecto! Dominás el tema.")
    elif porcentaje >= 60:
        print("👍 ¡Muy bien! Vas por buen camino.")
    else:
        print("💪 Seguí practicando, la próxima te va mejor.")
    print("=" * 40)


# ---------------------------------------------------------
# 3. Programa principal
# ---------------------------------------------------------

def main():
    print("=" * 40)
    print("  BIENVENIDO/A AL QUIZ INTERACTIVO")
    print("=" * 40)

    jugar_de_nuevo = True
    while jugar_de_nuevo:
        categoria = elegir_categoria()
        puntaje, total = jugar_quiz(categoria)
        mostrar_resultado(puntaje, total)

        respuesta = input("\n¿Querés jugar de nuevo? (s/n): ").strip().lower()
        jugar_de_nuevo = respuesta == "s"

    print("\n¡Gracias por jugar! 👋")


if __name__ == "__main__":
    main()
