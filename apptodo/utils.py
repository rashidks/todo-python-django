from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(user_email):
    subject='sucsefully logined'
    from_mail='muhammedrashidks1@gmail.com'
    recipient_email=[user_email]
    html_content=render_to_string('email.html')
    text_content=strip_tags(html_content)

    message= EmailMultiAlternatives(subject,text_content,from_mail,recipient_email)
    message.attach_alternative(html_content,"text/html")
    message.send()
