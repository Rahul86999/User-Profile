
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import  ProfileForm
from .models import UserProfile
from django.views import View
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder 
from django.db.models.fields.files import ImageFieldFile
import simplejson

class IndexView(View):
    template_name = 'index.html'
    
    def get(self,request):
        users = UserProfile.objects.all().order_by('-id')
        return render(request,self.template_name,{'users':users})

# User Create user profile
class UserProfileView(View):
    form_class = ProfileForm
    template_name = 'profile.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' Profile created successfully.')
            return redirect("/")
        else:
            form = self.form_class(request.POST)
        return render(request,self.template_name, {'form': form})

# Delete user profile
class DeleteProfile(View):
    def  get(self, request):
        id1 = request.GET.get('id')
        UserProfile.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

#Image encoded 
class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)

class UpdateDoctor(View):
    
    def get(self, request):
        id1 = request.GET.get('id')
        obj = UserProfile.objects.get(id=id1)
        user = {
            'id':obj.id,
            'profile_image':obj.profile_image,
            'name':obj.name,
            'username':obj.username,
            'email':obj.email,
            'phone_no':obj.phone_no,
            'comments':obj.comments
            }
        data = json.dumps(user,cls=ExtendedEncoder)
        return JsonResponse(data,safe=False)
        # return JsonResponse(data)

    def post(self, request):
        id1 = request.POST.get('formId')
        profile_image = request.FILES.get('profile_image')
        name = request.POST.get('formName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_no = request.POST.get('formPhone_no')
        comments = request.POST.get('formComments')

        obj = UserProfile.objects.get(id=id1)
        
        if profile_image:
            obj.profile_image = profile_image
        obj.name = name
        obj.username = username
        obj.email = email 
        obj.phone_no = phone_no
        obj.comments =comments 
        obj.save()
        user = {
            'id':obj.id,
            'profile_image':obj.profile_image,
            'name':obj.name,
            'username':obj.username,
            'email':obj.email,
            'phone_no':obj.phone_no,
            'comments':obj.comments
            }
        data = json.dumps(user,cls=ExtendedEncoder)
        return JsonResponse(data,safe=False)
        # return JsonResponse({'user':data})

# Username and Email Validation
def user_validate(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    username = UserProfile.objects.filter(username=username).exists()
    email = UserProfile.objects.filter(email=email).exists()
    if username:
        result ="false"
    elif email:
        result = "false"
    else:
        result = "true"
    return HttpResponse(result)