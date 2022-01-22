from flask_admin.contrib.sqla import ModelView


class CommentView(ModelView):
    column_labels = {
        'name': 'Имя комментария'
    }
    can_delete = True
    can_create = True
    can_edit = True
