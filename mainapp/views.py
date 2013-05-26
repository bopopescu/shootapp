from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, Context
from mainapp.models import *
import datetime
from forms import IdeaForm, CommentForm


def submit(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea_info = form.cleaned_data
            idea_title_form = idea_info['idea_title']
            idea_text_form = idea_info['idea_text']
            idea_created_form = datetime.datetime.now()
            idea_last_activity_form = datetime.datetime.now()
            idea = Idea(idea_title=idea_title_form, idea_text=idea_text_form, idea_created=idea_created_form, idea_last_activity=idea_last_activity_form)
            idea.save()
            ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
            dict = {}
            for i,each in enumerate(ideas):
                dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
                c = {'idealist': ideas, 'commentlist': dict}
            #return HttpResponseRedirect('/')
               
            #return render_to_response('index.html', context_instance=RequestContext(request))
            return HttpResponseRedirect('/')


    else:
        form = IdeaForm
        return render(request, 'submit.html', {'form': form})

    '''
    return render_to_response('index.html', context_instance=RequestContext(request, {'idealist': ideas, 'commentlist': dict}))
'''
    #return render_to_response('.html', context_instance=RequestContext(request))
    

def index(request):
    idea_db = Idea.objects.all().order_by('idea_last_activity').reverse()
    limit = len(Idea.objects.all())
    i = 0
    ideas = []
    while i <= limit-1:
        url = '/idea/' + str(idea_db[i].id) + '/'
        ideas.append({'idea_title': idea_db[i].idea_title, 'idea_text': idea_db[i].idea_text, 'idea_url': url})
        i = i+1
    '''
    dict = {}
    for i,each in enumerate(ideas):
        dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
    '''
    return render(request, 'index.html', {'idealist': ideas})
        #return render_to_response('index.html', context_instance=RequestContext(request, ))

def idea(request, offset):
    try:
        offset = int(offset)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_info = form.cleaned_data
                comment_text_form = comment_info['comment_text']
                comment_agree_form = 1 #placeholder
                idea_id_form = int(offset)
                comment = Comment(comment_text = comment_text_form, comment_agree = comment_agree_form, idea_id = idea_id_form)
                comment.save()
                url = '/idea/' + str(offset)
                return HttpResponseRedirect(url)
        else:
            idea = Idea.objects.get(id=offset)
            idea_title = idea.idea_title
            idea_text = idea.idea_text
            #comments = idea.comment_set.all()
            comments = Comment.objects.filter(idea_id=offset).reverse()
            form = CommentForm
    except ValueError:
        raise Http404()
    return render(request, 'idea.html', {'idea_title': idea_title, 'idea_text': idea_text, 'comments': comments, 'form': form})



#basic html/css
#fix template inheritance
#figure out more of general direction of site, 
#https://devcenter.heroku.com/articles/s3-upload-python
#install django south
    
