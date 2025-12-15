from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/send/', views.message_to_seller, name='message_to_seller'),
    path('contact-admin/', views.contact_admin, name='contact_admin'),
    path('reply/<int:message_id>/', views.reply_message, name='reply_message'),
    path('inbox/', views.inbox, name='inbox'),
]
