def palindrome(data: str) -> bool:
    return data == data[::-1]

if __name__ == "__main__":
    data = input().strip()
    if palindrome(data):
        print("YES")
    else:
        print("NO")