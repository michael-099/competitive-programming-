# class ListNode:
#     def __init__(self,val,next=None):
#     self.val=val
#     self.next=next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.visited = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.visited = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.stack) > 1:
            self.visited.append(self.stack.pop())
            steps -= 1
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.visited) > 0:
            self.stack.append(self.visited.pop())
            steps -= 1
        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
