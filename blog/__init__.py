from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
babel = Babel()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    babel.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from blog.routes import MyMainView
    from models import User, Post, Tag, Comment, Storage
    from blog.views.user_view import UserView
    from blog.views.post_view import PostView
    from blog.views.tag_view import TagView
    from blog.views.comment_view import CommentView
    from blog.views.storage_view import StorageView

    from blog.routes import MySignInView, MyLoginView, MyAccountView, MyExitView, MyMainView

    admin = Admin(app, 'Mike do IT', base_template='admin/change_brand.html', index_view=MyMainView(),
                  template_mode='bootstrap4', url='/')
    admin.add_view(MySignInView(name='Регистрация', url='register'))
    admin.add_view(MyLoginView(name='Логин', url='login'))
    admin.add_view(MyAccountView(name='Аккаунт', url='account'))
    admin.add_view(UserView(User, db.session, name='Пользователь', category='Админка', endpoint='admin/user'))
    admin.add_view(PostView(Post, db.session, name='Посты', category='Админка', endpoint='admin/post'))
    admin.add_view(TagView(Tag, db.session, name='Тэги', category='Админка', endpoint='admin/tag'))
    admin.add_view(CommentView(Comment, db.session, name='Комментарии', category='Админка', endpoint='admin/comment'))
    admin.add_view(StorageView(Storage, db.session, name='Файловая помойка'))
    admin.add_view(MyExitView(name='Выход', url='exit'))
    return app
