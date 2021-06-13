from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddStaffForm,SendEmailForm
from .models import Staff
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
  return render(request,'Report/home.html',{})


def staff_list(request):
  staff = Staff.objects.all().order_by('staff_id')
  return render(request,'Report/staff_index.html',{'staff':staff})

def staff_create(request):
  form = AddStaffForm()
  if(request.POST):
    form = AddStaffForm(request.POST)
    if form.is_valid():
      staff = form.save()
      messages.success(request,f'New staff added {staff.staff_name}')
      return redirect('home')
    else:
      messages.error(request,f'Error while adding staff')
  return render(request,'Report/staff_form.html',{'form':form})

def send_email_to_manager(request):
  form = SendEmailForm()
  if(request.POST):
    form = SendEmailForm(request.POST)
    if(form.is_valid()):
      remail = [form.cleaned_data.get('email')]
      staff_details = Staff.getDetails()
      semail = settings.EMAIL_HOST_USER
      send_mail("Staff details",staff_details,semail,remail)
      messages.success(request,f'Email sent to {remail}')
      return redirect('home')
    else:
      messages.error(request,f'Error while sending')
  return render(request,'Report/send_email.html',{'form':form})
