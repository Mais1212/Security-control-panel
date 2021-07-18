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
        entered_at = django.utils.timezone.localtime(self.entered_at)
        leaved_at = django.utils.timezone.localtime(self.leaved_at)
        time_now = django.utils.timezone.now()
        duration = leaved_at - entered_at

        return duration, entered_at

    def is_visit_long(visit, minutes=60):
        duration = visit.get_duration()[0]
        minutes = datetime.timedelta(minutes=minutes)

        if duration > minutes:
            return True
        return False
