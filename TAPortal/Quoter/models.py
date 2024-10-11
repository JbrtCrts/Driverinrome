from django.db import models
from django.utils.dateformat import DateFormat

# Create your models here.

class Rate(models.Model):
    Rate = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        if self.Rate == 1.00:
            return "Standard Price"
        else:
            Surge = (self.Rate - 1) * 100
            return f"{Surge:.0f}%"



class Date_Rate(models.Model):
    Date = models.DateField(primary_key=True)
    Rate = models.ForeignKey(Rate, on_delete=models.CASCADE, related_name='Price_Rate')

    #def __str__(self):
        # Format the date to 'April 15, 2025'
    #    formatted_date = DateFormat(self.Date).format('F j, Y')

        # Get the rate value from the related Rate model and calculate the percentage
    #    if self.Rate == 1.00:
    #        rate_display = "Standard Price"
    #    else:
    #        Surge = (self.Rate - 1) * 100
    #        rate_display = f"{Surge:.0f}%"

        # Return the final string representation
    #    return f"The Price Rate for {formatted_date} is {Surge:.0f}%"



