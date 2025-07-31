from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for the About model, using Summernote for rich text editing.
    """

    summernote_fields = ('content',)