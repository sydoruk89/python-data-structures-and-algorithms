from binarytree import tree


def tree_intersection(tree1, tree2):
    tree1_set = pre_order(tree1)
    set_result = pre_order2(tree2, tree1_set)
    if set_result == set():
        return None
    else:
        return set_result


def pre_order(tree, node=None, tree_set=None):
    if tree == None:
        return None
    if tree_set is None:
        tree_set = set()

    node = node or tree

    tree_set.add(node.value)
    if node.left:
        pre_order(tree, node.left, tree_set)
    if node.right:
        pre_order(tree, node.right, tree_set)
    return tree_set

def pre_order2(tree, tree_set, node=None, set_result=None):
    if tree_set == None or tree == None:
        return None
    if set_result is None:
        set_result = set()

    node = node or tree

    if node.value in tree_set:
        set_result.add(node.value)

    if node.left:
        pre_order2(tree, tree_set, node.left, set_result)
    if node.right:
        pre_order2(tree, tree_set, node.right, set_result)
    return set_result