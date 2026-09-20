# 🧠 Quiz Interactivo por Consola

Programa en Python que permite jugar un quiz de opción múltiple, organizado por categorías, con puntaje final y posibilidad de volver a jugar.

## ¿Qué hace?

- Muestra categorías disponibles (Matemática, Programación) para elegir
- Presenta preguntas de opción múltiple en orden aleatorio
- Valida las respuestas del usuario y da feedback inmediato (✅ / ❌)
- Calcula el puntaje final y muestra un mensaje según el desempeño
- Permite jugar varias rondas sin reiniciar el programa

## Tecnologías

- Python 3
- Módulo `random` de la librería estándar

## Cómo ejecutarlo

```bash
python quiz.py
```

No requiere instalar ninguna dependencia externa.

## Estructura del código

- `PREGUNTAS`: diccionario con las preguntas organizadas por categoría
- `elegir_categoria()`: maneja la selección de categoría
- `hacer_pregunta()`: muestra una pregunta y valida la respuesta
- `jugar_quiz()`: recorre todas las preguntas de una categoría
- `mostrar_resultado()`: muestra el resumen final
- `main()`: controla el flujo general del programa

## Posibles mejoras a futuro

- Agregar más categorías y preguntas
- Guardar el mejor puntaje en un archivo
- Poner un límite de tiempo por pregunta
- Convertirlo en una versión web

---
Proyecto realizado como parte de mi camino de aprendizaje en Python.
