from django.shortcuts import render,redirect
from .forms import homeForm,m_form
# Create your views here.

def home(req):
    if req.method == "POST":
        form = homeForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else :
        form = homeForm()
    return render(req,'form.html',{'form':form})
def model(req):
    mdl= m_form()
    if req.method == "POST":
        form = m_form(req.POST,req.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./app/upload/'+file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            form.save()
            print(form.cleaned_data)
            return redirect("model")
    else :
        form = m_form()
    return render(req,'model.html',{'form':mdl})
