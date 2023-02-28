from django.core.mail import EmailMessage
class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['subject'], body=data['email_body'], to=[data['email_to']])
        email.send(fail_silently=False)