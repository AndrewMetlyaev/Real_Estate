from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('property/', include('apps.property.urls')),
]
