from collections import defaultdict
from src.trie import Trie

def serialize(root):
    output = ['<']

    for key in root.keys():
        output.append(key)

        value = root[key]
        if value is not '_end':
            output += serialize(value)

    output.append('>')

    return output


def deserialize(data):
    ddict = defaultdict(lambda : "_end")
    current = ddict
    stack = []

    for char in data:
        if char is '<':
            stack.append(current)
        elif char is '>':
            if (len(stack) > 1):
                stack[len(stack) - 1]["_end"] = "_end"
            stack.pop()
        else:
            current = defaultdict(lambda: "_end")
            if (len(stack) > 0):
                stack[len(stack) - 1].setdefault(char, current)
    
    output = Trie()
    output.root = ddict

    return output
