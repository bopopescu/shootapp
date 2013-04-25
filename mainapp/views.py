from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, Context
from mainapp.models import *
import datetime


def submit(request):
    if request.method == 'POST':
        idea_title_form = request.POST['idea_title']
        idea_text_form = request.POST['idea_text']
        idea_created_form = datetime.datetime.now()
        idea_last_activity_form = datetime.datetime.now()
        idea = Idea(idea_title=idea_title_form, idea_text=idea_text_form, idea_created=idea_created_form, idea_last_activity=idea_last_activity_form)
        idea.save()
        ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
        dict = {}
        for i,each in enumerate(ideas):
            dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
            c = {'idealist': ideas, 'commentlist': dict}
        return render_to_response('submit.html', context_instance=RequestContext(request))
    else:
        return render_to_response('submit.html', context_instance=RequestContext(request))

    '''
    return render_to_response('index.html', context_instance=RequestContext(request, {'idealist': ideas, 'commentlist': dict}))
'''
    #return render_to_response('.html', context_instance=RequestContext(request))
    

def index(request):
    
#    ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
#    allcomments = Context()
#    i = 0
#    while i < len(ideas):
#        comments = Comment.objects.filter(idea=ideas[i])
#        allcomments[ideas[i].id] = comments
#        i = i+1
#
#    return render(request, 'index.html', {'ideaslist':ideas, 'commentlist':allcomments})

    ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
    dict = {}
    for i,each in enumerate(ideas):
        dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
    
    return render_to_response('index.html', context_instance=RequestContext(request, {'idealist': ideas, 'commentlist': dict}))
