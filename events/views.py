from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, MyUser, Venue
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import VenueForm, EventForm, EventFormAdmin
from .forms import UserForm
from django.http import HttpResponse
from django.contrib import messages

# Import Pagination Stuff
from django.core.paginator import Paginator



def about_us(request) :
    return render(request, 'events/aboutus.html', {
    })
  

def library(request):
          return render(request, 'events/library.html', {
    })
  

 #Generate Text File Event list
def event_text(request):
    response = HttpResponse(content_type= 'text/plain')
    response['Content-Disposition']='attachment;filename=events.txt'
    #Designate The Model
    events = Event.objects.all()

    #Creat blank list
    lines=[]

    #Loop Throu and Output


    for event in events:
        lines.append(f'{event.name}\n{event.event_date}\n{event.venue}\n{event.description}\n\n')

    response.writelines(lines)
    return response

def pray_time(request):    
    
    
      return render(request, 'events/praytime.html', {
    })


# Delete an Event
def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user == event.manager:
		event.delete()
		messages.success(request, ("Event Deleted!!"))
		return redirect('list-events')		
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Event!"))
		return redirect('list-events')	




def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_event?submitted=True')	
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_event?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event )
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {
     'event': event,
     'form': form   
    })    

def search_events(request):
	if request.method == "POST":
		searched = request.POST['searched']
		events = Event.objects.filter(description__contains=searched)
	
		return render(request, 
		'events/search_events.html', 
		{'searched':searched,
		'events':events})
	else:
		return render(request, 
		'events/search_events.html', 
		{})
        
def add_venue(request):
    submitted = False
    if request.method =="POST":
        form=VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit = False)
            venue.owner = request.user.id #logged in user
            venue.save()
            #form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form =VenueForm
        if 'submitted'in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted
    })

def add_info(request):
    submitted = False
    if request.method =="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_info?submitted=True')

    else:
        form =UserForm
        if 'submitted'in request.GET:
            submitted = True


    return render(request, 'events/add_info.html', {'form': form, 'submitted':submitted
    })

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venues')

	return render(request, 'events/update_venue.html', 
		{'venue': venue,
		'form':form})

def all_events(request):
    event_list = Event.objects.all().order_by('-event_date')
    return render(request, 'events/event_list.html', {
        "event_list": event_list
    })
def list_venues(request):
	#venue_list = Venue.objects.all().order_by('?')
	venue_list = Venue.objects.all()

	# Set up Pagination
	p = Paginator(Venue.objects.all(), 3)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" * venues.paginator.num_pages
	return render(request, 'events/venue.html', 
		{'venue_list': venue_list,
		'venues': venues,
		'nums':nums}
		)

# Create My Events Page
def my_events(request):
	if request.user.is_authenticated:
		me = request.user.id
		events = Event.objects.filter(manager=me)
		return render(request, 
			'events/my_events.html', {
				"events":events
			})

	else:
		messages.success(request, ("You Aren't Authorized To View This Page"))
		return redirect('home')

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request, 'events/show-venue.html', 
		{'venue': venue,
		'venue_owner':venue_owner})

# Delete a Venue
def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('list-venues')		


def donation(request):    
      return render(request, 'events/donation.html', {
    })



def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "ER"
	month = month.capitalize()
	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(
		year, 
		month_number)
	# Get current year
	now = datetime.now()
	current_year = now.year
	
	# Query the Events Model For Dates
	event_list = Event.objects.filter(
		event_date__year = year,
		event_date__month = month_number
		)

	# Get current time
	time = now.strftime('%I:%M %p')
	return render(request, 
		'events/home.html', {
		"name": name,
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal": cal,
		"current_year": current_year,
		"time":time,
		"event_list": event_list,
		})

    
