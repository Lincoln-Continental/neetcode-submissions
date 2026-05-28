class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in CloseToOpen: #finding key
                if stack and stack[-1] == CloseToOpen[c]: #stack is not empty and stack top element is in dict 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # add open bracket, we store only open brackets in stack and then removing when find close ones 
        return not stack