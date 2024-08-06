#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        #code here
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if self.maxTime(arr, mid) > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
        
    def maxTime(self, arr, time):
        n = len(arr)
        painter = 1
        time_taken = 0
        for i in range(n):
            if time_taken + arr[i] <= time:
                time_taken += arr[i]
            else:
                painter += 1
                time_taken = arr[i]
                
        return painter
        
      


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends