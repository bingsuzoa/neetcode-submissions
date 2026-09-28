# length 10000 O(N) 가능 O(N^2)불가

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = set()
        opers.add('*')
        opers.add('+')
        opers.add('-')
        opers.add('/')

        for token in tokens :
            if not token in opers :
                stack.append(int(token))
            else :
                right = stack.pop()
                left = stack.pop()

                if token == '+' :
                    stack.append(left + right)
                elif token == '*' :
                    stack.append(left * right)
                elif token == '/' :
                    stack.append(int(left / right))
                else :
                    stack.append(left - right)
        return stack[-1]
        