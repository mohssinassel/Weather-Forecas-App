from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox

from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

window = Tk()
window.title("Weather App")
window.geometry("890x470")
image = PhotoImage(file='weatherApp/back_weatherv.png')
label = Label(window,image=image)
label.pack()
window.resizable(False, False)


def getWeather(self):
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=366604cc8bd6c6a4f6ec1b57044ec496"
    # api = f"https://api.openweathermap.org/data/2.5/onecall?q={city}&appid=366604cc8bd6c6a4f6ec1b57044ec496"
    json_data = requests.get(api).json()
    temp = json_data["main"]['temp']
    humidity = json_data["main"]['humidity']
    pressure = json_data["main"]['pressure']
    wind = json_data["wind"]['speed']
    description = json_data['weather'][0]['description']


    t.config(text=(temp - 256, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    fivth = first + timedelta(days=4)
    day5.config(text=fivth.strftime("%A"))
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

    firstdayimage = json_data['weather'][0]['icon']
    tempMin1 = json_data['main']["temp_min"]
    tempMax1 = json_data['main']["temp_max"]
    photo1 = ImageTk.PhotoImage(file=f"weatherApp/icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.Image = photo1
    daytmp.config(text=f"Tmin = {round(tempMin1 - 256)} °C\n\nTmax = {round(tempMax1 - 256)} °C")





    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=366604cc8bd6c6a4f6ec1b57044ec496"
    response = requests.get(url)
    data = response.json()
    forecasts = data["list"]
    i = 6
    icona = []
    tmpMin = []
    tmpMax = []
    for forecast in forecasts:
        if i == 6:
            icona.append(forecast["weather"][0]["icon"])
            tmpMin.append(forecast["main"]["temp_min"])
            tmpMax.append(forecast["main"]["temp_max"])
            i = 0
        else:
            i = i+1

    img1 = (Image.open(f"weatherApp/icon/{icona[0]}@2x.png"))
    resized_image = img1.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.Image = photo2
    day2tmp.config(text=f"Tmin = {round(tmpMin[0] - 256)} °C\nTmax = {round(tmpMax[0] - 256)} °C")


    img2 = (Image.open(f"weatherApp/icon/{icona[1]}@2x.png"))
    resized_image2 = img2.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image2)
    thirdimage.config(image=photo3)
    thirdimage.Image = photo3
    day3tmp.config(text=f"Tmin = {round(tmpMin[1] - 256)} °C\nTmax = {round(tmpMax[1] - 256)} °C")


    img3 = (Image.open(f"weatherApp/icon/{icona[2]}@2x.png"))
    resized_image3 = img3.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image3)
    fourthimage.config(image=photo4)
    fourthimage.Image = photo4
    day4tmp.config(text=f"Tmin = {round(tmpMin[2] - 256)} °C\nTmax = {round(tmpMax[2] - 256)} °C")


    img4 = (Image.open(f"weatherApp/icon/{icona[3]}@2x.png"))
    resized_image4 = img4.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image4)
    fivthimage.config(image=photo5)
    fivthimage.Image = photo5
    day5tmp.config(text=f"Tmin = {round(tmpMin[3] - 256)} °C\nTmax = {round(tmpMax[3] - 256)} °C")


    img5 = (Image.open(f"weatherApp/icon/{icona[4]}@2x.png"))
    resized_image5 = img5.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image5)
    sixthimage.config(image=photo6)
    sixthimage.Image = photo6
    day6tmp.config(text=f"Tmin = {round(tmpMin[4] - 256)} °C\nTmax = {round(tmpMax[4] - 256)} °C")


    img6 = (Image.open(f"weatherApp/icon/{icona[5]}@2x.png"))
    resized_image6 = img6.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image6)
    seventhimage.config(image=photo7)
    seventhimage.Image = photo7
    day7tmp.config(text=f"Tmin = {round(tmpMin[5] - 256)} °C\nTmax = {round(tmpMax[5] - 256)} °C")

    loc.config(text=f"{city}")








icon = PhotoImage(file="weatherApp/weather.png")
window.iconphoto(False, icon)

Round_box = PhotoImage(file="weatherApp/rectangle.png")
Round_box = Round_box.subsample(2, 2)
Label(window, image=Round_box ,bg="black").place(x=30, y=35)

label1 = Label(window, text="Temperature", fg="white", bg="black")
label1.place(x=50, y=100)
label2 = Label(window, text="Humidity", fg="white", bg="black")
label2.place(x=50, y=140)
label3 = Label(window, text="Pressure", fg="white", bg="black")
label3.place(x=50, y=180)
label4 = Label(window, text="Wind Speed", fg="white", bg="black")
label4.place(x=50, y=220)
label5 = Label(window, text="Description", fg="white", bg="black")
label5.place(x=50, y=260)

search_image = PhotoImage(file="weatherApp/moins-grand-symbole.png")

search_img = Label(image=search_image, bg="#00DEFF")
search_img.config(height=70, width=450)

search_img.place(x=370, y=35)

imaginserch = PhotoImage(file="weatherApp/icon/10d@2x.png")
imaginsearch = Label(window, image=imaginserch, bg="black")
imaginsearch.config(height=70, width=70)
imaginsearch.place(x=350, y=35)

textfield = tk.Entry(window, justify='center', width=20, bg="black", font=('poppins', 25, 'bold'), fg="white", border=0)
textfield.place(x=420, y=45)
textfield.focus()

