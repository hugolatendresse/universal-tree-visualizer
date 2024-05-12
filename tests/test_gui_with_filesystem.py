# Test visualize_tree_gui()
import os

from visualize_tree_gui import visualize_tree_gui


root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def func_children(x):
    if os.path.isdir(x):
        return [os.path.join(x, f) for f in os.listdir(x)]
    else:
        return []

def func_label(x):
    if os.path.isdir(x):
        return os.path.basename(x)

visualize_tree_gui(root, func_children=func_children, func_label=func_label)