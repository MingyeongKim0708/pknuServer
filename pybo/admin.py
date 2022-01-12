from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #제목으로 검색

# Register your models here.
admin.site.register(Question, QuestionAdmin)
