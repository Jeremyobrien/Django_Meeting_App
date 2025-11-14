from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.forms import modelform_factory
from .models import Meeting, Room

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms(request):
    allrooms = get_list_or_404(Room)
    return render(request, "meetings/rooms.html", {"rooms":allrooms})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})