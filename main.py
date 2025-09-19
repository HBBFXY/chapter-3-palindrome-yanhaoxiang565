# 获取用户输入并去除前后空格
input_str = input().strip()

# 检查输入是否为5位且全为数字
if len(input_str) != 5 or not input_str.isdigit():
    print("错误")
else:
    # 反转字符串并与原字符串比较
    if input_str == input_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
