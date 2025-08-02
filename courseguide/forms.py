from django import forms
from .models import HoleGuide


class HoleGuideForm(forms.ModelForm):
    class Meta:
        model = HoleGuide
        fields = (
            'hole_number',
            'name',
            'par',
            'yardage',
            'stroke_index',
            'guide',
            'image',
        )
