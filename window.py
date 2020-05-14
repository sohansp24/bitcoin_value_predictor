from tkinter import Button,Label,Entry,Tk,Canvas,PhotoImage,Frame,TOP,BOTTOM,BOTH
from datetime import timedelta,date
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure


def refresh(data):
        img1.destroy()
        L1.destroy()
        L2.destroy()
        for widget in F1.winfo_children():
                widget.destroy()
        for widget in F2.winfo_children():
                widget.destroy()
        for widget in F3.winfo_children():
                widget.destroy()
        for widget in F4.winfo_children():
                widget.destroy() 
        user_input(data)
    
    
def displaytext(arr,p,q):
    l=len(arr)
    for i in range(l):
        L3=Label(canvas,text=arr[i],font=('verdana',15),background="#67B6A7",fg="yellow")
        L3.place(x=p,y=q)
        q=q+40



def user_input(data):
        master =Tk()
        master.config(background="#67B6A7",)
        master.geometry('300x200')
        master.title("Enter the values")
        Label(master, text="Open Value : ",font=('verdana',13),background="#67B6A7").place(x=5,y=10)
        Label(master, text="Close Value : ",font=('verdana',13),background="#67B6A7").place(x=5,y=45)
        Label(master, text="Min Value : ",font=('verdana',13),background="#67B6A7").place(x=5,y=80)
        Label(master, text="Max Value : ",font=('verdana',13),background="#67B6A7").place(x=5,y=115)
        E1=Entry(master,relief='flat',bd=5,width=10)
        E1.place(x=150,y=10)
        E2=Entry(master,relief='flat',bd=5,width=10)
        E2.place(x=150,y=45)
        E3=Entry(master,relief='flat',bd=5,width=10)
        E3.place(x=150,y=80)
        E4=Entry(master,relief='flat',bd=5,width=10)
        E4.place(x=150,y=115)
        master.geometry('+{}+{}'.format(500,300)) 
        Button(master,text=" Submit ",relief="raised",bd=3,font="Verdana",background="#A3BCB7",cursor="hand2",command=lambda :graph(data,master,E1.get(),E2.get(),E3.get(),E4.get(),1)).place(x=125,y=150)
        master.mainloop()

def graph(data,master=None,open=0,close=0,min=0,max=0,flag=0):
        if(master!=None):
            master.destroy()
            newframe=pd.DataFrame({'Date':[data['Date'][0]+1],'Open':[float(open)],'Close':[float(close)],'High':[float(max)],'Low':[float(min)]})
            data=newframe.append(data,ignore_index=True)
        output=main(data)[0]
        # ploting Open Graph
        fig1 = Figure(figsize=(6.0,2.39), dpi=100)
        fig1.add_subplot(111).plot(data['Date'].iloc[:300],data['Open'].iloc[:300])
        c1 = FigureCanvasTkAgg(fig1, F1)  
        c1.draw()
        c1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #navigation toolbar
        toolbar1 = NavigationToolbar2Tk(c1,canvas)
        toolbar1.update()
        toolbar1.place(x=200,y=100)
        
        #ploting Close Graph
        fig2 = Figure(figsize=(6.0,2.39), dpi=100)
        fig2.add_subplot(111).plot(data['Date'].iloc[:300],data['Close'].iloc[:300])
        c2 = FigureCanvasTkAgg(fig2, F2)  
        c2.draw()
        c2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #navigation toolbar
        toolbar2 = NavigationToolbar2Tk(c2,canvas)
        toolbar2.update()
        toolbar2.place(x=900,y=100)
        
        #ploting Min Graph
        fig3 = Figure(figsize=(6.0,2.39), dpi=100)
        fig3.add_subplot(111).plot(data['Date'].iloc[:300],data['Low'].iloc[:300])
        c3 = FigureCanvasTkAgg(fig3, F3) 
        c3.draw()
        c3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #navigation toolbar
        toolbar3 = NavigationToolbar2Tk(c3,canvas)
        toolbar3.update()
        toolbar3.place(x=200,y=635)

        #ploting Max Graph
        fig4 = Figure(figsize=(6.0,2.39), dpi=100)
        fig4.add_subplot(111).plot(data['Date'].iloc[:300],data['High'].iloc[:300])
        c4 = FigureCanvasTkAgg(fig4, F4) 
        c4.draw()
        c4.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #navigation toolbar
        toolbar4 = NavigationToolbar2Tk(c4,canvas)
        toolbar4.update()
        toolbar4.place(x=900,y=635)
        if(status(output)):
                flag1=1
                path='upward_big.png'
        else:
                flag1=0
                path='downward_big.png'
        global img1,L1,L2
        img=PhotoImage(master=canvas,file=path)
        img1=Label(canvas,image=img)
        img1.image=img
        img1.place(x=1280,y=10)
        L1=Label(canvas, text="Overall result -",font=('verdana',11,'bold'),background="#67B6A7")
        L1.place(x=1100,y=10)
        if(flag1==1):
                L2=Label(canvas, text=str("Increment ratio :  "+change(output)+"%"),font=('verdana',11,'bold'),background="#67B6A7")
                L2.place(x=1050,y=40)
        else:
                L2=Label(canvas, text=str("Decrement ratio :  "+change(output)+"%"),font=('verdana',11,'bold'),background="#67B6A7")
                L2.place(x=1050,y=40)  
        for i in range(4):

                if(i==0):
                        if (float(str(data['Open'][0])[:8])) < (float(str(output['Open'][0])[:8])):
                                decideupordown(0,5,90,F1)
                        else:
                                decideupordown(1,5,130,F1)
                elif(i==1):
                        if (float(str(data['Close'][0])[:8])) < (float(str(output['Close'][0])[:8])):
                                decideupordown(0,550,90,F2)
                        else:
                                decideupordown(1,550,130,F2)
                elif(i==2):
                        if (float(str(data['Low'][0])[:8])) < (float(str(output['Low'][0])[:8])):
                                decideupordown(0,5,90,F3)
                        else:
                                decideupordown(1,5,130,F3)
                else:
                        if (float(str(data['High'][0])[:8])) < (float(str(output['High'][0])[:8])):
                                decideupordown(0,550,90,F4)
                        else:
                                decideupordown(1,550,130,F4)
        alert(output,flag)

