
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from client_tenant.models import *
from client_tenant.forms import *
from django.views.generic.edit import CreateView


# Create your views here.
def index(request):
    """ A view to show ..... """
    context= {}
    task=Project.objects.all() 
    context["task"]=task
    return render(request, 'tenant/index.html', context)

def projectdetails(request, task_id):
    """ A view to show individual project task details """
    task = get_object_or_404(Project, pk=task_id)  # Retrieve the task by ID
    comments = task.comments.order_by('-created_date')[:5]
    commentform = CommentForm()
    context = {
        'task': task,
        'comments': comments,
        'commentform': commentform,
        }
    return render(request, 'tenant/projectdetails.html', context)


def home(request):
    return render(request, 'tenant/home.html')

 

def createcomment(request, task_id):
    post= get_object_or_404(Project, pk=task_id) 

    task = post.comments.all()
   
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.project = post
            comment.save()
            return redirect("client_tenant:projectdetails", task_id=task_id)
        else:
            return render(request, 'tenant/projectdetails.html', {'form':form, 'post':post, "task":task})


def deletecomment(request, comment_id, task_id):
    """ Delete a product from the store """
   
        
    comment = get_object_or_404(Comment, pk=comment_id)    
    comment.delete()
    
    return redirect("client_tenant:projectdetails", task_id=task_id)

 

def editcomment(request, comment_id, task_id):
    """ Delete a product from the store """
   
    task = get_object_or_404(Project, pk=task_id)       
    comment = get_object_or_404(Comment, pk=comment_id)    
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()  
            return redirect("client_tenant:projectdetails", task_id=task_id)
    else:
        form=CommentForm(instance=comment)
    
    return render(request, 'tenant/projectdetails.html', {'form':form, 'comment':comment, "task":task})
    


#def delete_comment():

#def add_task():


#def edit_task():


#def delete_task():

#def display_uploads():

#def check_user_tenant():

