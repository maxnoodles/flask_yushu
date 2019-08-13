import time
import threading
from werkzeug.local import LocalStack


# def work():
#     # 新线程
#     my_obj.b = 5
#     print('in new thread b is: ', my_obj.b)
#

# my_obj = Local()
# my_obj.b = 1
# new_t = threading.Thread(target=work, name='test_thread')
# new_t.start()
# time.sleep(1)
#
# print('in main b is: ', my_obj.b)

my_stack = LocalStack()
my_stack.push(1)
print('main', my_stack.top)


def work():
    print('new thread', my_stack.top)
    my_stack.push(2)
    print('new thread', my_stack.top)


new_t = threading.Thread(target=work, name='new_t')
new_t.start()
time.sleep(0.1)
print('main', my_stack.top)
