from celery import shared_task
from datetime import timedelta
from news.models import Post, Category
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def post_publication(pk):
    post = Post.objects.get(pk=pk)
    emails = User.objects.filter(
            subscriptions__category__in=post.category.all()
            ).values_list('email', flat=True)
    categories = ','.join([i.category_name for i in post.category.all()])
    subject = f'Новая запись в категории {categories}'

    text_content = (
            f'Опубликована {post.heading}\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000{post.get_absolute_url()}'
        )
    html_content = (
        f'Опубликована {post.heading}<br><br>'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'Посмотреть публикацию:</a>'
        )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()



@shared_task
def friday_send():
    current_date = timezone.now()
    prev_send = current_date - timedelta(days=7)
    new_posts = Post.objects.filter(publication_time__gte=prev_send)
    categories = set(new_posts.values_list('category__category_name', flat=True))
    subscribers = set(
        Category.objects.filter(category_name__in=categories).values_list('subscriptions__user__email', flat=True))
    html_content = render_to_string(
        'weekly_send.html',
        {
            'link': settings.SITE_URL,
            'posts': new_posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Новые публикации за прошедшую неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()