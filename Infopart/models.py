from django.db import models
# importing timezone so to put our timezone in consideration when applied
from django.utils import timezone
# To import the Users that django already set in the admin page
from django.contrib.auth.models import User

from django.urls import reverse

# #LC we create a class which will be a table in our database, each attribute will be a field of that table


'''class Orders(models.Model):
    # Creating a tuples of choices, 1st values are the programmed choices, but the user sees the 2nd values as options)
    flavours = (('CHO', 'Chocolate'),
                ('VAN', 'Vanilla'))
    flavour = models.CharField(max_length=3, choices=flavours)
    number = models.CharField(max_length=3)
    phone = models.CharField(max_length=14)
    # Timezone as at whenever updated
    date_ordered = models.DateTimeField(auto_now=True)
    # timezone unchangeable, after kept
    date_delivered = models.DateTimeField(auto_now_add=True)
    # Since a User can have many orders, but an order will have just one user (This is a one to many relationship)
    # This is done using a foreignKey, which shows the many the ONE in charge
    # on_delete says what happens to the customer if the customer is deleted, SET_NULL says it shouldn't delete the order as well
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)


'''


class Board(models.Model):
    director = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    get_to_know = models.TextField()
    # timezone.now without ending bracket so that it doesnt call the function
    hire_date = models.DateTimeField(default=timezone.now)
    # on_delete says what happens to the board member if the user(Admin) is deleted, CASCADE says it should delete the whole board member
    referee = models.ForeignKey(User, on_delete=models.CASCADE)

    # to show what will represent a Board member whenever it is made
    def __str__(self):
        return self.director

class Review(models.Model):
    intro = models.CharField(max_length= 10)
    comment = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.intro

    # THis function gives where the model should usually take one to after an operation
    def get_absolute_url(self):
        # returning the DetailView of the Review on ground
        # since the particular pk is needed for the views to take it there, we note the pk to be the pk of the current Review
        return reverse('Review-detail', kwargs={'pk': self.pk})

