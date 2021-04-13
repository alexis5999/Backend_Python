from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include(('apis.urls', 'apis'), namespace='api')),

]
