from django.urls import path



from diary.views import HomeView, DiaryEntryList, DiaryEntryCreateView, DiaryEntryUpdateView, DiaryEntryFormDetailView

app_name = 'diary'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('diarylist/', DiaryEntryList.as_view(), name='diary_list'),
    path('diarycreatelist/', DiaryEntryCreateView.as_view(), name='diary_create'),
    path('diary/update/<int:pk>', DiaryEntryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>', DiaryEntryFormDetailView.as_view(), name='diary_detail'),
]