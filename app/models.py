from django.db import models

# Create your models here.
def interest_per_month(principal):
    interest = 0
    if principal <= 5000:
        interest = (principal/100)*3 
    else:
        interest = (principal/100)*2
    return interest
        
def CompoundInterest(principal,year):
    interest = interest_per_month(principal)* 12
    grand_total = principal + interest
    if year > 1:
        year -= 1
        return grand_total + CompoundInterest(grand_total,year)
    return  grand_total

class CalcualteInterstModel(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    principal = models.IntegerField()

    @property
    def interest(self):
        days =   self.end_date.day - self.start_date.day
        month =  self.end_date.month - self.start_date.month
        year =   self.end_date.year - self.start_date.year
        
        
        if self.start_date.month > self.end_date.month:
            month = (12 + self.end_date.month) - self.start_date.month
            year -= 1

        if self.start_date.day > self.end_date.day:
            days =   (30 + self.end_date.day) - self.start_date.day
            month -= 1
        
        if year > 0:
            self.principal = CompoundInterest(self.principal,year)

        interest_in_month = interest_per_month(self.principal) * month
        interest_in_day = (interest_per_month(self.principal)/30)* days
        grand_total = self.principal + interest_in_month + interest_in_day
        
        return "{:.2f}".format(grand_total)