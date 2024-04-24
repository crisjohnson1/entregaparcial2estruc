class ClothingItem:
    def __init__(self, name, code, value):
        self.name = name
        self.code = code
        self.value = value

class BSTNode:
    def __init__(self, clothing_item=None):
        self.left = None
        self.right = None
        self.clothing_item = clothing_item

    def insert(self, clothing_item):
        if not self.clothing_item:
            self.clothing_item = clothing_item
            return

        if clothing_item.code == self.clothing_item.code:
            
            self.clothing_item = clothing_item
            return

        if clothing_item.code < self.clothing_item.code:
            if self.left:
                self.left.insert(clothing_item)
            else:
                self.left = BSTNode(clothing_item)
        else:
            if self.right:
                self.right.insert(clothing_item)
            else:
                self.right = BSTNode(clothing_item)

    def get_min(self):
        current = self
        while current.left:
            current = current.left
        return current.clothing_item

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.clothing_item

    def delete(self, code):
        if not self.clothing_item:
            return None

        if code < self.clothing_item.code:
            if self.left:
                self.left = self.left.delete(code)
        elif code > self.clothing_item.code:
            if self.right:
                self.right = self.right.delete(code)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

          
            min_right_node = self.right.get_min()

           
            self.clothing_item = min_right_node

           
            self.right = self.right.delete(min_right_node.code)

        return self

    def exists(self, code):
        if code == self.clothing_item.code:
            return True
        elif code < self.clothing_item.code:
            if self.left:
                return self.left.exists(code)
            else:
                return False
        else:
            if self.right:
                return self.right.exists(code)
            else:
                return False

    def preorder(self, items):
        if self.clothing_item:
            items.append(self.clothing_item)
        if self.left:
            self.left.preorder(items)
        if self.right:
            self.right.preorder(items)
        return items

    def inorder(self, items):
        if self.left:
            self.left.inorder(items)
        if self.clothing_item:
            items.append(self.clothing_item)
        if self.right:
            self.right.inorder(items)
        return items

    def postorder(self, items):
        if self.left:
            self.left.postorder(items)
        if self.right:
            self.right.postorder(items)
        if self.clothing_item:
            items.append(self.clothing_item)
        return items

# espacio para ingresar, buscar, eliminar ropa y recorrer

root = BSTNode()

# Insertar elementos
root.insert(ClothingItem("Camiseta", 1001, 20))
root.insert(ClothingItem("Pantalón", 1002, 30))
root.insert(ClothingItem("Chaqueta", 1003, 50))
root.insert(ClothingItem("Falda", 1004, 25))

# Búsqueda
print(root.exists(1002))  # True
print(root.exists(1005))  # False

# Eliminar ropa del inventario
root.delete(1003)

# Recorrer el árbol
print("Inorder traversal:", [item.code for item in root.inorder([])])  # Imprimir los códigos en orden
