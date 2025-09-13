num_input = input("请输入一个5位数字：")
if len(num_input) != 5 or not num_input.isdigit():
    print("输入错误，必须输入一个5位数字")
else:
    if num_input == num_input[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
