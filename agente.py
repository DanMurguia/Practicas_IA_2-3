import Nodo
 
humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5} #definicion humano
pulpo = {0: False, 1: 2, 2: 1, 3: False, 4: 3, 5: 2, 6: False} #definicion humano
mono = {0: False, 1: 2, 2: 4, 3: 3, 4: 1, 5: 5, 6: False}
chupacabras = {0: 15, 1: 4, 2: False, 3: False, 4: 4, 5: 5, 6: 3}
ente={}
root = None
nodo_aux = None 
contador = 0




'''for x in range(0, fil):
    print()
    for y in range(0, col):
        print(str(x),str(y), paramsd[(x, y)])
'''
def definirAgente(agente):
    if agente==1:
        ente=humano
    elif agente==2:
        ente=pulpo
    elif agente==3:
        ente = mono
    elif agente==4:
        ente =chupacabras
    elif agente<1 and agente>4:
        print("ente no definido")
    return ente

def spawn(paramsd,matriz, ente):
    col= matriz.shape[0]
    fil = matriz.shape[1]
    for i in range(0, fil):
        for j in range(0, col):
            if(paramsd[(i,j)]['I']):
                if (ente[matriz[i][j]]):#generalizar
                    paramsd[(i,j)]['S'] = True
                    paramsd[(i,j)]['X'] = True
                    paramsd[(i,j)]['n'] = True
                    root = Nodo.Nodo((i,j))
                else:
                    paramsd[(i,j)]['I'] = False
                    paramsd[(i,j)]['S'] = False
                    paramsd[(i,j)]['X'] = False
                    paramsd[(i-1,j)]['I'] = True
                    paramsd[(i-1,j)]['S'] = True
                    paramsd[(i-1,j)]['X'] = True
                    paramsd[(i,j)]['n'] = True
                    root = Nodo.Nodo((i-1,j))

            if (paramsd[(i, j)]['F']):
                if (ente[matriz[i][j]]):

                    paramsd[(i, j)]['S'] = True
                else:
                    paramsd[(i, j)]['F'] = False
                    paramsd[(i, j)]['S'] = False
                    paramsd[(i - 1, j)]['F'] = True
                    paramsd[(i - 1, j)]['S'] = True
    return root



def sense(paramsd, matriz, ente):
    col= matriz.shape[0]
    fil = matriz.shape[1]
    aux=0;
    caminos_bloqueados = 0 
    for i in range(0, fil):
        for j in range(0, col):
            if (paramsd[(i, j)]['X']):
                paramsd[(i, j)]['S'] = True

                if(i>0):
                    paramsd[(i-1, j)]['S']= True
                    if (ente[matriz[i -1][j]]and not paramsd[(i-1, j)]['V']):
                        aux = aux + 1
                    if not ente[matriz[i-1][j]] or paramsd[(i-1, j)]['V']:
                        caminos_bloqueados += 1    
                else: 
                    caminos_bloqueados += 1

                if(i<fil-1):
                    paramsd[(i+1,j)]['S'] = True
                    if (ente[matriz[i+1][j]]and not paramsd[(i+1, j)]['V']):
                        aux = aux + 1
                    if not ente[matriz[i+1][j]] or paramsd[(i+1, j)]['V']:
                        caminos_bloqueados += 1
                else:
                    caminos_bloqueados += 1

                if (j>0):
                    paramsd[(i, j-1)]['S']= True
                    if (ente[matriz[i][j -1]] and not paramsd[(i, j-1)]['V']):
                        aux = aux + 1
                    if not ente[matriz[i][j-1]] or paramsd[(i, j-1)]['V']:
                        caminos_bloqueados += 1
                else:
                    caminos_bloqueados += 1

                if (j < col-1):
                    paramsd[(i, j+1)]['S'] = True
                    if (ente[matriz[i][j+1]]and not paramsd[(i, j+1)]['V']):
                        aux = aux+1
                    if not ente[matriz[i][j+1]] or paramsd[(i, j+1)]['V']:
                        caminos_bloqueados += 1
                else:
                    caminos_bloqueados += 1

                if aux>1:
                    paramsd[(i, j )]['O'] = True
                    
                elif caminos_bloqueados > 3:
                    paramsd[(i, j )]['k'] = True





