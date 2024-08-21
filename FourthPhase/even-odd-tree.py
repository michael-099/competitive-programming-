class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def is_even(num):return num%2==0
        queue = deque()
        queue.append(root)
        current,level=None,0
        
        while queue:
            prev=None
            for i in range(len(queue)):
                current = queue.popleft()
                if current :
                    if is_even(level):
                        if is_even(current.val):
                            return False
                        if prev is not None :
                            if current.val<= prev:
                                return False
                    else:
                        if not is_even(current.val) :
                            return False
                        if prev is not None:
                            if current.val>=prev:
                                return False
                    prev=current.val
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            
            level+=1
        return True 
        
