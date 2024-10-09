
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
       
        
            
        for index in range(len(flowerbed)):
            if flowerbed[index] == 0:
                
                if index+1 <= len(flowerbed)-1:
                    if flowerbed[index+1] == 1:
                        continue

                if index-1 >= 0:
                    if flowerbed[index-1] == 1:
                        continue

                flowerbed[index] = 1
                n-=1
       
        
        
        if n>0:
            return False
        else:
            return True
                    
                


        