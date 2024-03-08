from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'text',
            'category',
            'author'
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 5:
            raise ValidationError({"text": "Содержание должно быть больше 5 слов."})
        heading = cleaned_data.get("heading")
        if heading == text:
            raise ValidationError("Содержание должно отличаться от заголовка.")

        return cleaned_data
