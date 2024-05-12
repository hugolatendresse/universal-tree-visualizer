
def visualize_tree_command_line(root, func_children, func_label):
    def _visualize_tree(root, func_children, func_label, depth=0):
        if root is None:
            return
        print(' ' * depth + func_label(root))
        for child in func_children(root):
            _visualize_tree(child, func_children, func_label, depth + 1)

    _visualize_tree(root, func_children, func_label)
