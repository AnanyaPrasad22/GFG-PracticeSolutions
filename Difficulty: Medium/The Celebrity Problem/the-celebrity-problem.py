class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = [i for i in range(n)]
        
        while len(stack)>1:
            p1 = stack.pop()
            p2 = stack.pop()
            
            if mat[p1][p2] == 1:
                stack.append(p2)
            elif mat[p1][p2] == 0:
                stack.append(p1)
        p = stack.pop()
        
        for i in range(n):
            if i != p:
                if mat[p][i] == 1:
                    return -1
                elif mat[i][p] == 0:
                    return -1
        else:
            return p 

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends