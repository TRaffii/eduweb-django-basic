from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs=
                                                   {'placeholder': 'Provide a review title'}))

    class Meta:
        model = Review
        fields = [
            'title',
            'text',
            'movie'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "badword" in title:
            raise forms.ValidationError("You've added a bad word!")
        return title
