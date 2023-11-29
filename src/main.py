import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
script_dir = os.getcwd()
func_dir = os.path.join(script_dir)
sys.path.append(func_dir)
from events import actions

def type_print(texto, velocidad=0.02):
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

    def mostrar_opciones(self):
        type_print("Opciones disponibles:")
        for accion, descripcion in self.acciones.items():
            type_print(f"- {accion}: {descripcion.get('mensaje', 'Mensaje no definido para esta acción.')}")

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
            'inicio': Escena('inicio', """""", {
                'revisar codigo': {"mensaje": "Al sumergirte en el código, descubres una anomalía.",
                                "a_escena": 'consecuencias_decisiones'},
                'entrevistar colegas': {"mensaje": "Decides entrevistar a tus antiguos colegas.",
                                        "a_escena": 'consecuencias_decisiones'},
                'buscar pistas': {"mensaje": "Optas por buscar pistas en los registros de actividad del laboratorio.",
                                "a_escena": 'consecuencias_decisiones'},
                'irse': "Decides abandonar el laboratorio.",
            }),
            'consecuencias_decisiones': Escena('consecuencias_decisiones', "Te enfrentas a las consecuencias de tus decisiones.", {
                'desactivar secuencia': {"mensaje": "Al desactivar la secuencia de comandos, el comportamiento extraño de Esditeo cesa momentáneamente. Sin embargo, pronto te das cuenta de que tu acción ha alertado a alguien o algo.",
                                        "a_escena": 'decision_desactivar_secuencia'},
                'analizar secuencia': {"mensaje": "Al analizar la secuencia de comandos, descubres que es un intento de hacer que Esditeo actúe de manera autónoma y evite ser controlado.",
                                    "a_escena": 'decision_analizar_secuencia'},
            }),
            'decision_desactivar_secuencia': Escena('decision_desactivar_secuencia', """¡Vaya, eso parece haberlo detenido por ahora!
            Pero algo no está bien, siento que alguien nos está observando...""", {
                'seguir investigando': {"mensaje": "Bueno, no hay tiempo que perder. Seguiré investigando, aunque me siento observado...",
                                        "a_escena": 'bosque'},
                'rastrear fuente': {"mensaje": "Antes de seguir, necesito saber quién intentó tomar el control de Esditeo. Puede haber pistas en el sistema. Vamos a rastrearlos.",
                                    "a_escena": 'decision_rastrear_fuente'},
            }),
            'decision_analizar_secuencia': Escena('decision_analizar_secuencia', """Interesante, esto parece un intento de liberar a Esditeo.
            ¿Pero con qué propósito?""", {
                'modificar secuencia': {"mensaje": "Podría usar esto para tener a Esditeo de mi lado, pero debo tener cuidado. No quiero que vuelva a descontrolarse.",
                                    "a_escena": 'decision_modificar_secuencia'},
                'eliminar secuencia': {"mensaje": "No puedo arriesgarme a perder el control de Esditeo. Esto debe irse, y rápido.",
                                    "a_escena": 'decision_eliminar_secuencia'},
            }),
            'decision_rastrear_fuente': Escena('decision_rastrear_fuente', """Encuentras un dispositivo de rastreo que podría ayudarte en tu búsqueda.""", {
                'continuar investigacion': {"mensaje": "Continúas investigando con el dispositivo de rastreo en mano.",
                                            "a_escena": 'bosque'},
            }),
            'decision_modificar_secuencia': Escena('decision_modificar_secuencia', """Podría usar esto para tener a Esditeo de mi lado,
            pero debo tener cuidado. No quiero que vuelva a descontrolarse.""", {
                'continuar investigacion': {"mensaje": "Decides continuar la investigación con la secuencia modificada.",
                                            "a_escena": 'bosque'},
            }),
            'decision_eliminar_secuencia': Escena('decision_eliminar_secuencia', """No puedo arriesgarme a perder el control de Esditeo.
            Esto debe irse, y rápido.""", {
                'continuar investigacion': {"mensaje": "Aunque has eliminado la secuencia, decides seguir investigando.",
                                            "a_escena": 'bosque'},
            }),
            'bosque': Escena('bosque', "Has llegado a un misterioso bosque.", {
                'explorar': "Te aventuras más profundamente en el bosque.",
                'regresar': "Decides volver al laboratorio.",
                'descansar': "Tomar un descanso en medio del bosque.",
            }),
        }
        self.escena_actual = 'inicio'
        self.musica_actual = None

    def cambiar_escena(self, nombre_escena):
        self.escena_actual = nombre_escena
        self.escenas[nombre_escena].mostrar_descripcion()

    def cargar_y_reproducir_musica(self, ruta):
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)

    def ejecutar_accion(self, accion_usuario):
        if accion_usuario == 'salir':
            type_print("Gracias por jugar. ¡Hasta luego!")
            sys.exit()
        acciones_escena_actual = self.escenas[self.escena_actual].acciones
        if accion_usuario == 'ayuda':
            self.escenas[self.escena_actual].mostrar_opciones()
        elif accion_usuario in acciones_escena_actual:
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
        self.cargar_y_reproducir_musica("H:/My Drive/programacion/juego_texto/music/inicio.mp3")
        print()
        type_print("""░▒█▀▀▀░█░░░░█▀▄░█▀▀░█▀▀░▄▀▀▄░█▀▀░█▀▀▄░▀█▀░█▀▀▄░█▀▀▄░░░█▀▄░█▀▀░░░█░░█▀▀▄░░░▀█▀░█▀▀▄
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
            print()
            accion_usuario = input().lower()
            self.ejecutar_accion(accion_usuario)

juego = Juego()
juego.iniciar()