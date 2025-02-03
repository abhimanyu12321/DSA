class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) == 0: return False
                char = stack.pop()
                if char == '(':
                     if i != ')': return False 
                if char == '[':
                    if i != ']': return False
                if char == '{':
                    if i != '}': return False
        return len(stack) == 0
                    
        