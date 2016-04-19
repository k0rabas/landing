from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from .models import SignUp

def home(request):
    title = "Sign Up"
    form = SignUpForm(request.POST or None)
    context = {
        'title' : title,
        'form' : form,
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        # grab the raw unprocessed post data - not recommended!
        # full_name = request.POST['full_name']

        #  field postprocessing variant
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = "Anonynous full name"
        instance.full_name = full_name

        context = {
            'title' : "Thank you"
                   }
        
        instance.save()
    
    if request.user.is_authenticated() and request.user.is_staff:
#         counter = 1
#         for i in SignUp.objects.all():
#             print(counter,i.full_name)
#             counter += 1
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            'queryset' : queryset,
        }
    
    return render(request, "home.html", context)

def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    context = {
        'form' : form,
        'title' : title,
    }
    if form.is_valid():
        # iterate through many form fields
        # for key in form.cleaned_data:
        #    print("\n",key)
        #    print(form.cleaned_data.get(key))

        # postprocess fields one by one
        form_full_name = form.cleaned_data.get('full_name')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        # print(full_name,email,message)
        subject = 'Email contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'dmitrydyatel@gmail.com']
        contact_message = """
        %s: %s via %s
        """ %(form_full_name, form_message, form_email)
        my_html_message="""
        <h1>Big Header</h1>
        <h3>%s: %s via %s</h3>
        """ %(form_full_name, form_message, form_email)
        send_mail(subject,
            contact_message,
            from_email,
            to_email,
            html_message=my_html_message,
            fail_silently=False)

            
    return render(request, "forms.html", context)












