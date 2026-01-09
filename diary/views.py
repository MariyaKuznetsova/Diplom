from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from diary.forms import RecordForm, BootstrapFormMixin
from diary.models import Record



class RecordCreateView(LoginRequiredMixin,CreateView):
    """Контроллер по созданию записи в дневник"""

    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("diary:record_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecordListView(LoginRequiredMixin, ListView):
    """Контроллер по выводу списка записей в дневнике"""

    model = Record
    template_name = "diary/record_list.html"
    context_object_name = "records"


class RecordDetailView(LoginRequiredMixin, DetailView):
    """Контроллер по выводу записи в дневнике"""

    model = Record


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер по редактированию записи в дневнике"""
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("diary:record_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden("У вас нет прав для редактирование этого продукта")
        return obj


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер по удаления записи в дневнике"""
    model = Record
    permission_required = "diary:record_delete"
    success_url = reverse_lazy("diary:record_list")
    context_object_name = "record"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden("У вас нет прав для удаление этого продукта")
        return obj
