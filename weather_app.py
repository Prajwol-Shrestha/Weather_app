from tkinter import *
#from PIL import ImageTk,Image
import requests
import json


window = Tk()
window.title("Weather App")
#window.iconbitmap("Images/itachi.jpg")
window.geometry('300x180')
window.configure(background ="black")


#Creating fuctionality of submit button
def Submit():
	try:
		#Requesting data from API
		API_request = requests.get("https://nepal-weather-api.herokuapp.com/api/?place="+Place.get())
		#This API returns data in dictonary form

		#Converting json format data to python format
		API = json.loads(API_request.content)

		#Accesing the python dictonary
		status = API['status']
		place = API['place']
		Temp_min = API['min']
		Temp_max = API['max']
		rain = API['rain']

		status_label = Label(window, text = 'Valid Place Name ---> ' + status, bg ="black", fg = "white", font = 10)
		status_label.pack()

		place_label = Label(window,text = 'Place ---> ' + place, bg ="black", fg = "white", font = 10)
		place_label.pack()

		Temperature_label_min = Label(window, text = 'Mininum Temperature ---> ' + Temp_min, bg ="black", fg = "white", font = 10)
		Temperature_label_min.pack()

		Temperature_label_max = Label(window, text = 'Maximum Temperature ---> ' + Temp_max, bg ="black", fg = "white", font = 10)
		Temperature_label_max.pack()

		Rain_label = Label(window, text = 'Rainfall ---> ' + rain, bg ="black", fg = "white", font = 10)
		Rain_label.pack()

		window.geometry('400x400')

	# Catching errors	
	except Exception as e: 
		Label(window, text = "Place Does Not Exist", bg = "black", fg = "white", font = 10).pack()



Text = Label(window, text = "Enter the place name ", bg = "black", fg = "white", font = 10).pack()

'''Does not work if like this for some reason
		Place = Entry(window).pack()
''' 
Place = Entry(window, bd = 10, width = 30, bg ="black", fg = "white", font = 20)
Place.pack(padx = 10, pady = 5)



#Creating submit button
submit = Button(window, text = "Submit", command = Submit, padx = 10, pady = 5, bd = 8, bg ="black", fg = "white")
submit.pack(padx = 10, pady = 15)

window.mainloop()