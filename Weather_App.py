from tkinter import *
from PIL import ImageTk, Image
from  tkinter import  messagebox
from configparser import ConfigParser
import  requests

app=Tk()
app.title("weather App")
app.iconbitmap('weather_icon.ico')
app.geometry("400x300")
app.configure(background='powder blue')

taps=Frame(app,bg='cadet blue',pady=2,width=1000,height=1000,relief=RIDGE)
#taps.grid(row=0,column=0)

'''
mycanvas=Canvas(app,width=730,height=480)
imagee=ImageTk.PhotoImage(Image.open('back_weather.jpg'))
mycanvas.create_image(0,0,anchor=NW,image=imagee)
mycanvas.pack()
'''

url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
configr=ConfigParser()
configr.read(config_file)
api_key=configr['api_key']['key']
#=========creat fonftions===========

def search():
    global image
    city=city_txt.get()
    weather=get_weather(city)
    if weather:
        location_lbl['text']='{},{}'.format(weather[0],weather[1])
#        image['bitmap']=open('weather_icons/{}@2x.png'.format(weather[4],'r'))
#        image['bitmap']=ImageTk.PhotoImage(image=Image.open(f"weather_icons/{weather[4]}@2x.png"))

        img1=ImageTk.PhotoImage(image=Image.open(f"weather_icons/{weather[4]}@2x.png"))
        lbl = Label(image=img1,width=68,height=52)
        lbl.image = img1
        lbl['bg']='powder blue'
        lbl.grid(row=3,column=1)


        temp_lbl['text']='{:.2f}°C,{:.2f}°F'.format(weather[2],weather[3])
        weather_lbl['text']=weather[5]
    else:
        messagebox.showerror('Error','cannot Find city {}'.format(city))

def get_weather(city):
    result=requests.get(url.format(city,api_key))
    if result :
        #(city,country,temp_selsieus,temp_fahreheit,icon,weather)
        json=result.json()
        city=json['name']
        country=json['sys']['country']
        temp_k=json['main']['temp']
        temp_sel=temp_k-273.15
        temp_fah=(temp_k-273.15)*9/5+32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        final=(city,country,temp_sel,temp_fah,icon,weather)
        return final
    else:
        return None



chose_lbl=Label(app,text="Chose the city :",font=('bold',15),bg='powder blue')
#chose_lbl.pack(pady=10)
chose_lbl.grid(row=0,column=0,padx=17,pady=17)

#chose_lbl=mycanvas.create_text(360,100,text='Chose the city :',font=('bold',15))

city_txt=StringVar()
city_entry=Entry(app,textvariable=city_txt)
#city_entry.pack()
city_entry.grid(row=0,column=1)

search_btn=Button(app,text='Search Weather',width=12,command=search)
#search_btn.pack(pady=20)
search_btn.grid(row=1,column=1)

#button_window=mycanvas.create_window(360,140,anchor='nw',window=search_btn)

location_lbl=Label(app,text='',font=('Times',20,'bold'),bg='powder blue')
#location_lbl.pack()
location_lbl.grid(row=2,column=1)

#location_lbl=mycanvas.create_text(360,140,text='',font=('Times',20))

image=Label(app,bitmap='')
#image.pack()
#image=mycanvas.create_text(360,145,text='')

temp_lbl=Label(app,text='',font=('Times',12,'bold'),bg='powder blue')
#temp_lbl.pack(pady=5)
temp_lbl.grid(row=4,column=1)

#temp_lbl=mycanvas.create_text(360,150,text='',font=('Times',10))

weather_lbl=Label(app,text='',font=('bold',10),underline=1,bg='powder blue')
#weather_lbl.pack()
weather_lbl.grid(row=5,column=1)
#weather_lbl=mycanvas.create_text(360,160,text='',font=(10))

app.mainloop()