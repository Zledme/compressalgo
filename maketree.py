from urllib.parse import ParseResultBytes


class node:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def children(self):
        return (self.right, self.left)
