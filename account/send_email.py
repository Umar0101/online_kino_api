from django.core.mail import send_mail

from decouple import config

HOST = config('HOST_FOR_SEND_MAIL')

def send_activation_email(email,activation_code):
    activation_url = f'{HOST}/account/activate/?u={activation_code}'
    message = ""
    html = f"""
<h1> для активации нажмите на кнопку </h1>
<a href="{activation_url}">
<button>Activate</button>
</a>
"""
    send_mail(
        subject=' Активация Аккаунта',
        message=message,
        from_email="a@gmail.com",
        recipient_list=[email],
        html_message=html
    )
