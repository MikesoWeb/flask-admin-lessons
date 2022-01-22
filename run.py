from flask import redirect, url_for
from blog import create_app, db

app = create_app()


@app.route('/')
def main():
    # return redirect('/admin', 302)
    return redirect(url_for('admin.admin_main'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5654)
