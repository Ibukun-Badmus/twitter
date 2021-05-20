from django.shortcuts import render, redirect
from polls.models import Tweet
from .forms import TweetForm


# Create your views here.
def home(request):
    tweets = Tweet.objects.all()

    context = {
        "tweets": tweets
    }

    return render(request, "polls/index.html", context)


def create_tweet(request):
    if request.method != "POST":
        form = TweetForm()
    else:
        form = TweetForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("polls:home")

    context = {"form": form}
    return render(request, "polls/new_tweet.html", context)
