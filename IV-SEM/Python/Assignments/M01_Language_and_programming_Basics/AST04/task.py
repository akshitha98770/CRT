def Reverse_String(s: str) -> str:
    result = ""
    i = len(s) - 1
    
    while i >= 0:
        result += s[i]
        i -= 1
        
    return result


if __name__ == '__main__':
    s = input().strip()
    print(Reverse_String(s))