# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def insert(root,data):
        temp=ListNode(0)
        temp.val=data
        temp.next=root
        root=temp
        return root
class Solution(object):
   
        
        
    def insert(root,data):
        temp=ListNode(0)
        temp.val=data
        temp.next=root
        root=temp
        return root
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=0
        ans=0
        while (l1):
            ans=ans+l1.val*pow(10,i)
            i=i+1
            l1=l1.next
        
        i=0
        ans1=0
        while(l2):
            ans1=ans1+l2.val*pow(10,i)
            i=i+1
            l2=l2.next
        
        ans=(ans+ans1)
        
        temp=[]
        if(ans==0):
            temp.append(0)
        else:
            while(ans>0):
                a=ans%10
                temp.append(a)
                ans=ans//10

        temp.reverse()
        num=len(temp)
        print(temp)
        root=None
        for i in range(0,num):
            root=insert(root,temp[i])
        return root
            
        
        
