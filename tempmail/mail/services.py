# mail/services.py

'''import requests


class EmailService:
    BASE_URL = 'https://www.1secmail.com/api/v1/'

    @staticmethod
    def get_domains():
        response = requests.get(f'{EmailService.BASE_URL}?action=getDomainList')
        return response.json()

    @staticmethod
    def get_messages(domain, login):
        response = requests.get(f'{EmailService.BASE_URL}?action=getMessages&login={login}&domain={domain}')
        return response.json()

    @staticmethod
    def get_message_content(domain, login, message_id):
        response = requests.get(f'{EmailService.BASE_URL}?action=readMessage&login={login}&domain={domain}&id={message_id}')
        message = response.json()
        attachments = message.get('attachments', [])
        for attachment in attachments:
            file_response = requests.get(f'{EmailService.BASE_URL}?action=download&login={login}&domain={domain}&id={message_id}&file={attachment["filename"]}')
            attachment['file_content'] = file_response.content
        return message
'''
# mail/services.py
import requests

class EmailService:
    BASE_URL = 'https://www.1secmail.com/api/v1/'

    @staticmethod
    def get_domains():
        response = requests.get(f'{EmailService.BASE_URL}?action=getDomainList')
        return response.json()

    @staticmethod
    def get_messages(domain, login):
        response = requests.get(f'{EmailService.BASE_URL}?action=getMessages&login={login}&domain={domain}')
        return response.json()

    @staticmethod
    def get_message_content(domain, login, message_id):
        response = requests.get(f'{EmailService.BASE_URL}?action=readMessage&login={login}&domain={domain}&id={message_id}')
        message = response.json()
        attachments = message.get('attachments', [])
        for attachment in attachments:
            file_response = requests.get(f'{EmailService.BASE_URL}?action=download&login={login}&domain={domain}&id={message_id}&file={attachment["filename"]}')
            attachment['downloadUrl'] = file_response.url  # Store the download URL in the attachment
        return message
