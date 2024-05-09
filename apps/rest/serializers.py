from rest_framework import serializers


class ExcelDuplicateCleanerSerializer(serializers.Serializer):
    main_file = serializers.FileField()
    duplicates_file = serializers.FileField()
