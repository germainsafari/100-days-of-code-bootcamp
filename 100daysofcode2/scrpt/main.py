class Node:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None

    def printTree(self):
        n = self.data
        return n

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left.Node(data)
            self.left.insert(data)
        if data < self.data:
            if self.right is None:
                self.right.Node(data)
            self.right.insert(data)

        else:
            self.data = data

    def inOrder(self, data):
        # left-root-right
        res = []
        if self.left:
            res += self.left.inorder()
        res.append(data)
        if self.right:
            res += self.right.inorder()



    def preOrder(self, data):
        # root-left-right
        res = []
        res.append(data)
        if self.left:
            res += self.left.preOrder()
        if self.right:
            res += self.right.preOrder()


    def postOrder(self, data):
        # left-right-root
        res = []
        if self.left:
            res += self.left.postOrder()
        if self.right:
            res += self.right.postOrder()
        res.append(data)

# bubblesort
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
r = bubble([4,3,5,6,0,1])
print(r)



# mergesort
# insertionsort
# selectio nsort
