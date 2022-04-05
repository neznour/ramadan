from django.contrib import admin
from .models import Venue
from .models import  MyUser
from .models import Event

#It can be like this one down here or with @
#admin.site.register(Venue, VenueAdmin)
admin.site.register(MyUser)
#admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display =('name', 'address','phone' )
    ordering =('name',)
     #for opposite way
     # ordering =('-name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date','description','manager', 'approved')  
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date',)
    ordering = ('event_date', )