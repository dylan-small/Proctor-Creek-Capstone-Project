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
        day = database.child('Data').child('Day').get().val()
        id = database.child('Data').child('Id').get().val()
        projectname = database.child('Data').child('Projectname').get().val()
        context = {"day": day, "id": id, "projectname": projectname}
        return render(request, 'proctor_creek/index.html', context)
