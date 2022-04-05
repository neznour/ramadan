from django import forms
from django.forms import ModelForm
from  .models import Venue, Event
from .models import MyUser



# Admin SuperUser Event Form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'manager': 'Manager',
			'attendees': 'Attendees',
			'description': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


#Creat a event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields= ('name', 'event_date', 'venue',  'attendees','description' )
        labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD',
			'venue': 'Venue',
			'manager': 'Manager',
			'attendees': 'Attendees',
            'description': '',	
        }

        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
                    'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'event_date'}),
                    'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'venue'}),
                    'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'manager'}),
                    'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'attendees'}),
                    'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}),
                }

#Creat a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields= ('name', 'address', 'zip_code', 'phone','web', 'email_address', 'venue_image')
        labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',
            'venue_image':'',
        }

        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
                    'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
                    'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
                    'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
                    'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
                    'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                }


class UserForm(ModelForm):
    class Meta:
        model=MyUser
        fields=('first_name','last_name', 'email', 'subject', 'message')
        labels = {
			'first_name': '',
            'last_name': '',
			'email': '',
            'subject':'',
            'message':'',	
        }
        widgets ={
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name (required)'},),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Your Last Name(required)'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email (required)'}),
            'subject': forms.Textarea(attrs={'class':'form-control', 'rows':"3", 'placeholder':'Your Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'}),

    }
