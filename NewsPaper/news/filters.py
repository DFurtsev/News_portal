from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter, DateTimeFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    heading = CharFilter(lookup_expr='iexact', label='Заголовок')
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Категория', empty_label='Любая')
    publication_time = DateFilter(lookup_expr='gt', widget=DateTimeInput({'type': 'date'}), label='От')

    class Meta:
        model = Post
        fields = {'heading', 'category', 'publication_time'}
