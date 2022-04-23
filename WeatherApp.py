from tkinter import*
from tkinter import messagebox
import requests


root=Tk()
root.title("Wheather App")
root.geometry("900x600")
root.config(bg="#d5fdfa")
root.resizable(0,0)

#*********************************************************

def get_weather():

    try:
        global city
        global description
        city=search_entry.get()
        city=city.capitalize()

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        data=requests.get(api).json()


        temp=int(data['main']['temp']-273.15)
        temp=str(temp)

        description=str(data["weather"][0]["description"])
        description=description.capitalize()
        wind=str(data["wind"]["speed"])
        humidity=str(data["main"]["humidity"])
        pressure=str(data["main"]["pressure"])

        temphigh=int(data["main"]["temp_max"]-273.15)
        # temphigh=float("{:.2f}".format(temphigh))
        temphigh=str(temphigh)
        templow=int(data["main"]["temp_min"]-273.15)
        # templow=float("{:.2f}".format(templow))
        templow=str(templow)

        # feel_like=int(data["main"]["feels_like"])-273.15
        feel_like=int(data["main"]["feels_like"]-273.15)
        feel_like=float("{:.2f}".format(feel_like))
        feel_like=str(temphigh)

        l2.config(text=city)
        tem_l.config(text=temp+"\u00b0")
        des_l.config(text=description+" | "+"Feels Like "+feel_like+"\u00b0")
        l_windspeed.config(text=wind+"km/h")
        l_humidity.config(text=humidity+"%")
        l_pressure.config(text=pressure+"mbar")
        l_temhigh.config(text=temphigh+"\u00b0")
        l_templow.config(text=templow+"\u00b0")
        
    except:
        messagebox.showerror("Weather App","Invalid Entry")


#*****************************************************************************************


bg_load=PhotoImage(file=r"images/searchbar.png")
bg=bg_load.subsample(3,3)
back=Label(root,image=bg,bg="#d5fdfa")
back.place(x=50,y=1,height=100)

sbn_load=PhotoImage(file=r"images/searchbn.png")
sbn=sbn_load.subsample(15,15)
seaech_button=Button(root,image=sbn,bg="grey",activebackground="grey",borderwidth=0,command=get_weather)
seaech_button.place(x=219,y=32)

search_entry=Entry(root,font=(10),bg="grey",fg="white",borderwidth=0,cursor="hand2")
search_entry.place(x=65,y=32,height=34,width=150)
search_entry.focus()




tem_l=Label(root,text="0\u00b0",font=('Courier',100,'bold'),fg="red",bg="#d5fdfa")
tem_l.place(x=500,y=40)

des_l=Label(root,text=" --- | Feels Like  ---",font=('Arial',20,'bold'),fg="#bb22ff",bg="#d5fdfa")
des_l.place(x=450,y=175)

l1=Label(root,text="CURRENT WEATHER",font=('Courier',27,'bold'),fg="#0c090a",bg="#d5fdfa")
l1.place(x=30,y=110)

l2=Label(root,text="---",font=('Arial',50,'bold'),fg="green",bg="#d5fdfa")
l2.place(x=90,y=150)

#****************************************************************************************
#***************************************************************************************


bar_load=PhotoImage(file=r"images/bar.png")
bar=bar_load.subsample(2,2)
bar_l=Label(root,image=bar,font=('Courier',100,'bold'),fg="red",bg="#d5fdfd")
bar_l.place(x=40,y=280,relheight=0.5,relwidth=0.9)


l_windspeed=Label(root,text="--",bg="#8ab5d4",font=('Courier',25,'bold'))
l_windspeed.place(x=240,y=370)


l_humidity=Label(root,text="--",bg="#8ab5d4",font=('Courier',25,'bold'))
l_humidity.place(x=250,y=490)


l_pressure=Label(root,text="--",bg="#8ab5d4",font=('Courier',19,'bold'))
l_pressure.place(x=590,y=325)


l_temhigh=Label(root,text="--",bg="#8ab5d4",font=('Courier',25,'bold'))
l_temhigh.place(x=590,y=400)


l_templow=Label(root,text="--",bg="#8ab5d4",font=('Courier',25,'bold'))
l_templow.place(x=590,y=480)



root.mainloop()
