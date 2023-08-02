class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        parentheses = {")" : "(", "]": "[", "}": "{"}
        closing_parentheses = set(parentheses.keys())
        opening_parentheses = set(parentheses.values())
        for char in s:
            if char in opening_parentheses:
                stack.append(char)
            else:
                if not stack:
                    return False
                stack_top = stack.pop()
                if stack_top != parentheses[char]:
                    return False

        if stack:
            return False
        return True

