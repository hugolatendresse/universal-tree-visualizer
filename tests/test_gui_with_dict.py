# Test visualize_tree_gui()
from visualize_tree_gui import visualize_tree_gui

root = {
    'id': 1,
    'children': [
        {
            'id': 2,
            'children': [
                {
                    'id': 3,
                    'children': [
                        {
                            'id': 4,
                            'children': []
                        }
                    ]
                }
            ]
        },
        {
            'id': 5,
            'children': [
                {
                    'id': 6,
                    'children': []
                }
            ]
        }, {
            'id': 7,
            'children': [
                {
                    'id': 8,
                    'children': []
                }
            ]
        },
{
            'id': 9,
            'children': [
                {
                    'id': 10,
                    'children': [
                        {
                            'id': 11,
                            'children': []
                        }
                    ]
                }
            ]
        },
        {
            'id': 12,
            'children': [
                {
                    'id': 13,
                    'children': []
                }
            ]
        }, {
            'id': 14,
            'children': [
                {
                    'id': 15,
                    'children': []
                }
            ]
        }
    ],
}
visualize_tree_gui(root, func_children=lambda x: x['children'], func_label=lambda x: str(x['id']))
