from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from project1.project1.tags.models import Tag, TagPost
from project1.project1.posts.models import Post
from project1.project1.users.models import User, UserUser, UserPost
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.template.engine import Engine
# Create your views here.
# def user_list(request):
#     if request.method == "POST":
#         # form = UserForm(request.POST)
#         # if form.is_valid():
#         #     user = form.save(commit=False)
#         #     username = form.cleaned_data['username']
#         #     password = form.cleaned_data['password']
#         #     user.set_password(password)
#         #     user.save()
#         #     user = authenticate(username=username, password=password)
#         #     login(request, user)
#         #     return redirect("home")
#         # else:
#         #     context = {}
#         #     context['form'] = form
#             return render(request,"user_create.html",context)

# def user_detail(request, pk):
#     if request.method == "GET":
#         # profile = get_object_or_404(Profile, pk = pk)
#         # context = {}
#         # context['profile'] = profile
#         return render(request,"profile_detail.html",context)
    # elif request.method == "PATCH" and request.is_ajax():
    #     profile = Profile.objects.get(pk = pk)
    #     patch = QueryDict(request.body)
    #     form = ProfileForm(patch, instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Profile updated.")
    #         response = {}
    #         return JsonResponse(response)
    #     else:
    #         print('error')
    # elif request.method == "POST":
    #     profile = Profile.objects.get(pk = pk)
    #     if "avatar" in request.FILES:
    #         form = ProfileAvatarForm(request.POST, request.FILES, instance=profile)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, "Profile avatar updated.")
    #             return redirect(profile)
    #         else:
    #             print('error')
    #     else:
    #         form = ProfileBackgroundForm(request.POST, request.FILES, instance=profile)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, "Profile background updated.")
    #             return redirect(profile)
    #         else:
    #             print('error')

# @login_required
# def user_edit(request, pk):
#     if request.method == "GET":
#         profile = get_object_or_404(Profile, pk=pk)
#         if profile.user == request.user:
#             context = {}
#             context['form'] = ProfileForm(instance = profile)
#             context['profile'] = profile
#             return render(request,"profile_edit.html",context)
#         else:
#             raise PermissionDenied
#
# def user_create(request):
#     if request.method == "GET":
#         context = {}
#         context['form'] = UserForm()
#         return render(request,"user_create.html",context)

def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            print('w')
        else:
            general_tags = Tag.objects.filter(id__lt=11)
            for t in general_tags:
                bool(t.posts.all())
            # bool(general_tags)
            context = {'general_tags':general_tags}
            return render(request, 'home.html', context)


    # if request.method == "GET":
    #     context = {}
    #     # if request.user.is_authenticated:
    #     #
    #     #     if request.user.profile.get_followed_tags_count() != 0:
    #     #         context['followed_tags'] = request.user.profile.get_followed_tags()
    #     # else:
    #     context['general_tags'] = Tag.objects.filter(general = True)
    #     return render(request,"home.html",context)
