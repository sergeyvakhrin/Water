from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from users.forms import UserRegisterForm, MyAuthenticationForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """ Контроллер регистрации новых пользователей """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)


class MyLoginView(LoginView):
    """ Все ради слова Пароль при авторизации """
    form_class = MyAuthenticationForm


def logout_view(request):
    """ Функция для кастомного выходы из сервиса """
    logout(request)
    return redirect('/')


class UserProfileView(LoginRequiredMixin, UpdateView):
    """ Класс для просмотра и редактирования профиля пользователя """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(LoginRequiredMixin, DetailView):
    """ Контроллер для отображения данных поставщика """
    model = User


class UserListView(LoginRequiredMixin, ListView):
    """ Контроллер получения списка клиентов """
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """ Контроллер обновления пользователей """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_list')
