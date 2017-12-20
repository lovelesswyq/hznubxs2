from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Travel, travelComment
from .forms import CommentForm
from taggit.models import Tag
from travel import models

def travel_detail(request, year, month, day, post):
    travel = get_object_or_404(Travel, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # List of active comments for this post
    comments = travel.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = travel
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/travel/detail.html',
                  {'travel': travel,
                  'comments': comments, 
                  'new_comment': new_comment,
                  'comment_form': comment_form})
    

class TravelListView(ListView):
    queryset = Travel.published.all()
    context_object_name = 'travels'
    paginate_by = 3
    template_name = 'blog/travel/list.html'
def travel_list(request, tag_slug=None):
   object_list = Travel.published.all()
   tag = None
   
   if tag_slug:
       tag = get_object_or_404(Tag, slug=tag_slug)
       object_list = object_list.filter(tags__in=[tag])
       
   paginator = Paginator(object_list, 5) # 3 posts in each page
   page = request.GET.get('page')
   try:
       travels = paginator.page(page)
   except PageNotAnInteger:
       # If page is not an integer deliver the first page
       travels = paginator.page(1)
   except EmptyPage:
       # If page is out of range deliver last page of results
       travels = paginator.page(paginator.num_pages)
   return render(request, 'blog/travel/list.html', {'page': page,
                                                  'travels': travels,
                                                  'tag': tag})
def contact(request):
    
   if request.method == 'POST':
       #增加数据
       a_title=request.POST['a_title']
       a_slug=request.POST['a_slug']
       a_author=request.user
       a_body=request.POST['a_body']
       models.Travel.objects.create(title=a_title,slug=a_slug,author=a_author,body=a_body,status='published')

       object_list = Travel.published.all()
       tag = None
       tag_slug = None
       if tag_slug:
              tag = get_object_or_404(Tag, slug=tag_slug)
              object_list = object_list.filter(tags__in=[tag])
       
       paginator = Paginator(object_list, 5) # 3 posts in each page
       page = request.GET.get('page')
       try:
              travels = paginator.page(page)
       except PageNotAnInteger:
              # If page is not an integer deliver the first page
              travels = paginator.page(1)
       except EmptyPage:
              # If page is out of range deliver last page of results
              travels = paginator.page(paginator.num_pages)
       return render(request, 'blog/travel/list.html', {'page': page,
                                                  'travels': travels,
                                                  'tag': tag})
       
       
       
   post_list = models.Travel.objects.all()
   return render(request, 'blog/travel/bbs_pub.html', {'post_list': post_list})   