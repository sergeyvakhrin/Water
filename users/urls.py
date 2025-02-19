from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, MyLoginView, logout_view, UserProfileView, UserDetailView, UserListView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/<int:pk>/view', UserDetailView.as_view(), name='user_detail'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
]
