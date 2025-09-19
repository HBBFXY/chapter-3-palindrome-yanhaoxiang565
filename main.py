def main():
    try:
        # 从键盘输入
        num_str = input().strip()
        
        # 检查输入是否为5位且为纯数字
        if len(num_str) != 5:
            raise ValueError("输入错误，请输入一个5位数字")
        
        if not num_str.isdigit():
            raise ValueError("输入错误，请输入一个5位数字")
        
        # 检查是否为回文数
        if num_str == num_str[::-1]:
            print("是回文数")
        else:
            print("不是回文数")
            
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
