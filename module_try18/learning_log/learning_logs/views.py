from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics' : topics}
	return render (request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	#checking the request send from the current user
	if topic.owner !=request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	""" adding new topic"""
	if request.method != 'POST':
		#unpush data: creating a new list
		form = TopicForm()
	else:
		#POST upload data, and process it
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	
	context ={'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""adding new entry"""
	topic = Topic.objects.get(id=topic_id)

	if request.method !='POST':
		#create a empty form
		form = EntryForm()
	else:
		#POST upload data, and processing it
		form = EntryForm(data = request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic':topic, 'form':form}
	return render(request,'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""edit the entry"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner !=request.user:
		raise Http404

	if request.method !='POST':
		#initial request, using the current form
		form = EntryForm(instance = entry)
	else:
		#POST upload the data, and process the data
		form= EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic.id]))

	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)

