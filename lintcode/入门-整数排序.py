class Solution:
    """
    @param: A: an integer array
    @return:
    """
    def sortIntegers(self, A):
        # write your code here
        length=len(A)
        for i in range(length-1):
            for j in range(1,length-i):
                if A[j]<A[j-1]:
                    A[j],A[j-1]=A[j-1],A[j]