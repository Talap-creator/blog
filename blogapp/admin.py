from django.contrib import admin
from .models import BlogPost
from django_ckeditor_5.fields import CKEditor5Widget


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'short_description', 'created_at', 'updated_at')
    search_fields = ('title', 'category','content', 'short_description')
    fields = ('title', 'category','content', 'short_description','image')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=CKEditor5Widget())
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(BlogPost, BlogPostAdmin)
