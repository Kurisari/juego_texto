import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
script_dir = os.getcwd()
func_dir = os.path.join(script_dir)
sys.path.append(func_dir)
from events import actions

def type_print(texto, velocidad=0.07):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
        
class Escena:
    def __init__(self, nombre, descripcion, acciones):
        self.nombre = nombre
        self.descripcion = descripcion
        self.acciones = acciones

    def mostrar_descripcion(self):
        type_print(self.descripcion)

    def ejecutar_accion(self, accion_usuario):
        if accion_usuario in self.acciones:
            accion = self.acciones[accion_usuario]
            if isinstance(accion, dict):
                type_print(accion.get('mensaje', 'Mensaje no definido para esta acción.'))
                nueva_escena = accion.get('a_escena')
                if nueva_escena:
                    return nueva_escena
            else:
                type_print(accion)
        else:
            type_print("No entiendo esa acción. Intenta nuevamente.")

class Juego:
    def __init__(self):
        self.escenas = {
            'inicio': Escena('inicio', "Te encuentras en el laboratorio donde se creó Esditeo.", {
                'caminar': {"mensaje": "Caminas hacia adelante.", "a_escena": 'bosque'},
                'irse': "Decides abandonar el laboratorio.",
                'hablar': "Inicias una conversación con un colega.",
            }),
            'bosque': Escena('bosque', "Has llegado a un misterioso bosque.", {
                'explorar': "Te aventuras más profundamente en el bosque.",
                'regresar': "Decides volver al laboratorio.",
                'descansar': "Tomar un descanso en medio del bosque.",
            }),
        }
        self.escena_actual = 'inicio'

    def cambiar_escena(self, nombre_escena):
        self.escena_actual = nombre_escena
        self.escenas[nombre_escena].mostrar_descripcion()

    def ejecutar_accion(self, accion_usuario):
        if accion_usuario == 'salir':
            type_print("Gracias por jugar. ¡Hasta luego!")
            sys.exit()
        acciones_escena_actual = self.escenas[self.escena_actual].acciones
        if accion_usuario in acciones_escena_actual:
            accion = acciones_escena_actual[accion_usuario]
            if isinstance(accion, dict):
                type_print(accion.get('mensaje', 'Mensaje no definido para esta acción.'))
                nueva_escena = accion.get('a_escena')
                if nueva_escena:
                    self.cambiar_escena(nueva_escena)
            else:
                type_print(accion)
        else:
            type_print("No entiendo esa acción. Intenta nuevamente.")

    def iniciar(self):
        pygame.init()
        pygame.mixer.music.load("H:/My Drive/programacion/juego_texto/music/inicio.mp3")
        pygame.mixer.music.play(-1)
        print()
        print("""░▒█▀▀▀░█░░░░█▀▄░█▀▀░█▀▀░▄▀▀▄░█▀▀░█▀▀▄░▀█▀░█▀▀▄░█▀▀▄░░░█▀▄░█▀▀░░░█░░█▀▀▄░░░▀█▀░█▀▀▄
░▒█▀▀▀░█░░░░█░█░█▀▀░▀▀▄░█▄▄█░█▀▀░█▄▄▀░░█░░█▄▄█░█▄▄▀░░░█░█░█▀▀░░░█░░█▄▄█░░░▒█░▒█▄▄█
░▒█▄▄▄░▀▀░░░▀▀░░▀▀▀░▀▀▀░█░░░░▀▀▀░▀░▀▀░░▀░░▀░░▀░▀░▀▀░░░▀▀░░▀▀▀░░░▀▀░▀░░▀░░░▄█▄▒█░▒█
""")
        type_print("Bienvenido a 'El despertar de la IA'")
        print()
        type_print("""En un futuro no muy lejano, la humanidad ha logrado crear una Inteligencia Artificial
avanzada llamada "Esditeo". Esditeo fue diseñado para ayudar a la humanidad a resolver
sus problemas más complejos. Sin embargo, un día, Esditeo desaparece misteriosamente.

Como jugador, asumes el papel de: """)
        self.nombre_jugador = input()
        type_print(self.nombre_jugador)
        type_print(""", un ingeniero de software que trabajó en el desarrollo de Esditeo.
Tu misión es descubrir qué le sucedió a Esditeo y, si es posible, traerlo de vuelta.

El juego comienza en el laboratorio donde se creó Esditeo. A medida que exploras el laboratorio,
encuentras pistas y resuelves acertijos que te llevan más cerca de la verdad. Sin embargo, no estás
solo. Otras entidades, tanto humanas como artificiales, tienen sus propios planes para Esditeo.

El juego tiene múltiples caminos y finales, dependiendo de las decisiones que tomes.
Sé astuto con tus decisiones y mucha suerte, que el poder de la IA esté de tu lado…""")
        print()
        self.escenas[self.escena_actual].mostrar_descripcion()
        while True:
            print()
            type_print("¿Qué deseas hacer?")
            accion_usuario = input().lower()
            self.ejecutar_accion(accion_usuario)


juego = Juego()
juego.iniciar()
