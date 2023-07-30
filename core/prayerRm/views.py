from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import PrayerRm

# Create your views here.

# prayer group
def create_prayerRm(request):
    user = request.user
    if request.method == 'POST':
        form_data =dict(request.POST)
        group_name = form_data['group_name']
        prayer_rm = PrayerRm(name=group_name, admin=user)
        prayer_rm.save()
        
        return HttpResponse(request,'Created group successfully')

def view_prayerRm(request,rm_id):
    group = get_object_or_404(PrayerRm, id = rm_id)
    return JsonResponse(group, safe=False)

def edit_prayerRm(request, rm_id):
    pass

def delete_prayerRm(request, rm_id):
    group = get_object_or_404(PrayerRm, id = rm_id)
    group.delete()
    
    return HttpResponse(request,'done')


# prayer group admin
def add_admin(user_id, group_id):
    pass

def view_admin(group_id):
    pass

def remove_admin(user_id, group_id):
    pass

# prayer_group participants
def add_participant(user_id, group_id):
    pass

def view_participants(user_id, group_id):
    pass

def remove_participants(user_id, group_id):
    pass
