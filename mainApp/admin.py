from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'posted_date')

admin.site.register(Question,QuestionAdmin)