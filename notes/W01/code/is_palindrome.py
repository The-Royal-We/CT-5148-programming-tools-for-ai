def is_palindrome(s):
    return s == s[::-1] # notice we don't need if here, just return the result
                        # of the == test directly, it is a bool

def is_palindrome_bad(s):
    return s == reversed(s) # doesn't work as reversed() returns a generator

def is_palindrome2(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]: # eg, if s[0] == s[-1], compare first and last chars
            return False
    return True # notice that return False is inside the if, inside the for.
                # whereas return True is outside the for.

def is_palindrome2_bad(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i]: # this fails, because when i == 0, s[-i] is s[0]
            return False
    return True # notice that return False is inside the if, inside the for.
                # whereas return True is outside the for.
    
def is_palindrome3(s): # recursive function
    if len(s) <= 1: return True # one base case
    if s[0] != s[-1]: return False # another base case
    return is_palindrome3(s[1:-1]) # recursive case


def tests():
    p1 = "abccba"
    p2 = "abcdcba"
    q1 = "abcdefg"

    for fn in [is_palindrome, is_palindrome_bad,
               is_palindrome2, is_palindrome2_bad,
               is_palindrome3]:
        for s in [p1, p2, q1]:
            print(fn.__name__, s, fn(s))
    
if __name__ == "__main__":
    tests()
