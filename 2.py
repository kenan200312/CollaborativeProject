class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.profile = {}

    def update_profile(self, key, value):
        self.profile[key] = value

    def display_profile(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Profile:")
        for key, value in self.profile.items():
            print(f"{key}: {value}")

# 示例用法
if __name__ == "__main__":
    # 创建一个用户对象
    user = User("john_doe", "john@example.com")
    
    # 更新用户资料
    user.update_profile("first_name", "John")
    user.update_profile("last_name", "Doe")
    user.update_profile("age", 30)
    
    # 显示用户资料
    user.display_profile()
