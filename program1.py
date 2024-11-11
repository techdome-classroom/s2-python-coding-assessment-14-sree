class Solution(object):
    def isValid(self, s):
         stack = []
    
         bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        # Iterate through each character in the input string
         for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack (or use a dummy value if stack is empty)
                top_element = stack.pop() if stack else '#'
                # Check if the popped element is the matching opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched
         return not stack 
pass







    



  

