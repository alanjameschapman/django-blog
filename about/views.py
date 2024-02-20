from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the most recent information on the website author and allows
    requests for collaboration.
    Displays an individual instance of :model:`about.About`
    **Context**
    ''about''
        An instance of :model:`about.About` containing the most recent
        information on the website author.
    ''collaborate_form''
        A form to request collaboration.
    **Template:**
    :template:`about/about.html`
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavor to respond within 2 working days.'
            )

    collaborate_form = CollaborateForm()

    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()


    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form}
    )
