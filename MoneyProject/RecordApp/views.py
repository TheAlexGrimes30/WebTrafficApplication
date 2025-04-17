from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from RecordApp.forms import StatusForm
from RecordApp.models import Status


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "status_create.html"
    success_url = reverse_lazy('record_utils')

def additional_view(request):
    return render(request, "record_utils.html")
