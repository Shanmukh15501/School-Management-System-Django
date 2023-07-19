from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
import urllib.request
import urllib.parse

import threading
import logging
from datetime import datetime, date, time

from PIL import Image
import json

log = logging.getLogger(__name__)

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email

    def run(self):
        self.email.send()



class Util:
    @staticmethod
    def send_email(data):
        print("Data",data)
        data['email']=[]
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['email']])
        EmailThread(email).start()




def getcode(model, prefix):
    lastRec = model.objects.last()
    if lastRec:
        nxtId = lastRec.id + 1
    else:
        nxtId = 1
    nxtIdlen = len(str(nxtId))
    if nxtIdlen == 1:
        prenum = '0000'
    elif nxtIdlen == 2:
        prenum = '000'
    elif nxtIdlen == 3:
        prenum = '00'
    elif nxtIdlen == 4:
        prenum = '0'
    else:
        prenum =''
        
    return str(prefix) + str(prenum) + str(nxtId)