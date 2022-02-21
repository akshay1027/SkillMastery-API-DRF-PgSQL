from celery import shared_task
from django.core.mail import send_mail
from .models import User
from backend import settings


@shared_task(bind=True)
def sendMailFunc(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"


# import time

# from celery import shared_task

# # Define a new task


# @shared_task
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return True
