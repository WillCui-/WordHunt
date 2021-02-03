from collections import defaultdict
from src.trie import Trie

def serialize(root):
    output = ['<']

    for key in root.keys():
        output.append(key)

        value = root[key]
        if value != '_end':
            output += serialize(value)

    output.append('>')

    return output


def deserialize(data):
    ddict = defaultdict(lambda : "_end")
    current = ddict
    stack = []

    for char in data:
        if char == '<':
            stack.append(current)
        elif char == '>':
            stack.pop()
        elif char == '_end':
            stack[-1]["_end"] = "_end"
        else:
            current = defaultdict(lambda: "_end")
            if (len(stack) > 0):
                stack[-1].setdefault(char, current)
    
    output = Trie()
    output.root = ddict

    return output
