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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_info = form.cleaned_data
            comment_info_form = comment_info['comment_text']
            comment_upvote_form = 0
            comment_stuff = Comment(comment_text=comment_info_form, comment_agree=comment_upvote_form)
            comment_stuff.save()
            ideas = Idea.objects.all().order_by('idea_last_activity').reverse()[0:4]
            dict = {}
            for i,each in enumerate(ideas):
                dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
    
            return render_to_response('index.html', context_instance=RequestContext(request, {'idealist': ideas, 'commentlist': dict, 'form': form}))
    else:
        idea_db = Idea.objects.all().order_by('idea_last_activity').reverse()
        ideas = [idea_db.idea_title, idea_db.idea_text, idea_db.id]
        '''
        dict = {}
        for i,each in enumerate(ideas):
            dict[ideas[i].id] = Comment.objects.filter(idea=ideas[i])
        '''
        return render(request, 'index.html', {'idealist': ideas})
        #return render_to_response('index.html', context_instance=RequestContext(request, ))
