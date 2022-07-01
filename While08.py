def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    c = 0
    while i<len(s):
        if str(s[i]).isdigit():
            if int(s[i])%2 != 0:
                c += 1
            else:
                c += 0
        i += 1
    return c
print(main("5,3,9,5,8"))