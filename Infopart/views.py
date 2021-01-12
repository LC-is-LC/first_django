from django.shortcuts import render, get_object_or_404
# #LC importing HttpResponse]
# HttpResponse is no longer needed after the creation of templates and use of render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#since a class cant use a decorator, we use mixins. This mixin is to show a login is required before one can access
# User passes test, makes it that only the user who made the particular post can use the mode
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importing the table(class) we have made in our database in the models.py file
from .models import Board, Review

''' Creating dummy data at first (No longer needed after putting tables in oure database
 Board_of_Directors = [
    {
        'Director': 'Akanbi Anjola',
        'Department': 'Baking department',
        'Get_to_know': 'She is LC\'s Gee, Chief Chef and the CEO of CBA.',
        'Hire_date': 'August 23, 2020'
    },
    {
        'Director': 'Arowolo Abdulazeez',
        'Department': 'Financial department',
        'Get_to_know': 'He is the financial assistant and fine boy of CBA. He is awesome',
        'Hire_date': 'August 23, 2020'
    }
]


# #LC function to handle traffic from homepage of Infopart, it takes a request argument which...(explained later)
# #LC the function is going to help return what user sees when they come to this route
# #LC to create the urls which we lead to different views we create a url.py under the Infopart file
# #LC when a template has been created, the response returns it by using render which as been imported above '''
def home(request):
    # This would have been it if we didn't make a template
    # return HttpResponse("<h1> Cookies by Anjiee (CBA) </h1>")
    context = {'title' : 'home', 'Review': Review.objects.all()}
    return render(request, 'Infopart/home.html', context)


class PostReview(ListView):
    model = Review
    template_name = 'Infopart/home.html'
    context_object_name = 'Review'
    ordering = ['-post_date']
    paginate_by = 5

    # A List view for reviews of a particular user
class UserPostReview(ListView):
    model = Review
    template_name = 'Infopart/User_review.html'
    context_object_name = 'Review'
    paginate_by = 5

    # Overriding the normal query set that will deliver all the reviews in 'Review' to just that of the user
    def get_queryset(self):
        # To get the object from the User with a username  as the 'username' in the url and put it in the variable; user
        # ... Or return a 404 if User does not exist
        # Then return a filtered Review
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Review.objects.filter(customer=user).order_by('-post_date')


class OneReview(DetailView):
    model = Review

#Loginrequired mixin is added, so one can only create a review when logged in, and this redirects us to login page
# N>B the mixins must come first before the view type
class MakeReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['intro', 'comment']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super( ).form_valid(form)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['intro', 'comment']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super( ).form_valid(form)

    # The test to go through to see if the logged in user is the owner of the review they want to edit
    def test_func(self):
        # Get the precise object(review) trying to be accessed
        Review = self.get_object()
        # If the current user is the author of that review allow
        if self.request.user == Review.customer:
            return True
        return False

class DelReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Review
        success_url = "/"

        # The test to go through to see if the logged in user is the owner of the review they want to edit
        def test_func(self):
            # Get the precise object(review) trying to be accessed
            Review = self.get_object()
            # If the current user is the author of that review allow
            if self.request.user == Review.customer:
                return True
            return False




def about(request):
    # A context can be added to also go with the information rendered
    context = {
        'Board_of_Directors': Board.objects.all() # formerly the dummy data above i.e Board_of_Directors
    }
    # return HttpResponse('<h1> About CBA </h1>')
    return render(request, 'Infopart/about.html', context)




