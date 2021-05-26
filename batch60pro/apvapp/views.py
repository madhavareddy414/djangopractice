from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Institute(APIView):
    def post(self,request):
        databases = [
            {
            "oracle":1000,
            "mysql" : 2000
        },
        ]
        languages = [
            {
                "python":1000,
                "django":2000
            }
        ]

        return Response(
            {
                "databases":databases,
                "languages": languages
            }
        )
