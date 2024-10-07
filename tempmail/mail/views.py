from django.shortcuts import render

'''# mail/views.py
from django.core.cache import cache
from django.shortcuts import render
from .services import EmailService

def home(request):
    if request.method == 'POST':
        domain = request.POST.get('domain')
        login = request.POST.get('login')
        messages = EmailService.get_messages(domain, login)
        return render(request, 'inbox.html', {'messages': messages, 'domain': domain, 'login': login})
    
    domains = EmailService.get_domains()
    return render(request, 'home.html', {'domains': domains})

def message_detail(request, domain, login, message_id):
    message = EmailService.get_message_content(domain, login, message_id)
    return render(request, 'message_detail.html', {'message': message})

def inbox(request, domain, login):
    cache_key = f'inbox_{domain}_{login}'
    messages = cache.get(cache_key)
    
    if not messages:
        messages = EmailService.get_messages(domain, login)
        cache.set(cache_key, messages, timeout=60)  # Cache for 60 seconds

    response = render(request, 'inbox.html', {'messages': messages, 'domain': domain, 'login': login})
    
    return response
    '''
# mail/views.py
from django.core.cache import cache
from django.shortcuts import render
from .services import EmailService

def home(request):
    if request.method == 'POST':
        domain = request.POST.get('domain')
        login = request.POST.get('login')
        messages = EmailService.get_messages(domain, login)
        for message in messages:
            message['domain'] = domain
            message['login'] = login
        return render(request, 'inbox.html', {'messages': messages, 'domain': domain, 'login': login})
    
    domains = EmailService.get_domains()
    return render(request, 'home.html', {'domains': domains})

def message_detail(request, domain, login, message_id):
    message = EmailService.get_message_content(domain, login, message_id)
    return render(request, 'message_detail.html', {'message': message})

def inbox(request, domain, login):
    cache_key = f'inbox_{domain}_{login}'
    messages = cache.get(cache_key)
    
    if not messages:
        messages = EmailService.get_messages(domain, login)
        for message in messages:
            message['domain'] = domain
            message['login'] = login
        cache.set(cache_key, messages, timeout=60)  # Cache for 60 seconds

    response = render(request, 'inbox.html', {'messages': messages, 'domain': domain, 'login': login})
    
    return response
