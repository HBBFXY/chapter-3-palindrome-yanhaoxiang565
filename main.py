input_str = input().strip()
if len(input_str) != 5 or not input_str.isdigit():
    print("错误")
else:
    if input_str == input_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
