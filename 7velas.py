#AAAAAAAAAA ESTOY ESTRESADO
import os
from colorama import init, Fore, Back, Style
os.system("clear")
name = input("\n Introduce tu nombre visitante...: ")

def banner():
    os.system("clear")
    print(Fore.YELLOW+f"""
                                                                              
            =============================================
            %               Las 7 velas                  %
            %      ESTE JUEGO TIENE MÁS DE 20 FINALES    %
            %      TE HARA REFLEXIONAR Y DECIDIR.        %
            %      deberas ser inteligente, para escapar %
            %            Creditos a Vulk4n0              %
            % Actualizado: 28-03-21                      %
              =========================================== 

  Bienvenid@ {name} este juego se basa en las  desiciones que tomes,
  elegiras un personaje con el cual deberas de jugar y ser su 
  acompañante.Ten siempre presente
  que tus desiciones influyen en el juego
  y no olvides, NO CONFIES EN NADIE.
  (Tendras muchas oportunidades, pero para ganar)
  (deberas encontrar los 7 finales buenos. por nivel.)

 
 1)Frank: -este personaje es amistoso.- es un viejo amigo tuyo

 2)Khiara: -este personaje es muy seria.(no disponible aun)

 0)Salir
 """)


def frank():
    print()
    print(f"""

 [La historia se situa en que Frank te invita]
 [A pasar tiempo junto a el, como los viejos tiempos]

 Hola {name} ....
 hoy volvi de viaje y tenia pensado
 visitar a un antiguo amigo en el hospital psiquiatrico.
 NO pienses que mi amigo este loco eh, solo, son cosas del pasado.

 pero bueno, a donde vamos primero? a mi casa a cambiarme de ropa?
 o vamos directo donde mi amigo?

    """)
    
    eleccion = int(input(" 1)Ir donde su amigo [nivel 1]\n 2)Ir a su casa(aun no)\n 3)No acompañarlo(aun no) \n Introduce tu opción: "))
    os.system("clear")
    if eleccion == 1: #opcion 1 ir donde su amigo
        print("""
 Excelente broder, vamos pues directamente donde mi amigo...

 35  MINUTOS DESPUES

 "suena un bombazo" -Frank: hey... tan bien que ibamos no crees?
 voy a tener que revisar.. creo que puede ser la rueda.
 "baja del vehiculo" -Frank: Jajajaj como sospechaba, la rueda era.
 la pobre rueda se pincho con un clavo.

 ¿Que hacemos?
        """)
        
        l = int(input(" 1)llama a una grua y que nos lleven. \n 2)Llama a un amigo que nos recoja en su auto. \n respuesta: "))
        os.system("clear")
        if l == 1: #opcion1 sub1
            print("\n Okey hermano, ¿sabes cual es el numero de la grua?")
            r = int(input(" 1)si \n 2)no\n respuesta: "))
            os.system("clear")
            if r == 1:
                print(f"\n -Frank: Me la pasas? porfavor") #sigue la historia
                cel = int(input(" -el numero es: ")) 
                os.system("clear")
                print(f" \n -Frank: vaya, llame como 5 veces al {cel} y nadie me contesto...\n dile a tu amigo y este auto lo recoje mi primo")
                l = int(input("\n [presiona 2 para llamar a un]\n [amigo que nos recoja en su auto.]\n [responde: ")) #termina la historia
                os.system("clear")
            if r == 2:
                print(" \n -Frank: Okey broder, pues llama a tu amigo pues") #termina esa historia y se salta al otro punto
                l = int(input("\n [presiona 2 para llamar a un]\n [amigo que nos recoja en su auto.]\n\n [responde: "))
                os.system("clear")
        
        if l == 2:
            n = input("\n-Frank: Tu amigo como se llama?: ")
            os.system("clear")
            print(f"""
 -Frank: supe que llamaste a {n},que bueno que llegara pronto jajaja

  *llega {n}* -{n}: Vaya problema que te has montado dios mio...
  pero ok, subanse a mi auto y los llevare a su casa

  40 minutos despues
  *llegan a casa*

  -frank: Gracias {n}.... okey, nos arreglamos, compramos unas flores
          y vamos a visitar a mi amigo. de acuerdo?
            
            """) #opcion2 sub2 que tu amigo nos recoja
            d = int(input(" 1)si \n 2)no \n responde: "))
            os.system("clear")
            while d == 2:
                print("\n Necesito visitar a mi amigo, de acuerdo?")
                d = int(input(" 1)si \n 2)no \n Responde: "))
                os.system("clear")
            if d == 1:
                print("""
 OKey vamos!!!....

 "camino al hospital"

-frank: oye una duda... trabajas en algo?    
                """)
                pr = int(input("\n 1)si \n 2)no \n Responde: "))
                os.system("clear")
                if pr == 1:
                    print(" \n-Frank: ¿Enserio? wow\n")
                    pro = input(" -Frank: Ha que te dedicas?: ")
                    os.system("clear")
                    print(f" \n -Frank: wow... ser {pro} siempre me ha aparecido algo\n muy interesante...pero bueno, ya casi llegamos...")
                else:
                    print(" \n -Frank: okok, no hay problema.... igualmente yo \n tampoco trabajo en algo jajajja.. pero ok, casi llegamos")
            print(""" 

 *llegan al hospital*

 -Frank: Hey...quieres acompañarme o quedarte en el auto?           
            """)
            ele = int(input(" 1)Acompañalo\n 2)quedate en el auto\n [Responde: "))
            os.system("clear")
            if ele == 1: #1 desenlance acompañar
                print(" \n -Frank: gracias por acompañarme... es cerca de aca.")
                print()
                print(" -Frank: no se si te conte... mi amigo se llama jack...")
                print("""
-Guardia: hola, cual es el motivo de su llegada?
-Frank: pues vengo a visitar a mi hermano
-Guardia: como se llama tu hermano?
-Frank: se llama jack blanco
-Guardia: okey...por que vienen a esta hora? (11 pm)
-Frank: es que recien llegue de un viaje y aproveche...
-Guardia: bajese del auto por favor.
"Frank se baja del auto pero con una piedra en la mano"
 y golpea fuertemente al guardia.
                """)
                siono = int(input("\n -Frank: Ayudame a meter este hombre a la maleta\n 1)aceptar \n 2)negarte \n Responde: "))
                os.system("clear")
                if siono == 1: #mini desenlase 1 ayudas
                    print("\n *cargas al hombre al auto y se bajan*\n\n *llegan a la puerta principal*\n\n-Frank: oye gracias por ayudarme jajaja....\n-1 minuto luego-\n-Frank: me cago en todo... esta puerta tiene una clave...ah,\n -Frank: la tarjeta del guardia decia esto:'mb dmbwf ft 4589'\n """)
                    hack = int(input(" Introduce la contraseña: "))
                    if hack == 3478:
                        print("")
                    while hack != 3478:
                        print("error, contraseña incorrecta")
                        hack = int(input("Introduce la contraseña: "))
                    os.system("clear")
                    print("\n [Acceso permitido]\n")
                    print(" -Frank: La verdad muchas gracias por ayudarme...\n -Frank: oye...me esperas aca? o vamos a buscar a jack?")
                    elije = int(input("\n 1)Ir a buscar a jack\n 2)Quedarte y esperar\n Respuesta: "))
                    os.system("clear")
                    if elije == 1: #van al auto y son asesino
                        print(" \n -Frank: okey...jack debe estar en los pasillos de arriba, vamos\n\n*vas caminando y ves pisadas de sangre y ruidos extraños.*\n\n-Frank: hey no te preocupes, este lugar es viejo...\n Este es el lugar... (tok tok)...parece que no es aca.\n-alguien:eh? quien me molesta para tener que arrancarles los ojos")
                        print("-Frank: tal vez si es el jajaj... hey jack, que tal?")
                        print("-jack: vienes con acompañantes? joder... bueno da igual\n-Frank: no te enojes... deja abro esta puerta")
                        print()
                        print("*bajan con jack y van al auto*")
                        nu = input("\n-jack: y tu como te llamas?: ")
                        os.system("clear")
                        print(f" \n-Jack: Buenas {nu} un gusto conocerte...\n Oye frank trajiste mis juguetes?\n-Frank: jajaja, las que mas usas...Que haremos?\n-jack: Cazar...{nu} has cazado algunas vez?  ")
                        input("\n-Dile si o no y preguntale que caza el. \n Respuesta: ")
                        os.system("clear")
                        print("\n-Jack: ah vale... jajaja.... cazo h-u-m-a-n-o-s\n y hoy lo haremos de nuevo ajajjaja\n")
                        des = int(input(" *Jack y Frank son asesinos.* \n ¿Que haras?\n 1)hacer que choquen\n 2)bajarte del auto en movimiento\n \nResponde: "))
                        os.system("clear")
                        if des == 1:
                            print(" \n*tomas el volante y lo giras todo a la derecha*")
                            print()
                            print("-jack: y esta mierda que hace????")
                            print()
                            print("*chocan y frank y jack salen disparados por no usar cinturon*\n\n '*Quedas mal herido, pero eres libre y te salvas de estas 2 personas.*")
                            print("\nFINAL BUENO, has sobrevivido.")
                            n1 = int(input("\n Fin de uno de los finales\n ¿volver a jugar?\n 1)si\n 2)no\n \nRespuesta: "))
                            if n1 == 1:
                                os.system("clear")
                                os.system("python3 7velas.py")
                            else:
                                os.system("clear")
                                print("\nGracias por jugar mi juego :D")
                                exit
                        if des == 2:
                            print(f"-Frank: {nu} te noto algo nervios@...\n\n *abres el pestillo y saltas a un monton de pasto seco*\n *que habia en el camino.* ")
                            print("-jack: Que intentas hacer? te asustas y quieres delatarnos?")
                            print()
                            print("'Frank saca una pistola y te dispara en las piernas.")
                            print()
                            print("¿Que haras?")
                            a = int(input(" 1)Pelear por tu vida\n 2)Aceptas tu destino"))
                            if a == 1:
                                print(" Final terrible.\n\n *Te disparan nuevamente y te dejan morir desangrado.*")
                                n1 = int(input("\n Finanl terrible. \n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    print("\nGracias por utilizarme :D")
                                    exit
                            if a == 2:
                                print(" Final cruel.\n\n *Jack te amarra las manos y te meten al auto.*\n estas perdido! te han secuestrado.")
                                n1 = int(input("\n Fin de uno de los finales.\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\nGracias por utilizarme :D")
                                    exit



                    
                    
                    
                    
                    if elije == 2: # debes esperarlos
                        print("\n-Frank: Bueno... como quieras, yo no tardo.")
                        print("-PASA 1 HORA DESDE QUE FRANK SE FUE A BUSCAR A JACK")
                        ase = int(input(" \n Ha pasado mucho tiempo, le habra pasado algo?\n ¿Que haras? \n 1)Investigar \n 2)Volver al auto\n Responde: "))
                        os.system("clear")
                        if ase ==1:
                            print("\n *Te decides ir a buscarlos y subes a los pasillos* ")
                            print()
                            print("-15 minutos te pasas buscando-\n -pero no encuentras nada.-")
                            q = int(input(" 1)bajas al sotano\n 2)sigues buscando por los pasillos \n Respuesta: "))
                            if q ==1:
                                os.system("clear")
                                print()
                                print(" *Bajas las escaleras...pero haces mucho ruido*")
                                print(" *viene alguien bajando*")
                                qe = int(input("¿Que haces? \n 1)Te metes a un habitacion rapido\n 2)bajas rapido las escaleras hacia la salida. \n responde: "))
                                os.system("clear")
                                if qe == 1:
                                    print("*te metes dentro de una habitacion*\n-¿no te fijaste quien estaba adentro?-")
                                    print(" \n*Otro preso te golpea y te encierra, el escapa*")
                                    n1 = int(input("\n Final trajico. Dejaste escapar a un psicopata.\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                    if n1 == 1:
                                        os.system("clear")
                                        os.system("python3 7velas.py")
                                    else:
                                        os.system("clear")
                                        print("\n Gracias por jugar :D")
                                        exit
                                if qe  == 2:
                                    print("*bajas rapido hacia la salida*")
                                    print(" *afuera te recibe la policia y ves*\n *que tomaron preso a frank.*\n te has salvado. EL ERA UN ASESINO")
                                    n1 = int(input("\n Final bueno, te has salvado,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                    if n1 == 1:
                                        os.system("clear")
                                        os.system("python3 7velas.py")
                                    else:
                                        os.system("clear")
                                        print("\n Gracias por jugar :D")
                                        exit


                        if ase ==2:
                            print("*bajas las escaleras y sales*\n*te subes al auto y llegan 2 policias a tu ventana*")
                            print("*te toman como sospechoso de la presunta*\n*ayuda que le diste al asesino frank*")
                            print("FRANK ERA UN ASESINO!\n tu no hiciste nada malo, no lo sabias...")
                            n1 = int(input("\n Final injusto, te han arrestado injustamente,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                            if n1 == 1:
                                os.system("clear")
                                os.system("python3 7velas.py")
                            else:
                                os.system("clear")
                                print("\n Gracias por jugar :D")
                                exit
                            
 








                if siono == 2: #mini desenlase 2 no ayudas
                    print("""
-Frank: okey, esta bien...

"*te golpea con la misma 
roca y quedas inconciente.*"

-pasan 45 minutos-

-Frank: hey, que tal va la siesta?
 disculpame si te he golpeado muy fuerte.
 ¿Por que te negaste? digo... pense que
 eramos amigos. por cierto, el es jack.
 (jack trae un cuchillo en la mano)

 -Jack: he, no te preocupes, solo ayudame
 debajo de este lugar hay mucho dinero.
 Al parecer ganan dinero fabricando animales
 superdotados... que raro.
                    """)
                    inco = int(input("\n Te estan ofreciendo robar, ¿que haces? \n 1)negarme a robar \n 2)pedir perdon y aceptar \n respuesta: "))
                    os.system("clear")
                    if inco == 1:
                        print(" -Jack: Que mala desicion... pense que esta mierda era más inteligente.\n\n -Frank: Lo siento, pero las reglas mandan.")
                        print(" -Jack saca un arma y te dispara.- HAS MUERTO.")
                        n1 = int(input("\n Final inesperado, no puedes negarte contra un asesino,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                        if n1 == 1:
                            os.system("clear")
                            os.system("python3 7velas.py")
                        else:
                            os.system("clear")
                            print("\n Gracias por jugar :D")
                            exit

                    if inco == 2:
                        print("\n *les pides perdón*")
                        print()
                        print(" -Frank: no te preocupes, un error lo comete cualquiera. \n Ahora esperemos que nos ayudes.")
                        print("\n -Frank y Jack se distraen un momento buscando algo")
                        wa = int(input("\n Tienes una oportunidad, ¿que haces? \n 1)Quedarte donde mismo \n 2)Escapar de la habitacion \n responde: "))
                        os.system("clear")
                        if wa == 1:
                            print("\n -Jack: te negaste una vez, el perdon no bastara\n *jack saca una pistola y dispara*, HAS MUERTO")
                            n1 = int(input("\n Final inesperado, no funciono tu perdón.\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                            if n1 == 1:
                                os.system("clear")
                                os.system("python3 7velas.py")
                            else:
                                os.system("clear")
                                print("\n Gracias por jugar :D")
                                exit
                        if wa == 2:
                            print("\n -es hora de escapar-\n *la puerta estaba algo abierta y puedes escapar.*\n *corres con todas tus fuerzas pero son rapidos*-\n -hay una habitacion al frente-\n")
                            hk = int(input(" ¿Que haces? \n 1)Bajar por la escalera rapidamente\n 2)Meterme en la habitacion \n Responde: "))
                            os.system("clear")
                            if hk == 1:
                                print(" *bajas las escaleras muy rapido, pero te tropesaste.*\n *tu cabeza choco con el piso, ya sabes tu final.* \n\n HAS PERDIDO!")
                                n1 = int(input("\n Final triste, casi ganas...,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit
                            if hk == 2:
                                print("\n -Estas a salvo pero no por mucho tiempo-\n -Hay una ventilacion... y tambien una pistola.")
                                rk = int(input(" ¿Que elijes? \n 1)Tomo la pistola y me enfrento \n 2)Me meto al conducto sin saber a que lleva \n Responde: "))
                                os.system("clear")
                                if rk == 1:
                                    print("\n *te armaste de valor y tomaste la pistola* \n *abres la puerta mientras apuntas y apretas el gatillo*\n *Jack te noquea con la culata de su arma*\n\n HAS PERDIDO!,tu arma no tenia balas.")
                                    n1 = int(input("\n Final penoso, tan solo tuviese balas...,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                    if n1 == 1:
                                        os.system("clear")
                                        os.system("python3 7velas.py")
                                    else:
                                        os.system("clear")
                                        print("\n Gracias por jugar :D")
                                        exit

                                if rk == 2:
                                    print("\n *Abres las rejilla y te metes a tiempo, justo habian abierto la puerta.*\n *Sientes la adrenalina al caer...y caes sobre un monton de carton*")
                                    print(" -Estas en la sala de suministros de gasolina, ademas en la misma- \n -Habitacion hay como un tigre negro...parece ser un experimento.")
                                    print(" -se vienen un monton de ideas, el tiempo corre-\n -y ellos estan llegando donde estas tu.-")
                                    lol = int(input("\n ¿Que haras? \n 1)llenar todo de gasolina y prenderla, y escapar. \n 2)Liberas al animal ahora y esperas que lleguen frank y jack \n 3) que entre jack y frank a la habitacion y liberar al animal. \n Responde: "))
                                    os.system("clear")
                                    if lol == 1:
                                        print("\n *Te apuras, tomas el botellon de keroseno y lo exparses por la habitación*")
                                        print(" *prendes y tiras el mechero, y corres a la salida*")
                                        print(" *mala tuya que te empapaste los zapatos y el fuego prendio*")
                                        print(" *Todos mueren en su infierno, literal*")
                                        print()
                                        print("HAS PERDIDO!")
                                        n1 = int(input("\n Final ardiente,si supieses que eso prende altiro...,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                        if n1 == 1:
                                            os.system("clear")
                                            os.system("python3 7velas.py")
                                        else:
                                            os.system("clear")
                                            print("\n Gracias por jugar :D")
                                            exit

                                    if lol == 2:
                                        print("\n *Tu decision es liberar al animal ahora*")
                                        print(" [lo liberas de su jaula]")
                                        print("-Frank y jack estan lejos para que el animal ataque")
                                        print(" *El animal te ataca y es tu final*")
                                        print()
                                        print("HAS MUERTO")
                                        n1 = int(input("\n Final salvaje, el animal tenia hambre...,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                        if n1 == 1:
                                            os.system("clear")
                                            os.system("python3 7velas.py")
                                        else:
                                            os.system("clear")
                                            print("\n Gracias por jugar :D")
                                            exit

                                    if lol == 3:
                                        print("\n-Escuchas bajar a frank y jack-")
                                        print(" *tocan a la puerta (tok tok)*")
                                        print()
                                        print("-es hora de liberar a la bestia-")
                                        print("-el rostro de tus perseguidores lo dice todo-")
                                        print("-aprovechas y corres hacia la salida-\n-tomas el auto y escapas de ahi-")
                                        print()
                                        print(" HAS SALVADO TU VIDA")
                                        n1 = int(input("\n Final de suerte, por los pelos...,\n ¿volver a jugar?\n 1)si\n 2)no\n Respuesta: "))
                                        if n1 == 1:
                                            os.system("clear")
                                            os.system("python3 7velas.py")
                                        else:
                                            os.system("clear")
                                            print("\n Gracias por jugar :D")
                                            exit


                                    

                                


        


            if ele == 2: #2desenlace #dormir
                print("\n -Frank: Okey,quedate dormido si quieres....no me tardo")
                print()
                print(" -Han pasado 2 horas, son las 1 AM-\n\n ¿Por que Frank no ha llegado?\n\n -¿Que piensas hacer?")
                oop = int(input(" 1)Seguir esperando hasta que lleguen \n 2)Investigar dentro del hospital \n [Responde: "))
                os.system("clear")
                if oop == 1:
                    print("\n -Ha pasado 1 hora, ya son las 2 AM-\n -Empezo a hacer mucho frio y suenan sirenas-\n\n ¿Que haras?")
                    lele = int(input(" 1)Prendes el motor y te vas a casa \n 2)Te quedas dormido hasta que lleguen \n [Responde: "))
                    os.system("clear")
                    if lele == 1:
                        print("\n -El sueño y el frio te ha ganado-\n -Decides prender el auto e irte-\n -sin saberlo, te has salvado...HAS GANADO!")
                        n1 = int(input("\n Final de curioso...\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                        if n1 == 1:
                            os.system("clear")
                            os.system("python3 7velas.py")
                        else:
                            os.system("clear")
                            print("\n Gracias por jugar :D")
                            exit

                    if lele == 2:
                        print("\n -El sueño te ha ganado y te duermes-")
                        print(" -Lo que no sabes es que estas en un lugar del crimen- ")
                        print(" *Te despiertan las sirenas de los autos*")
                        print()
                        print(" -La policia te toma como sospechoso de ayudar a un asesino-\n -te suben a un carro donde esta frank y jack- te han engañado.\n HAS PERDIDO")
                        n1 = int(input("\n Final engañoso...\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                        if n1 == 1:
                            os.system("clear")
                            os.system("python3 7velas.py")
                        else:
                            os.system("clear")
                            print("\n Gracias por jugar :D")
                            exit
                        
                if oop == 2:
                    print("\n -Decides meterte al hospital y buscar a Frank-\n *entras sigilosamente y ves 2 escaleras* \n -Una de las escaleras va al subterraneo y otra a los pasillos- \n\n ¿Donde buscaras a Frank?")
                    dom = int(input("\n 1)Subir a los pasillos\n 2)Bajar al subterraneo \n [Respuesta: "))
                    os.system("clear")
                    if dom == 1:
                        print("\n -Te armas de valor y subes las escaleras hacia los pasillos- \n -Esta todo muy oscuro y ves muy poco-\n -Por suerte traes una linterna contigo- \n ¿Prendes la linterna si o no?")
                        luz = int(input("\n 1)Si \n 2)No \n Responde: "))
                        os.system("clear")
                        if luz == 1:
                            print("\n -Prendes la linterna y ahora si puedes visualizar tu camino- \n -Sientes la incomodidad de que te observan- \n\n -Mala tuya! aparece un enfermo de la mente con una palanca-\n -te metes al baño más cercano, el esta afuera golpeando-")
                            print("\n -hay una reja donde te lleva al patio del hospital-\n -pero tambien el techo tiene un un escape hacia el techo del hospital-\n -el loco esta afuera, ¿Que haras?-")
                            desi = int(input("\n 1)Subir al techo \n 2)Ir al patio del hospital \n [Responde: "))
                            os.system("clear")
                            if desi == 1:
                                print("\n -Decides subir al techo y te metes por el escape- \n - el loco rompio la puerta e intenta subir a donde estas tu- \n\n ¿Que haces?")
                                des = int(input("\n 1)Tomar un fierro y pelear contra el loco\n 2)Saltar desde el techo al lago de abajo \n [Respuesta: "))
                                os.system("clear")
                                if des == 1:
                                    print("\n -Tomas el fierro dispuesto a proteger tu vida- \n -el loco aparece y se abalanza hacia ti- \n -el miedo te consume y no reaccionas\n -eres victima del loco del hospital-")
                                    print()
                                    print(" HAS MUERTO ")
                                    n1 = int(input("\n Final de paralisis...el miedo no te dejo actuar\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                    if n1 == 1:
                                        os.system("clear")
                                        os.system("python3 7velas.py")
                                    else:
                                        os.system("clear")
                                        print("\n Gracias por jugar :D")
                                        exit
                
                                if des == 2:
                                    print("\n -El miedo es grande, pero el loco esta cerca tuyo- \n -te fijas que al lado del hospital hay un inmenso lago- \n -esta puede ser tu oportunidad de escape- ")
                                    print()
                                    print(" -Tienes el valor de saltar?- \n ¿Saltas al lago?")
                                    lago = int(input("\n 1)si \n 2)no \n [Responde: "))
                                    os.system("clear")
                                    if lago == 1:
                                        print("\n -Es demasiada imponente la altura, pero son solo 15 metros- \n -te armas de valor y saltas de la mejor forma posible-\n")
                                        print(" -Chocas con el agua y sientes un dolor tremendo- \n -la adrenalina te hace correr al auto- \n -prendes el motor y escapas- ")
                                        print()
                                        print(" Has sobrevivido")
                                        n1 = int(input("\n -Final de valientes...fuiste valiente al saltar\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                        if n1 == 1:
                                            os.system("clear")
                                            os.system("python3 7velas.py")
                                        else:
                                            os.system("clear")
                                            print("\n Gracias por jugar :D")
                                            exit
                                    if lago == 2:
                                        print("\n -el miedo no te deja saltar- \n -el loco esta ahora en el techo... \n -Es tu final.")
                                        print()
                                        print(" HAS MUERTO")
                                        n1 = int(input("\n -Final cobarde...fuiste cobarde\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                        if n1 == 1:
                                            os.system("clear")
                                            os.system("python3 7velas.py")
                                        else:
                                            os.system("clear")
                                            print("\n Gracias por jugar :D")
                                            exit

                            if desi == 2:
                                print("\n -Te decides finalmente y por la rejilla bajas al patio- \n -esta oscuro y muy tenebroso-\n -has escapado del loco, pero el patio es hogar-\n -de una manada de lobos experimentados-\n\n -Mala eleccion, los lobos te devoran.")
                                print()
                                print( " HAS MUERTO")
                                n1 = int(input("\n -Final sangriento...no eres parte de la manada\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit
                        


                        if luz == 2:
                            print("\n -Decides no prender la linterna para no alertar a nadie- \n -vas caminando y suena algo extraño, corres.- \n -el piso estaba mojado, te tropiesas y caes al vacio.-")
                            print()
                            print(" HAS FALLECIDO")
                            n1 = int(input("\n -Final de lastima...¿Por que no prender la linterna?\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                            if n1 == 1:
                                os.system("clear")
                                os.system("python3 7velas.py")
                            else:
                                os.system("clear")
                                print("\n Gracias por jugar :D")
                                exit



                    if dom == 2:
                        print("\n -prefieres bajar al subterraneo-\n -a pesar de que da miedo, eres valiente-\n\n -te detienes un momento por que escuchas sonidos raros- \n -te da curiosidad esos sonidos y miras un poco- \n\n -Frank y Jack devoran lo que parece ser un humano.- ")
                        print()
                        print(" ¿Que haras?")
                        kan = int(input(" 1)Correr del hospital y escapar \n 2)enfrentarlos \n [Responde: "))
                        os.system("clear")
                        if kan == 1:
                            print("\n -Piensas en dejarlos, el miedo te hace corres- \n -Mala suerte, te tropiezas sin querer- \n -Frank abre la puerta y te mira enojado- \n -no te puedes mover por el impacto del momento-")
                            print(" -Frank: No pense que nos miraras asi\n esto debia ser una sorpresa jajaja... \n igual tenemos espacio para ti")
                            print()
                            print(" -Frank te ofrece a comer con ellos, que horrible piensas...")
                            car = int(input("\n ¿Que haras? \n 1)Aceptar \n 2)negarse \n [Responde: "))
                            os.system("clear")
                            if car == 1:
                                print("\n -Por el miedo, aceptas la propuesta- \n\n -Jack: jajaja, tu eres la personita que invito Frank...\n -Frank: Sientate. \n -Tu rostro lo dice absolutamente todo-")
                                print()
                                print(" -de una patada abren la puerta y los apuntan- \n -tu gritas y dices que te secuestraron- \n -te arrestan pero te has salvado-")
                                print()
                                print(" HAS SOBREVIVIDO")
                                n1 = int(input("\n -Final de suerte...la policia te salvo\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit
                            
                            if car == 2:
                                print("\n -Frank: da igual...no te quedaras con esto \n -su mirada te lo dice todo\n\n -Saca una navaja y se abalanza hacia ti-")
                                print()
                                print(" HAS MUERTO")
                                n1 = int(input("\n -Final penoso...estuvo bien negarte, pero tiene consecuencias.\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit

                        if kan == 2:
                            print(" \n -tu desicion es enfrentarles-\n -la pieza de al lado es un closet- \n -hay una pistola y una pala-\n\n -Es hora de acabar a estos asesinos.-")
                            arm = int(input("\n ¿Que elejiras? \n 1)Pistola \n 2)Pala \n [Responde: "))
                            os.system("clear")
                            if arm == 1:
                                print(" -Tomas el arma, y te dispones abrir la puerta- \n *Abres la puerta y los tomas por sorpresas* \n -Jack: pero que mierda? ")
                                input(" -Dile unas ultimas palabras: ")
                                print(" -te armas de valor y aprietas el gatillo-")
                                print("   ...  ")
                                print("   ...  ")
                                print(" -La pistola se ha trabado, el peor dia de tu vida.-\n *Jack se abalanza contra ti*")
                                print()
                                print(" HAS MUERTO")
                                n1 = int(input("\n -Final traicionero...el arma te ha traicionado\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit
                            
                            if arm == 2:
                                print("\n -Tomas la pala, confiaste en tu fuerza mental y fisica- \n -tocas la puerta y sin chance de dejarles hablar los golpeas- \n -Escuchas la agonia de estas lacras- \n\n [manchado de sangre escapas de ese horrible lugar] ")
                                print()
                                print(" HAS SOBREVIVIDO")
                                n1 = int(input("\n -Final justo...repartiste justicia.\n ¿volver a jugar?\n 1)si\n 2)no\n [Respuesta: "))
                                if n1 == 1:
                                    os.system("clear")
                                    os.system("python3 7velas.py")
                                else:
                                    os.system("clear")
                                    print("\n Gracias por jugar :D")
                                    exit




                                                  











    if eleccion == 2: #opcion2 ir a su casa
        print("pendiente")

    if eleccion == 3: #opcion3 de no acompañarlo
        print("pendiente")    
"""
   if muerte == 0:
        exit
        os.system("clear")
        print(" Has muerto\n")
        n1 = int(input("\n ¿Quieres volver a intentarlo?\n 1)si\n 2)no\n Respuesta: "))
        if n1 == 1:
            os.system("clear")
            os.system("python3 wea.py")
        else:
            print("\nGracias por utilizarme :D")
            exit
"""
def Salir():
    print()
    print("Muchas gracias por jugar :D")
    exit

banner()
try:
    op = int(input(f" {name},¿Que personaje elegiras?: "))
    os.system("clear")
except ValueError:
    print("\nerror, no has seleccionado una opcion")  

if op == 1:
	frank()

#if op == 1:
#	kiara()
