#User function Template for python3

class Solution:
    def canPlace(self, stalls, k, n, dist):
        count_cows = 1
        last_stall = stalls[0]
        for i in range(1, n):
            if stalls[i] - last_stall >= dist:
                count_cows += 1
                last_stall = stalls[i]
                if count_cows >= k:
                    return True
        return False
        
        
    def solve(self,n,k,stalls):
        stalls = sorted(stalls)
        low = 1
        high = stalls[n-1] - stalls[0]
        while low <= high:
            mid = low + (high - low) // 2
            if self.canPlace(stalls, k, n, mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
        
    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends