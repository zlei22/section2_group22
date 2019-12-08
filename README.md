
# Squirrel Tracker Project of 4150


## Contributors

Project Group 22 Section 2

Contributors: Zijing Lei, Chang Gao

UNIs: [zl2847, cg3177]

Webpage: [**Link**](https://tools-254023.appspot.com/sightings/)

## Documentation
Project description: [**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Data Set
The data we use is [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which was counted by the [**Squirrel Census**](https://www.thesquirrelcensus.com/). 

It contains squirrel data for each of the 3,023 sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans.


## Management Commands
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```
## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the ``Django`` framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 

## Features

- A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.   
  Located at: /map   
	Method: GET   
	Will use the [leaflet](https://leafletjs.com/) library for plotting

- A view that lists all squirrel sightings with links to edit and add sightings   
  Located at: /sightings   
  Method: GET  
  
- A view to update a particular sighting   
  Located at: /sightings/<unique-squirrel-id>
  Method: POST  
 
- A view to create a new sighting   
  Located at: /sightings/add   
  Method: POST  

- A view with general stats about the sightings
 : Particular stats are for you to decide but must include five of the attributes listed in the initial CSV download.    
  Located at: /sightings/stats   
  Method: GET   

