from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#tworzenie funkcji pobiera i zwraca wartość uzyskaną dzieki innej funkcji która renderuje szablon html

