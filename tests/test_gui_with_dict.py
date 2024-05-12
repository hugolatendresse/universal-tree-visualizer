# Test visualize_tree_gui()
from visualize_tree_gui import visualize_tree_gui


root = {'id': 1, 'children': [{'id': 500, 'children': [{'id': 300, 'children': []}]},{'id': 2, 'children': [{'id': 3, 'children': []}]}]}
visualize_tree_gui(root, func_children=lambda x: x['children'], func_label=lambda x: str(x['id']))