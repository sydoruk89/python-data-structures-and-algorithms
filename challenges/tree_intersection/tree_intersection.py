from tree import Queue, BinaryTree

def tree_intersection(tree1, tree2):
    result = set()
    q1 = q2 = Queue()

    if tree1.root and tree2.root:
        q1.enqueue(tree1.root)
        q2.enqueue(tree2.root)

    while not (q1.is_empty() and q2.is_empty()):
        node1, node2 = q1.dequeue().value, q2.dequeue().value
        if node1.value == node2.value:
            result.add(node1.value)
        
        if node1.left and node2.left:
            q1.enqueue(node1.left)
            q2.enqueue(node2.left)

        if node1.right and node2.right:
            q1.enqueue(node1.right)
            q2.enqueue(node2.right)

    return result
