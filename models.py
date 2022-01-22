from blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # use a regular string field, for which we can specify a list of available choices later on
    role = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    image_user = db.Column(db.String(255), nullable=True, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    image_post = db.Column(db.String(255), nullable=True, default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    tags = db.relationship('Tag', backref='tag_post', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.title


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return self.name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return self.name


class Storage(db.Model):
    __tablename__ = 'storage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    path = db.Column(db.String(128))
    type = db.Column(db.String(4))
    create_date = db.Column(db.DateTime)
