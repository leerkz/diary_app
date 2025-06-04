from django.urls import path



from diary.views import HomeView, DiaryEntryList, DiaryEntryCreateView, DiaryEntryUpdateView, DiaryEntryFormDetailView, \
    DiaryEntryDeleteView, DiaryEntrySearchView

app_name = 'diary'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('diarylist/', DiaryEntryList.as_view(), name='diary_list'),
    path('diarycreatelist/', DiaryEntryCreateView.as_view(), name='diary_create'),
    path('diary/update/<int:pk>', DiaryEntryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>', DiaryEntryFormDetailView.as_view(), name='diary_detail'),
    path('diary/delete/<int:pk>', DiaryEntryDeleteView.as_view(), name='diary_delete'),
    path('diary/search/', DiaryEntrySearchView.as_view(), name='diary_search'),
]