class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        #code here
        if m > n:
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if self.canAllot(arr, mid) > m:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
    def canAllot(self, arr, pages):
        n = len(arr)
        students = 1
        page_count = 0
        for i in range(0, n):
            if page_count + arr[i] <= pages:
                page_count += arr[i]
            else:
                students += 1
                page_count = arr[i]
                
        return students
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(n, arr, m))

# } Driver Code Ends