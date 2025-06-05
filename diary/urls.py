from django.urls import path
from diary.views import (
    DiaryEntryList,
    DiaryEntryCreateView,
    DiaryEntryUpdateView,
    DiaryEntryFormDetailView,
    DiaryEntryDeleteView
)

app_name = 'diary'

urlpatterns = [
    path('', DiaryEntryList.as_view(), name='diary_list'),
    path('diary/create/', DiaryEntryCreateView.as_view(), name='diarycreatelist'),
    path('diary/update/<int:pk>/', DiaryEntryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>/', DiaryEntryFormDetailView.as_view(), name='diary_detail'),
    path('diary/delete/<int:pk>/', DiaryEntryDeleteView.as_view(), name='diary_delete'),
]
