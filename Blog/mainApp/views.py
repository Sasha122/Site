from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'mainApp/homePage.html')
def contact(request):
    return render(request , 'mainApp/Contact.html' , {'values': ['GameDevX Следеите за нами на наешм сайте , если есть вопросы задавайте по email' , 'motyrev2004@mail.ru']})
def log_in(request):
    return render(request , 'mainApp/Login.html')
def makeNews(request):
    return  render(request, 'MkNews/mk.html')

def post_new(request):
    form = PostForm()
    return render(request, 'main_app/post_edit.html', {'form': form})