def generateParenthesis(n):
        def generate(A = []):
            if len(A) == 2*n:
                print(A,"if")
                if valid(A):
                    print(ans)
                    ans.append("".join(A))
            else:
                A.append('(')
                print(A,"else 1")
                generate(A)
                A.pop()
                A.append(')')
                print(A,"else 2")
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans
print('generateParenthesis(3): ', generateParenthesis(3))