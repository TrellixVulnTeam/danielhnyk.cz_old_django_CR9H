from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Aladin

def get_urlofpic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Aladin(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.urlOfPic
            return render(request, 'result.html')
#            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Aladin()

    return render(request, 'aladin.html', {'form': form})
