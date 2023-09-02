class Solution:
    def binary_search(self, lst, left, right, key):
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == key:
                return mid
            elif lst[mid] < key:
                left = mid + 1
            else:
                right = mid -1
        return -1
    
    def find_pivot(self, lst):
        left = 0
        right = len(lst) - 1
        while left < right:
            mid = (left + right) // 2
            if lst[mid] > lst[mid+1]:
                return mid
            elif left < mid and lst[mid] < lst[mid-1]:
                return mid-1
            elif mid < right and lst[mid] > lst[right]:
                left = mid + 1
            elif left < mid and lst[left] > lst[mid]:
                right = mid - 1
            else:
                return -1
        return -1

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.find_pivot(A)
        if pivot == -1:
            return (self.binary_search(A, 0, len(A)-1, B))
        else:
            if A[0] == B:
                return 0
            elif A[0] < B:
                return(self.binary_search(A, 0, pivot, B))
            else:
                return(self.binary_search(A, pivot+1, len(A)-1, B))
