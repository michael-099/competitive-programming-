class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # pointer on the m-1 th index from the nums1 array
        # pointer on the n-1 array of the nums2 array
        # start from the end of the nums1 array and fill the n+m the value with max of the nums1[m] and nums2[n]
        # return nums1

        p1, p2, i = m - 1, n - 1, (n + m) - 1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
            i -= 1

        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
