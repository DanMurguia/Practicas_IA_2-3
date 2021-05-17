import Nodo

def Crear_Nodo(x,y,nodoActual,O):
	nodo=Nodo.TreeNode((x,y))
	nodoActual.add_child(nodo)
	if O == 1:
		return nodo
	elif O == 2:
		return nodoActual
	elif O == 3:
		return nodoActual.parent
