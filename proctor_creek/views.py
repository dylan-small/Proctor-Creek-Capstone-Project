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

class ReportView(View):

    def get(self, request):

        return render(request, 'proctor_creek/report.html')

    def post(self, request):

        # get formatted string of date and time
        from datetime import datetime
        report_number = datetime.now().strftime("%Y/%m%d%y%H%M%S")

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
                problem_type = form.cleaned_data['problem_type']
                summary = form.cleaned_data['summary']
                image = form.cleaned_data['image']

                report_datetime = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

                # create a dictionary to push to db
                data = {
                    "date": report_datetime,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "phone": phone,
                    'problem_type': problem_type,
                    "summary": summary,
                    "image": image
                }

                # db.child('Unresolved Reports').child(problem_type).child(current_time).set(data)
                db.child('Unresolved Reports').child(problem_type).child(report_number).set(data)

        return redirect('report')