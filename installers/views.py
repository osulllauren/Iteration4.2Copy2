from django.shortcuts import render

from .forms import InstallerForm, RawInstallerForm

from .models import Installer

# Create your views here.

#https://www.youtube.com/watch?v=uz5gyXemak0&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=25
# def installer_create_view(request):
#     my_form = RawInstallerForm()
#     if request.method == "POST":
#         my_form = RawInstallerForm(request.POST) #does the validation
#         if my_form.is_valid():
#             #data is good
#             print(my_form.cleaned_data)
#             Installer.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = { 
#         "form": my_form
#     } 
#     return render(request, "installers/installer_create.html", context)




#https://www.youtube.com/watch?v=6oOHlcHkX2U&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=23
def installer_create_view(request):
    form = InstallerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InstallerForm() #re-renders the form so it clears the data 
    context = {
        'form': form
    } 
    return render(request, "installers/installer_create.html", context)


# def installer_detail_view(request):
#     obj = Installer.objects.get(id=1)
#     #     context = {
#     #         'name': obj.name,
#     #         'email': obj.email, 
#     #         'mobile': obj.mobile,
#     #         'address': obj.address,
#     #         'bio': obj.bio
#     #     }
#     context = {
#         'object': obj
#     } 
#     return render(request, "installers/installer_detail.html", context)