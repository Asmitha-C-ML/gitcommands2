#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        arr.sort()
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends
