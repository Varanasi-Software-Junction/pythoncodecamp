class Solution:
    def fn(self, a):
        return a[1]

    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, a):
        n = len(a)
        r = range(n)
        print(nums)
        awithindex = [(i, a[i]) for i in r]  # 0 is index, 1 is value
        print("original ", awithindex)
        awithindex.sort(key=self.fn)  # sort with value
        print("sorted", awithindex)
        count = 0

        i = 0

        while i <= n - 1:
            if awithindex[i][0] == i:
                i += 1  # element in proper index
                continue
            index = awithindex[i][0]
            a[awithindex[index][0]], a[index] = a[index], a[awithindex[index][0]]
            print("swap ", awithindex[index][0], "with ", index, " values ", a[awithindex[index][0]], " with ", a[index])
            print(a)
            awithindex[i], awithindex[index] = awithindex[index], awithindex[i]
            # self.swap( i, awithindex[i][0])
            print(awithindex)
            count += 1

        return count


# {
#  Driver Code Starts


nums = [5,4,3,2,1]
obj = Solution()
ans = obj.minSwaps(nums)
print(ans)

# } Driver Code Ends
