# def sortedInsert(s,elem):
#     if len(s)==0 or elem <s[-1]:
#         s.append(elem)
#         return
#     else:
#         temp=s.pop()
#         sortedInsert(s,elem)
#         s.append(temp)


# def sortStack(s):
#     if len(s) !=0:
#         # remove the element from last 
#         temp=s.pop()
#         # here it is recursively called unless stack became empty
#         sortStack(s)
#         # push item if prev > than current
#         sortedInsert(s,temp)
#         # print(s)
#     return s
# x=sortStack([-3,14,18,-5,30])
# print(x)
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        if len(s)!=0:
            temp=s.pop()
            self.sorted(s)
            self.sortStack(s,temp)
        return s
                
    def sortStack(self,s,elem):
        if len(s)==0 or elem<s[-1]:
            s.append(elem)
            return
        else:
            temp=s.pop()
            self.sortStack(s,elem)
            s.append(temp)

ob=Solution()
x=ob.sorted([3,1,3,2])
print(x)
