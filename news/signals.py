from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory
from NewsPaper import settings
from django.core.mail import send_mail, EmailMultiAlternatives


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {'text': preview,
         'link': f'{settings.SITE_URL}news/{pk}',

        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers =[s.email for s in subscribers]
        print(subscribers)

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)



