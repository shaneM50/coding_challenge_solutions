from src.binary_search_solution import BinarySearchSolution

class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        self.data = []

    def get_length(self) -> int:
        return len(self.data)
    
    def get_index_for_insert(self, value: int) -> int:
        for i, element in enumerate(self.data):
                if element >= value:
                    return i
    
    def get_index_for_delete(self, value: int) -> int:
        #return self.index_search_linear(value)
        
        return self.index_search_binary(value)
    
    def index_search_linear(self, value: int) -> int:
        for i, element in enumerate(self.data):
                if element == value:
                    return i
        
        return -1

    def index_search_binary(self, value: int) -> int:
        binary_search = BinarySearchSolution()

        return binary_search.search(self.data, value)

    
    def add(self, value: int) -> None:
        if self.get_length() == 0 or self.data[-1] <= value:
            self.data.append(value)
        
        else:
            self.data.insert(self.get_index_for_insert(value), value)
    
    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        
        index_for_delete = self.get_index_for_delete(value)
        
        if index_for_delete == -1:
            return False
        else:
            del self.data[index_for_delete]
            return True

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        container_length = self.get_length()
        
        if container_length == 0:
            raise RuntimeError("Empty container has no median value.")
        elif container_length == 1 or container_length == 2:
            return self.data[0]
        else:
            middle_element = self.data[self.get_middle_index()]
            return middle_element
    
    def get_middle_index(self) -> int:
        container_length = self.get_length()
        is_even = (container_length % 2 == 0)
        
        if is_even:
            middle_index = (self.get_length() // 2) - 1
        else:
            middle_index = self.get_length() // 2
        
        return middle_index