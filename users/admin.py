from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу пользователей """
    list_display = ['id','phone', 'email']
    list_display_links = list_display

    save_on_top = True

    def save_model(self, request, obj, form, change):
        """ Хэшируем пароль """
        if "password" in form.changed_data:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)



