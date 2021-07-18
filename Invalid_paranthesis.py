"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        list1 = []
        
        dict1 = {'(':')','{':'}','[':']'}
        was_anything_popped = False

        for i in s:
            print(i)

            if i in dict1.keys():
                list1.append(i)
            else:
                if len(list1) == 0:
                    return False

                elif dict1[list1[-1]] == i:
                    list1.pop()
                    was_anything_popped = True
                else:
                    return False
                
        if was_anything_popped == False:
            return False
        
        elif len(list1) == 0:
            return True
        
        else:
            return False


                