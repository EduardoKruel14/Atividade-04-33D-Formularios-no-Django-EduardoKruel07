from django.shortcuts import render, redirect
from.models import TopMovies, MoviesILike

# Create your views here.
def home(request):
  movies = TopMovies.objects.all()
  Like = MoviesILike.objects.all()
  return render(request,"home.html",
context={"movies": movies,'Like':Like})

def create_TopMovies(request):
  if request.method=='POST':
    TopMovies.objects.create(
        title= request.POST['title'],
        director= request.POST['director'],
        genre= request.POST['genre'],
        release_date= request.POST['release_date'],
      )
    return redirect("home")
  return render(request, 'forms.html', context={'action':'Adicionar'})


def update_TopMovies(request, id):
  movie=TopMovies.objects.get(id=id)
  if request.method=='POST':
    movie.title= request.POST['title']
    movie.director= request.POST['director']
    movie.genre= request.POST['genre']
    movie.release_date= request.POST['release_date']
    movie.save()
      
    return redirect("home")
  return render(request, 'forms.html',context={'action':'Atualizar','movie':movie})

def delete_TopMovies(request, id):
  movie=TopMovies.objects.get(id=id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      movie.delete()
    
      
    return redirect("home")
  return render(request, 'are_you_sure.html',context={'action':'Atualizar','movie':movie})



def create_MoviesILike(request):
  if request.method=='POST':
    MoviesILike.objects.create(
        title= request.POST['title'],
       
        
      )
    return redirect("home")
  return render(request, 'forms.html')

def update_MoviesILike(request, id):
  movie=MoviesILike.objects.get(id=id)
  if request.method=='POST':
    movie.title= request.POST['title']
    movie.save()
      
    return redirect("home")
  return render(request, 'forms.html',context={'action':'Atualizar','movie':movie})

def delete_MoviesILike(request, id):
  movie=MoviesILike.objects.get(id=id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      movie.delete()
    
      
    return redirect("home")
  return render(request, 'are_you_sure.html',context={'action':'Atualizar','movie':movie})