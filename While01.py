def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    ans = 0
    while idx<len(s):
        ans+=s[idx].isdigit()
        idx+=1

    return ans
print(main("pyth125on2022"))