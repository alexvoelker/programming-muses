from binary_tree import Binary_Tree as b_tree


tree = b_tree(0)
tree.add_node(2)
tree.add_node(3)
tree.add_node(4)
tree.add_node(6)
tree.add_node(1)
tree.add_node(5)
tree.add_node(2)

tree.add_node(7)
tree.add_node(277)
tree.add_node(8)
tree.add_node(492)
tree.add_node(734)
tree.add_node(9)
tree.add_node(12)
tree.add_node(13)
tree.add_node(86)


tree.print_tree()
tree.reverse()
print("\nReversed!")
tree.print_tree()