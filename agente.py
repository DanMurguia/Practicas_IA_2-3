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
    for i in range(0, fil):
        for j in range(0, col):
            if (paramsd[(i, j)]['X']):

                paramsd[(i, j)]['S'] = True

                if(i>0):
                    paramsd[(i-1, j)]['S']= True
                    if (ente[matriz[i -1][j]]and not paramsd[(i-1, j)]['V']):
                        aux = aux + 1

                if(i<fil-1):
                    paramsd[(i+1,j)]['S'] = True
                    if (ente[matriz[i+1][j]]and not paramsd[(i+1, j)]['V']):
                        aux = aux + 1

                if (j>0):
                    paramsd[(i, j-1)]['S']= True
                    if (ente[matriz[i][j -1]] and not paramsd[(i, j-1)]['V']):
                        aux = aux + 1

                if (j < col-1):
                    paramsd[(i, j+1)]['S']= True
                    if (ente[matriz[i][j+1]]and not paramsd[(i, j+1)]['V']):
                        aux = aux+1

                if aux>1 and not paramsd[(i, j )]['F']:
                    paramsd[(i, j )]['O'] = True
                    
                else:
                    paramsd[(i, j )]['k'] = True



def step(paramsd, matriz, ente, nodo_act):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:
                    print(paramsd[(i, j)], i, j)



                    if not paramsd[(i, j)]['F']:

                        if paramsd[(i, j)]['X'] and paramsd[(i, j)]['V']:

                            for auxi in range(0, fil):
                                for auxj in range(0, col):
                                    if not paramsd[(auxi, auxj)]['k'] and paramsd[(auxi, auxj)]['O']:
                                        paramsd[(auxi, auxj)]['X'] = True
                                        paramsd[(i, j)]['X'] = False
                                        paramsd[(auxi, auxj)]['V'] = False
                                        return False

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
                            paramsd[(i, j - 1)]['O'] = True
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
                        

def step_down(paramsd, matriz, ente):

    col= matriz.shape[0]
    fil = matriz.shape[1]

    for i in range(0, fil):
        for j in range(0, col):

                if paramsd[(i, j)]['X']:
                    print(paramsd[(i, j)], i, j)



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
                    print(paramsd[(i, j)], i, j)



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
                    print(paramsd[(i, j)], i, j)



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
                    print(paramsd[(i, j)], i, j)



                    if not paramsd[(i, j)]['F']:
                        paramsd[(i, j)]['V'] = True

                        if j -1 >= 0 and ente[matriz[i][j-1]]:
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j - 1)]['X'] = True

                            costo = ente[matriz[i][j-1]]

                            return costo