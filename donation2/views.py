# supportapp2/donation2/views.py

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from donation2.forms import ContactForm


# Adding views here 
class HomePageView(TemplateView):
    template_name = "index.html"

# class AboutPageView(TemplateView):
#     template_name = "index.html"

class ContactPageView(TemplateView):
    template_name = "contact_success.html"



def contact(request):
    form_class = ContactForm


    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_subject = request.POST.get(
                'contact_subject'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')


    return render(request, 'contact_success.html', {
        'form': form_class,
    })    


