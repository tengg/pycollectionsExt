import utils

class TreeMap(dict):
    def __init__(self):
        self.__map = {}
        self.__bst = utils.RBTree()

    def __setitem__(self, key, value,
                    dict_setitem=dict.__setitem__):
        'od.__setitem__(i, y) <==> od[i]=y'
        if key not in self:
            self.__map[key] = self.__bst.insert(key)
        dict_setitem(self, key, value)

    def __iter__(self):
        'od.__iter__() <==> iter(od)'
        stk = []
        t = self.__bst.get_root()
        while stk or t:
            if t:
                stk.append(t)
                t = t.left
            else:
                t = stk.pop()
                yield t.val
                t = t.right

    def __reversed__(self):
        'od.__reversed__() <==> reversed(od)'
        # Traverse the BST in reversed in-order order.
        stk = []
        t = self.__bst.get_root()
        while stk or t:
            if t:
                stk.append(t)
                t = t.right
            else:
                t = stk.pop()
                yield t.val
                t = t.left

    def clear(self):
        'od.clear() -> None.  Remove all items from od.'
        self.__bst = utils.RBTree()
        self.__map.clear()
        dict.clear(self)