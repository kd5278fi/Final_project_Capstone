# Project Overview

This application helps the user track all food intake for the day and automatically calculates the amount of calories and other nutrients consumed. The user submits a general food item they would like to add to the day and the application responds with a list of approved items for the user to choose from. Once an item is selected the user then chooses the type of measurement that corresponds with what they ate. This list is generated diretly from the food item they selected. The user then inputs how many servings they had, and at what meal time they had it. Pressing the ADD button adds the food item to the selected meal time and displays the running total of calories for that time slot. As food is added to the tracker a final count of calories and other nutrients can be seen at the bottom of the application. As the nutrient counts are being updated they are compared against an internal plan for the user and will display any overages in red. On exiting the application a prompt will ask the user if they would like to save their data. If yes is selected, all of the data is saved to a local database for future use. If no is selected, the application is exited and the data for that session is erased. Every time the application is opened any saved items will load from the database and display on the screen.


# Project Utilities

The requests module is used in the API class in order to structure the URL calls and compile the Json responses. 
SQLite3 is used to structure the database class and data queries.
Tkinter and its sub-module, Ttk, are used for the application GUI.


# Project Structure

The applications code is structured around 5 sections which are accessed through a Main method. The Main method creates a database, and starts the GUI. The RunMain method sets up the GUI and all of the input/output fields. The GUI can only access the Middleman, which then accesses the API calls and the database manipulations. There are two classes, foodItem and MessageBox, which can be accessed by all. 

