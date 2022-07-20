"""Django's command-line utility for administrative tasks."""

from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)


#  admin.site.register(Choice)
