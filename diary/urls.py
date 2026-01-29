from django.urls import path

from diary.apps import DiaryConfig
from diary.views import (RecordCreateView, RecordDeleteView, RecordDetailView,
                         RecordListView, RecordUpdateView, post_search)

app_name = DiaryConfig.name

urlpatterns = [
    path("", RecordListView.as_view(), name="record_list"),
    path("diary/<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    path("diary/create/", RecordCreateView.as_view(), name="record_create"),
    path("diary/update/<int:pk>/", RecordUpdateView.as_view(), name="record_update"),
    path("diary/delete/<int:pk>/", RecordDeleteView.as_view(), name="record_delete"),
    path("diary/search/", post_search, name="search_results"),
]
