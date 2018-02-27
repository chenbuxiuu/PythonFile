
import random
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

    # search parent node
    def search_parent(self,parent,k):
        if parent==None:
            return False,None
        if (parent.leftChild!=None and parent.leftChild.value==k) or (parent.rightChild!=None and parent.rightChild.value==k):
            return True,parent
        elif parent.value<k:
            return self.search_parent(parent.rightChild,k)
        elif parent.value>k:
            return self.search_parent(parent.leftChild,k)




    # insert node to tree
    def insert(self,value,root):
        if not isinstance(value, Node):
            node= Node(value)
        if self.root==None:
            self.root=node
            root=self.root
            return root
        if root==None:
            root=node
        else :
            if value<root.value:
                root.leftChild=self.insert(value,root.leftChild)
            else:
                root.rightChild=self.insert(value,root.rightChild)
        return root

    # find min
    def findmin(self,node):  
        if node.leftChild!=None:  
            return self.findmin(node.leftChild);  
        else:  
            return node; 



    # delete node
    def delete(self,k):
        # delete ndoe is root
        if k==self.root.value:
            if self.root.rightChild!=None:
                tmp=self.findmin(self.root.rightChild)
            self.delete(tmp.value)
            self.root.value=tmp.value      
        else:
            # find the target node
            f,node=self.search(self.root,k)
            # find the target node's parent
            pf,pnode=self.search_parent(self.root,k)
            if f and pf:
                # 删除node没有左子树
                if node.leftChild is None:
                    if pnode.value<node.value:
                        pnode.rightChild=node.rightChild
                    else:
                        pnode.leftChild=node.rightChild
                # 删除node没有右子树
                elif node.rightChild is None:
                    if pnode.value<node.value:
                        pnode.rightChild=node.leftChild
                    else:
                        pnode.leftChild=node.leftChild
                # 删除node有左右子树
                else:
                    tmp=self.findmin(node.rightChild)
                    self.delete(tmp.value)
                    node.value=tmp.value


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
        
        level=[self.root.value]
        while q != []:
            for ii in range(len(q)):
                pop_node = q.pop(0)
                res = []
                if pop_node.leftChild is not None:
                    q.append(pop_node.leftChild)
                    res.append(pop_node.leftChild.value)

                if pop_node.rightChild is not None:
                    q.append(pop_node.rightChild)
                    res.append(pop_node.rightChild.value)
                level.append(res)
        print('print Tree by level+++++++++++++++++++++++++')
        for tlevel in level:
            print(tlevel)
        print('end Tree------------------------------------')
        return level


        

if __name__ == '__main__':

    t=Tree()

    array=[]
    for ii in range(100):
        array.append(ii)
    # print(array)


    # tree_array=random.sample(array,10)
    tree_array=[75,97,26,18,66,88,5,55,72,32]
    print(tree_array)


    # t.root=Node(12)
    for ii in tree_array:
        t.insert(ii,t.root)

    r=t.preorder(t.root)
    for item in r:
        item.showNodeInfo()

    t.traverse()
    delt=tree_array[4]
    print(delt)
    t.delete(delt)
    t.traverse()
# level=t.traverse()

    # for node in tlevel:
    #     print(ndoe)
# print(level)
# t.delete(2)

# t.traverse()






