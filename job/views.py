from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Job, jobComment
from .forms import CommentForm
from taggit.models import Tag
from job import models

def job_detail(request, year, month, day, post):
    job = get_object_or_404(Job, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # List of active comments for this post
    comments = job.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/job/detail.html',
                  {'job': job,
                  'comments': comments, 
                  'new_comment': new_comment,
                  'comment_form': comment_form})
    

class JobListView(ListView):
    queryset = Job.published.all()
    context_object_name = 'jobs'
    paginate_by = 3
    template_name = 'blog/job/list.html'
def job_list(request, tag_slug=None):
   object_list = Job.published.all()
   tag = None
   
   if tag_slug:
       tag = get_object_or_404(Tag, slug=tag_slug)
       object_list = object_list.filter(tags__in=[tag])
       
   paginator = Paginator(object_list, 3) # 3 posts in each page
   page = request.GET.get('page')
   try:
       jobs = paginator.page(page)
   except PageNotAnInteger:
       # If page is not an integer deliver the first page
       jobs = paginator.page(1)
   except EmptyPage:
       # If page is out of range deliver last page of results
       jobs = paginator.page(paginator.num_pages)
   return render(request, 'blog/job/list.html', {'page': page,
                                                  'jobs': jobs,
                                                  'tag': tag})

def contact(request):
    
   if request.method == 'POST':
       #增加数据
       a_title=request.POST['a_title']
       a_slug=request.POST['a_slug']
       a_author=request.user
       a_body=request.POST['a_body']
       a_tags=request.POST['a_tags']
       models.Job.objects.create(title=a_title,slug=a_slug,author=a_author,body=a_body,status='published',tags=a_tags)

       object_list = Job.published.all()
       tag = None
       tag_slug = None
       if tag_slug:
              tag = get_object_or_404(Tag, slug=tag_slug)
              object_list = object_list.filter(tags__in=[tag])
       paginator = Paginator(object_list, 3) # 3 posts in each page
       page = request.GET.get('page')
       try:
              jobs = paginator.page(page)
       except PageNotAnInteger:
              # If page is not an integer deliver the first page
              jobs = paginator.page(1)
       except EmptyPage:
              # If page is out of range deliver last page of results
              jobs = paginator.page(paginator.num_pages)
       return render(request, 'blog/job/list.html', {'page': page,
                                                  'jobs': jobs,
                                                  'tag': tag})
       
   post_list = models.Job.objects.all()
   return render(request, 'blog/job/bbs_pub.html', {'post_list': post_list})    