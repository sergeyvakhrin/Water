from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(ModelForm):
    """ Класс создания формы пользователя """
    class Meta:
        model = User
        fields = ['phone', 'email', 'password']

    def __init__(self, *args, **kwargs):
        """ Меняем password на Пароль """
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'


class UserProfileForm(UserChangeForm):
    """ Класс создания формы для просмотра деталей профиля пользователя """

    class Meta:
        model = User
        fields = ['phone', 'email', 'password']

    def __init__(self, *args, **kwargs):
        """
        Вводим ограничения на редактирование полей:
        password Что бы скрыть в форме "Пароль не задан"
        """
        super().__init__(*args, **kwargs)
        user = kwargs.get('instance')

        self.fields['password'].widget = forms.HiddenInput()


class MyAuthenticationForm(AuthenticationForm):
    """ Все ради слова Пароль при авторизации """

    def __init__(self, *args, **kwargs):
        """ Меняем password на Пароль """
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'
