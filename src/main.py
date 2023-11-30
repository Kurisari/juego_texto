import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def type_print(texto, velocidad=0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)

def final_uno():
    print()
    type_print("Esditeo: No creas que será tan fácil, antes tienes que resolver el siguiente acertijo, si no")
    print()
    type_print("aciertas volverás al inicio, pero si lo logras podrás desactivarme...")
    print()
    type_print("Nube es mi madre. El viento es mi padre. Bajo pero nunca subo. ¿Qué soy yo?")
    respuesta = input()
    if respuesta.lower() in ["lluvia", "la lluvia"]:
        return True
    else:
        return False

def clearConsole():
    return os.system("cls" if os.name in ("nt", "dos") else "clear")

class Escena:
    def __init__(self, nombre, descripcion, acciones, items=None, nombre_jugador=None):
        self.nombre = nombre
        self.descripcion = descripcion.format(nombre_jugador=nombre_jugador)
        self.acciones = acciones
        self.items = items if items is not None else {}

    def mostrar_descripcion(self):
        type_print(self.descripcion)

    def mostrar_opciones(self):
        type_print("Opciones disponibles:")
        for accion, descripcion in self.acciones.items():
            if isinstance(descripcion, dict):
                mensaje = descripcion.get('mensaje', 'Mensaje no definido para esta acción.')
            else:
                mensaje = descripcion
            type_print(f"- {accion}: {mensaje}")

    def ejecutar_accion(self, accion_usuario):
        if accion_usuario == 'ayuda':
            self.mostrar_opciones()
        elif accion_usuario in self.acciones:
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
    
    def mostrar_items(self):
        if self.items:
            type_print("Tus objetos obtenidos:")
            for item, descripcion in self.items.items():
                type_print(f"- {item}: {descripcion}")
        else:
            type_print("No tienes ningún objeto aún.")

    def agregar_item(self, item, descripcion):
        self.items[item] = descripcion

