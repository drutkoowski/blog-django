from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from django.urls import reverse
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View


# Create your views here.


# class StartingPageView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     ordering = ["-date"]
#     context_object_name = "posts"
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data
#
# class AllPostView(ListView):
#     template_name = "blog/all-posts.html"
#     model = Post
#
#
# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })
#
#
# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all(),
#     })

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", context={
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        else:
            return render(request, "blog/post-detail.html", context={
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by("-id"),
            })
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context
