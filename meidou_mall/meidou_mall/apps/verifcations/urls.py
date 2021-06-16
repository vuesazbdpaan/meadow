from django.conf.urls import url

from . import  views

url(r'^sms_codes/(?p<mobile>1[3-9]\d{9}))/$',views.SmSCodeview.as_view())
