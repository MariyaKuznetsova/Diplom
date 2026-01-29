from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from diary.forms import RecordForm, SearchForm
from diary.models import Record


class RecordCreateView(LoginRequiredMixin, CreateView):
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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden("У вас нет прав для просмотра этой записи")
        return obj


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер по редактированию записи в дневнике"""

    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("diary:record_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden(
                "У вас нет прав для редактирование этой записи"
            )
        return obj


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер по удаления записи в дневнике"""

    model = Record
    success_url = reverse_lazy("diary:record_list")
    context_object_name = "record"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden("У вас нет прав для удаление этой записи")
        return obj


def post_search(request):
    form = SearchForm(request.GET)
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Record.objects.filter(date=query)  # Поиск по заголовку
    return render(
        request,
        "diary/search_results.html",
        {"form": form, "query": query, "results": results},
    )

    #
    # query = request.GET.get('query')
    # if query:
    #     results = Record.objects.filter(date=query)
    # else:
    #     results = Record.objects.none()
    # return render(request, 'diary/search_results.html', {'form': form, 'results': results})
