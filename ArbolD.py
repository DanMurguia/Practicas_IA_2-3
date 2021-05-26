import Nodo
import ArbolA

root = Nodo.Nodo("ARBOL")
aux = Nodo.Nodo((0,9))
root.agregar_hijo(aux)
aux = ArbolA.Crear_Nodo(1,10,aux,1)
aux = ArbolA.Crear_Nodo(2,10,aux,3)
aux = ArbolA.Crear_Nodo(1,11,aux,1)
root.imprimir_arbol()
