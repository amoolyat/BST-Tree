class Binary_Search_Tree:

    class __BST_Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.__root = None
    
    def __get_height(self, root):   
        if root is None:
            return 0
        right_height = 0
        left_height = 0
        if root.left is not None:
            left_height = root.left.height
        if root.right is not None:
            right_height = root.right.height
        toreturn = max(left_height,right_height)
        return toreturn+1
    
    def __balance(self, root, value): 
        balance = self.__get_balance(root) 
        if balance > 1 and value < root.left.value: 
            root = self.__right_rotate(root) 
        elif balance > 1 and value > root.left.value: 
            root.left = self.__left_rotate(root.left) 
            root = self.__right_rotate(root) 
        elif balance < -1 and value < root.right.value: 
            root.right = self.__right_rotate(root.right) 
            root = self.__left_rotate(root) 
        elif balance < -1 and value > root.right.value: 
            root = self.__left_rotate(root) 
        return root
        
    def __get_balance(self,root):
        if root is None:
            return 0
        factor = self.__get_height(root.left) - self.__get_height(root.right)
        return factor
    
    def __left_rotate(self, root):
        new_root = root.right
        temp = new_root.left
        new_root.left = root
        root.right = temp
        root.height = self.__get_height(root)
        new_root.height = self.__get_height(new_root)
        return new_root
        
    def __right_rotate(self, root):
        new_root = root.left
        temp = new_root.right
        new_root.right = root
        root.left = temp
        root.height = self.__get_height(root)
        new_root.height = self.__get_height(new_root)
        return new_root
    
    def insert_element(self, value):
        if self.__root is None:
            node = Binary_Search_Tree.__BST_Node(value)
            self.__root = node
        else:
            self.__root = self.__recursive_insert(self.__root, value)
        
    def __recursive_insert(self, root, value):
        if root is None:
            return 
        if root.value == value:
            raise ValueError
        if root.value < value:
            if root.right is None:
                node = Binary_Search_Tree.__BST_Node(value)
                root.right = node
            else:
                root.right = self.__recursive_insert(root.right, value)
        else:
            if root.left is None:
                node = Binary_Search_Tree.__BST_Node(value)
                root.left = node
                root.height = self.__get_height(root)
            else:
                root.left = self.__recursive_insert(root.left, value)
        root.height = self.__get_height(root)
        root = self.__balance(root, value)
        return root 
    
    def __del_balance(self, root):
        balance = self.__get_balance(root)
        if balance > 1 and root.left.left is not None:
            return self.__right_rotate(root)
        if balance > 1 and root.left.right:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)
        if balance < -1 and root.right.left:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)
        if balance < -1 and root.right.right is not None:
            return self.__left_rotate(root)
        return root
    
    def remove_element(self, value):
        if self.__root is None:
            raise ValueError 
        self.__root = self.__recursive_remove(self.__root, value)
        
    def __recursive_remove(self, root, value):
        if root is None:
            raise ValueError
        if root.value == value:
            if root.left is None and root.right is None:
                root = None
                return root
            if root.left is None and root.right is not None:
                root = root.right
                return root
            if root.right is None and root.left is not None:
                root = root.left
                return root
            temp = root.right
            while temp.left:
                temp = temp.left
            root.value = temp.value
            root.right = self.__recursive_remove(root.right,root.value)   
        elif root.value < value:
            root.right = self.__recursive_remove(root.right,value)
        else:
            root.left = self.__recursive_remove(root.left,value)
        root.height = self.__get_height(root)
        root = self.__del_balance(root)
        return root
    
    def in_order(self):
        node = self.__root
        list = [ ]
        self.__recursive_inorder(node, list)
        if len(list) == 0:
            toReturn = '[ ]'
        else: 
            toReturn = '[ ' + str(list)[1:-1] + ' ]'
        return toReturn
    
    def __recursive_inorder(self, node, list):
        if node is None:
            return list
        self.__recursive_inorder(node.left, list)
        list.append(node.value)
        self.__recursive_inorder(node.right, list)
    
    def pre_order(self):
        node = self.__root
        list = [ ]
        self.__recursive_preorder(node, list)
        if len(list) == 0:
            toReturn = '[ ]'
        else: 
            toReturn = '[ ' + str(list)[1:-1] + ' ]'
        return toReturn
    
    def __recursive_preorder(self, node, list):
        if node is None:
            return list
        list.append(node.value)
        self.__recursive_preorder(node.left, list)
        self.__recursive_preorder(node.right, list) 

    def post_order(self):
        node = self.__root
        list = [ ]
        self.__recursive_postorder(node, list)
        if len(list) == 0:
            toReturn = '[ ]'
        else: 
            toReturn = '[ ' + str(list)[1:-1] + ' ]'
        return toReturn
        
    def __recursive_postorder(self, node, list):
        if node is None:
            return list
        self.__recursive_postorder(node.left, list)
        self.__recursive_postorder(node.right, list)
        list.append(node.value)
    
    def get_height(self):
        if self.__root is None:
            return 0 
        return self.__root.height
    
    def to_list(self):
        list = [] 
        self.__recursive_inorder(self.__root, list)
        return list

    def __str__(self):
        return self.in_order()

