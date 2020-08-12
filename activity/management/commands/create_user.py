import json

from django.core.management.base import BaseCommand, CommandError
from activity.serializers import UserSerializer


class Command(BaseCommand):
    help = 'Prepopulates user data from a json file'

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         'file_name', type=str,
    #         help='Specifies the json file to be taken')

    def handle(self, *args, **kwargs):
        import os
        path = os.path.dirname(os.path.realpath(__file__)) + '/../../'

        # file_name = kwargs['file_name']
        file_name = 'sample.json'
        json_data = open(path+file_name)
        users = json.load(json_data)

        for user in users:
            serializer = UserSerializer(data=user)
            if serializer.is_valid():
                serializer.save()

        json_data.close()
