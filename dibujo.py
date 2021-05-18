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

def dibujar(agente,modo,xx,yy):
    print("Agente"+str(agente))
    print("Modo"+str(modo))
    pygame.init()
    costo=0
    costoAcumulado=0

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


    for x in range(0, fil):
        for y in range(0, col):
            paramsd[(x, y)] = {'V': False, 'O': False, 'I': False, 'X': False,
                               'S':False, 'F':False, 'k':False, 'n':False}

    paramsd[(xx, yy)] = {'V': False, 'O': False, 'I': True, 'X': False,
                         'S':False,'F':False, 'k':False, 'n':False}
    paramsd[(6,8)] = {'V': False, 'O': False, 'I': False, 'X': False, 
                      'S':False,'F':True, 'k':False, 'n':False}

    ente=ag.definirAgente(agente)
    
        
    root = Nodo.Nodo("ARBOL")
    nodo_act = ag.spawn(paramsd, matriz, ente)
    root.agregar_hijo(nodo_act)
    
    while not gameOver:
            
        pantalla.fill(BLACK)  # La pantalla se llena de un fondo negro.
        # T es un contador para pintar las coordenadas
        T = 0
        #fila es la fila que se va a recorrer de la matriz :V 
        fila = 0
        ag.sense(paramsd,matriz, ente)
        # este for recorre el ancho de la pantalla
        for i in range(1, tamañoPantalla[0], 40):
            linea = matriz[fila] #se obtiene una fila de la matriz
            fila = fila+1
            if linea != '':
                columna = 0
                # este for recorre el alto de la pantalla
                for j in range(1, tamañoPantalla[1], 40):

                    lista_params = paramsd[(fila-1, columna)]

                    if lista_params['V'] or lista_params['S']:

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


                    columna = columna+1

                    ## Se obtiene la lista de parametros para esta coordenada
            
                    if(lista_params['V']):
                        V = Fuente.render('V', lista_params['V'], BLACK)
                        pantalla.blit(V, [j+3, i+26])
                    if(lista_params['O']):
                        O = Fuente.render('O', lista_params['O'], BLACK)
                        pantalla.blit(O, [j+12, i+26])
                    if(lista_params['I']):
                        I = Fuente.render('I', lista_params['I'], BLACK)
                        pantalla.blit(I, [j+15, i+15])
                    if(lista_params['X']):
                        X = Fuente.render('X', lista_params['X'], BLACK)
                        pantalla.blit(X, [j+30, i+26])
                    if (lista_params['F']):
                        X = Fuente.render('F', lista_params['F'], BLACK)
                        pantalla.blit(X, [j+15, i+15])
        
            # Texto es la imagen con la que se pintarán las coordenadas
            Texto = Fuente.render(str(T), True, BLACK)
            pantalla.blit(Texto, [i, 2])  # Coordenadas en el eje X
            if T != 0:
                pantalla.blit(Texto, [2, i])  # Coordenadas en el eje Y
            T += 1

        pygame.display.flip()

        if modo == 2:
            costo, nodo_act = ag.step(paramsd, matriz, ente, nodo_act)
            root.imprimir_arbol()
            costoAcumulado=costo+costoAcumulado
        elif modo == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("GameOver!")
                    gameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        costo, nodo_act=ag.step_up(paramsd, matriz, ente, nodo_act)
                        if(costo):
                            costoAcumulado=costo+costoAcumulado
                    elif event.key == pygame.K_a:
                        costo,nodo_act=ag.step_left(paramsd, matriz, ente, nodo_act)
                        if(costo):
                            costoAcumulado=costo+costoAcumulado
                    elif event.key == pygame.K_s:
                        costo,nodo_act=ag.step_down(paramsd, matriz, ente, nodo_act)
                        if(costo):
                            costoAcumulado=costo+costoAcumulado
                    elif event.key == pygame.K_d:
                        costo,nodo_act =ag.step_right(paramsd, matriz, ente, nodo_act)
                        if(costo):
                            costoAcumulado=costo+costoAcumulado
        
        
        reloj.tick(5)
    pygame.quit()
    print("Costo acumulado: "+str(costoAcumulado))
