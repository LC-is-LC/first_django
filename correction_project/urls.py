"""my_first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# #LC this is the Oga url file of the site, all apps url must be here too to inform the site
# # to add other app urls we add include to what is imported from django.urls
# #LC include, let's us tell the paths to get its views for those urls from the file we include
# #LC leaving an empty path means if you just click the link that is where it takes you

from django.contrib import admin
from django.urls import path, include


# url connected to it's views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Infopart.urls")),
    path('', include("Users.urls"))
]