from django.shortcuts import render

posts = [
    {
        'author': 'Aidan Victor George Pratt',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2024'
    },
    {
        'author': 'Adel Ashcroft',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2024'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


