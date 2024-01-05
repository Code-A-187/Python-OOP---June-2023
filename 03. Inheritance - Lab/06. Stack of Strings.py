from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


class AddStack(BaseStack):
    def push(self, element: str):
        self.data.append(element)


class RemoveStack(BaseStack):
    def pop(self):
        return self.data.pop()


class TopStack(BaseStack):

    def top(self):
        return self.data[-1]


class Stack(AddStack, RemoveStack, TopStack):
    pass


s = Stack()

print(s)
s.push('a')
s.push('b')
s.push('c')
s.push('d')
print(s)
s.pop()
print(s)
print(s.pop())
print(s.is_empty())
