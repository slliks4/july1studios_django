from django.contrib import admin
from .models import First_slide,Gallery_slide,Event_slide,Our_service,Comments

admin.site.register(First_slide)
admin.site.register(Gallery_slide)
admin.site.register(Event_slide)
admin.site.register(Comments)
admin.site.register(Our_service)
admin.site.site_header="July First Studio"
admin.site.site_title="July First Studio"
admin.site.index_title="Administrator"