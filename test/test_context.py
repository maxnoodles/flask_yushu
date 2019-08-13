# class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('close resource connection')
    #
    # def query(self):
    #     print('query data')

#
# with MyResource() as r:
#     r.query()

# 上下文管理器最大的作用是将一个类变成上下文类
from contextlib import contextmanager
#
#
# @contextmanager
# def make_my_resource():
#     print('connect to resource')
#     yield MyResource()
#     print('close resource connection')
#
#
# # yield 生成器
# with make_my_resource() as r:
#     r.query


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print('心灵的焦灼', end='')