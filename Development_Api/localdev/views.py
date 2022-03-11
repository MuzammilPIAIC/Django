from django.shortcuts import redirect, render
from .models import Call_logs
from start.models import CrmLead
from .forms import AddStudentForm

# Create your views here.
def index(request):
    stu_data = Call_logs.objects.all()
    stu_data_2 = CrmLead.objects.all()
    return render(request, 'localdev/index copy.html', {'studata': stu_data})


def Add_Student(request):
    if request.method == "GET":
        fm = AddStudentForm()
        return render(request, 'localdev/add-student.html', {'form':fm})
    else:
        
        print('################################## Got POST request ####################')
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            print("data is valid.....................")
            fm.save()
        else:
            print(fm.errors.as_data())
        return redirect('/')

def Delete_Student(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        studata = Call_logs.objects.get(id=id)
        studata.delete()
        return redirect('/')

# def Update_Student(request):


