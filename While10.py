def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    c = 0
    while i<len(s):
        if str(s[i]).isdigit():
            if int(s[i]) % 2 == 1:
                c += int(s[i])
        i += 1
    return c
print(main("1236547989"))