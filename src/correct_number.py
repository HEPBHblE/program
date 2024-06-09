import re

def correct_number(number: str) -> bool:
    clean_number = re.sub(r'[\s()-]', '', number)
    
    if not clean_number.startswith(('8', '+7')):
        return False
    
    if clean_number.startswith('7') and not number.startswith('+7'):
        return False
    
    if (number.startswith('+7') and len(clean_number) != 12) or (number.startswith('8') and len(clean_number) != 11):
        return False
    
    pattern = r"^(\+7|8)?\d{10}$"
    return re.match(pattern, clean_number) is not None

if __name__ == "__main__":
    number = input().strip()
    if correct_number(number):
        print("YES")
    else:
        print("NO")


        