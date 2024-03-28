"""from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if kwargs['action'] != 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__category__in=instance.category.all()
        ).values_list('email', flat=True)
    categories = ','.join([i.category_name for i in instance.category.all()])
    subject = f'Новая запись в категории {categories}'

    text_content = (
        f'Опубликована {instance.heading}\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
    html_content = (
        f'Опубликована {instance.heading}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Посмотреть публикацию:</a>'
        )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()"""
