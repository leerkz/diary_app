from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, "Ваш email не подтвержден. Пожалуйста, проверьте почту.")
            return HttpResponseRedirect(reverse_lazy("users:login"))  # Перенаправляем обратно на вход
        return super().form_valid(form)
