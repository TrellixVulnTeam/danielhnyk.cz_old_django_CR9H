from django import forms

def get_codes():
    import json
    with open("aladin/kody.json", "r") as ifile:
        r = json.load(ifile)
    return r

def get_last_time():

    import datetime
    date = datetime.date.today().strftime("%Y%m%d")

    import time
    hours = str((int(time.strftime("%H")) % 6) * 6)
    
    if len(hours) < 2:
        hours = "0" + hours
    
    return date + hours

class Aladin(forms.Form):
    
    cas = get_last_time()

    urlOfPic = forms.URLField(initial="http://www.chmi.cz/files/portal/docs/meteo/ov/aladin/results/public/meteogramy/data/{}/351.png".format(cas), label='URL pole obrázku')

    out_format = forms.ChoiceField(choices=[("json", "JSON"), ("csv","CSV")], label="Formát výstupu")
    kod = forms.ChoiceField(choices=get_codes(), label="Kód města")

    cas = forms.ChoiceField(choices=((cas,cas),), label="Čas")
    varianta = forms.ChoiceField(choices=((True,"Použít URL"),(False, "Použít výběr pomocí nabídek")), label="varianta")
