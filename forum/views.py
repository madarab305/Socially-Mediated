from django.shortcuts import render
from .models import Post
# Create your views here.

def list_view(request):
	object_list = Post.objects.all()
	context = {
	"post_list":object_list,
	}
	return render (request, "list.html", context)

def detail_view(request, p_id):
	detail = Post.objects.get(id=p_id)
	context = {
	"post":detail,
	}
	
	return render (request, "detail.html", context)

