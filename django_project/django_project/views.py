# import Http Response from django
from django.http import HttpResponse
import pyodbc 
from .forms import NameForm

dbcon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=localhost;Database=django;Trusted_Connection=yes;')
cursorObject= dbcon.cursor()
    
# create a function
def done(request):
    print(request)
    form = NameForm()
    value1= request.GET.get('first_val')
    value2= request.GET.get('second_val')
    value3= request.GET.get('third_val')
    #if form.is_valid():
    cursorObject.execute("INSERT INTO [dbo].[Prj01] ([How are you],	[Where are you], [Who are you]) VALUES (?,?,?);", (value1,value2,value3))
    dbcon.commit()
    dbcon.close()
    return HttpResponse("Values stored in database!  Here is the response from user: " +value1+ " , "+value2+ " , "+value3)