def main():
    # 获取输入
    input_str = input().strip()
    
    # 检查是否为5位纯数字
    if not input_str.isdigit():
        print("输入错误，请输入一个5位数字")
        return
        
    if len(input_str) != 5:
        print("输入错误，请输入一个5位数字")
        return
        
    # 检查回文数
    if input_str == input_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

if __name__ == "__main__":
    main()
