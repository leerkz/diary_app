from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='diary:diary_list'), name='logout'),

]