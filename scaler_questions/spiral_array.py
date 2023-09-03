class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        if A == 0:
            return [[]]
        result = [[None] * A for i in range(A)]
        value = 1
        steps = (A-1)//2 + 1
        for i in range(steps):
            # write data in four strips
            for j in range(i, A-i):
                result[i][j] = value
                value += 1
            for j in range(i+1, A-i):
                result[j][A-i-1] = value
                value += 1
            for j in range(A-i-2, i-1, -1):
                result[A-i-1][j] = value
                value += 1
            for j in range(A-i-2, i, -1):
                result[j][i] = value
                value += 1
        return result


num = int(input("Enter the number : "))
s = Solution()
print(s.generateMatrix(num))