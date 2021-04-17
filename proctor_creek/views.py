from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import pyrebase
from django.views import View
from .forms import Report

# Create your views here.
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
    "apiKey": "AIzaSyBnh3EsTetGpOzDeGUXuQsT7Q-oF8fu1mU",
    "authDomain": "proctor-creek-capstone-project.firebaseapp.com",
    "projectId": "proctor-creek-capstone-project",
    "storageBucket": "proctor-creek-capstone-project.appspot.com",
    "messagingSenderId": "1099094981367",
    "appId": "1:1099094981367:web:74525f31783efc681971f2",
    "measurementId": "G-04YP1GBKLL",
    "databaseURL": "https://proctor-creek-capstone-project-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
db = firebase.database()

class IndexView(View):

    def get(self, request):
        mem1 = db.child('Member 1').get().val()
        mem2 = db.child('Member 2').get().val()
        mem3 = db.child('Member 3').get().val()
        mem4 = db.child('Member 4').get().val()
        mem5 = db.child('Member 5').get().val()
        context = {
            "mem1": mem1,
            "mem2": mem2,
            "mem3": mem3,
            "mem4": mem4,
            "mem5": mem5
        }
        return render(request, 'proctor_creek/index.html', context)

    def post(self, request):

        # get formatted string of date and time
        from datetime import datetime
        current_time = datetime.now().strftime("%Y/%B/%d/%H:%M:%S")

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = Report(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # get data from input tags in html with these names
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                # type = form.cleaned_data['type']
                summary = form.cleaned_data['summary']

                # create a dictionary to push to db
                data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "phone": phone,
                    # 'type': type,
                    "summary": summary
                }

            # db.child('Reports').child(type).child(current_time).set(data)
            db.child('Unresolved Reports').child(current_time).set(data)

        return redirect('index')