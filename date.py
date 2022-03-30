import os
import sys
import datetime
class datebro():
    def year():
        selfx = datetime.datetime.now()
        selfb=os.path.dirname(os.path.abspath(sys.argv[0]))
        
        try:
            g=os.path.join(selfb,str(selfx.year))
            try:
                os.makedirs(r"{}".format(g))
            except:
                pass
            return(r"{}".format(g))
        except:
            print("Folder already exist")
            pass
    def month():
        selfx = datetime.datetime.now()
        selfb=os.path.dirname(os.path.abspath(sys.argv[0]))

        a=datebro.year()
        try:
            g=os.path.join(a,str(selfx.month))
            os.makedirs(r"{}".format(g))
            return(r"{}".format(g))
        except:
            print("Folder already exist")
            pass
datebro.month()
def givepath():
    checker=datebro.month()
    if checker is None:
        x = datetime.datetime.now()
        b=os.path.dirname(os.path.abspath(sys.argv[0]))
        g=os.path.join(b,str(x.year))
        b=os.path.join(g,str(x.month))
        return b
    else:
        return checker
def dategive():
    today = datetime.date.today() 
    return(str(today.day))
def givetime():
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    return(t)
