from django.shortcuts import render
import pyrebase
from django.views import View

# Create your views here.
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  apiKey: "AIzaSyBnh3EsTetGpOzDeGUXuQsT7Q-oF8fu1mU",
  authDomain: "proctor-creek-capstone-project.firebaseapp.com",
  projectId: "proctor-creek-capstone-project",
  storageBucket: "proctor-creek-capstone-project.appspot.com",
  messagingSenderId: "1099094981367",
  appId: "1:1099094981367:web:74525f31783efc681971f2",
  measurementId: "G-04YP1GBKLL"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

class IndexView(View):

    def home(self, request):
        mem1 = database.child('Member 1').get().val()
        mem2 = database.child('Member 2').get().val()
        mem3 = database.child('Member 3').get().val()
        mem4 = database.child('Member 4').get().val()
        mem5 = database.child('Member 5').get().val()
        context = {
            "mem1": mem1,
            "mem2": mem2,
            "mem3": mem3,
            "mem4": mem4,
            "mem5": mem5
        }
        return render(request, 'proctor_creek/index.html', context)
