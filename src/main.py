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

class Juego:
    def __init__(self):
        self.camino = ""
        self.final = ""
        self.nombre_jugador = ""
        self.accion = ""

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
        self.ejecutar_accion()
        

    def ejecutar_accion(self):
        while True:
            type_print("¿Qué deseas hacer?")
            accion_usuario = input().lower()
            if accion_usuario == 'salir':
                type_print("Gracias por jugar. ¡Hasta luego!")
                sys.exit()
            if accion_usuario in actions.acciones:
                type_print(actions.acciones[accion_usuario])
            else:
                type_print("No entiendo esa acción. Intenta nuevamente.")

juego = Juego()
juego.iniciar()
