from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, HoleGuide


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('course_name', 'slug', 'author', 'status', 'created_on')
    search_fields = ('course_name', 'slug', 'author__username')
    prepopulated_fields = {'slug': ('course_name',)}
    summernote_fields = ('content',)

# Register your models here.


admin.site.register(HoleGuide)
