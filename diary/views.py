from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.form import DiaryEntryForm
from diary.models import DiaryEntry


# Create your views here.

class HomeView(TemplateView):
    template_name = "diary/base.html"


class DiaryEntryList(ListView):
    model = DiaryEntry
    template_name = "diary/diary_list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(user=self.request.user)
        else:
            return DiaryEntry.objects.none()


class DiaryEntryCreateView(LoginRequiredMixin, CreateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:diary_list')

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiaryEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:diary_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DiaryEntryFormDetailView(DetailView):
    model = DiaryEntry
    template_name = "diary/diary_detail.html"


class DiaryEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diary:diary_list')
    template_name = "diary/diary_confirm_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user