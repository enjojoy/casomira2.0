from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    nickname = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return (f"{self.first_name} {self.nickname} {self.last_name}")

class Aircraft(models.Model):
    aircraft_type = models.CharField(max_length=60)
    registration = models.CharField(max_length=15)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return(f'{self.aircraft_type}, {self.registration}')

class Flight(models.Model):
    date = models.DateTimeField('date of provoz')
    takeoff = models.DateTimeField('takeoff', default = None, null=True, blank=True)
    landing = models.DateTimeField('landing', default = None, null=True, blank=True)
    student = models.ForeignKey(Person, on_delete = models.RESTRICT, related_name = 'student', null=True, default=None)
    captain = models.ForeignKey(Person, on_delete = models.RESTRICT, related_name = 'captain', null=True)
    aircraft = models.ForeignKey(Aircraft, on_delete = models.RESTRICT, related_name = 'letadlo', null=True)
    
    def __str__(self):
        return(f"{self.date}, {self.takeoff}, {self.landing}, {self.student}, {self.captain}, {self.aircraft}")






