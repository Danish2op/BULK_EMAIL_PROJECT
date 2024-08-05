from django.urls import path
from .views import send_bulk_emails

urlpatterns = [
    path('', send_bulk_emails, name='send_bulk_emails'),
]
