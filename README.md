# Certificate Generator

This Python script generates certificates based on user input. It uses the easygui library for the GUI and pathlib for handling file paths.

# ScreenShorts
<img src="https://raw.githubusercontent.com/Mrinmay-Nath/Certificate-Generator---Automated-Certificate-Creation-with-Python/main/certificate-template.jpg" height="500px">

# CODE
<img src="https://raw.githubusercontent.com/Mrinmay-Nath/Certificate-Generator---Automated-Certificate-Creation-with-Python/main/code.png" height="500px">

# UI
<img src="https://raw.githubusercontent.com/Mrinmay-Nath/Certificate-Generator---Automated-Certificate-Creation-with-Python/main/UI.png" height="300px">



## Dependencies
- easygui: A module for very simple, very easy GUI programming in Python.
- pathlib: A built-in Python library used for creating and manipulating filesystem paths.
- logging: A built-in Python library used for logging error messages.

## Installation
To install the required modules, run the following command in your terminal (CMD for Windows users):

```bash
pip install -r requirements.txt

Usage
------------

1.Enter the names in name data.txt that you want to print on the Certificate.
2.Run the script.
3.A message box will appear welcoming you to the Certificate Generator.
4.You will then be asked to choose how you want to input the names (either a single name or multiple names).
5.If you choose "Single Name", you will be asked to enter the name you want to generate a certificate for.
6.If you choose "Multiple Names", you will be asked to select a .txt file with one name per line.
7.The names are then processed and certificates are generated.

Using the Coordinate Finder
------------

The coordinates.py script is used to find the coordinates of a point in an image. Here's how to use it:

1.Run the coordinates.py script.
2.An image window will open displaying the certificate template.
3.Click anywhere on the image. The script will print the x and y coordinates of the point you clicked on.

Note: The cleanup_data function is not defined in this excerpt. It should take a Path object pointing to a .txt file and return a list of names.

Error Handling
------------

If there's an error while processing a name, the script logs the error message and the name that caused the error.

Author
Created by Mrinmay Nath

```
