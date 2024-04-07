"""LoginFormBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_maker.urls')),
    path('users/', include('users.urls')),
    # Will be included when made compatible with new form_maker
    # path('api_form_maker/', include('api_form_maker.urls')),
    path('form_output/',include('form_output.urls')),
]

# PROBLEM: This exposes all the stored media, so if anyone knows the filename they can easily
# access the files here. This is here as a temporary solution to allow users to view their
# previously uploaded media. A dedicated route has to be implemented and the below must be removed.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
