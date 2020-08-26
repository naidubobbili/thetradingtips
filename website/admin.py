from django.contrib import admin
from .models import topic
# Register your models here.

#admin.site.register(topic)

@admin.register(topic)
class topic_admin(admin.ModelAdmin):
    #fields=['Title','Pic','Text','uploaded_on','is_uploaded']
    search_fields=['Title','Text']
    list_display=['Title','is_uploaded','uploaded_on',]
    list_filter=['is_uploaded','uploaded_on']
    #readonly_fields=['COURSE','COLLEGE','REGISTERED']
