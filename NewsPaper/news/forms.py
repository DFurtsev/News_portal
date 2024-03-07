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
        text = cleaned_data.get("description")
        if text is not None and len(text) < 20:
            raise ValidationError({"description": "Содержание должно быть больше 20 слов."})
        heading = cleaned_data.get("heading")
        if heading == text:
            raise ValidationError("Заголовок должен отличаться от названия.")

        return cleaned_data
