from django.shortcuts import render
from django.views import View
from datetime  import datetime
 
 def home(request):
    name="Krithick"
    current_time=datetime.now().strftime("%d/%m%Y %H:%M:%S")
    context={'current_time':current_time,'name':name}

    return render(request,'myfirstapp/home.html',context)

class MyView(View):

    def get(self,request):
        context={'user_name':"John",'user_age':30}
        return render(request,'myfirstapp/my_template.html',context)
    