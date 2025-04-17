from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from RecordApp.forms import StatusForm
from RecordApp.models import Status


def additional_view(request):
    statuses = Status.objects.all()
    context = {
        "statuses": statuses
    }
    return render(request, "record_utils.html", context=context)

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "status_create.html"
    success_url = reverse_lazy('record_utils')

class StatusDetails(DetailView):
    model = Status
    template_name = "status_details.html"

