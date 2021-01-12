
# #LC learning from the url.py in the main project file, we learn that we have to import path and create urlpatterns
from django.urls import path

# #LC import the views.py so you could connect it to the urls
from . import views
from .views import PostReview, OneReview, MakeReview, EditReview, DelReview, UserPostReview

# #LC for homepages the path should be empty, and the view (what should show ) should be what the home function in views returns
# #LC It can also be named for future lookups on other app routes
urlpatterns = [
    path('', PostReview.as_view(), name= "Info-home"),
    # the values inside the <> are the parameters that the site needs to be able to access that particular path
    path('user/<str:username>', UserPostReview.as_view(), name= "User-review"),
    path('Review/<int:pk>/', OneReview.as_view(), name= "Review-detail"),
    path('Review/<int:pk>/update/', EditReview.as_view(), name= "Review-update"),
    path('Review/new/', MakeReview.as_view(), name= "Review-create"),
    path('Review/<int:pk>/delete/', DelReview.as_view(), name= "Review-delete"),
    path('about/', views.about, name= "Info-about"),
]
