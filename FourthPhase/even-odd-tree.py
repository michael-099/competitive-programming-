class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def is_increasing(arr):
            if len(arr)==1:
                if arr[0] % 2 == 0 :
                    return False
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
                if arr[i] % 2 == 0 or arr[i+1] % 2 == 0:
                    return False
            return True

        def is_decreasing(arr):
            if len(arr)==1:
                if arr[0] % 2 != 0 :
                    return False
            for i in range(len(arr) - 1):
                if arr[i] <= arr[i + 1] :
                    return False
                if arr[i] % 2 != 0 or arr[i+1] % 2 != 0:
                    return False
            return True

        queue = deque()
        queue.append(root)
        arr = []
        while queue:
            temp = []
            for i in range(len(queue)):
                temp.append(queue[i].val)
            arr.append(temp)

            for i in range(len(queue)):
                x = queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
        print(arr)
        for i in range(len(arr)):
            if i % 2 == 0:
                print(is_increasing(arr[i]))
                if not is_increasing(arr[i]):
                    return False
            else:
                print(is_decreasing(arr[i]))
                if not is_decreasing(arr[i]):
                    return False

        return True
