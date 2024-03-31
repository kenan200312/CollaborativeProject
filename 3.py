class Dashboard:
    def __init__(self, title):
        self.title = title
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    def display(self):
        print("Dashboard Title:", self.title)
        print("Widgets:")
        for widget in self.widgets:
            widget.display()

class Widget:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def display(self):
        print(f"Widget: {self.name}")
        print("Data:", self.data)

# 示例用法
if __name__ == "__main__":
    # 创建一个仪表盘对象
    dashboard = Dashboard("Main Dashboard")
    
    # 添加一些小部件
    widget1 = Widget("Widget 1", {"value": 10})
    widget2 = Widget("Widget 2", {"value": 20})
    widget3 = Widget("Widget 3", {"value": 30})
    
    dashboard.add_widget(widget1)
    dashboard.add_widget(widget2)
    dashboard.add_widget(widget3)
    
    # 显示仪表盘
    dashboard.display()
