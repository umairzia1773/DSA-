class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def add_node(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            self._add_node_recursive(self.root, new_node)


    def _add_node_recursive(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._add_node_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._add_node_recursive(current_node.right, new_node)



    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")


    def get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.get_height(node.left)
            right_height = self.get_height(node.right)
            return max(left_height, right_height) + 1


    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(" " * 4 * level + "->", node.data)
            self._print_tree(node.left, level + 1)


    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.data == value:
            return node
        if value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)



    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):
        if node is None:
            return node

        if value < node.data:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.data:
            node.right = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._remove_recursive(node.right, temp.data)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def main():
    tree = Tree()
    tree.add_node(10)
    tree.add_node(20)
    tree.add_node(22)
    tree.add_node(17)
    tree.add_node(9)
    tree.add_node(44)
    tree.add_node(8)

    print("--------------------")
    print("PRE-ORDER TRAVERSAL:")
    print("====================")
    tree.pre_order_traversal(tree.root)
    print()
    print("\nPOST-ORDER TRAVERSAL:")
    print("=====================")
    tree.post_order_traversal(tree.root)
    print("\n--------------------")

    print("\nHEIGHT OF THE TREE:", tree.get_height(tree.root))
    print("===================")

    print("\nTREE STRUCTURE:")
    print("===============")
    tree.print_tree()
    print()


    print("SEARCHING VALUE IN THE TREE: ")
    print("===========================")
    search_value = 44
    result_node = tree.search(search_value)
    if result_node:
        print(f"Value {search_value} found in the tree.")
    else:
        print(f"Value {search_value} not found in the tree.")
    print()

    print("REMOVING VALUE FROM THE TREE: ")
    print("============================")
    remove_value = 9
    tree.remove(remove_value)
    print(f"Value {remove_value} removed from the tree.")
    print("\nUPDATED TREE STRUCTURE AFTER REMOVAL:")
    print("====================================")
    tree.print_tree()
main()
