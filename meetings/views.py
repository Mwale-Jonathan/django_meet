import os
import time
import json
import random

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

from .forms import MeetingForm
from accounts.models import User
from .models import MeetingMember, Meeting
from agora_token_builder import RtcTokenBuilder


# Create your views here.
@login_required
def room(request, slug):
    meeting = get_object_or_404(Meeting, slug=slug)

    context = {
        'meeting': meeting,
        'title': meeting.channel
    }
    return render(request, 'meetings/room.html', context)

@login_required
def new_room(request):
    form = MeetingForm(initial={ 'host': request.user.id })
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            channel = request.POST['channel']
            form.save()
            messages.success(request, f'Your meeting {channel} has been scheduled successifully.')
            return redirect(reverse('lobby'))

    context = {
        'title': 'Create a new Room',
        'form': form
    }
    return render(request, 'meetings/new_room.html', context)


@login_required
def get_token(request):
    if request.GET.get('channel'):
        appId = os.environ.get('AGORA_APP_ID')
        appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
        channelName = request.GET.get('channel')
        uid = request.user.id
        expiration_time_in_seconds = 3600 * 24
        current_time_stamp = time.time()
        privilegeExpiredTs = current_time_stamp + expiration_time_in_seconds

        meeting = Meeting.objects.get(slug=request.GET.get('channel'))
        if meeting and meeting.host == request.user:
            role = 1
        else:
            role = 2

        channel = str(request.GET.get('channel')).replace('-', ' ').capitalize()

        token = RtcTokenBuilder.buildTokenWithUid(
                appId,
                appCertificate,
                channelName,
                uid,
                role,
                privilegeExpiredTs
            )
        return JsonResponse({ 'token': token, 'uid': uid, 'channel': channelName, 'username': request.user.username }, safe=False)
    else:
        return JsonResponse({ 'message': 'Please pass a channelName in the url.' }, safe=False)


@login_required
@csrf_exempt
def create_meeting_member(request):
    data = json.loads(request.body)

    member = MeetingMember.objects.filter(
        Q(name=data['name']) &
        Q(uid=request.user.id) &
        Q(channel=data['channel'])
        ).first()

    if not member:
        member = MeetingMember(
            name=data['name'],
            uid=request.user.id,
            channel=data['channel']
            )
        member.save()

    return JsonResponse( { 'name': data['name'] }, safe=False )

@login_required
@csrf_exempt
def delete_meeting_member(request):
    data = json.loads(request.body)

    member = MeetingMember.objects.filter(
        Q(name=data['name']) &
        Q(uid=request.user.id) &
        Q(channel=data['channel'])
        ).first()
    if member:
        member.delete()
    return JsonResponse('Member was deleted', safe=False )


@login_required
def get_meeting_member(request):
    uid = request.GET.get('uid')
    channel = request.GET.get('channel')

    member = MeetingMember.objects.get(
        uid=uid,
        channel=channel
    )
    name = member.name
    return JsonResponse({ 'name': name }, safe=False)
