from django.shortcuts import render
import matplotlib.pyplot as plt



# Create your views here.
def index(request):
    xbar=["HTML","CSS","JAVASCRIPT","NODE.JS","EXPRESS","MYSQL","MONGODB","DAJNGO"]
    ybar=[60,60,70,70,70,65,70,50]  
    plt.bar(xbar,ybar)
    
    # Save the plot image in the static directory
    plt.savefig('skill2.png')
    plt.close()
    context={
        "skillimg":"skill2.png",
    }
    return render(request , "index.html",context)