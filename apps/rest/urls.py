from django.urls import path
from apps.rest.views import ExcelDuplicateCleanerAPIView

urlpatterns = [
    path(
        "duplicates-cleaner/",
        ExcelDuplicateCleanerAPIView.as_view(),
        name="duplicates-cleaner",
    )
]
