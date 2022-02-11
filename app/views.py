from django.shortcuts import redirect, render
from .models import CalcualteInterstModel
from .forms  import CalculateInteresForm
# Create your views here.
def index(request):
    if request.method == "POST":
        form = CalculateInteresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CalculateInteresForm()
            
    
    return render(request,'index.html',context={'cim':CalcualteInterstModel.objects.all(),'form':form})