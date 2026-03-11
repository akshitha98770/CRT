def count_digits(n: int) -> int:
    n = abs(n)          
    return len(str(n)) 

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))