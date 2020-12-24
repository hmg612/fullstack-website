from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from blog_control.user_mgmt import User
from flask_login import login_user, current_user, logout_user
import datetime

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else:
        print('set_email', request.headers)
        # content type이 application/json인 경우에만 request.get_json() 호출 가능
        #print('set_email', request.get_json())
        print('set_email', request.form['user_email'])
        user = User.create(request.form['user_email'], 'A')
        login_user(user, remember=True, duration=datetime.timedelta(
            days=365))  # session/cookie 생성객체

        return redirect(url_for('blog.test_blog'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@blog_abtest.route('/test_blog')
def test_blog():
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        return render_template('blog_A.html')


@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test_blog'))
