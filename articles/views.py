from django.shortcuts import render
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.all()
    return render(
        request,
        'articles.html',
        {'articles': articles}
    )


def show_article(request, id):
    article = Article.objects.get(pk=id)
    context = dict()
    context['title'] = article.title
    context['image'] = article.image

    if request.user.is_authenticated:
        user_subs = Profile.objects.get(user_id=request.user).has_subs
    else:
        user_subs = False

    if article.paid_article != False and user_subs != True:
        context['text'] = 'Статья для платных пользователей!'
    else:
        context['text'] = article.text


    return render(
        request,
        'article.html',
        context
    )

def show_home(request):
    return render(request=request, template_name='home.html')

