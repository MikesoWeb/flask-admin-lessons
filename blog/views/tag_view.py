from flask_admin.contrib.sqla import ModelView


class TagView(ModelView):
    column_labels = {
        'name': 'Имя тега',
        'tag_post': 'Посты тега',
    }
    can_delete = True
    can_create = True
    can_edit = True

