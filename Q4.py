
# coding: utf-8

# In[1]:


# Q4 
#Recursive solution
def fibonacci(n):    
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


# because of overlapping subproblems we can use dynamic programming to avoid unnecessary function calls

# In[2]:


#Dynamic programming solution

result = [-1]*100

def fibonacci_dp(n):
    
    if result[n] != -1:
        return result[n]

    result[n] = n if n <= 1 else fibonacci_dp(n-1) + fibonacci_dp(n-2)
    
    return result[n]


# In[3]:


n = int(raw_input("enter number to find fibonacci series:"))
fibonacci_dp(n)
result[:n]

