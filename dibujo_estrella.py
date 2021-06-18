import pygame
import random
import genera_matriz as gm
import agente as ag
import time
import Nodo

BLACK = (0, 0, 0)
water = (0, 0, 255)
forest = (6, 71, 12)
redP = (230, 0, 20)
pinkP = (255, 77, 195)
mountains = (160, 160, 160)
aquaP = (90, 139, 185)
sand = (194, 178, 128)
pantano = (102, 0, 102)
nieve = (255, 255, 255)
land = (181, 101, 29)



# tamañoCasilla es el tamaño que tendrá cada lado de las casillas
tamañoCasilla = 40

# tamañoCuadricula es el numero de casillas que tendrá la cuadricula por lado
tamañoCuadricula = 15
columna = 0

'''def dibujar(agente,algoritmo,modo,xinicial,yinicial,xfinal,yfinal):
    if algoritmo == 3:
        dibujar_estrella(agente,xinicial,yinicial,xfinal,yfinal)'''

def dibujar(parametros_iniciales):
    agente=parametros_iniciales['ente']
    modo=parametros_iniciales['modo']
    j_inicial=parametros_iniciales['j_inicial']
    i_inicial=parametros_iniciales['i_inicial']
    j_final=parametros_iniciales['j_final']
    i_final=parametros_iniciales['i_final']
    i1=parametros_iniciales['i1']
    j1=parametros_iniciales['j1']
    i2=parametros_iniciales['i2']
    j2=parametros_iniciales['j2']

    print("Agente"+str(agente))
    print("Modo"+str(modo))
    pygame.init()
    costo=0
    costoAcumulado=0
    lista_obj=[]
    contf = 0

    # tamañoPantalla es el una tupla con los valores del tamaño de la pantalla
    tamañoPantalla = (tamañoCasilla*tamañoCuadricula,
                      tamañoCasilla*tamañoCuadricula)

    # pantall es la pantalla a desplegar
    pantalla = pygame.display.set_mode(tamañoPantalla)

    # se le da un titulo a la ventana a desplegar
    pygame.display.set_caption("Grid on PYGAME")

    # reloj es un timer que indica la velocidad de actualización de la pantalla
    reloj = pygame.time.Clock()

    # gameOver el el indicador de querer cerrar la pantalla
    gameOver = False

    # Fuente es un estilo de imagen inicializada dentro de pygame. Pygame solo muestra imagenes o dibujos, no texto.
    Fuente = pygame.font.SysFont('fontname', 16)
    matriz = gm.cargar_matriz('laberinto.txt')
    fil = matriz.shape[0]
    col = matriz.shape[1]
    paramsd = {}             #Se crea el diccionario de parametros


    for i in range(0, fil):
        for j in range(0, col):
            paramsd[(i, j)] = {'V': False, 'O': False, 'I': False, 'X': False,
                               'S':False, 'F':False, 'k':False, 'n':False, 'h':0,'Obj':False}

    paramsd[(i_inicial, j_inicial)] = {'V': False, 'O': False, 'I': True, 'X': False,
                         'S':False,'F':False, 'k':False, 'n':False,'h':0,'Obj':False}
    paramsd[(i_final, j_final)] = {'V': False, 'O': False, 'I': False, 'X': False, 
                      'S':False,'F':True, 'k':False, 'n':False,'h':0,'Obj':False}
    paramsd[(i1, j1)]['Obj'] = True
    paramsd[(i2, j2)]['Obj'] = True            
    lista_obj.append((i1,j1))
    lista_obj.append((i2,j2))    
    lista_obj.append((i_final,j_final))
    print(lista_obj)


    agente=ag.Agente(agente)
    
    agente.spawn(paramsd, matriz)
       
    while not gameOver:
            
        pantalla.fill(BLACK)  # La pantalla se llena de un fondo negro.
        # T es un contador para pintar las coordenadas
        T = 0
        #fila es la fila que se va a recorrer de la matriz :V 
        fila = 0

        agente.sense_estrella(paramsd,matriz,lista_obj[0][0],lista_obj[0][1])
        print(lista_obj[0])
        # este for recorre el ancho de la pantalla
        for i in range(1, tamañoPantalla[0], 40):
            linea = matriz[fila] #se obtiene una fila de la matriz
            fila = fila+1
            if linea != '':
                columna = 0
                # este for recorre el alto de la pantalla
                for j in range(1, tamañoPantalla[1], 40):

                    lista_params = paramsd[(fila-1, columna)]

                    if lista_params['V'] or lista_params['S'] or lista_params['Obj']:

                        if linea[columna] == 0:
                               # Los cuadros son ligeramente más pequeños para dar el efecto de la cuadricula.
                               pygame.draw.rect(pantalla, mountains, [j, i, 38, 38], 0)
                        elif linea[columna] == 1:
                                pygame.draw.rect(pantalla, land, [j, i, 38, 38], 0)
                        elif linea[columna] == 2:
                                pygame.draw.rect(pantalla, water, [j, i, 38, 38], 0)
                        elif linea[columna] == 3:
                                pygame.draw.rect(pantalla, sand, [j, i, 38, 38], 0)
                        elif linea[columna] == 4:
                                pygame.draw.rect(pantalla, forest, [j, i, 38, 38], 0)
                        elif linea[columna] == 5:
                                pygame.draw.rect(pantalla, pantano, [j, i, 38, 38], 0)
                        elif linea[columna] == 6:
                                pygame.draw.rect(pantalla, nieve, [j, i, 38, 38], 0)
                        elif linea[columna] == 7:
                                pygame.draw.rect(pantalla, aquaP, [j, i, 38, 38], 0)
                        elif linea[columna] == 8:
                                pygame.draw.rect(pantalla, redP, [j, i, 38, 38], 0)
                        elif linea[columna] == 9:
                                pygame.draw.rect(pantalla, pinkP, [j, i, 38, 38], 0)


                    else:
                        pygame.draw.rect(pantalla, BLACK, [j, i, 38, 38], 0)

                    ## Se obtiene la lista de parametros para esta coordenada
            
                    
                    if(lista_params['O']):
                        O = Fuente.render('O('+str(lista_params['h'])+')', lista_params['O'], BLACK)
                        pantalla.blit(O, [j+5, i+25])
                    if(lista_params['I']):
                        I = Fuente.render('I', lista_params['I'], BLACK)
                        pantalla.blit(I, [j+15, i+15])
                    if(lista_params['X']):
                        X = Fuente.render('X', lista_params['X'], BLACK)
                        pantalla.blit(X, [j+3, i+3])
                    if(lista_params['Obj']):
                        X = Fuente.render('Obj', lista_params['Obj'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if (lista_params['F']):
                        X = Fuente.render('F', lista_params['F'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
                    if lista_params['X'] and lista_params['F'] and contf == 2:
                        gameOver=True
                        print("Recorrido optimo!!!")
                        agente.recorrido_optimo()
                        print("Ha llegado a su objetivo!!!")
                        time.sleep(10)
                    elif lista_params['X'] and lista_params['F']:
                        contf += 1
                    if lista_params['X'] and lista_params['Obj']:
                        lista_obj.pop(0)
                        lista_params['Obj']=False
                        reiniciar(paramsd,fil,col)
                        agente.reiniciar_lista()
                        agente.sense_estrella(paramsd,matriz,lista_obj[0][0],lista_obj[0][1])
                    columna = columna+1


        
            # Texto es la imagen con la que se pintarán las coordenadas
            Texto = Fuente.render(str(T), True, BLACK)
            pantalla.blit(Texto, [i, 2])  # Coordenadas en el eje X
            if T != 0:
                pantalla.blit(Texto, [2, i])  # Coordenadas en el eje Y
            T += 1

        pygame.display.flip()

        agente.ordenar_nodos()
        agente.step_estrella(paramsd, lista_obj)
        #agente.root.imprimir_arbol()
        
        
        reloj.tick(100)
    pygame.quit()
    print("Costo acumulado: "+str(costoAcumulado))
def reiniciar(parametros, fil, col):
    for i in range(0, fil):
        for j in range(0, col):
            parametros[(i, j)]['V'] = False
            parametros[(i, j)]['O'] = False
            parametros[(i, j)]['k'] = False
            parametros[(i, j)]['n'] = False
            parametros[(i, j)]['h'] = False