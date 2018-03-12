class Node:
    def __init__(self, val: object = "", child: object = []) -> object:
        self.value = val
        self.children = child


class NaryTree:

    def __init__(self):
    
        self.tree1 = Node("",
                          [Node("",
                                [Node("Attitude", []), Node("",
                                                            [Node("",
                                                                  [Node("is everything", []), Node("that", [])]
                                                                  )]
                                                            )]
                                ), Node("matters", [])]
                          )
                          
        self.tree2 = Node("",
                          [Node("",
                                [Node("Attitude", []), Node("is", []), Node("",
                                                                            [Node("",
                                                                                  [Node("everything", [])]
                                                                                  )]
                                                                            ), Node("",
                                                                                    [Node("",
                                                                                          [Node("",
                                                                                                [Node("",
                                                                                                      [Node("that", []),
                                                                                                       Node("matters",
                                                                                                            [])]
                                                                                                      )]
                                                                                                )]
                                                                                          )]
                                                                                    )]
                                )])

    def traverse(self, node):
    
        stack = [node]
        while stack:
            cur = stack.pop(0)
            if cur.value != "":
                yield cur.value
            else:
                stack = cur.children + stack

    def printTree(self):
    
        for i in self.traverse(self.tree1):
            print(i)
        for j in self.traverse(self.tree2):
            print(j)

    def compare(self):
    
        iter1, iter2 = self.traverse(self.tree1), self.traverse(self.tree2)
        word1, word2 = next(iter1, "").strip(), next(iter2, "").strip()
        res = ""
        while (word1 and word2):
            l = min(len(word1), len(word2))
            print(word1, '\t', word2)
            if not all(x == y for x, y in zip(word1, word2)):
                return False
            word1 = (word1[l:] + next(iter1, "")).strip()
            word2 = (word2[l:] + next(iter2, "")).strip()

        return True if not (word1 or word2) else False


test = NaryTree()
print(test.compare())
