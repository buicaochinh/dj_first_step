from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  fieldsets = [
      ('Question Text',               {'fields': ['question_text']}),
      ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]
  list_filter = ['pub_date']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
