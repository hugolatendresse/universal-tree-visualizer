# Test visualize_tree_gui()
import os
import pandas as pd

from visualize_tree_gui import visualize_tree_gui

df = pd.DataFrame({"colA": [1, 2, 3], "colB": [4, 5, 6]})

root = df

# TODO need to implement max recursion depth in vizualizer

def func_children(x):
    children=[]
    attnames = list(dir(x))
    attnames = [x for x in attnames if not x.startswith("__")]  # ignore attirbues starting with __ for now
    for a in attnames:
        try:
            y= x.__getattribute__(a)
            if y is not None:
                children.append(y)
        except:
            pass
    return children

def func_label(x):
    return str(x)

visualize_tree_gui(root, func_children=func_children, func_label=func_label)