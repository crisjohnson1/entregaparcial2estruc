
# Entrega Parcial 2 Estructura de Datos

Juan Pablo Aparicio Torres 2230048

Cristian Eduardo Johnson Acevedo 2155160

Jhoan Sebastian Rey Sánchez 2210060

Cristian Chávez  2182190

# Gestión de Inventario 

Los árboles de busqueda son fundamentales en este proyecto, ya que nos ayudan a buscar, insertar y eliminar elementos y así tener un mejor control sobre los productos que existen en el Inventario.

Este proyecto consiste en implementar un árbol de búsqueda binaria adaptado para almacenar un inventario de prendas de vestir. Cada nodo del árbol representa una prenda y está organizado de manera que las prendas se almacenan de manera ordenada según su código.

Inserción de prendas: Al insertar una nueva prenda, el algoritmo la coloca en el árbol de manera que se mantenga el orden ascendente de los códigos. Si la prenda ya existe en el árbol (según su código), se actualiza con la nueva información.


Búsqueda de prendas: se puede buscar una prenda en el árbol proporcionando su código. El algoritmo recorre el árbol de manera eficiente, comparando el código de la prenda buscada con los códigos de las prendas almacenadas en cada nodo, y retorna verdadero si la encuentra o falso si no.


Eliminación de prendas: Para eliminar una prenda del árbol, se busca el nodo que contiene la prenda a eliminar y luego se ajusta el árbol para mantener su estructura de búsqueda binaria. Si la prenda tiene hijos, se realiza una reorganización cuidadosa para preservar el orden del árbol.


Recorrido del árbol: Puedes recorrer el árbol en orden ascendente de códigos (inorder traversal) para obtener las prendas ordenadas por código. Esto te permite listar las prendas en orden, lo que puede ser útil para generar reportes o visualizar el inventario.
