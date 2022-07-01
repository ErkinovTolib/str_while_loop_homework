def main(s):
    """
    A variable of type str is given. Find how many lowercase letters
     there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    ans = 0
    while idx<len(s):
        ans += s[idx].islower()
        idx += 1
    return ans
print(main("CodeSchool"))