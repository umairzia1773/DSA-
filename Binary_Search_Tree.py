from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, root):
        if root is None:
            return
        else:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root is None:
            return
        else:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is None:
            return
        else:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

    def level_order_traversal(self, root):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    def search_element(self, root, val):
        if root is None or root.val == val:
            return root
        left_search = self.search_element(root.left, val)
        if left_search:
            return left_search
        return self.search_element(root.right, val)

    def add_element_left(self, parent_val, new_val):
        if self.root is None:
            self.root = TreeNode(parent_val)
        parent_node = self.search_element(self.root, parent_val)
        if parent_node:
            parent_node.left = TreeNode(new_val)
        else:
            print("Parent node not found.")

    def add_element_right(self, parent_val, new_val):
        if self.root is None:
            self.root = TreeNode(parent_val)
        parent_node = self.search_element(self.root, parent_val)
        if parent_node:
            parent_node.right = TreeNode(new_val)
        else:
            print("Parent node not found.")

    def find_min(self, root):
        if root is None:
            return float('inf')

        min_val = root.val
        left_min = self.find_min(root.left)
        right_min = self.find_min(root.right)

        if left_min < min_val:
            min_val = left_min
        if right_min < min_val:
            min_val = right_min

        return min_val

    def find_max(self, root):
        if root is None:
            return float('-inf')

        max_val = root.val
        left_max = self.find_max(root.left)
        right_max = self.find_max(root.right)

        if left_max > max_val:
            max_val = left_max
        if right_max > max_val:
            max_val = right_max

        return max_val

    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.find_min(root.right)
            root.val = temp
            root.right = self.delete_node(root.right, temp)

        return root


def main():
    BT = Binary_Search_Tree()
    BT.root = TreeNode(10)
    BT.root.left = TreeNode(20)
    BT.root.right = TreeNode(30)
    BT.root.left.left = TreeNode(40)
    BT.root.left.right = TreeNode(50)

    print("IN-ORDER TRAVERSAL:")
    print("==================")
    BT.inorder_traversal(BT.root)
    print("\n------------------")
    print("PRE-ORDER TRAVERSAL:")
    print("===================")
    BT.preorder_traversal(BT.root)
    print("\n-------------------")
    print("POST-ORDER TRAVERSAL:")
    print("====================")
    BT.postorder_traversal(BT.root)
    print("\n--------------------")
    print("LEVEL ORDER TRAVERSAL:")
    print("=====================")
    BT.level_order_traversal(BT.root)
    print("\n---------------------")

    print("\nSEARCHING ELEMENT IN THE BINARY TREE:")
    print("=====================================")
    search = BT.search_element(BT.root, 20)
    if search:
        print("||Element found in the Tree|| : ", search.val)
    else:
        print("||Element not found in the Tree||")

    BT.add_element_left(40, 64)
    BT.add_element_right(50, 100)

    print("\nIN-ORDER TRAVERSAL AFTER ADDING ELEMENT:")
    print("=======================================")
    BT.inorder_traversal(BT.root)
    print()

    min_val = BT.find_min(BT.root)
    max_val = BT.find_max(BT.root)
    print(f"\nMINIMUM VALUE IN THE BINARY TREE: {min_val}")
    print("=================================")
    print(f"MAXIMUM VALUE IN THE BINARY TREE: {max_val}")
    print("=================================")

    BT.delete_node(BT.root, 30)
    print("\nLEVEL ORDER TRAVERSAL AFTER DELETING ELEMENT:")
    print("============================================")
    BT.level_order_traversal(BT.root)

main()
