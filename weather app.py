from tkinter import *
from tkinter import ttk
import requests

def data_get():

  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=44af6c733f4a3e9e3ace959d4230742f").json()
  w_label1.config(text=data["weather"][0]["main"])
  wb_label1.config(text=data["weather"][0]["description"])
  temp_label1.config(text=str(int(data["main"]["temp"])-273.15))
  per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Mahreen")
win.config(bg = "blue")
win.geometry("500x570")

name_label = Label(win,text="Weather App",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Ahmadpur East"," Ahmed Nager Chatha"," Ali Khan Abad"," Alipur"," Arifwala"," Attock"," Bhera"," Bhalwal"," Bahawalnagar"," Bahawalpur"," Bhakkar"," Burewala"," Chillianwala"," Choa Saidanshah"," Chakwal"," Chak Jhumra"," Chichawatni"," Chiniot"," Chishtian"," Chunian"," Dajkot"," Daska"," Davispur"," Darya Khan"," Dera Ghazi Khan"," Dhaular"," Dina"," Dinga"," Dhudial Chakwal"," Dipalpur"," Faisalabad"," Fateh Jang"," Ghakhar Mandi"," Gojra"," Gujranwala"," Gujrat"," Gujar Khan"," Harappa"," Hafizabad"," Haroonabad",
             " Hasilpur"," Haveli Lakha"," Jalalpur Jattan"," Jampur"," Jaranwala"," Jhang"," Jhelum"," Kallar Syedan"," Kalabagh"," Karor Lal Esan"," Kasur"," Kamalia"," Kāmoke"," Khanewal"," Khanpur"," Khanqah Sharif"," Kharian"," Khushab"," Kot Adu"," Jauharabad"," Lahore"," Islamabad"," Lalamusa"," Layyah"," Lawa Chakwal"," Liaquat Pur"," Lodhran"," Malakwal"," Mamoori"," Mailsi"," Mandi Bahauddin"," Mian Channu"," Mianwali"," Miani"," Multan"," Murree"," Muridke"," Mianwali Bangla"," Muzaffargarh"," Narowal"," Nankana Sahib"," Okara"," Renala Khurd"," Pakpattan"," Pattoki"," Pindi Bhattian"," Pind Dadan Khan"," Pir Mahal"," Qaimpur"," Qila Didar Singh"," Rabwah"," Raiwind"," Rajanpur"," Rahim Yar Khan"," Rawalpindi"," Sadiqabad"," Sagri"," Sahiwal"," Sambrial"," Samundri"," Sangla Hill"," Sarai Alamgir"," Sargodha"," Shakargarh"," Sheikhupura"," Shujaabad"," Sialkot"," Sohawa"," Soianwala"," Siranwali"," Tandlianwala"," Talagang"," Taxila"," Toba Tek Singh"," Vehari"," Wah Cantonment"," Wazirabad"," Yazman"," Zafarwal",]


com = ttk.Combobox(win,text="Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)




w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",
                   font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)



wb_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text="",
                   font=("Time New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)



temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label = Label(win,text="Pressure",
                   font=("Time New Roman",17))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",
                   font=("Time New Roman",17))
per_label1.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done",
                     font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()
