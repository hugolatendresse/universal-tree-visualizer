import tkinter as tk
from tkinter import ttk


def visualize_tree_gui(root, func_children, func_label):

    def _visualize_tree(root, func_children, func_label, parent):
        if root is None:
            return
        node_id = tree.insert(parent, 'end', text=func_label(root))
        tree.item(node_id, open=True)
        for child in func_children(root):
            _visualize_tree(child, func_children, func_label, parent=node_id)

    root_window = tk.Tk()
    root_window.state('zoomed')
    tree = ttk.Treeview(root_window)
    tree.pack(expand=True, fill='both')
    _visualize_tree(root, func_children, func_label, parent='')
    root_window.mainloop()

