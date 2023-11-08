from django.shortcuts import render,redirect
from .models import Device
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import pickle
import pandas as pd
import prophet
import numpy as np

# Create your views here.
@csrf_exempt
def new_data(request, id, m):
    device = get_object_or_404(Device, device_id=id)
    device.gas_sensor.append(min(150,m))
    while len(device.gas_sensor)>50:
        device.gas_sensor.pop(0)
    device.save()
    if device.manual_mode:
        return JsonResponse({'status':'false','message':'Manual Mode'}, status=300)
    return JsonResponse({'status':'ok'})

@csrf_exempt
def turn_on_alert(request, id):
    device = get_object_or_404(Device, device_id=id)
    device.manual_mode=True
    device.save()
    return JsonResponse({'status':'ok'})

@csrf_exempt
def get_prediction(request, id):
    try:
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        future = pd.DataFrame({"ds": [timestamp]})
        with open('prophet_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
            forecast = loaded_model.predict(future)
    except Exception as e:
        print(f"Error {e}")
    return JsonResponse({'status':'ok', 'forecast':forecast["yhat"][0]})

def index(request):
    if request.user.is_authenticated is False:
        return redirect("/login")
    name=request.user.first_name
    username=request.user.username
    email=request.user.email
    devices=Device.objects.filter(user__contains=[request.user.id]).count()
    return render(request, "user.html", {'name':name,'username':username,'email':email,'devices':devices})

def devices(request):
    if request.user.is_authenticated is False:
        return redirect("/login")
    print(Device)
    devices=Device.objects.filter(user__contains=[request.user.id])
    print(devices)
    return render(request, "devices.html", {'devices':devices})

def add_device(request,id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    print(Device)
    device, created = Device.objects.get_or_create(device_id=id)
    print(device)
    device.user.append(request.user.id)
    device.save()
    return redirect("/devices")

def manual_mode(request, id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    
    device = get_object_or_404(Device, device_id=id)
    device.manual_mode=not device.manual_mode
    device.save()
    return redirect("/devices")

def delete_device(request,id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    
    device = get_object_or_404(Device, device_id=id)
    device.user.remove(request.user.id)
    if(len(device.user)==0):
        device.delete()
    else:
        device.save()
    return redirect("/devices")