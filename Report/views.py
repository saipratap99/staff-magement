from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddStaffForm
from .models import Staff

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
  return render(request,'Report/staff_form.html',{'form':form})

def send_email_to_manager(request):
  return render(request,'Report/send_email.html',{})
