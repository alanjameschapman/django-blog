from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customizes the admin panel view for the :model:`about.About`
    model.

    **Fields**
    ``content``
        A text field containing the content of the about page.

    **Methods**
    ``__str__``
        Returns a string representation of the model instance.

    **Template:**
    :template:`admin/about/about/change_form.html`

    """
    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel view for the :model:`about.CollaborateRequest`
    model.

    **Fields**
    ``message``
        A text field containing the message of the collaboration request.
    ``read``
        A boolean field indicating whether the request has been read.

    **Methods**
    ``__str__``
        Returns a string representation of the model instance.

    **Template:**
    :template:`admin/about/collaboraterequest/change_form.html`

    """

    list_display = ('message', 'read',)