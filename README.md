# About the Project
This project is aimed at allowing animal shelters to track and categorize
animals. It is a full-stack application that allows visualization of 
database content via an interactive client-facing dashboard.

# Motivation
The client is an international animal shelter that finds and shelters animals, 
then trains certain dogs for search-and-rescue missions. This application will 
allow the company to track and categorize all animals to easily find good
candidates for search-and-rescue dog training.

# Application Demo
![Login window:](FinalProjectScreencast.gif)

### YouTube link to project demo: ###
https://www.youtube.com/embed/DMIArZGrEjE?feature=oembed

# Installation #
#### Tools used: ####
1.	MongoDB server version 4.2.6 – This is the document-based NoSQL database server that will allow tracking object states. You need to have this server running for the CRUD application to work. Installation instructions: https://docs.mongodb.com/manual/release-notes/4.2/
2.	Python 3.6 – This allows the use of the object-oriented programming language Python. It is used in this project to manipulate the database with more logic than MongoDB alone offers. Installation instructions: https://www.python.org/downloads/release/python-360/
3.	PyMongo – This is the official driver that supports MongoDB interaction with Python. Documentation including installation instructions can be found here: https://pymongo.readthedocs.io/en/stable/
#### Frameworks and libraries used within Python: ####
1.	Dash – This Python framework allows building data visualization interfaces that are interactive. For more information about this framework, visit https://dash.plotly.com/
2.	Pandas – this library is used for data analysis and manipulation. To learn more about this useful tool, visit https://pandas.pydata.org/
3.	json – used for converting update and delete results to JSON format
4.	traceback – used for troubleshooting exceptions by printing a traceback to the console
5.	MongoClient – imported from PyMongo to allow queries to the MongoDB database
6.	pymongo.errors – imported WriteConcernError and WriteError so the update and delete methods can return these errors if they occur
7.	base64 – allows images to be displayed in the app


# Explanation of CRUD Operations: #
The CRUDHandler class is a custom python module that has two attributes: client and collection. The client attribute utilizes the MongoClient class from PyMongo and receives an IP address of a database and the DB user credentials as constructor arguments. 

The methods of CRUDHandler include: create(), findDocs(), update, and delete(). The create() method receives a python dictionary as an argument and inserts it as a document in the animals collection. The findDocs() method receives search criteria as an argument in the form of a python dictionary, then searches thru the animals collection for the given search criteria. The update() method takes two arguments: search criteria in the form of a dictionary and new values to update with (also a dictionary). If the animals collection contains a document that matches the search criteria, the document’s contents are updated with the new values. The delete() method takes search criteria as an argument in the form of a dictionary and searches the animals collection for a match. If a match is found, the matching document is then deleted from the database.

# Explanation the Middleware Code and Client Facing Application: #
The middleware is comprised of the CRUDHandler.py module that allows interaction with MongoDB as well as pandas dataframe code for data analysis. Additionally, the Dash framework is used for controlling the 

Divs and other html components are implemented through Dash to create the web page layout. Inside the html elements are the dashboard components. These include the radio buttons, data table, pie chart, and map. They are developed using the Dash framework.

A combination of Dash, Pandas, and core Python are used to implement the functionality of these dashboard components. Pandas dataframes are used to harness and filter the data extracted from the database queries, while Dash callback functions provide a structure for making the components interactive.
