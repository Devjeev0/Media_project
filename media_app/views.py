from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
# from rest_framework.views import APIView

from .models import *
from .serializers import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/team-list/',
        'Detail view': '/team-details/<int:id>/',
        'Create': '/team-create/',
        'Update': '/team-update/<int:id>',
        'Delete': '/team_delete/<int:id>',
    }
    return Response(api_urls);

@api_view(['GET'])
def showAll(request):
    team = team_model.objects.all()
    serializer = team_serializer(team, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = team_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update(request,pk):
    team = team_model.objects.get(id=pk)
    serializer = team_serializer(instance=team,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def delete(request,pk):
    team = team_model.objects.get(id=pk)
    team.delete()
    return Response("Item has been deleted succesfully")


#Room-----------------------------------------
@api_view(['POST'])
def create_room(request):
    serializer = room_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def showAll_room(request):
    room = room_model.objects.all()
    serializer = room_serializer(room, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_room(request,pk):
    room = room_model.objects.get(id=pk)
    serializer = room_serializer(instance=room,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def delete_room(request,pk):
    room = room_model.objects.get(id=pk)
    room.delete()
    return Response('room Deleted succesfully')

#date--------------------------------------------
@api_view(['POST'])
def add_time(request):
    serializer = timing_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def show_time(request):
    time = timing_model.objects.all()
    serializer = timing_serializer(time,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_time(request,pk):
    time = timing_model.objects.get(id=pk)
    serializer = timing_serializer(indance=time,data=request.data)
    return Response(serializer.data)

@api_view(['GET'])
def delete_time(request,pk):
    time = timing_model.objects.get(id=pk)
    time.delete()
    return Response('time data deleted successfully')

# @api_view(['GET'])
# def show_time(request,pk):
#     time = timing_model.objects.get(id=pk)
#     serializer = timing_serializer(time,many=True)
#     return Response(serializer.data)

def teams(request):
    all_data = team_model.objects.all()
    return render(request, 'index.html',{'all_data': all_data})
