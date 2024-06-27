def TreeConstructor(strArr):
    
    tree = {}

    for pair in strArr:
        child, parent = pair.strip('()').split(',')
        child = int(child)
        parent = int(parent)

        if parent in tree:
            if len(tree[parent]) >= 2:
                return False
            else:
                tree[parent].append(child)
        else:
            tree[parent] = [child]

        
        if child in tree and parent in tree[child]:
            return False

    
    roots = [node for node in tree if node not in sum(tree.values(), [])]
    if len(roots) != 1:
        return False

    return True


# keep this function call here 
print(TreeConstructor(input()))