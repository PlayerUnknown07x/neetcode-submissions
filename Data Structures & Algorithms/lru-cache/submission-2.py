class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value_map = {}
        self.key_addr_map = {}
        self.stack = []
    def get(self, key: int) -> int:
        val = -1
        if key in self.key_value_map.keys():
            val = self.key_value_map[key]
            if key not in self.key_addr_map.keys():
                self.stack.append(key)
                self.key_addr_map[key] = len(self.stack)-1
            else:
                self.stack.pop(self.key_addr_map[key])
                for k in range(self.key_addr_map[key],len(self.stack)):
                    self.key_addr_map[self.stack[k]] -= 1
                self.stack.append(key)
                self.key_addr_map[key] = len(self.stack)-1
        print("after get ",key,":",self.key_addr_map)
        return val 
    def put(self, key: int, value: int) -> None:
        if key in self.key_value_map.keys():
            self.key_value_map[key] = value
        else:
            if len(self.key_value_map) == self.capacity:
                l_key = self.stack.pop(0)
                for k in self.stack:
                    self.key_addr_map[k] -= 1
                self.key_value_map.pop(l_key)
                self.key_addr_map.pop(l_key)
            self.key_value_map[key] = value
        if key not in self.key_addr_map.keys():
            self.stack.append(key)
            self.key_addr_map[key] = len(self.stack)-1
        else:
            self.stack.pop(self.key_addr_map[key])
            for k in range(self.key_addr_map[key],len(self.stack)):
                self.key_addr_map[self.stack[k]] -= 1
            self.stack.append(key)
            self.key_addr_map[key] = len(self.stack)-1
        print("after put ",key,":",self.key_addr_map)





        
