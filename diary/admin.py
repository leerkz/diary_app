from django.contrib import admin
from diary.models import DiaryEntry

# Register your models here.
@admin.register(DiaryEntry)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'content', 'created_at')
    list_filter = ('title', 'content',)
    search_fields = ('title', 'content')