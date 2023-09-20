from django.core.mail import send_mail
print('import etdim waska')
send_mail('Django mail',
        'This e-mail was sent with Django.',
        'hashiflame@gmail.com',
        ['hashiflame@gmail.com', 'qwertostar122@gmail.com', 'koroisdead@gmail.com'],
        fail_silently=False)