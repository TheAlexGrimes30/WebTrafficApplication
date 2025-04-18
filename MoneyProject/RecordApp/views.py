from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from RecordApp.forms import StatusForm, TransactionTypeForm, CategoryForm, SubCategoryForm, DDSRecordForm
from RecordApp.models import Status, TransactionType, Category, SubCategory, DDSRecord


def additional_view(request):
    return render(request, "record_utils.html")

class HomeView(ListView):
    model = DDSRecord
    template_name = "home.html"
    context_object_name = "records"
    paginate_by = 10

    def get_queryset(self):
        queryset = DDSRecord.objects.select_related(
            'status', 'type_model', 'category', 'subcategory'
        ).all()

        status = self.request.GET.get('status')
        type_ = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if status:
            queryset = queryset.filter(status_id=status)

        if type_:
            queryset = queryset.filter(type_model_id=type_)

        if category:
            queryset = queryset.filter(category_id=category)

        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)

        if date_from:
            queryset = queryset.filter(date_created__gte=parse_date(date_from))
        if date_to:
            queryset = queryset.filter(date_created__lte=parse_date(date_to))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = TransactionType.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        context['filter_data'] = self.request.GET
        return context

def status_list_view(request):
    statuses = Status.objects.all()
    context = {
        "statuses": statuses
    }
    return render(request, "status_list.html", context=context)

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "status_create.html"
    success_url = reverse_lazy('status_list')

class StatusDetails(DetailView):
    model = Status
    template_name = "status_details.html"
    context_object_name = "status"

class StatusEditView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_edit.html'
    success_url = reverse_lazy('status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Status'
        return context

class StatusDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('status_list')

def type_list_view(request):
    types = TransactionType.objects.all()
    context = {
        "types": types
    }
    return render(request, "type_list.html", context=context)

class TypeCreateView(CreateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = "type_create.html"
    success_url = reverse_lazy("type_list")

class TypeDetails(DetailView):
    model = TransactionType
    template_name = "type_details.html"
    context_object_name = "type"

class TypeEditView(UpdateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = "type_edit.html"
    success_url = reverse_lazy("type_list")

class TypeDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        transaction_type = get_object_or_404(TransactionType, pk=pk)
        transaction_type.delete()
        return redirect('type_list')

def category_list_view(request):
    categories = Category.objects.select_related("type_model").all()
    context = {
        "categories": categories
    }
    return render(request, "category_list.html", context=context)

class CategoryDetails(DetailView):
    model = Category
    template_name = "category_details.html"
    context_object_name = "category"

class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_edit.html"
    success_url = reverse_lazy("category_list")

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_create.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('category_list')

def subcategory_list_view(request):
    subcategories = SubCategory.objects.select_related("category").all()
    context = {
        "subcategories": subcategories
    }
    return render(request, "subcategory_list.html", context=context)

class SubCategoryDetails(DetailView):
    model = SubCategory
    template_name = "subcategory_details.html"
    context_object_name = "subcategory"

class SubCategoryEditView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "subcategory_edit.html"
    success_url = reverse_lazy("subcategory_list")

class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "subcategory_create.html"
    success_url = reverse_lazy("subcategory_list")

class SubCategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        subcategory = get_object_or_404(SubCategory, pk=pk)
        subcategory.delete()
        return redirect('subcategory_list')

class RecordCreateView(CreateView):
    model = DDSRecord
    form_class = DDSRecordForm
    template_name = "record_create.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["types"] = TransactionType.objects.all()
        context["subcategories"] = SubCategory.objects.all()
        context["categories"] = Category.objects.all()
        return context

class RecordEditView(UpdateView):
    model = DDSRecord
    form_class = DDSRecordForm
    template_name = "record_edit.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["types"] = TransactionType.objects.all()
        context["subcategories"] = SubCategory.objects.all()
        context["categories"] = Category.objects.all()
        return context

class RecordDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        record = get_object_or_404(DDSRecord, pk=pk)
        record.delete()
        return redirect('home')
