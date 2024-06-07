def remove_consecutive_k(s, k):
    # Helper function to find and remove consecutively occurring characters
    def helper(s, k):
        n = len(s)
        if n < k:
            return s
        
        i = 0
        new_s = ""
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            
            if j - i != k:  # if the length of consecutive characters is not k
                new_s += s[i:j]
            
            i = j
        
        return new_s
    
    # Recursively remove consecutive characters occurring exactly k times
    new_s = helper(s, k)
    if new_s == s:
        return new_s
    else:
        return remove_consecutive_k(new_s, k)

def str_count(str,k):
    for char in str:
        if 
        


# Test the function
str1 = "abcccbdddbda"
k = 3
print(str_count(str1, k)) 
"""i = 0
print(len(str1))
while i <= len(str1)-k:
    nstr = str1[i:i+k]
    i+=1
    print(nstr)"""