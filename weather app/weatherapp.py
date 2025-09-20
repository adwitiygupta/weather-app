import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

#  list for recent searches
recent_searches = []

# Function to fetch weather
def weather(city_from_list=None):
    city = city_entry.get() if not city_from_list else city_from_list
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return
    
    api_key = "e2c640b881fb7c25dabeb5bcf89dc755"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return
        
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"].lower()
        desc = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        result_label.config(text=f"{city_name}, {country}\n{temp}°C | {desc}\nHumidity: {humidity}% \n Wind Speed: {wind_speed} m/s")
        
        #corresponding weather icon
        if "cloud" in weather :
            icon_file = "icons/cloudy.gif"
        elif "rain" in weather:
            icon_file = "icons/rain.gif"
        elif "clear" in weather:
            icon_file = "icons/sunny.gif"
        elif "snow" in weather:
            icon_file = "icons/snow.gif"
        elif "storm" in weather or "thunder" in weather:
            icon_file = "icons/storm.gif"
        elif "mist" in weather :
            icon_file = "icons/mist.gif" 
        elif "fog" in weather :
            icon_file = "icons/fog.png"       
        elif "haze" in weather:
            icon_file = "icons/haze.gif"
        else:
            icon_file = "icons/na.png"
        
        try:
            img = Image.open(icon_file).resize((80,80))
            weather_icon = ImageTk.PhotoImage(img)
            icon_label.config(image=weather_icon, text="")
            icon_label.image = weather_icon
        except:
            icon_label.config(image="", text="(No icon)")
        
        # Update recent searches
        if city_name not in recent_searches:
            recent_searches.insert(0, city_name)  # add to top
            if len(recent_searches) > 5:  # keep only last 5
                recent_searches.pop()
        updatelist()
        
    except:
        messagebox.showerror("Error", "Failed to fetch data. Check your internet connection.")

# Function to reset inputs
def reset():
    city_entry.delete(0, tk.END)
    result_label.config(text="")
    icon_label.config(image="", text="")

# Update recent searches UI
def updatelist():
    for widget in recent_frame.winfo_children():
        widget.destroy()
    
    if recent_searches:
        tk.Label(recent_frame, text="Recent Searches:", font=("Arial", 12, "bold"), bg="#87CEEB").pack(anchor="w")
        
        for city in recent_searches:
            btn = tk.Button(recent_frame, text=city, font=("Arial", 11), 
                            command=lambda c=city: weather(c), bg="white")
            btn.pack(fill="x", pady=2)

# gui setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x600")
root.config(bg="#87CEEB")

title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#87CEEB")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

# Buttons frame
btn_frame = tk.Frame(root, bg="#87CEEB")
btn_frame.pack(pady=10)

search_btn = tk.Button(btn_frame, text="Get Weather", font=("Arial", 12, "bold"), command=weather, bg="#1E90FF", fg="white")
search_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", font=("Arial", 12, "bold"), command=reset, bg="#FF4500", fg="white")
reset_btn.grid(row=0, column=1, padx=5)

# Weather icon
icon_label = tk.Label(root, bg="#87CEEB")
icon_label.pack(pady=10)

# Result text
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#87CEEB")
result_label.pack(pady=10)

# Recent searches
recent_frame = tk.Frame(root, bg="#87CEEB")
recent_frame.pack(pady=10, fill="x")

root.mainloop()
