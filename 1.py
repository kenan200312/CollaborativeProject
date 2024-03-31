# 假设这是用户数据的示例
users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login(username, password):
    # 检查用户名是否存在
    if username in users:
        # 检查密码是否匹配
        if users[username] == password:
            print("登录成功！欢迎回来，", username)
            return True
        else:
            print("密码错误！请重试。")
            return False
    else:
        print("用户名不存在！")
        return False

# 测试登录功能
username = input("请输入用户名：")
password = input("请输入密码：")
login(username, password)
