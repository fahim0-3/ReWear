from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
 
 

# Register models
admin.site.register(user)
admin.site.register(product)
admin.site.register(main_category)
admin.site.register(branding)
admin.site.register(prize)
admin.site.register(color)
admin.site.register(size)
admin.site.register(billing)
admin.site.register(wishlist)
