from django.shortcuts import get_object_or_404, redirect, render

from meetings.forms import MeetingForm
from meetings.models import Meeting, Room


# def detail(request, id):
#     meeting = Meeting.objects.get(pk=id)
#     return render(request, "meetings/detail.html", {"meeting": meeting})

# def detail(request, id):
#     meeting = get_object_or_404(Meeting, id)
#     return render(request, "meetings/detail.html", {"meeting": meeting})


def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings

    return render(request, 'meetings.html', {'meetings': meetings, })


def detail(request, id):

    meeting = get_object_or_404(Meeting, id=id)  

    return render(request, "details.html", {"meeting": meeting})


def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('meetings_list_view')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'new.html', {'form': form})

 

def room_list_view(request):

    rooms = Room.objects.all()  # Get all meetings

    return render(request, 'rooms_list.html', {'rooms': rooms, })


def room_detail(request, id):

    room = get_object_or_404(Room, id=id)  

    return render(request, "room_detail.html", {"room": room})

