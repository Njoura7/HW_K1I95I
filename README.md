
# Chess Stats Application

Since I became obsessed with chess lately, I decided to create a simple app: "ChessStats",This desktop application retrieves and displays a user's chess ratings from Chess.com. The application prompts the user to enter their Chess.com username, then uses the Chess.com API to retrieve the user's ratings for the three main types of chess games: rapid, blitz, and classical. The application then displays these ratings to the user in a user-friendly way.
 


## Requirements

 - Python3  
 - PyQt5 library
 - Requests library


## Usage

1. Open a terminal in the project directory

2. Run the following command to start the application:

``
python python_k1i95i.py
``

3. Enter your Chess.com username in the text input and click the "Submit" button

Your ratings for rapid, blitz, and classical games will be displayed in the application window


## Solution design

### User Interface Design: 
The application is designed using PyQt5, a Python library that allows for the creation of desktop applications with a graphical user interface (GUI). The user interface consists of a window with a text input for the username, a submit button, and labels to display the user's ratings.

### API Integration: 
The Chess.com API provides access to data about Chess.com users, including their ratings for different types of chess games. The application uses the requests library to make HTTP requests to the Chess.com API and retrieve the user's ratings.

### Data Processing: 
Once the ratings have been retrieved from the API, the application processes the data and extracts the user's ratings for rapid, blitz, and classical games. The ratings are stored in variables and displayed to the user in the GUI.

### Error Handling: 
Finally, the application handles errors that may occur during the API integration or data processing steps. If an error occurs, the application displays an error message to the user indicating that their ratings could not be retrieved.

## 🔗 Links

This project is made for the subject : system programming with the proferssor : "László Tamás Storcz"
and this is the repo of the code:

[github repo](https://github.com/Njoura7/HW_K1I95I)


## Authors

- [@Njoura7](https://github.com/Njoura7)

