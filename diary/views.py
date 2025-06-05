from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.form import DiaryEntryForm, DiaryEntrySearchForm
from diary.models import DiaryEntry


class DiaryEntryList(LoginRequiredMixin, ListView):
    model = DiaryEntry
    template_name = "diary/diary_list.html"
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = DiaryEntry.objects.filter(user=self.request.user)

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        return queryset


class DiaryEntryCreateView(LoginRequiredMixin, CreateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiaryEntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:diary_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DiaryEntryFormDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = DiaryEntry
    template_name = "diary/diary_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DiaryEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiaryEntry
    success_url = reverse_lazy('diary:diary_list')
    template_name = "diary/diary_confirm_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
