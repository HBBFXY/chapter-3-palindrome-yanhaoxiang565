num_str = input("请输入一个5位数字：").strip()

# 输入验证：必须是5位纯数字
if not (len(num_str) == 5 and num_str.isdigit()):
    print("错误提示")
else:
    # 字符串反转判断回文
    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        print("是回文数")
    else:
        print("不是回文数")
代码解析
