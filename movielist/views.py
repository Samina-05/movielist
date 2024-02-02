from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm
import requests
from django.http import JsonResponse

def hello(request):
    return render(request,'hello.html')


def get_movie_name(request):
    api_key = 'a1dbeb53238770ea605b31c3346c696f'
    base_url = "https://api.themoviedb.org/3/search/movie"
    query = request.GET.get('query', '')  # Get search query from request parameters
    if not query:
        return render(request, 'movielist.html', {'error': 'Please provide a search query'})

    params = {
        'api_key': api_key,
        'query': query,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        movie_results = [{'title': movie['title'], 'id': movie['id']} for movie in data.get('results', [])]
        return render(request, 'movielist.html', {'movies': movie_results})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error fetching data from TMDb: {e}'})
    
    
    
    
'''
def home(request):
    
    form = MovieForm()

    if request.method == 'POST':
        form =MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['name']
            movie_data = get_movie_name(movie_name)
            context = {'form': form, 'movie_data': movie_data}
            return render(request, 'movielist.html', context)

    context = {'form': form}
    return render(request, 'movielist.html', context)
'''