import copy
class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def showNodeInfo(self):
        print("node value=%d"%self.value)
        if self.leftChild!=None:
            print("leftChild=%d"%self.leftChild.value)
        if self.rightChild!=None:
            print("rightChild=%d"%self.rightChild.value)
        print('-----------------------------')

class Tree:
    # init tree
    def __init__(self):
        self.root=None

    # # check para
    # def checkIsNode(self,node):
    #     if not isinstance(node, Node):
    #         n = Node(node)
    #         # print('make %d to be class Node'%node)
    #         return n
    #     else:
    #         # print('%d is a value of a class Node'%(node.value))
    #         return node

    # search  specified key from tree
    def  search(self,parent,k):
        if parent==None:
            return False,None
        elif parent.value<k:
            return self.search(parent.rightChild,k)
        elif parent.value>k:
            return self.search(parent.leftChild,k)
        elif parent.value==k:
            return True,parent




    # insert node to tree
    def insert(self,value):
        if not isinstance(value, Node):
            node= Node(value)

        if self.root==None:
            self.root=node
        else :
            parent=self.root
            child=None
            # insert right subtree
            if parent.value<node.value:
                while 1:
                    current=parent.rightChild
                    if current==None :  
                        parent.rightChild=node
                        break
                    elif current.value>node.value:
                        node.rightChild=parent.rightChild
                        parent.rightChild=node
                        break
                    else:
                        parent=parent.rightChild
            # insert left subtree
            if parent.value>node.value:
                while 1:
                    current=parent.leftChild
                    if current==None:
                        parent.leftChild=node
                        break
                    elif current.value<node.value:  
                        node.leftChild=parent.leftChild
                        parent.leftChild=node
                        break                  
                    else:
                        parent=parent.leftChild



    # delete node
    def delete(self,parent,value):
        if self.root is None:  
            print('Tree is null')
        if parent.leftChild is None:
            print('111') 
            parent=parent.rightChild
        elif parent.rightChild is None:
            print('222') 
            parent=parent.leftChild
        else:
            print('333')                                             # 删除要区分左右孩子是否为空的情况    
            tmp=parent.rightChild;             #找到后继结点  
            parent.value=tmp.value;  
            parent.rightChild=self.delete(parent.rightChild,value)    #实际删除的是这个后继结点  



    # traverse
    def preorder(self,root):
        if root==None:
            return []
        else:
            result=[root]
            left=self.preorder(root.leftChild)
            right=self.preorder(root.rightChild)
            return left+result+right

    def traverse(self):  # 层次遍历
        if self.root is None:
            return []
        q = [self.root]
        res = [self.root.value]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.leftChild is not None:
                q.append(pop_node.leftChild)
                res.append(pop_node.leftChild.value)

            if pop_node.rightChild is not None:
                q.append(pop_node.rightChild)
                res.append(pop_node.rightChild.value)
        return res

        



t=Tree()
t.insert(2)
t.insert(1)
# t.insert(5)
t.insert(6)
t.insert(5)
t.insert(7)
t.insert(4)

# r=t.preorder(t.root)
# for item in r:
#     item.showNodeInfo()


print(t.traverse())
t.delete(t.root,1)

print(t.traverse())