search_icon = PhotoImage(file="weatherApp/Layer 6.png")

search_icone = Label(image=search_icon, cursor="hand2",bg="black")
search_icone.bind("<Button-1>", getWeather)
search_icone.config(height=70, width=70)
search_icone.place(x=750, y=35)

bottombox = Frame(window, width=900, height=170, bg="black")
bottombox.pack(side=BOTTOM)

firstbox = PhotoImage(file="weatherApp/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="weatherApp/Rounded Rectangle 2 copy.png")
box1 = Label(bottombox, image=firstbox, bg="white")
# box1.config(height=130,width=130)
box1.place(x=30, y=15)
Label(bottombox, image=secondbox, bg="white").place(x=300,y=24)
Label(bottombox, image=secondbox, bg="white").place(x=400,y=24)
Label(bottombox, image=secondbox, bg="white").place(x=500,y=24)
Label(bottombox, image=secondbox, bg="white").place(x=600,y=24)
Label(bottombox, image=secondbox, bg="white").place(x=700,y=24)
Label(bottombox, image=secondbox, bg="white").place(x=800,y=24)



#time
clock = Label(window,font=("Helvetica",30,'bold'),fg="white",bg="black")
clock.place(x=65, y=35)




#rep
t = Label (window, fg="white", bg="black")
t.place(x=150, y=100)
h = Label(window, fg="white", bg="black")
h.place(x=150, y=140)
p = Label(window, fg="white", bg="black")
p.place(x=150, y=180)
w = Label(window, fg="white", bg="black")
w.place(x=150, y=220)
d = Label(window,fg="white", bg="black")
d.place(x=150, y=260)

firstFrame = Frame(window, width=238, height=139, bg="#9C9C9C")
firstFrame.place(x=31, y=316)
day1 = Label(firstFrame,font="arial 20",bg="#9C9C9C",fg="#fff")
day1.place(x=60,y=1)
firstimage=Label (firstFrame,bg="#9C9C9C")
firstimage.place (x=10, y=30)
daytmp = Label(firstFrame,bg="#9C9C9C",fg="#fff")
daytmp.place(x=140,y=50)

secondFrame = Frame(window,width=79,height=123, bg="#9C9C9C")
secondFrame.place(x=301, y=325)
day2 = Label(secondFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day2.place(x=8,y=1)
secondimage=Label (secondFrame,bg="#9C9C9C")
secondimage.place (x=12, y=20)
day2tmp = Label(secondFrame,bg="#9C9C9C",fg="#fff")
day2tmp.place(x=3,y=70)


thirdFrame = Frame(window, width=79,height=123,bg="#9C9C9C")
thirdFrame.place(x=401,y=325)
day3 = Label(thirdFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day3.place(x=8,y=1)
thirdimage=Label (thirdFrame,bg="#9C9C9C")
thirdimage.place (x=12, y=20)
day3tmp = Label(thirdFrame,bg="#9C9C9C",fg="#fff")
day3tmp.place(x=3,y=70)


fourthFrame = Frame(window, width=79,height=123, bg="#9C9C9C")
fourthFrame.place(x=501, y=325)
day4 = Label(fourthFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day4.place(x=8,y=1)
fourthimage=Label (fourthFrame,bg="#9C9C9C")
fourthimage.place (x=12, y=20)
day4tmp = Label(fourthFrame,bg="#9C9C9C",fg="#fff")
day4tmp.place(x=3,y=70)


fivthFrame = Frame(window, width=79,height=123, bg="#9C9C9C")
fivthFrame.place(x=601, y=325)
day5 = Label(fivthFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day5.place(x=8,y=1)
fivthimage=Label (fivthFrame,bg="#9C9C9C")
fivthimage.place (x=12, y=20)
day5tmp = Label(fivthFrame,bg="#9C9C9C",fg="#fff")
day5tmp.place(x=3,y=70)


sixthFrame = Frame(window, width=79,height=123, bg="#9C9C9C")
sixthFrame.place(x=701, y=325)
day6 = Label(sixthFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day6.place(x=8,y=1)
sixthimage=Label (sixthFrame,bg="#9C9C9C")
sixthimage.place (x=12, y=20)
day6tmp = Label(sixthFrame,bg="#9C9C9C",fg="#fff")
day6tmp.place(x=3,y=70)


seventhFrame = Frame(window, width=79,height=123, bg="#9C9C9C")
seventhFrame.place(x=801, y=325)
day7 = Label(seventhFrame,font="arial 10",bg="#9C9C9C",fg="#fff")
day7.place(x=8,y=1)
seventhimage=Label (seventhFrame,bg="#9C9C9C")
seventhimage.place (x=12, y=20)
day7tmp = Label(seventhFrame,bg="#9C9C9C",fg="#fff")
day7tmp.place(x=3,y=70)


locfr = Frame(window, width=170,height=50, bg="#9C9C9C")
locfr.place(x=500, y=109)
loc = Label(locfr,text="location",font="Courier 15 bold",bg="#9C9C9C",fg="#1A1818")
loc.place(x=45,y=10)
loc_icon = (Image.open(f"weatherApp/goupille-de-localisation.png"))
resized_image1 = loc_icon.resize((50, 50))
photo0 = ImageTk.PhotoImage(resized_image1)
loc_icone = Label(image=photo0,bg="#9C9C9C")
loc_icone.config(height=40, width=35)
loc_icone.place(x=507, y=110)




window.mainloop()
