import django
from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = []

    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        user_name = visit.passcard.owner_name
        duration, time_entering = visit.get_duration()

        person_info = {
            "who_entered": user_name,
            "entered_at": time_entering,
            "duration": duration,
        }

        non_closed_visits.append(person_info)
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
