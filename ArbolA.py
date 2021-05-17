import Nodo

def Crear_Nodo(x,y,nodoActual,O):
	nodo=Nodo.Nodo((x,y))
	nodoActual.agregar_hijo(nodo)
	if O == 1:
		return nodo
	elif O == 2:
		return nodoActual
	elif O == 3:
		return nodoActual.padre
