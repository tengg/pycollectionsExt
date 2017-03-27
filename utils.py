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
        'Insert a new node that has specified value'
        t = self.root
        if not t:
            self.root = RBTreeNode(val)
            return self.root
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

    def delete(self, p):
        'Delete the specified entry from the tree'
        if p.left and p.right:
            s = self.successor(p)
            self._swap_nodes(s, p)
            if p is self.root:
                self.root = s
        replacement = p.left or p.right
        if replacement:
            replacement.parent = p.parent
            if not p.parent:
                self.root = replacement
            elif p is p.parent.left:
                p.parent.left = replacement
            else:
                p.parent.right = replacement
            p.left = p.right = p.parent = None
            if p.black:
                self._fix_after_deletion(replacement)
        elif not p.parent:
            self.root = None
        else:
            if p.black:
                self._fix_after_deletion(p)
            if p.parent:
                if p is p.parent.left:
                    p.parent.left = None
                elif p is p.parent.right:
                    p.parent.right = None
                p.parent = None

    def successor(self, t):
        'Return the successor of the specified entry, or None if no such.'
        if not t:
            return None
        if t.right:
            p = t.right
            while p.left:
                p = p.left
        else:
            ch, p = t, t.parent
            while p and ch is p.right:
                ch = p
                p = p.parent
        return p

    def predecessor(self, t):
        'Return the predecessor of the specified entry, or None if no such.'
        if not t:
            return None
        if t.left:
            p = t.left
            while p.right:
                p = p.right
        else:
            ch, p = t, t.parent
            while p and ch is p.left:
                ch = p
                p = p.parent
        return p

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
        while x is not self.root and x.black:
            if x is x.parent.left:
                sib = x.parent.right
                if not sib.black:
                    sib.black = True
                    sib.parent.black = False
                    self._rotate_left(x.parent)
                    sib = x.parent.right
                if sib.left.black and sib.right.black:
                    sib.black = False
                    x = x.parent
                else:
                    if sib.right.black:
                        sib.left.black = True
                        sib.black = False
                        self._rotate_right(sib)
                        sib = x.parent.right
                    sib.black = x.parent.black
                    x.parent.black = sib.right.black = True
                    self._rotate_left(x.parent)
                    x = root
            else:
                sib = x.parent.left
                if not sib.black:
                    sib.black = True
                    x.parent.black = False
                    self._rotate_right(x.parent)
                    sib = x.parent.left
                if sib.right.black and sib.left.black:
                    sib.black = False
                    x = x.parent
                else:
                    if sib.left.black:
                        sib.right.black = True
                        sib.black = False
                        self._rotate_left(sib)
                        sib = x.parent.left
                    sib.black = x.parent.black
                    x.parent.black = sib.left.black = True
                    self._rotate_right(x.parent)
                    x = root
        x.black = True

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
            l.parent = p.parent
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

    def _swap_nodes(self, n1, n2):
        n1l, n1r, n1p = n1.left, n1.right, n1.parent
        if n1p:
            if n1p.left is n1:
                n1p.left = n2
            else:
                n1p.right = n2
        n1.left, n1.right, n1.parent = n2.left, n2.right, n2.parent
        if n2.parent:
            if n2.parent.left is n2:
                n2.parent.left = n1
            else:
                n2.parent.right = n1
        n2.left, n2.right, n2.parent = n1l, n1r, n1p
