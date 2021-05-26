from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class Institute(APIView):
    def get(self,request):
        subjects = [
            {
                'telug':'Ravi',
                'hindi':'Raju',
                'maths':'Jahanvai'
            }
        ]
        languages = [
            {
                'python':1,
                'java':2,
                'C':3
            }
        ]
        schools =[
            {
                'nagarjuna':1,
                'vivekananda':2
            }
        ]
        return Response({
            'languages':languages,
            'schools':schools,
            'subjects':subjects
        })

    def post(self, request):
        subjects = [
            {
                'telug': 'Ravi',
                'hindi': 'Raju',
                'maths': 'Jahanvai'
            }
        ]
        languages = [
            {
                'python': 1,
                'java': 2,
                'C': 3
            }
        ]
        schools = [
            {
                'nagarjuna': 1,
                'vivekananda': 2
            }
        ]
        return Response({
            'languages': languages,
            'schools': schools,
            'subjects': subjects
        })
    def put(self, request):
        subjects = [
            {
                'telug': 'Ravi',
                'hindi': 'Raju',
                'maths': 'Jahanvai'
            }
        ]
        languages = [
            {
                'python': 1,
                'java': 2,
                'C': 3
            }
        ]
        schools = [
            {
                'nagarjuna': 1,
                'vivekananda': 2
            }
        ]
        return Response({
            'languages': languages,
            'schools': schools,
            'subjects': subjects
        })
    def delete(self, request):
        subjects = [
            {
                'telug': 'Ravi',
                'hindi': 'Raju',
                'maths': 'Jahanvai'
            }
        ]
        languages = [
            {
                'python': 1,
                'java': 2,
                'C': 3
            }
        ]
        schools = [
            {
                'nagarjuna': 1,
                'vivekananda': 2
            }
        ]
        return Response({
            'languages': languages,
            'schools': schools,
            'subjects': subjects
        })