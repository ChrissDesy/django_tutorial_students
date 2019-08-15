from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'saved_date', 'was_added_recently')
    search_fields = ['question_text']


admin.site.register(Student, StudentAdmin)