import Nodo
import ArbolA

root = Nodo.TreeNode("ARBOL")
aux = Nodo.TreeNode((0,9))
root.add_child(aux)
aux = ArbolA.Crear_Nodo(1,10,aux,1)
aux = ArbolA.Crear_Nodo(2,10,aux,3)
aux = ArbolA.Crear_Nodo(1,11,aux,1)
root.print_tree()