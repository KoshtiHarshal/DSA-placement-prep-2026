# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid(s):
    n = len(s)
    if n % 2 == 1:
        return False

    st = []

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            st.append(ch)

        else:
            if len(st) == 0:
                return False
            
            top = st.pop()

            if ch == ')' and top != '(':
                return False
            elif ch == '}' and top != '{':
                return False
            elif ch == ']' and top != '[':
                return False

    if len(st) == 0:
        return True
    else:
        return False

# Test your string
s = "()[]{"
print(is_valid(s))

# Time Complexity = O(N)
# Space Complexity = O(N)