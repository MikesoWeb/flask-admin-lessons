import os

from flask import url_for, Markup
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from wtforms import validators
from blog import bcrypt

# 'C:\\Users\\mike\\pythonProject\\NAME_PROJECT'

file_path = os.path.abspath(os.path.dirname(__name__))


# Функция, которая будет генерировать имя файла из модели и загруженного файлового объекта.
def name_gen_image(model, file_data):
    hash_name = f'{model}/{model.username}'
    return hash_name


class UserView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'username': 'Имя пользователя',
        'last_seen': 'Последний вход',
        'image_user': 'Аватар',
        'posts': 'Посты',
        'email': 'Емайл',
        'password': 'Пароль',
        'role': 'Роль',
        'file': 'Выберите изображение'
    }

    # Список отображаемых колонок
    column_list = ['id', 'role', 'username', 'email', 'password', 'last_seen', 'image_user']

    column_default_sort = ('username', True)
    column_sortable_list = ('id', 'role', 'username', 'email')

    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    export_max_rows = 500
    export_types = ['csv']

    form_args = {
        'username': dict(label='ЮЗЕР', validators=[validators.DataRequired()]),
        'email': dict(label='МЫЛО', validators=[validators.Email()]),
        'password': dict(label='ПАРОЛЬ', validators=[validators.DataRequired()]),
    }

    AVAILABLE_USER_TYPES = [
        (u'Админ', u'Админ'),
        (u'Автор', u'Автор'),
        (u'Редактор', u'Редактор'),
        (u'Пользователь', u'Пользователь'),
    ]

    form_choices = {
        'role': AVAILABLE_USER_TYPES,
    }

    # Словарь, где ключ — это имя столбца, а значение — описание столбца представления списка или поля формы добавления/редактирования.
    column_descriptions = dict(
        username='First and Last name'
    )

    # исключенные колонки
    column_exclude_list = ['password']

    column_searchable_list = ['email', 'username']
    column_filters = ['email', 'username']
    column_editable_list = ['role', 'username', 'email']

    create_modal = True
    edit_modal = True

    # Исключить колонку из создания, редактирования
    form_excluded_columns = ['id']

    def _list_thumbnail(view, context, model, name):
        if not model.image_user:
            return ''

        url = url_for('static', filename=os.path.join('storage/user_img/', model.image_user))
        if model.image_user.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')

    # передаю функцию _list_thumbnail в поле image_user
    column_formatters = {
        'image_user': _list_thumbnail
    }

    form_extra_fields = {
        # ImageUploadField Выполняет проверку изображений, создание эскизов, обновление и удаление изображений.
        "image_user": form.ImageUploadField('',
                                            # Абсолютный путь к каталогу, в котором будут храниться файлы
                                            base_path=
                                            os.path.join(file_path, 'blog/static/storage/user_img/'),
                                            # Относительный путь из каталога. Будет добавляться к имени загружаемого файла.
                                            url_relative_path='storage/user_img/',
                                            namegen=name_gen_image,
                                            # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
                                            allowed_extensions=['jpg'],
                                            max_size=(1200, 780, True),
                                            thumbnail_size=(100, 100, True),

                                            )}

    def create_form(self, obj=None):
        return super(UserView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(UserView, self).edit_form(obj)

    def on_model_change(self, view, model, is_created):
        model.password = bcrypt.generate_password_hash(model.password)
