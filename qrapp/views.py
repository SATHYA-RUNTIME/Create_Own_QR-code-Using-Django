from django.shortcuts import render
import pyqrcode
import png
import os
# Create your views here.
def qr(request):
    path1=""
    if request.method=="POST":
        content=request.POST['data']
        qr=pyqrcode.create(content)
        ln=len(content)
        path1=str(ln)+".png"
        path=os.path.join("sta/img",path1)
        qr.png(path,scale=8)
        path2=ln
        return render(request,"qr.html",{"fnme":path2,"path":"path"})
    if request.method=="POST":    
        os.remove(path1)
    return render(request,"home.html")

def qrimg(request):
    return render(request,"qr.html")

