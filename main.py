def main():
    num = input().strip()
    
    if len(num) != 5:
        print("输入错误，请输入一个5位数字")
        return
        
    for char in num:
        if not char.isdigit():
            print("输入错误，请输入一个5位数字")
            return
            
    # 判断回文
    is_palindrome = True
    for i in range(2):
