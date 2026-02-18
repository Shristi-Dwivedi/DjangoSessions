from django.contrib import admin
from django.urls import path
from mysession import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view, name="login"),
    path('dashboard/',views.dashboard, name="dashboard"),
]
