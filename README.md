# weather-app
first i made code work for base version (without gui)
  i defined a function 'weather'  give out desired data about its weather like temprature,humidity,wind speed etc from input city 
  program dosent have error handel capacity so used if else to handel the error
  data is requested from OpenWeatherMap using api key which send data in .json format
  
After compleating the above problem i needed to add gui which i had no prior experience of so i used help of ai (format  and examples)
  after reading about format of gui i learned i need to import tkinter and message box
  then i added title ,box size,color this made basic box in which i had to add buttons and input city name
  made entry for input city name whose data we need 
  i made a button named search which execute command for fetching data of the city inputed
  
code was not reusable so i defined a reset command and and added a reset button which executed the reset command

Now my problem was adding icons
  using if elif and output data from weather  i used specific images for specific weather which i have added in a folder named icons this gives desired image for given weather
  Tkinter cannot directly display PNG/JPG images, so the Pillow library is used then i resized the image and got image output
  
Now my final problem was adding Recent searches list (used ai here)
  A Python list keeps track of recent searches:  (recent_searches = []) new searches are added to the top of the list ,duplicates are removed and the list is capped at 5 cities, Tkinter Buttons display recent searches, allowing one-click access

------------INSTRUCTIONS TO USE THE APP------------- 
Enter a city name in the input box.
Click Get Weather ( the app will show):
  Current temperature
  Weather condition
  Weather icon (sunny, cloudy, rain, etc.)
Recent Searches:
  Shows the last 5 cities you searched.
  Click any city to see its weather again instantly.
Reset Button: Clears the city input, result text, and icon
