from flask import current_app, render_template
from threading import Thread
from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    # msg = Message('测试邮件',
    #               sender='924461845@qq.com',
    #               body='test',
    #               recipients=['924461845@qq.com'])
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    # 取 flask 真实对象，而不是 current_app 只是 app_context 的栈顶
    app = current_app._get_current_object()
    t = Thread(target=send_async_email, args=[app, msg])
    t.start()
    return t