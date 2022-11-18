class No:
    def __init__(self, data):
        self.rightSon = None
        self.leftSon = None
        self.data = data
        self.setSons(None, None)

    def setSons(self, left, right):
        self.leftSon = left
        self.rightSon = right

    def balance(self):
        prof_esq = 0
        if self.leftSon:
            prof_esq = self.leftSon.depth()
        prof_dir = 0
        if self.rightSon:
            prof_dir = self.rightSon.depth()
        return prof_esq - prof_dir

    def depth(self):
        left_depth = 0
        if self.leftSon:
            left_depth = self.leftSon.depth()
        right_depth = 0
        if self.rightSon:
            right_depth = self.rightSon.depth()
        return 1 + max(left_depth, right_depth)

    def leftRotation(self):
        self.data, self.rightSon.data = self.rightSon.data, self.data
        old_left = self.leftSon
        self.setSons(self.rightSon, self.rightSon.rightSon)
        self.leftSon.setSons(old_left, self.leftSon.leftSon)

    def rightRotation(self):
        self.data, self.leftSon.data = self.leftSon.data, self.data
        old_right = self.rightSon
        self.setSons(self.leftSon.leftSon, self.leftSon)
        self.rightSon.setSons(self.rightSon.rightSon, old_right)

    def leftRightRotation(self):
        self.leftSon.leftRotation()
        self.rightRotation()

    def rightLeftRotation(self):
        self.rightSon.rightRotation()
        self.leftRotation()

    def execBalance(self):
        bal = self.balance()
        if bal > 1:
            if self.leftSon.balance() > 0:
                self.rightRotation()
            else:
                self.leftRightRotation()
        elif bal < -1:
            if self.rightSon.balance() < 0:
                self.leftRotation()
            else:
                self.rightLeftRotation()

    def insert(self, data):
        if data <= self.data:
            if not self.leftSon:
                self.leftSon = No(data)
            else:
                self.leftSon.insert(data)
        else:
            if not self.rightSon:
                self.rightSon = No(data)
            else:
                self.rightSon.insert(data)
        self.execBalance()

    def prinTree(self, indent=0):
        print(" " * indent + str(self.data))
        if self.leftSon:
            self.leftSon.prinTree(indent + 2)
        if self.rightSon:
            self.rightSon.prinTree(indent + 2)

root = No(1)
data = '2 3 4 5 6'
data = data.split(' ')
for i in data:
    i = int(i)
    root.insert(i)
    root.execBalance()

root.prinTree()

