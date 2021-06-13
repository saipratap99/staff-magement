from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('staff/',views.staff_list,name='staff-list'),
  path('staff/new/',views.staff_create,name='staff-create'),
  path('send_email/',views.send_email_to_manager,name='send-email')
]
