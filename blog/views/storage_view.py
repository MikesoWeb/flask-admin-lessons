import datetime
import os
import random

from flask import url_for, Markup
from flask_admin import form
from flask_admin.contrib.sqla import ModelView

file_path = os.path.abspath(os.path.dirname(__name__))
STORAGE = os.path.join(file_path, 'blog/static/storage_file')


class StorageView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'name': 'Имя файла',
        'path': 'Файл',
        'type': 'Тип файла',
        'create_date': 'Дата добавления'
    }

    create_modal = True
    edit_modal = True

    def _list_thumbnail(StorageView, context, model, name):
        if not model.path:
            return ''

        url = url_for('static', filename=os.path.join('storage_file/', model.path))

        if model.type in ['pdf', 'txt', 'doc', 'html']:
            return Markup(f'<a href="{url}" target="_blank">Скачать файл</a>')

        if model.type in ['jpg', 'jpeg', 'png', 'svg', 'gif', 'PNG']:
            return Markup(f'<img src="{url}" width="100">')

        if model.type in ['mp3']:
            return Markup(f'<audio controls="controls"><source src="{url}" type="audio/mpeg" /></audio>')

        if model.type in ['mp4']:
            return Markup(
                f'<video width="200" height="150" controls="controls"><source src="{url}" type="audio/mpeg" /></video>')

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        "file": form.FileUploadField('',
                                     base_path=STORAGE,

                                     )}

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                new_file_name = f'{hash}.{ext}'
                create_date = datetime.datetime.now()

                storage_file.save(
                    os.path.join(STORAGE, new_file_name)
                )

                _form.name.data = _form.name.data or storage_file.filename
                _form.path.data = new_file_name
                _form.type.data = ext
                _form.create_date.data = create_date

                del _form.file

        except Exception as ex:
            pass

        return _form

    def create_form(self, obj=None):
        return self._change_path_data(
            super(StorageView, self).create_form(obj)
        )

    def edit_form(self, obj=None):
        return self._change_path_data(
            super(StorageView, self).edit_form(obj)
        )
