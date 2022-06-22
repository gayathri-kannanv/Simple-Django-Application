# import Http Response from django
from django.http import HttpResponse

 
# create a function
def done(request):
    print(request)
  
    value1= request.GET.get('first_val')
    value2= request.GET.get('second_val')
    value3= request.GET.get('third_val')

    return HttpResponse("Here is the response from user: " +value1+ " , "+value2+ " , "+value3)