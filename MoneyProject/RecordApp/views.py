from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

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
    context_object_name = "status"

class StatusEditView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_edit.html'
    success_url = reverse_lazy('record_utils')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Status'
        return context

class StatusDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('record_utils')

