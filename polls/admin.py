from django.contrib import admin

# Register your models here.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('日期', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)

