from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors = ['Red','Black','Gray','Browon','White']
        return Response({'msg':'happy new year','colors':colors})
    def post(self,request,*args,**kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f'hello {name} happy pongal'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg':'this method from put method '})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'this method from patch method '})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'this method from delete method '})

from rest_framework.viewsets import ViewSet

class TestViewSet(ViewSet):
   def list(self,request):
        colors = ['Red', 'Black', 'Gray', 'Browon', 'White']
        return Response({'msg': 'happy new year', 'colors': colors})
   def create(self,request):
       serializer = NameSerializer(data=request.data)
       if serializer.is_valid():
           name = serializer.data.get('name')
           msg = f'hello {name} happy pongal'
           return Response({'msg': msg})
       else:
           return Response(serializer.errors, status=400)

   def retrieve(self,request,pk=None):
       return Response({'msg':'this is form retrive method of Viewset'})

   def update(self,request,pk=None):
       return Response({'msg':"this is form update method of Viewset"})

   def partial_update(self,request,pk=None):
       return Response({'msg':"this is form partial update method of Viewset"})

   def destroy(self,request,pk=None):
       return Response({'msg':"this is form destroy method of Viewset"})
