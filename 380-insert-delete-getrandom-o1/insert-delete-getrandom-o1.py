
import random

class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.Array = []
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False

        else:
            self.hashMap[val] = len(self.Array)
            self.Array.append(val)
            return True

        

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            index = self.hashMap[val]
            last_val = self.Array[-1]
            self.Array[index] = last_val
            self.Array.pop()
            del self.hashMap[val]
            if val!=last_val:
                self.hashMap[last_val] = index
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        random_val = random.choice(self.Array)
        
        return random_val

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()