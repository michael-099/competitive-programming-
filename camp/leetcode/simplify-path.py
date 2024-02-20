class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        stack=[]
        for current in path:
            if current != "" and current!=".." and current != ".":
                stack.append(current)
            elif current=="..":
                if stack:
                    stack.pop()
        return "/"+"/".join(stack)
                   
        