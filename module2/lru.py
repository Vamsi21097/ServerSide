class LRUCache(object):
    def __init__(self, max_items=100):
        self.cache = {}
        self.key_order = []
        self.max_items = max_items

    def __setitem__(self, key, value):
        self.cache[key] = value
        self._mark(key)

    def __getitem__(self, key): 
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def _mark(self, key):
        if key in self.key_order:
            self.key_order.remove(key)

        self.key_order.insert(0, key)
        if len(self.key_order) > self.max_items:
            remove = self.key_order[self.max_items]
            del self.cache[remove]
            self.key_order.remove(remove)

cache = LRUCache(4)
cache.__setitem__(1,10)
print(cache.cache)

cache.__setitem__(2,20)
print(cache.cache)


cache.__setitem__(3,30)
print(cache.cache)

cache.__setitem__(4,40)
print(cache.cache)

cache.__setitem__(5,50)
print(cache.cache)

cache.__setitem__(4,30)
print(cache.cache)

cache.__setitem__(4,50)
print(cache.cache)

cache.__getitem__(1)
print(cache.cache)
# import *



# class LRUCache:

#   def __init__(self, capacity):
#     self.capacity = capacity
#     self.cache = set()
#     self.cache_vals = LinkedList()

#   def set(self, value):
#     node = self.get(value)
#     if node == None:
#       if(self.cache_vals.size >= self.capacity):
#         self.cache_vals.insert_at_tail(value)
#         self.cache.add(value)
#         self.cache.remove(self.cache_vals.get_head().data)
#         self.cache_vals.remove_head()
#       else:
#         self.cache_vals.insert_at_tail(value)
#         self.cache.add(value)
    
#     else:
#       self.cache_vals.remove(value)
#       self.cache_vals.insert_at_tail(value)
  
#   def get(self, value):
#     if value not in self.cache:
#       return None
#     else:
#       i = self.cache_vals.get_head()
#       while i is not None:
#         if i.data == value:
#           return i
#         i = i.next

#   def printcache(self):
#     node = self.cache_vals.get_head()
#     while node != None :
#       print(str(node.data) + ", ")
#       node = node.next
      
# cache1 = LRUCache(4)
# cache1.set(10)
# cache1.printcache()

# cache1.set(15)
# cache1.printcache()

# cache1.set(20)
# cache1.printcache()

# cache1.set(25)
# cache1.printcache()

# cache1.set(30)
# cache1.printcache()

# cache1.set(20)
# cache1.printcache()