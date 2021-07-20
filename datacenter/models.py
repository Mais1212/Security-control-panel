import datetime

import django
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                "leaved at " + str(self.leaved_at) if self.leaved_at else
                "not leaved"
            )
        )

    def get_duration(self):
        leaved_at = django.utils.timezone.localtime(self.leaved_at)
        entered_at = django.utils.timezone.localtime(self.entered_at)
        duration = leaved_at - entered_at

        return duration

    def is_visit_long(visit, minutes=60):
        is_long = False
        duration = visit.get_duration()
        minutes = datetime.timedelta(minutes=minutes)

        if duration > minutes:
            is_long = True
        return is_long
