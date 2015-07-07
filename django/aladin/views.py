from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Aladin

def parse_that(url, format="csv"):
    from .pocasi import Aladin
    aladin = Aladin(url)
    aladin.collection()
    
    res = ""
    if format == "csv":
        res = aladin.data.to_csv(None)
    elif format == "json":
        res = aladin.data.to_json(None)
    else:
        res = aladin.data.to_csv(None)

    return res

def get_urlofpic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = Aladin(request.POST)
        if form.is_valid():
            url = form.data["urlOfPic"]
            out_format = form.data["out_format"]
            kod = form.data["kod"]
            cas = form.data["cas"]
            varianta = form.data["varianta"]
            
            if not varianta:
                print("Generuju dle vyberu")
                initc = "http://www.chmi.cz/files/portal/docs/meteo/ov/aladin/results/public/meteogramy/data/"
                url = initc + cas + "/" + str(kod) + ".png"
            data = parse_that(url, out_format)
            return render(request, 'result.html', {"data": data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Aladin()
    return render(request, 'aladin.html', {'form': form})
