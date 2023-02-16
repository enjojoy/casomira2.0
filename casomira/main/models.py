from django.db import models
from django.utils.timesince import timesince
from django.db.models import DurationField


# Create your models here


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    nickname = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.nickname} {self.last_name}"


class Aircraft(models.Model):
    aircraft_type = models.CharField(max_length=60)
    registration = models.CharField(max_length=15)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aircraft_type}, {self.registration}"


class Flight(models.Model):
    date = models.DateField("date of provoz", auto_now_add=True)
    takeoff = models.DateTimeField("takeoff", default=None, null=True, blank=True)
    landing = models.DateTimeField("landing", default=None, null=True, blank=True)
    student = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
        related_name="student",
        null=True,
        default=None,
        blank=True,
    )
    captain = models.ForeignKey(
        Person, on_delete=models.RESTRICT, related_name="captain", null=True
    )
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.RESTRICT, related_name="letadlo", null=True
    )
    # duration = models.DurationField('duration', )

    def __str__(self):
        return f"{self.date}, {self.takeoff}, {self.landing}, {self.student}, {self.captain}, {self.aircraft}"

    @property
    def duration(self):  
        # return round((self.landing - self.takeoff).total_seconds() / 60)
        landing = self.landing
        takeoff = self.takeoff
        time_delta = timesince(takeoff, landing)
        return time_delta

    # duration = property(__duration)
