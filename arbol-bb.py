class ClothingItem:
    def __init__(self, name, code, value, quantity):
        self.name = name
        self.code = code
        self.value = value
        self.quantity = quantity
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
            print("Item found in inventory.")
            quantity = int(input("Enter the quantity to delete: "))
            if quantity <= 0 or quantity > self.clothing_item.quantity:
                print("Invalid quantity to delete.")
                return self

            if quantity == self.clothing_item.quantity:
                print("Item removed completely from inventory.")
                if self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left

                min_right_node = self.right.get_min()
                self.clothing_item = min_right_node
                self.right = self.right.delete(min_right_node.code)
                return self
            else:
                self.clothing_item.quantity -= quantity
                print(f"{quantity} units of {self.clothing_item.name} deleted from inventory.")
                return self
        return self
    def exists(self, code):
        if self.clothing_item is None:
            print("Inventory is empty")
        elif code == self.clothing_item.code:
            print("Item found in inventory:")
            print(f"Name: {self.clothing_item.name}, Code: {self.clothing_item.code}, Quantity: {self.clothing_item.quantity}")
        elif code < self.clothing_item.code:
            if self.left:
                self.left.exists(code)
            else:
                print("Item doesn't exist in inventory")
        else:
            if self.right:
                self.right.exists(code)
            else:
                print("Item doesn't exist in inventory")
    def inorder(self, items):
        if self.left:
            self.left.inorder(items)
        if self.clothing_item:
            items.append(self.clothing_item)
        if self.right:
            self.right.inorder(items)
        return items
root = BSTNode()
root.insert(ClothingItem("Camiseta", 1001, 20, 1))
root.insert(ClothingItem("Pantalón", 1002, 30, 1))
root.insert(ClothingItem("Chaqueta", 1003, 50, 1))
root.insert(ClothingItem("Falda", 1004, 25, 1))
root.exists(1001)
root.exists(1005)
root.delete(1003)
print("Inorder traversal:", [item.code for item in root.inorder([])])
