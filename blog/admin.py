from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customizes the admin panel view for the :model:`blog.Post`
    model.

    **Fields**
    ``title``
        A character field containing the title of the post.
    ``slug``
        A character field containing the slug of the post.
    ``author``
        A foreign key to the :model:`auth.User` model.
    ``updated_on``
        A date and time field containing the date and time the post was last updated.
    ``content``
        A text field containing the content of the post.
    ``status``
        A choice field containing the status of the post.
    ``created_on``
        A date and time field containing the date and time the post was created.

    **Methods**
    ``__str__``
        Returns a string representation of the model instance.

    **Template:**
    :template:`admin/blog/post/change_form.html`

    """
    

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
