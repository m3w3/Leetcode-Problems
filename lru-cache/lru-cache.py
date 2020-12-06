class Node: 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res
        

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
        else: 
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            node.value = value # update node to new value
            self._move_to_head(node)
        else: 
            newNode = Node()
            newNode.key, newNode.value = key, value # initialize key-value pair
            self.cache[key] = newNode # new nodes are always added
            self._add_node(newNode) # add newNode to front of linkedlist
            self.size += 1
            
            # now, need to check if list is full -> evict nodes
            if self.size > self.capacity:
                lru = self._pop_tail()
                self.cache.pop(lru.key, None)
                self.size -= 1
