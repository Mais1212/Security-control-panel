from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard__passcode=passcode)
    passcard = visits[0].passcard

    for visit in visits:
        is_strange = False
        duration = visit.get_duration()
        if visit.is_visit_long():
            is_strange = True

        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": duration,
                "is_strange": is_strange
            })

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
