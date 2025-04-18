"""
URL configuration for MoneyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from RecordApp.views import additional_view, StatusCreateView, StatusDetails, StatusEditView, StatusDeleteView, \
    status_list_view, TypeCreateView, TypeDetails, TypeEditView, TypeDeleteView, type_list_view, category_list_view, \
    CategoryCreateView, CategoryDetails, CategoryEditView, CategoryDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('additional/status_list/', status_list_view, name="status_list"),
    path('additional/', additional_view, name="record_utils"),
    path('additional/status_list/create', StatusCreateView.as_view(), name="status_create"),
    path('additional/status_list/<int:pk>/', StatusDetails.as_view(), name="status_detail"),
    path('additional/status_list/edit/<int:pk>/', StatusEditView.as_view(), name="status_edit"),
    path('additional/status_list/delete/<int:pk>/', StatusDeleteView.as_view(), name="status_delete"),
    path('additional/type_list/', type_list_view, name="type_list"),
    path('additional/type_list/create', TypeCreateView.as_view(), name="type_create"),
    path('additional/type_list/<int:pk>/', TypeDetails.as_view(), name="type_detail"),
    path('additional/type_list/edit/<int:pk>/', TypeEditView.as_view(), name="type_edit"),
    path('additional/type_list/delete/<int:pk>/', TypeDeleteView.as_view(), name="type_delete"),
    path('additional/category_list/', category_list_view, name="category_list"),
    path('additional/category_list/create', CategoryCreateView.as_view(), name="category_create"),
    path('additional/category_list/<int:pk>/', CategoryDetails.as_view(), name="category_detail"),
    path('additional/category_list/edit/<int:pk>/', CategoryEditView.as_view(), name="category_edit"),
    path('additional/category_list/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
]