def alert(output,flag):
        master=Tk()
        today=date.today()
        if(flag==1):
                tomorrow=today+timedelta(days=1)
                msg="Predicted values for {}/{}/{} ".format(tomorrow.day,tomorrow.month,tomorrow.year)
        else:
                msg="Predicted values for {}/{}/{} ".format(today.day,today.month,today.year)
        master.config(background="#67B6A7",)
        master.geometry('330x200')
        master.title(msg)
        Label(master, text="Open Value : ",font=('verdana',13),background="#67B6A7").place(x=50,y=10)
        Label(master, text="Close Value : ",font=('verdana',13),background="#67B6A7").place(x=50,y=45)
        Label(master, text="Min Value : ",font=('verdana',13),background="#67B6A7").place(x=50,y=80)
        Label(master, text="Max Value : ",font=('verdana',13),background="#67B6A7").place(x=50,y=115)
        Label(master, text=str(output['Open'][0])[:8],font=('verdana',13),background="#67B6A7").place(x=200,y=10)
        Label(master, text=str(output['Close'][0])[:8],font=('verdana',13),background="#67B6A7").place(x=200,y=45)
        Label(master, text=str(output['Low'][0])[:8],font=('verdana',13),background="#67B6A7").place(x=200,y=80)
        Label(master, text=str(output['High'][0])[:8],font=('verdana',13),background="#67B6A7").place(x=200,y=115)
        master.geometry('+{}+{}'.format(500,300)) 
        Button(master,text=" Okay ",relief="raised",bd=3,font="Verdana",background="#A3BCB7",cursor="hand2",command=master.destroy).place(x=125,y=150)
        master.mainloop()

                    
def decideupordown(flag,p,q,root):
        if(flag==1):
                path='downward.png'
        else:
                path='upward.png'
        img=PhotoImage(master=root,file=path)
        i=Label(root,image=img)
        i.image=img
        i.place(x=p,y=q)

def status(output):
        if(float(output['Open'])-float(output['Close'])>0):
                return False
        else:
                return True
    
def change(data):
        return str(((float(data['Close'])-float(data['Open']))*100.0/float(data['Open'])))[:5]

def main(data):
        temp=len(data)
        data['Date']=list(range(temp,0,-1))
        data=data[data['Open']>1000]
        X=data['Date'].values.reshape(-1,1)
        Y_High=data['High'].values.reshape(-1,1)
        Y_Low=data['Low'].values.reshape(-1,1)
        Y_Close=data['Close'].values.reshape(-1,1)
        output={}
        output['Open']=1+np.random.random_sample(1)+data['Close'][[0]]
        test_case=np.array(temp+1).reshape(-1,1)

        #Randomtree model
        ran_high=RandomForestRegressor(n_estimators=300)
        ran_high.fit(X,Y_High)
        ran_low=RandomForestRegressor(n_estimators=300)
        ran_low.fit(X,Y_Low)
        ran_close=RandomForestRegressor(n_estimators=300)
        ran_close.fit(X,Y_Close)

        #Decision model
        des_high=DecisionTreeRegressor()
        des_high.fit(X,Y_High)
        des_low=DecisionTreeRegressor()
        des_low.fit(X,Y_Low)
        des_close=DecisionTreeRegressor()
        des_close.fit(X,Y_Close)
        output['High']=sum(ran_high.predict(test_case),des_high.predict(test_case))/2.0
        output['Low']=sum(ran_low.predict(test_case),des_low.predict(test_case))/2.0
        output['Close']=sum(ran_close.predict(test_case),des_close.predict(test_case))/2.0

        return [output]


#execution starts here
root=Tk()
global canvas,F1,F2,F3,F4
data=pd.read_csv("bitcoin.csv")

temp=len(data)
test=pd.read_csv("bitcoin_test.csv")
test['Date']=list(range(len(test)+temp,temp,-1))
root.title("BitCoin Value Predictor")
canvas=Canvas(root,height="768",width="1366",background="#67B6A7")
L1=Label(canvas,text="BitCoin Value Predictor",font=("Lucida Calligraphy",35),background="#67B6A7")
L1.place(x=400,y=10)
F1=Frame(canvas,cursor="dot",width="600",height="240")
F1.place(x=50,y=140)
F2=Frame(canvas,cursor="dot",width="600",height="240")
F2.place(x=690,y=140)
F3=Frame(canvas,cursor="dot",width="600",height="240")
F3.place(x=50,y=390)
F4=Frame(canvas,cursor="dot",width="600",height="240")
F4.place(x=690,y=390)
for i in range(4):
        if(i==0):
                arr=['O','P','E','N']
                x=30
                y=170
        elif(i==1):
                arr=['C','L','O','S','E']
                x=1295
                y=170
        elif(i==2):
                arr=['L','O','W']
                x=26
                y=450
        else:
                arr=['H','I','G','H']
                x=1295
                y=450
        displaytext(arr,x,y)

B1=Button(canvas,text=" Predict ",relief="raised",bd=3,height=1,width=5,font="Verdana",command=lambda : refresh(data),background="#A3BCB7",cursor="hand2")
B1.place(x=630,y=640)
canvas.pack()
graph(data)
root.mainloop()

