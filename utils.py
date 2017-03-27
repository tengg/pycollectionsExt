class RBTreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.black = True
        self.left = None
        self.right = None
        self.parent = parent


class RBTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, val):
        t = self.root
        if not t:
            self.root = RBTreeNode(val)
            return
        while t:
            parent = t
            if t.val < val:
                t = t.right
            elif t.val > val:
                t = t.left
            else:
                return t
        e = RBTreeNode(val, parent)
        if parent.val < val:
            parent.right = e
        else:
            parent.left = e
        self._fix_after_insertion(e)
        return e

    def delete(self, val):
        pass

    def _fix_after_insertion(self, x):
        x.black = False
        while x and x is not self.root and not x.parent.black:
            if x.parent is x.parent.parent.left:
                y = x.parent.parent.right
                if y and not y.black:
                    y.black = x.parent.black = True
                    x.parent.parent.black = False
                    x = x.parent.parent
                else:
                    if x is x.parent.right:
                        x = x.parent
                        self._rotate_left(x)
                    x.parent.black = True
                    x.parent.parent.black = False
                    self._rotate_right(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y and not y.black:
                    y.black = x.parent.black = True
                    x.parent.parent.black = False
                    x = x.parent.parent
                else:
                    if x is x.parent.left:
                        x = x.parent
                        self._rotate_right(x)
                    x.parent.black = True
                    x.parent.parent.black = False
                    self._rotate_left(x.parent.parent)
        self.root.black = True

    def _fix_after_deletion(self, x):
        pass

    def _rotate_left(self, p):
        if p:
            r = p.right
            p.right = r.left
            if r.left:
                r.left.parent = p
            r.parent = p.parent
            if not p.parent:
                self.root = r
            elif p.parent.left is p:
                p.parent.left = r
            else:
                p.parent.right = r
            r.left = p
            p.parent = r

    def _rotate_right(self, p):
        if p:
            l = p.left
            p.left = l.right
            if l.right:
                l.right.parent = p
            if not p.parent:
                self.root = l
            elif p.parent.right is p:
                p.parent.right = l
            else:
                p.parent.left = l
            l.right = p
            p.parent = l

    def _print_serialized_tree(self):
        t = self.root
        level = [t]
        res = []
        while t and level:
            nl = []
            for node in level:
                if node:
                    res.append(str(node.val))
                    nl.append(node.left)
                    nl.append(node.right)
                else:
                    res.append('#')
            level = nl
        print(''.join(res).rstrip('#'))