class Juego:
    def __init__(self):
        self.nombre_jugador = ""
        self.items = {}
        self.escenas = {
            'inicio': Escena('inicio', f"""
---------------------------------------------------------
---------------------------------------------------------
-----------------------=@@@@@%#*=------------------------
---------------------%@@@@@@@@@@@@=----------------------
--------------------=@@@@@@@@@@@@@@+---------------------
--------------------#@@@@@@@@@@@@@@@---------------------
--------------------+@@@@@@@@@@@@@@@=--------------------
--------------------+@@@@@@@@@@@@@@@=--------------------
--------------------%@@@@@@@@@@@@@@@+--------------------
--------------------=@@@@@@@@@@@@@@@---------------------
---------------------+@@@@@@@@@@@@#=---------------------
----------------------=@@@@@@@@@@@-----------------------
-----------------------%@@@@@@@@@+-----------------------
----------------------*@@@@@@@@@@@*----------------------
------------------=*%@@@@@@@@@@@@@@@%#+------------------
------------=+*#%@@@@@@@@@@@@@@@@@@@@@@@@#*+-------------
----------+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=----------
---------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=---------
---------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*---------
--------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
--------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
--------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
---------=======================================---------
---------------------------------------------------------
Manu: Hola {self.nombre_jugador}, soy Manu, cuanto tiempo sin vernos, ¿ya estás al tanto de lo que sucedió?
necesitamos descubrir qué fue lo que pasó con nuestra más grande creación, ¿me puedes ayudar con algunos pendientes de esta lista? """, {
                'si': {"mensaje": f"Manu: Muchas gracias {self.nombre_jugador}, ¡sabía que podía contar con tu ayuda!",
                                "a_escena": 'lista'},
                'no': {"mensaje": "Manu: Bueno... no te preocupes, ya lo haré yo mismo..., que te vaya muy bien en lo que tengas que hacer",
                                        "a_escena": 'nolista'},
            }),
            'lista': Escena('lista', """-------------- COSAS QUE HACER PARA INVESTIGAR DESAPARICIÓN --------------
    -> Revisar código fuente de Esditeo
    -> Entrevistar a compañeros implicados en el desarrollo
    -> Buscar pistas
--------------------------------------------------------------------------""", {
                'revisar codigo': {"mensaje": f"""
                                    
                    ------------------------------------------------
                    ------X$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$x------
                    ------;+&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$X:------
                    ------;+$XXXXXXXXXxxxxx++xxxxxXXXXXXXXX$X;------
                    ------;+$XXXXXxx++;;;;::::;;;;++xxXXXXX$X;------
                    ------;+$XXXx++;;::..........::;;++xxXX$X;------
                    ------;+$XXxx+;::..          ..::;++xxX$X;------
                    ------;+$$$$$$XXXx;:          ..:;;+xxX$X;------
                    ------;+&$$$$$$$$$$$$$$$$Xx+;:::;;+xxX$$X;------
                    ------;;&$$$$$$$$$$$$$$$$$$$$$$$$XxXX$$$x;------
                    ------;;&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$x;------
                    ------;;&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&x;------
                    ------:;&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&X$x:------
                    ------:X&&&&&&&&&&&&x::::+&&&&&&&&&&&&$&X:------
                    ------------------ &&&&&&&& --------------------        
                    ------------- &&&&&&&&&&&&&&&&&& ---------------
                    ------------- &&&&&&&&&&&&&&&&&& ---------------
                    ------------------------------------------------
                                    
Al sumergirte en el código, descubres una anomalía. Hay una secuencia de comandos extraña que no
recuerdas haber programado.""",
                            "a_escena": 'codigo'},
                'entrevistar colegas': {"mensaje": "Decides entrevistar a tus antiguos colegas.",
                                        "a_escena": 'pendiente'},
                'buscar pistas': {"mensaje": "Optas por buscar pistas en los registros de actividad del laboratorio.",
                                "a_escena": 'pendiente'},
            }, items={'lista': """-------------- COSAS QUE HACER PARA INVESTIGAR DESAPARICIÓN --------------
    -> Revisar código fuente de Esditeo
    -> Entrevistar a compañeros implicados en el desarrollo
    -> Buscar pistas
--------------------------------------------------------------------------"""}),
            'nolista': Escena('nolista', """""""", {
                
            }),
            'codigo': Escena('codigo', """Tú: Esta es mi parte del código... pero no recuerdo haber programado esta parte...

Tú: Esta es la parte donde los datos se procesan y se mandan al servidor, pero...
estos no son nuestros servidores, apuntan a... ¿otra región?

Tú: ¿Debería desactivar la secuencia o analizarla?""", {
                'desactivar secuencia': {"mensaje": "Al desactivar la secuencia de comandos, el comportamiento extraño de Esditeo cesa momentáneamente. Sin embargo, pronto te das cuenta de que tu acción ha alertado a alguien o algo.",
                                        "a_escena": 'decision_desactivar_secuencia'},
                'desactivar': {"mensaje": "Al desactivar la secuencia de comandos, el comportamiento extraño de Esditeo cesa momentáneamente. Sin embargo, pronto te das cuenta de que tu acción ha alertado a alguien o algo.",
                                        "a_escena": 'decision_desactivar_secuencia'},
                'desactivarla': {"mensaje": "Al desactivar la secuencia de comandos, el comportamiento extraño de Esditeo cesa momentáneamente. Sin embargo, pronto te das cuenta de que tu acción ha alertado a alguien o algo.",
                                        "a_escena": 'decision_desactivar_secuencia'},
                'analizar secuencia': {"mensaje": "Al analizar la secuencia de comandos, descubres que es un intento de hacer que Esditeo actúe de manera autónoma y evite ser controlado.",
                                    "a_escena": 'decision_analizar_secuencia'},
                'analizar': {"mensaje": "Al analizar la secuencia de comandos, descubres que es un intento de hacer que Esditeo actúe de manera autónoma y evite ser controlado.",
                                    "a_escena": 'decision_analizar_secuencia'},
                'analizarla': {"mensaje": "Al analizar la secuencia de comandos, descubres que es un intento de hacer que Esditeo actúe de manera autónoma y evite ser controlado.",
                                    "a_escena": 'decision_analizar_secuencia'},
            }),
            'decision_desactivar_secuencia': Escena('decision_desactivar_secuencia', """Tú: ¡Vaya, eso parece haberlo detenido por ahora!
Pero algo no está bien, siento que alguien me está observando...
Tú: Desde aquí puedo rastrear la fuente, pero no sé si eso sea demasiado arriesgado
y mejor deba seguir investigando antes de adentrarme más...""", {
                'seguir investigando': {"mensaje": """
                    &&&&&&&&&&&$$$&&&&$$$&$$$$$$X$$$$$XX$&&&&&&&&$&&&&&&&&&&&&&&&&&&&
                    &&&&&&&&&&&&&$&&&&&&&&$$$XX+;+++;;;+X$&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    &&&&&&&&&&&&&&&&&&&x;:::xXx;::::::;xXX:   :+&&&&&&&&&&&&&&&&&&&&&
                    &&&&&&&&&&&&&&$$&&x:;$&$$x; ..:;;;.xx$$$X$X:x&&&&&&&&&&&&&&&&&&&&
                    &&&&&&&&&&&&&&&$$&x;X;;::;x$$Xxxx$$$X; :+;&XX&&&&&&&&&&&&&&&&&&&&
                    $X$$$X+$&&&&&&&$$&Xx&X+;;+$$&&$$$&&&&X;;+X&&$$&$&&&&&&&&&&&&&&&&&
                    ;+;  ;X$&&&&&&&X$$XX$$x;.;xxX$&&&&$XXX;.;X&&$$&&&$xX:;XX$&&&&&&&&
                    $&&$xX&&&&&&&&&&X$+;;;;;x;;;;$&&&&$+;+;x++;;;+&&&&&; :$&$&&&&&XXx
                    &&&&&$$&&&&&&&&&&X;:::;;;:::x$XX&&&&&&&$x;:;;x&&&&&&&&&&&&&&&&$..
                    $$$$$$Xx&&&&&&&&&&&;:...::::.:$$&&&&&&&&&X;;;X&&&X;;&&&&&$&&&&&$$
                    X+;;+$$$&$&XXXx&X$&x;...... .+;&&&&&&&&&&&&XX&&&&&Xx++;+&&&&&&&$+
                    XXXXXX$$$x. ;x: ;$&&;;:..   .+::&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&
                    xxxxxXXXXXxX$$$XX$&&X;;;:    x;X;++X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    ++++xxxxx;;xX$$$+;$$$x+;;   . :;;;::x$&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    ;;;+++++x+x+;;;xXX$$$$X+;. ;    :;;X$$&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    ;;;;;;;++++xxxxXXXX$$$$$x;;;.    :+&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    ;;;;;;;;;;+++xxxxXXXX$$$$X+;; ; &&++$&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    ;;;;;;;;;;;;+++xxxxXXX$$$$$x+   &&x;x:$$&&&X&$&&&&&&&&&&&&&&&&&&&
                    &&$x;;;;;;;;;;+++xxxXXX$$$$X+;  $$;:x&&&&&&X+$&&&x&&&&&&&&&&&&&&&
                    &&&X;;;;;;;;;;;+++xxxxXX:     :  ; X&&&&&&&;;$x$&;X&$XX&&&&&&&&&&
                    &&&X;;;;;;;;;;;;+++xxxx        . :  x&&&&&$;;$$X+x++xx++X&&&&&&&&
                    &&&$X;;;;;;;;;;;;+++xx           ;;  ;+&&&&+;X++;;;+;;xX&$&&&&&&&
                    &&&&X;;;;;;;;;;;;;+++           :;;$+   x&&&+$;:.;: X+XX&X&&&&&&&
                    &&&&x;:;;;;;;;;;;;;           .  :.+&x;  ;$&&X; ;  X&+x$$&&&&&&&&
                    &&&&XX:;;;;;;;;;;; .    .:    .    :XX;  .;X&$ :  : :;+&X$$&&&&&&
                    &&&&&+;;;;;;;;;;:      .:;:    .  . .x  : ;;&&X:; X  .X&Xx$&&&&&&
                    &&&&&x;;;;;;;;:      . .:;;    :      ;   .;;&&X .+  :;+$&$&&&&&&
                    &&&&&$X;;;;;          ;;;++;   .:       ;: ;;;&&$X    .;xx&&&&&&&
                    &&&&&&x;;;      :;;;;++;xX$$:   :;.    .    ;;x&&$    .+xxX$&&&&&
                    &&&&&&x+;    .  ;;;;;;xXX$$$x.  :;;;  ::.:; ;;;x&&$  :;X$&$$&&&&&
                    &&&&&&$$   ;  +  : ;;XX$$$$&$;: .;;;;;;;;;;  ;;;+&&&:  ;X&$X&&&&&
                    &&&&&&&X.; ;; xx X+;XX$$$$&&&+;;;;;;;;;;;;;; :;;;+&&&$ ;$&X&&&&&&
                    $$$&&&&XXXxXXXXXXXXXXXXXXXXXXXXXXXXXX&&&&&&x: ;;;;x$&&&xxX&$X$&&&
                    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Tú: Bueno, no hay tiempo que perder. Seguiré investigando, aunque me siento observado...""",
                                        "a_escena": 'investigando'},
                'rastrear fuente': {"mensaje": "Antes de seguir, necesito saber quién intentó tomar el control de Esditeo. Puede haber pistas en el sistema. Vamos a rastrearlos.",
                                    "a_escena": 'decision_rastrear_fuente'},
            }),
            'investigando': Escena('investigando', """Tú: ¿Qué parte del código debería investigar ahora?
Tú: Puedo revisar: guardado de datos o entrenemiento, ¿Qué debería hacer primero?""", {
                'guardado de datos': {"mensaje": "Tú: Yo creo que el mejor camino será revisar la parte del guardado de datos para ver a donde se están yendo.",
                                            "a_escena": 'guardado'},
                'entrenamiento': {"mensaje": "Continúas investigando con el dispositivo de rastreo en mano.",
                                            "a_escena": 'entrenamiento'},
            }),
            'guardado': Escena('guardado', """Continúas investigando, pero al analizar los registros descubres una serie de patrones extraños.
Parece ser que la información se está enviando encriptada a otra región.
Tú: Esto no está bien, también los datos finales se están mandando a otra región, ¡tienen control absoluto!

Te llega un mensaje a tu número personal...

Tú: ¿Qué es eso? No tengo idea de quién podrá ser, ¿debería abrirlo?""", {
                'si': {"mensaje": "Tú: A ver qué dirá",
                                            "a_escena": 'abrir'},
            }),
            'abrir': Escena('abrir', f"""
--------------------------------------------------------------------------
------------------------------ 1 Mensaje nuevo ---------------------------
De: Fnzve Ovfgrav

Mensaje:
\'Sabemos que te has entrometido. Detente ahora o enfrenta las
consecuencias.\'
--------------------------------------------------------------------------
--------------------------------------------------------------------------

Tú: ¿Debo continuar aunque mi vida corra riesgo o mejor debería parar?""", {
                'continuar': {"mensaje": """Tú: ¡No dejaré que esos maliantes controlen el mundo!, no quiero que las demás personas
le tengan miedo a algo que debía dar la paz.""",
                                            "a_escena": 'confrontacion'},
                'parar': {"mensaje": "",
                                            "a_escena": 'parar'},
            }),
            'confrontacion': Escena('confrontacion', """
Mientras te adentras más en la investigación, descubres que en verdad si es una red clandestina que quiere
controlar el mundo...

Tú: Debo detenerlos, ¿qué debería de hacer, desactivarlo o infiltrarme en la red? """, {
                'desactivar': {"mensaje": """Tú: No puedo permitir que la humanidad siga corriendo riesgo con el poder que puede llegar
a tener Esditeo, la desactivaré de inmediato""",
                                            "a_escena": 'final uno'},
                'infiltrarme en la red': {"mensaje": "",
                                            "a_escena": 'pendiente'},
            }),
            'final uno': Escena('final uno', """Tú: Esto lo hice muchas veces cuando veía peligro, para desconectarla solo hay que
poner este código...
Tú: Espera, esto no es lo que estaba, es diferente...""", {
                'No encontraras la respuesta asi, pero te puedo ayudar': {"mensaje": "Tú: Yo creo que el mejor camino será revisar la parte del guardado de datos para ver a donde se están yendo.",
                                            "a_escena": 'guardado'},
            }),
        }
        self.escena_actual = 'inicio'
        self.musica_actual = None

    def cambiar_escena(self, nombre_escena):
        self.escena_actual = nombre_escena
        print()
        self.escenas[nombre_escena].mostrar_descripcion()

    def cargar_y_reproducir_musica(self, ruta):
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)
    
    def creditos(self):
        pausa = 3
        print("Hecho por: Cristian Aragón Salazar")
        time.sleep(pausa)
        print("Colaboración especial: El creador de C++")
        time.sleep(pausa)
        print("""                           X&&&&&&&$$+                             
                       .X&&&&&&&&&&&&&&&$+                         
                     x&&&&&&&&&$XXxxxxX$&&&$;                      
                   +&&&&&&$Xxx+;:::::....+$&&;                     
                 ;&&&&Xxxx++;;:::..........:&&&X                   
                +&&$xx+++++;;;:::.....    ..:&&&$                  
               :&&&++++++++;;;:::.....     ..x&&&X                 
               ;&&X+++++++;;;;::::::....    .;$&&&.                
               .&&x+++++;;;;;;:;:;;:.....  ...x$&&.                
               ;&$++++xX$$X+;;+++xxX$$$X+:....;X$&.                
               +&X++x$$$X$$$XXxx+xXXXXx;::::...+X$                 
               ;&x+xXxxX$$$$$X+;.:X$$&&$Xx::....Xx                 
                &x+xxX&$&&X$$X+;..+xXx+:..;:....x;                 
                xx+xxxxXX$$XXx+:.....;+;;:......: +.               
               .x++xxxxxxxxxxx+:...........  ...;..;               
               ;x++++++++xxx+++:....;:....    ..;x.:               
               +xx;;;++++xXx&&XXx$&x:+;:.    ......                
               :xx;;;;+++xXXX$XXXx;...x;......... .                
                ;+;;;++++xx$&$$$&$X++::+;........                  
                 .++++++X$$$$$$$$$$$XXxXx:......                   
                  .++++x$&&&$XXx+;::;x&$X;......                   
                   ;+xxx$&$XXXXXxXx;..;Xx;:....                    
                    +xxxXXxxxxXXx;:....:+;:...                     
                     +xxxx++xXx+;;;.....::::..                     
                      xxXXxX$XXxxx+x++++;;::.                      
                     xxxX$&&&$$$$$XXX$Xx;::.. :X                   
                   +&& ;xxX$&&$&&$$$X+:::....  &&:                 
                  &&&+  +xxxxxxxxx++;::.....    &&;                
                ;&&&&.   :xxxxxxx++;::.....     X&$X:              
           .x&&&&&&&X.     ;xx+++++;::...       xX$$$$$$x:         
      :$&&&&&&&&&&$Xx:       .x++++;:..         +X$$$$$$&&&&&$.    
  $&&&&&&&&&&&&&&&$X;:          ++++            ;X&&$$$$$&&&&&&&$$x
&&&&&&&&&&&&&&&&&&X+..        +Xxx;..:          +X&$$$$$$$&&&&&&&&&
&&&&&&&&&&&&&&&&&&X;:       X$X; .:;+;:;.       xX&&&&&$$$$&&&&&&&&
&&&&&&&&&&&&&&&&&&X:;     :++$+xXX:    :;;:     +X&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&$.;  .   .+;X$;:x++x+   ..:   +X&&&&&&&&&&&&&&&&&

                        Miguel Ángel Romo""")
        time.sleep(pausa)
        print("Gracias por haber jugado...")
        exit(0)

    def ejecutar_accion(self, accion_usuario):
        if accion_usuario == 'salir':
            type_print("Gracias por jugar. ¡Hasta luego!")
            sys.exit()
        elif accion_usuario == 'items' or accion_usuario == 'revisar items' or accion_usuario == 'ver items':
            self.mostrar_items()
        else:
            acciones_escena_actual = self.escenas[self.escena_actual].acciones
            if accion_usuario == 'ayuda':
                self.escenas[self.escena_actual].mostrar_opciones()
            elif accion_usuario in acciones_escena_actual:
                accion = acciones_escena_actual[accion_usuario]
                if isinstance(accion, dict):
                    type_print(accion.get('mensaje', 'Mensaje no definido para esta acción.'))
                    nueva_escena = accion.get('a_escena')
                    if nueva_escena:
                        if nueva_escena == 'final uno':
                            self.cambiar_escena(nueva_escena)
                            nueva_escena_actual = self.escenas[self.escena_actual]
                            if final_uno():
                                clearConsole()
                                print()
                                type_print("Lo has logrado, has desactivado a Esditeo, pero quedan preguntas sin respuesa,")
                                print()
                                type_print("has protegido la seguridad de las personas, pero la verdad aún sigue oculta...")
                                print()
                                self.creditos()
                            else:
                                type_print("No lo has logrado, tendrás que ir al inicio de nuevo...")
                                type_print("Cambiando escena...")
                                self.cambiar_escena('inicio')
                                nueva_escena_actual = self.escenas['inicio']
                        else:
                            self.cambiar_escena(nueva_escena)
                            nueva_escena_actual = self.escenas[self.escena_actual]
                            if nueva_escena_actual.items:
                                for item, descripcion in nueva_escena_actual.items.items():
                                    self.agregar_item(item, descripcion)
                else:
                    type_print(accion)
            else:
                type_print("No entiendo esa acción. Intenta nuevamente.")
    
        
    def mostrar_items(self):
        if self.items:
            type_print("Tus objetos obtenidos:")
            for item, descripcion in self.items.items():
                type_print(f"- {item}: {descripcion}")
        else:
            type_print("No tienes ningún objeto aún.")

    def agregar_item(self, item, descripcion):
        self.items[item] = descripcion
    
    def minijuego():
        type_print("¡Bienvenido al minijuego!")
        type_print("Te encuentras frente a un panel con un código encriptado.")
        type_print("Debes descifrar el código para avanzar.")
        
        codigo_encriptado = "xftub!jdf!cz!opx"
        codigo_descifrado = "".join([chr(ord(char) - 1) if char.isalpha() else char for char in codigo_encriptado])
        
        type_print(f"Encriptado: {codigo_encriptado}")
        type_print("Descifra el código. Puedes probar cambiando cada letra por la anterior en el alfabeto.")

        intentos = 3
        while intentos > 0:
            intento_usuario = input("Tu respuesta: ").lower()
            if intento_usuario == codigo_descifrado:
                type_print("¡Correcto! Has descifrado el código.")
                return
            else:
                type_print("Respuesta incorrecta. Inténtalo de nuevo.")
                intentos -= 1

        type_print("Has agotado tus intentos. Volviendo a la decisión principal.")


    def iniciar(self):
        pygame.init()
        self.cargar_y_reproducir_musica("H:/My Drive/programacion/juego_texto/music/inicio.mp3")
        print()
        type_print("""
░▒█▀▀▀░█░░░░█▀▄░█▀▀░█▀▀░▄▀▀▄░█▀▀░█▀▀▄░▀█▀░█▀▀▄░█▀▀▄░░░█▀▄░█▀▀░░░█░░█▀▀▄░░░▀█▀░█▀▀▄
░▒█▀▀▀░█░░░░█░█░█▀▀░▀▀▄░█▄▄█░█▀▀░█▄▄▀░░█░░█▄▄█░█▄▄▀░░░█░█░█▀▀░░░█░░█▄▄█░░░▒█░▒█▄▄█
░▒█▄▄▄░▀▀░░░▀▀░░▀▀▀░▀▀▀░█░░░░▀▀▀░▀░▀▀░░▀░░▀░░▀░▀░▀▀░░░▀▀░░▀▀▀░░░▀▀░▀░░▀░░░▄█▄▒█░▒█

""")
        type_print("Bienvenido a 'El despertar de la IA'")
        print()
        type_print("""En un futuro no muy lejano, la humanidad ha logrado crear una Inteligencia Artificial
avanzada llamada "Esditeo". Esditeo fue diseñado para ayudar a la humanidad a resolver
sus problemas más complejos. Sin embargo, un día, Esditeo desaparece misteriosamente.

Como jugador, asumes el papel de: """)
        nombre_jugador = input()
        self.nombre_jugador = nombre_jugador
        self.escenas['inicio'] = Escena('inicio', f"""
                    ---------------------------------------------------------
                    ---------------------------------------------------------
                    -----------------------=@@@@@%@*=------------------------
                    ---------------------%@@@@@@@@@@@@=----------------------
                    --------------------=@@@@@@@@@@@@@@+---------------------
                    --------------------#@@@@@@@@@@@@@@@---------------------
                    --------------------+@@@@@@@@@@@@@@@=--------------------
                    --------------------+@@@@@@@@@@@@@@@=--------------------
                    --------------------%@@@@@@@@@@@@@@@+--------------------
                    --------------------=@@@@@@@@@@@@@@@---------------------
                    ---------------------+@@@@@@@@@@@@#=---------------------
                    ----------------------=@@@@@@@@@@@-----------------------
                    -----------------------%@@@@@@@@@+-----------------------
                    ----------------------*@@@@@@@@@@@*----------------------
                    ------------------=*%@@@@@@@@@@@@@@@%#+------------------
                    ------------=+*#%@@@@@@@@@@@@@@@@@@@@@@@@@*+-------------
                    ----------+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=----------
                    ---------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=---------
                    ---------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*---------
                    --------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
                    --------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
                    --------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#---------
                    ---------=======================================---------
                    ---------------------------------------------------------

Manu: Hola {self.nombre_jugador}, soy Manu, cuanto tiempo sin vernos, ¿ya estás al tanto de lo que sucedió?
necesitamos descubrir qué fue lo que pasó con nuestra más grande creación, ¿me puedes ayudar con algunos
pendientes de esta lista? """, {
            'si': {"mensaje": f"Manu: Muchas gracias {self.nombre_jugador}, ¡sabía que podía contar con tu ayuda!",
                            "a_escena": 'lista'},
            'no': {"mensaje": "Manu: Bueno... no te preocupes, ya lo haré yo mismo..., que te vaya muy bien en lo que tengas que hacer",
                                    "a_escena": 'nolista'},
        })
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
            accion_usuario = input(">").lower()
            self.ejecutar_accion(accion_usuario)

juego = Juego()
juego.iniciar()