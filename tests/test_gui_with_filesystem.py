# Test visualize_tree_gui()
import os

from visualize_tree_gui import visualize_tree_gui


root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def func_children(x):
    children = []
    if os.path.isdir(x):
        children = [os.path.join(x, f) for f in os.listdir(x)]
        children = [x for x in children if not os.path.basename(x).startswith(".")]
    return children

def func_label(x):
    return os.path.basename(x)

visualize_tree_gui(root, func_children=func_children, func_label=func_label)