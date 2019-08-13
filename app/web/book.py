import json

from flask import jsonify, request, render_template, flash, make_response
from flask_login import current_user

from app.libs import helper
from models.gift import Gift
from models.wish import Wish
from spider.yushu_book import YuShuBook
from app.web import web
from app.forms.book import SearchForm
from view_models.books import BookCollection, BookViewModel
from view_models.trade import TradeInfo


@web.route('/book/search/')
def search():
    """
        q: 普通关键字 isbn
        page:
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = helper.is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
        # print(json.dumps(books, default=lambda o: o.__dict__))
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('搜索关键词不符合要求，请重新输入')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail/')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes
                           )




# @web.route('/test2/')
# def test():
#     r = {
#         'name': '',
#         'age': 18
#     }
#     flash('max', category='error')
#     flash('hello', category='warning')
#     # 模板 html
#     return render_template('test.html', data=r)

# @web.route('/test1/')
# def test_1():
#     from flask import request
#     from app.libs.none_local import n
#     print(n.v)
#     n.v = 2
#     print('--------')
#     print(getattr(request, 'v', None))
#     setattr(request, 'v', 5)
#     print(request.v)
#     print('----------')
#     return ''


