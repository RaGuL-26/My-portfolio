from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ContactSubmission
from django.contrib import messages


def main_page(request):
    return render(request,'index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactSubmission.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent!')
        return redirect('mainpage')
    return render(request, 'index.html')

@login_required
def view_submissions(request):
    submissions = ContactSubmission.objects.order_by('-submitted_at')
    return render(request, 'admin.html', {'submissions': submissions})

def delete_comment(request,comment_id=None):
    comment_delete = ContactSubmission.objects.get(id=comment_id)
    comment_delete.delete()
    messages.success(request,'Comment Deleted')
    return redirect('comments')