class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0

        else:
            insert = 0
            stack = []
            for char in s:
                if char == ")":
                    if not stack:
                        insert+=1

                    else:
                        stack.pop()

                elif char == "(":
                    stack.append(char)

            if stack:
                insert+=len(stack)

            return insert


        