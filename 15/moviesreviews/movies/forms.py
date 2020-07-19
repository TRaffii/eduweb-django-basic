from django.forms import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',
            'text',
            'movie'
        ]
