from django.shortcuts import render
from django.core.mail import send_mail
from dentist.settings import EMAIL_HOST_USER
# Create your views here.
def home(request):
	return render(request,'home.html',{})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        #sending email
        send_mail(
			'Message From '+message_name,
			message,
			EMAIL_HOST_USER,
			[message_email]
		)
        
        return render(request,'contact.html',{'message_name':message_name})
    else:
        return render(request,'contact.html',{})


def pricing(request):
    return render(request,'pricing.html',{})

def servicing(request):
    return render(request,'service.html',{})

def about(request):
    return render(request,'about.html',{})

def blog(request):
    return render(request,'blog.html',{})


def blog_details(request):
    return render(request,'blog-details.html',{})

def appointment(request):
    if request.method == 'POST':
        name = request.POST['your-name']
        phone = request.POST['your-phone']
        email = request.POST['your-email']
        address = request.POST['your-address']
        schedule = request.POST['your-scheldule']
        time = request.POST['your-time']
        message = request.POST['your-message']
        
        appointment = 'Mr/Mrs/Miss ' + name + ' who lives at ' + address + ', has asked for an appointment with you on '+ schedule +' between '+ time +'.\n He has send this messsage for you\n\t\"'+ message + '\" \nYou May Contact them at '+phone +' or ' + email
        send_mail(
			'Appointment Request From '+name,
			appointment,
			EMAIL_HOST_USER,
			[email]
		)
        return render(request,'appointment.html',{'your_schedule':schedule,'name':name,'time':time})
    else:
        return render(request,'home.html',{})