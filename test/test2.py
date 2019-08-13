class TestModel:
    def __init__(self, book):
        print('字典中的title: ', book['title'])
        self.title = book['title']
        print('赋值给类变量后的self.title: ', self.title)


a = {'title': '1Q84 BOOK 1'}
b = TestModel(a)
