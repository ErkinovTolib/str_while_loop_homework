def main(s):
    import string
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = str(s)
    idx = 0
    ans = 0
    while idx<len(s):
        if s[idx].isalpha() or s[idx].isdigit():
            ans += 0
        else:
            ans += 1
        idx+=1
    return ans
print(main("py,th1%25on2022"))