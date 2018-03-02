class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        l=[0,1,]
        if n<=2:
            return l[n-1]
        elif n>2:
            for i in range(n-2):
                l.append(int(l[-1])+int(l[-2]))
            return l[-1]