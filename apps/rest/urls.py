from django.urls import path
from apps.rest.views import ExcelDuplicateCleanerAPIView, GoogleCalendarAPIView

urlpatterns = [
    path(
        "duplicates-cleaner/",
        ExcelDuplicateCleanerAPIView.as_view(),
        name="duplicates-cleaner",
    ),
    path("calendar/", GoogleCalendarAPIView.as_view(), name="calendar"),
]
