class ZigZag:

    def solution(self, numbers):
        length = len(numbers)
        i = 0
        result = []
        
        zigzag_result = self.is_zigzag(i, numbers)
        result.append(zigzag_result)
        
        if (length == 3):
            return result
            
        else: 
            while (i + 3) <= length-1:
                i = (i + 1)
                zigzag_result = self.is_zigzag(i, numbers)
                result.append(zigzag_result)
            
            return result    

    def is_zigzag(self, i, numbers):
        isZigZag = (
            (numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]) 
            or 
            (numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2])    
        )
        
        return 1 if isZigZag else 0