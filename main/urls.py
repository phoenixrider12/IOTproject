from django.urls import path
from .views import index, new_data, devices, add_device, manual_mode, delete_device, turn_on_alert, get_prediction

urlpatterns = [
    path("", index, name="index"),
    path("data/<str:id>/<int:m>", new_data, name="data"),
    path("alert/<str:id>/<int:fn>", turn_on_alert, name="alert"),
    path("predict/<str:id>", get_prediction, name="predict"),
    path("devices", devices, name="devices"),
    path("add_device/<str:id>", add_device, name="add_devices"),
    path("manual_mode/<str:id>", manual_mode, name="manual_mode"),
    path("delete_device/<str:id>", delete_device, name="delete_device"),
]
