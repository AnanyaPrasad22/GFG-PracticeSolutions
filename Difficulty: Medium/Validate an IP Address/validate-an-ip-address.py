#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        arr=str.split(".")
        if len(arr)>4 or len(arr)<4:
            return False
        for item in arr:
            if not item.isdigit():
                return False
            num=int(item)
            if num<0 or num>255:
                return False
            if item!='0' and item[0]=='0':
                return False
        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends