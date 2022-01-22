Изучаем flask-admin


Чтобы переопределить поле brand в шаблоне нужно:

1) в admin добавить base_template='admin/change_brand.html'
admin = Admin(app, 'Mike do IT', base_template='admin/change_brand.html', index_view=MyMainView(),
                  template_mode='bootstrap4', url='/')
2) в папке шаблонов admin лежит файл change_brand.html

В этом файле закоментируем или уберем блок brand

<!--                BRAND -->
<!--            {% block brand %}-->
<!--                <a class="navbar-brand" href="{{ admin_view.admin.url }}">{{ admin_view.admin.name }}</a>-->
<!--            {% endblock %}-->

Там же вы можете переопределить и другие блоки или изменить стили меню, к примеру.


На моём  Youtube-канале снято три ролика на тему этого приложения

1) Flask-Admin - что умеет на примере работы с ORM SQLAlchemy / смотрим официальную доку # 0 https://youtu.be/I0wg1f6dizA
2) Flask-Admin - Создаем каркас проекта / админка на flask и пользовательские ModelView # 1 https://youtu.be/Ui3sE1gcJrA
3) Flask-Admin - работа с изображениями / вывод контента в views/ локализация приложения # 2 https://youtu.be/Xj5B6Lhw84Y

Михаил Терехов 2021-2022

