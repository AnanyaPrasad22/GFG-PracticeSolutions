#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        # n = len(arr)
        # low, high = 0, n-1
        # while low <= high:
        #     mid = low + (high-low) // 2
        #     if 

        ans=0
        for i in range(len(arr)-1,0,-1):
            if arr[i]<arr[i-1]:
                ans=i
                
        return ans  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)

# } Driver Code Ends