
# because of overlapping subproblems we can use dynamic programming to avoid unnecessary function calls
# Dynamic programming solution

result = [-1] * 100

def fibonacci_dp(n):
    if result[n] != -1:
        return result[n]

    result[n] = n if n <= 1 else fibonacci_dp(n - 1) + fibonacci_dp(n - 2)

    return result[n]

n = int(raw_input("enter number to find fibonacci series:"))
fibonacci_dp(n)
print(result[:n])

