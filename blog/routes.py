from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc

from models import Post


class MyMainView(AdminIndexView):
    @expose('/')
    def admin_main(self):
        posts = Post.query.order_by(desc(Post.date)).all()
        image = url_for('static', filename=f'storage/post_img')
        return self.render('admin/index.html', posts=posts, image=image)


class MySignInView(BaseView):
    @expose('/')
    def sing_in(self):
        return self.render('admin/sign_in.html', legend='Регистрация')


class MyLoginView(BaseView):
    @expose('/')
    def login(self):
        return self.render('admin/login.html', legend='Войти')


class MyAccountView(BaseView):
    @expose('/')
    def account(self):
        posts = Post.query.all()
        image = url_for('static', filename=f'storage/post_img')
        return self.render('admin/account.html', posts=posts, image=image)


class MyExitView(BaseView):
    @expose('/')
    def exit(self):
        return redirect(url_for('admin.admin_main'), 302)