def step(paramsd, matriz, ente, nodo_act):
    aux = 0
    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:


                    if not paramsd[(i, j)]['F']:
                    
                        if paramsd[(i, j)]['X'] and paramsd[(i, j)]['V']:
                            if  paramsd[(i, j)]['k']:
                                if not paramsd[(i, j)]['n']:
                                    nuevo_nodo = Nodo.Nodo((i,j))
                                    nodo_act.agregar_hijo(nuevo_nodo)
                                    coordenadas = nuevo_nodo.padre.data
                                    paramsd[(i,j)]['n'] = True
                                    print(coordenadas)
                                    paramsd[(i,j)]['X'] = False
                                    paramsd[coordenadas]['X'] = True
                                    return False, nodo_act
                                else:
                                    coordenadas = nodo_act.padre.data
                                    print(coordenadas)
                                    paramsd[(i,j)]['X'] = False
                                    paramsd[coordenadas]['X'] = True
                                    return False, nodo_act.padre
                                                                    
                                


                        paramsd[(i, j)]['V'] = True

                        if i-1 >= 0 and ente[matriz[i-1][j]] and not paramsd[(i-1, j)]['V']:
                            paramsd[(i, j)]['X']=False
                            paramsd[(i-1, j)]['X']=True
                            costo=ente[matriz[i-1][j]]
                            if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                nuevo_nodo = Nodo.Nodo((i,j))
                                nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                nodo_act = nuevo_nodo
                            return costo, nodo_act

                        if j -1 >= 0 and ente[matriz[i][j-1]] and not paramsd[(i, j-1)]['V']:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j - 1)]['X'] = True
                            costo=ente[matriz[i][j-1]]
                            if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                nuevo_nodo = Nodo.Nodo((i,j))
                                nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                nodo_act = nuevo_nodo
                            return costo, nodo_act
                        
                        if i+1 < fil and ente[matriz[i+1][j]] and not paramsd[(i+1, j)]['V'] :
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i +1, j)]['X'] = True
                            costo=ente[matriz[i+1][j]]
                            if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']:
                                nuevo_nodo = Nodo.Nodo((i,j))
                                nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                nodo_act = nuevo_nodo
                            return costo, nodo_act
                        
                        if j+1 < col and ente[matriz[i][j+1]] and not paramsd[(i, j+1)]['V']:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j+1)]['X'] = True
                            costo=ente[matriz[i][j+1]]
                            if paramsd[(i,j)]['O'] and not paramsd[(i,j)]['n']: 
                                nuevo_nodo = Nodo.Nodo((i,j))
                                nodo_act.agregar_hijo(nuevo_nodo)
                                paramsd[(i,j)]['n'] = True
                                nodo_act = nuevo_nodo
                            return costo, nodo_act
                        return False, nodo_act
                    else:
                        if not paramsd[(i, j)]['n']:
                            nuevo_nodo = Nodo.Nodo((i,j))
                            nodo_act.agregar_hijo(nuevo_nodo)
                            paramsd[(i,j)]['n'] = True
                            return False, nodo_act
                        else:
                            return False, nodo_act
                    



def step_down(paramsd, matriz, ente):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:



                    if not paramsd[(i, j)]['F']:
                        paramsd[(i, j)]['V'] = True

                        if i+1 < fil and ente[matriz[i+1][j]]:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i +1, j)]['X'] = True

                            costo = ente[matriz[i+1][j]]
                            return costo

def step_up(paramsd, matriz, ente):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:



                    if not paramsd[(i, j)]['F']:
                        paramsd[(i, j)]['V'] = True

                        if i-1 >= 0 and ente[matriz[i-1][j]]:
                            paramsd[(i, j)]['X']=False
                            paramsd[(i-1, j)]['X']=True

                            costo = ente[matriz[i-1][j]]
                            return costo

def step_right(paramsd, matriz, ente):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:



                    if not paramsd[(i, j)]['F']:
                        paramsd[(i, j)]['V'] = True

                        if j+1 < col and ente[matriz[i][j+1]]:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j+1)]['X'] = True

                            costo = ente[matriz[i][j+1]]
                            return costo

def step_left(paramsd, matriz, ente):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:



                    if not paramsd[(i, j)]['F']:
                        paramsd[(i, j)]['V'] = True

                        if j -1 >= 0 and ente[matriz[i][j-1]]:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j - 1)]['X'] = True

                            costo = ente[matriz[i][j-1]]

                            return costo