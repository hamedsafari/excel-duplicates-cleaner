from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.rest.serializers import ExcelDuplicateCleanerSerializer
from apps.rest.utils import ExcelWorker


class ExcelDuplicateCleanerAPIView(APIView):
    permission_classes = []

    def get_serializer(self):
        return ExcelDuplicateCleanerSerializer()

    def post(self, request, *args, **kwargs):
        serializer = ExcelDuplicateCleanerSerializer(data=request.data)
        if serializer.is_valid():
            main_file = serializer.validated_data.get("main_file")
            duplicates_file = serializer.validated_data.get("duplicates_file")
            excel_worker = ExcelWorker(main_file, duplicates_file)
            excel_worker.process_new_file()
            with NamedTemporaryFile() as temp_file:
                workbook = excel_worker.get_output_workbook()
                workbook.save(temp_file.name)
                temp_file.seek(0)
                stream = temp_file.read()
                response = HttpResponse(stream, content_type="application/vnd.ms-excel")
                response["Content-Disposition"] = f'attachment; filename="result.xlsx"'
                return response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
