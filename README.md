# pycollectionsExt
More container data structures that are missing in python collections lib.

Python's collections library is great. But comparing to Java, it lacks several data structures that is frequently used.

Here as a start, TreeMap and TreeSet classes are created. It provides the similar interfaces as other dict/set class.

TreeMap is similar to Java's util/TreeMap class. It maintains its keys by a self-balancing binary search tree. It provides the capability of traversing keys in ascending order in linear time, and return next biger/smaller key in guaranteed O(log N) time. 