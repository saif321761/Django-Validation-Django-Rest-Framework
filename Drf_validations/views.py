from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    # if request.method == 'GET':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id', None)
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)
    #         json_data = JSONRenderer().render(serializer.data)
    #         return HttpResponse(json_data, content_type='application/json')
        
    # stu = Student.objects.all()
    # serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    if request.method == 'POST':
        # DATA comes to the client side mean myapp file the data comes into json format first convert into python and then convert into complex form
        # json data convert into python native below i am writing code
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        # pythondata convert into complex object
        serializer = StudentSerializer(data=pythondata)
        # check valid
        if serializer.is_valid():
            serializer.save()
            # here you can see data save but we need to give some response after saving data
            res = {'msg': "data succesfully saved"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     stu = Student.objects.get(id=2)
    #     serializer = StudentSerializer(stu, data=pythondata, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'mes': "updated data"}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data,content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data,content_type='application/json')
    
    # if request.method == 'DELETE':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     stu = Student.objects.get(id=3)
    #     serializer = StudentSerializer(stu,data=pythondata)
    #     stu.delete()
    #     res = {'mes': "data delete successfully!!"}
    #     # json_data = JSONRenderer().render(res)
    #     # return HttpResponse(json_data,content_type= 'application/json')
    #     return JsonResponse(res, safe=False)
        



