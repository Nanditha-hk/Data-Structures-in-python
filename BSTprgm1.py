n=int(input())
nums=list(map(int,input().split()))
k=int(input())
class TreeNode:
    def _init_(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
def fillInorder(inorder,root) :
    if root == None:
        return 
 
    fillInorder(inorder,root.left)
    inorder.append(root.data)
    fillInorder(inorder,root.right)



root = None 
for ele in nums:
    root = insertIntoBST(root, ele)
    inorder = []
    fillInorder(inorder,root)
print(inorder[k-1])
