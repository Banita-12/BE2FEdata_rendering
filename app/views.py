from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='We are assuming that we got the data from database'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)
