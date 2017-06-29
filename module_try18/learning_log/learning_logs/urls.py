from django.conf.urls import url

from . import views

urlpatterns = [
	#index
	url(r'^$', views.index, name='index'),

	# showing all topics
	url(r'^topics/$', views.topics, name = 'topics'),

	#detail for the topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# for adding new topic to the web
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),

	# for adding new entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# for editing the entry
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]