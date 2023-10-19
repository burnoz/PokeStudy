from random import choice

preguntas = {
    "El perímetro de un cuadrado es de 80 cm. ¿Cuál es su área?" : ["400"],
    "Un tren viaja a una velocidad de 120 km/h. ¿Cuántos segundos tardará en recorrer 500 km?": ["15000"],
    "Una mezcla de agua y alcohol contiene 30% de alcohol. ¿Cuántos litros de alcohol hay en 10 litros de la mezcla?": ["3"],
    "Un rectángulo tiene una base de 12 cm y un área de 30 cm. ¿Cuál es su altura?": ["5"],
    "¿Cuál es el resultado de la siguiente operación?\n (2x + 3) - (x - 1) = ?": ["x + 4"],
    "¿Cuál es una posible solución para la siguiente ecuación?\n x² + 4x - 5 = 0": ["1", "-5"],
    "¿Cuál es el valor de x en la siguiente ecuación?\n 2x - 3 = 9": ["6"],
    "¿Cuál es el resultado de la siguiente operación?\n (2 + 3) / 5 * 4 = ?": ["4"],
    "¿Cuál es la ecuación cuadrática que tiene las soluciones x = 2 y x = -3?": ["(x - 2) * (x + 3) = 0", "(x - 2)(x + 3)"]
}

def cuestionario():
    p = []
    correctas = 0
    incorrectas = 0

    while len(p) < len(preguntas):
        pregunta = choice(list(preguntas.keys()))

        if pregunta not in p:
            p.append(pregunta)

        else:
            continue

        print(pregunta)
        respuesta = input("Respuesta: ")

        if respuesta in preguntas[pregunta]:
            print("Correcto")
            correctas += 1
            print()

        else:
            print("Incorrecto")
            incorrectas += 1
            print()

    print("Fin del cuestionario")
    print("Correctas:", correctas)
    print("Incorrectas:", incorrectas)
