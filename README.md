# Winter Holidays Challenge 2021 with Hard Coder
10 days and 10 application of coding in Python

Event link: https://www.facebook.com/events/843253696243420?active_tab=about


## Table of contents

* [Day 1: Palindromes and anagrams](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-1-palindromes-and-anagrams)
* [Day 2: Page from Callendar](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-2-page-from-callendar)
* [Day 3: Mail Sender](https://github.com/demensiss/winter-holidays-challenge#day-3-mail-sender)
* [Day 4: BMI Calculator](https://github.com/demensiss/winter-holidays-challenge#day-4-bmi-calculator)
* [Day 5: Movie Finder](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-5-movie-finder)
* [Day 6: Image Resizer](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-6-image-resizer)
* [Day 7: Password Generator](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-7-password-generator)
* [Day 8: Distance Calculator](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-8-distance-calculator)
* [Day 9: House Library](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-9-house-library)
* [Day 10: Summary](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-10-summary)


## Day 1: Palindromes and anagrams

A simple program that checks if a given word is a palindrome and creates anagrams from the letters of that word.

[Solving the task](https://github.com/demensiss/winter-holidays-challenge/blob/master/palindrom-and-anagram.py)

### Requirements:

* [x] Write a program that asks for a string.
* [x] The program displays this string inverted.
* [x] The program checks if the string is a palindrome and displays a message informing you about it.
* [x] When checking the string, the program ignores capital letters and non-letter characters.
* [x] The program calls a website that will display anagrams of the given text.
* [ ] Hard version: Search for anagrams and words formed after removing letters from the given word yourself

### Program status:

The basic requirements are made. The program doesn't report errors. 
Hard version under development.

### I learned today:

* Regular Expressions or regex
* time function that delayed opening of the browser
* how to open the url via the application


## Day 2: Page from Callendar

A simple program showing a card from the calendar, i.e. the current date and weather in the selected location.

[Solving the task](https://github.com/demensiss/winter-holidays-challenge/blob/master/page-from-callendar.py)

### Requirements:

* [x] Write a program that, when started, displays the current date, time, day of the week and weather, i.e. temperature and pressure in a given city.
* [x] Use requests and datetime.
* [x] Convert units from, for example: Calvin to Celsius
* [ ] Hard version: Display the current time for cities in different time zones (e.g. Beijing, Sydney, Washington, London)

### Program status:

The basic requirements are made. The program doesn't report errors. 
Hard version under development.

### I learned today:

* requests module
* datetime module
* random module

### Helpful links:

* https://2.python-requests.org/pl/latest/user/quickstart.html#wykonaj-zadanie
* https://www.w3schools.com/python/python_datetime.asp
* https://pl.python.org/docs/lib/module-random.html


## Day 3: Mail Sender

A simple program that will send personalized mailing to selected people.

[Solving the task](https://github.com/demensiss/winter-holidays-challenge/blob/master/mail-sender.py)

### Requirements:

* [ ] database: excel or csv file with two columns with the headings "email" and "name and surname"
* [x] email subject: “Your image”
* [x] personalized email content: “Hi {Name}! it’s file generated for you”.
* [x] in addition to the mail: graphic file named "{Name} _ {Surname} _image.png"
* [x] properly secure the program (e.g. missing Excel file, missing data in Excel, no png file)
* [x] protect against spam (e.g. one e-mail sent every second)
* [ ] Hard version: add an option to send emails with HTML content
* [ ] Hard version: add an email validator

### Program status:

Fix the error when opening excel file. The program is not complete and reports errors.
In search of a solution.

### I learned today:

* email and email.message module
* smtplib module
* ssl module
* openpyxl module
* getpass module
* imghdr module
* os module

### Helpful links:

* https://realpython.com/python-send-email/
* http://www.w3big.com/pl/python/python-email.html
* https://qabrio.pl/openpyxl-2/
* https://docs.python.org/3/library/os.html


## Day 4: BMI Calculator

Program that calculates the BMI index based on weight [kg] and height [cm].

[Solving the task](https://github.com/demensiss/winter-holidays-challenge/blob/master/calculator-bmi.py)

### Requirements:

* [x] the program gets the necessary information from the user
* [x] the program informs the user to what extent is its result
* [x] then the program randomizes one of the physical activities and the time of its execution
* [x] the execution time cannot be longer than the free time declared by the user
* [x] create a training plan for 7 days and save the results in a .txt file
* [ ] Hard version: Prepare a varied training plan taking into account the maximum time entered by the user. It should be a few physical activities that will fill the entire daily amount of time, have a certain minimum length (e.g. 10 minutes). Activities cannot be repeated in one day.

### Program status:

The basic requirements are made. The program doesn't report errors. 
Hard version under development.

### I learned today:

* random module

### Helpful links:

* https://docs.python.org/3/library/random.html
* https://www.w3schools.com/python/module_random.asp


## Day 5: Movie Finder

A simple movie search program similar to the filmweb site.

[Solving the task](https://github.com/demensiss/winter-holidays-challenge/blob/master/movie-finder.py)

### Requirements:

* [x] using the API search for all parts of the movie specified in the search
* [x] filter out incorrect search results
* [x] display basic information for each movie, e.g. year, length, rating, list of actors

### Program status:

All requirements have been met.

### I learned today:

* implementing api with a search engine

### Helpful links:

* https://rapidapi.com/blog/imdb-api-python/
* https://rapidapi.com/blog/how-to-use-imdb-api/


## Day 6: Image Resizer

A simple program that reduces the size of images in the specified folder.

### Requirements:

* [ ] the program reads all graphic files in the selected location (in specific formats, e.g. jpg, png, bmp etc.)
* [ ] the program reduces the resolution of images by 50%
* [ ] the program saves the reduced images in the "smaller" subdirectory with the appropriate names
* [ ] use pillow or another library to work with images
* [ ] Hard version: Calculate how much disk space can be saved after compression (read the size of files in the original folder and "smaller" and compare both values - absolute and in %)

### Program status:

Program in progress.


## Day 7: Password Generator

A simple program that generates a random string of characters taking into account the indicated requirements.

### Requirements:

* [X] write a program to generate random passwords of user-specified length
* [X] the password must meet the given conditions, e.g. at least one number, at least one uppercase and one lowercase letter
* [X] use the string and secrets modules
* [X] Hard version: After generating the password, copy it to the system clipboard

### Program status:

All requirements have been met.

### I learned today:

* string library methods
* concatenation of strings with the method .join()
* copying information to the system clipboard

## Day 8: Distance Calculator

The program calculates the linear distance between any two points on the map.

### Requirements:

* [ ] write a program that calculates the linear distance between any two points on the map, using their geographic coordinates
* [ ] use any algorithm, e.g. https://pl.wikibooks.org/wiki/Astronomiczne_podstawy_geografii/Odleg%C5%82o%C5%9Bci?fbclid=IwAR2RXbacsE_nwQFpSDGuiYQlcvS0YCmTWjg3Qzvs92pZXUf4hLgTdoHjmtA
* [ ] use the API (e.g. https://rapidapi.com/trueway/api/trueway-geocoding)
* [ ] calculate the distance between your address and landmarks such as the Eiffel Tower or the Taj Mahal.
* [ ] Hard version: instead of entering your address, use geolocation

### Program status:

Program in progress.


## Day 9: House Library

Library program that shows the list of books available in the library and allows you to borrow them.

### Requirements:

* [ ] write a program that imports the catalog from any library (e.g. API of the National Library http://data.bn.org.pl/
* [ ] the user can name the author and the program will show him what books of that author are in the library's collection
* [ ] give the user the ability to "check out" and "return" books
* [ ] the borrowed items are stored in a file containing a certain identifying data set, e.g. title, author, publisher, year of publication (you can also use a local database)
* [ ] when "borrowed", books are added to the file
* [ ] when "returned" books are removed from the file
* [ ] Hard version: Secure the program in such a way that when downloading data, it also recognizes local “borrowed” items and does not show them as search results.

### Program status:

Program in progress.

### Helpful links:

* http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka


## Day 10: Summary

Program summary of the winter break challenge with Hard Coder

### Requirements:

* [ ] the program reads all files created by you during #feriechallenge - searches local directories or connects to Github for this purpose
* [ ] do not list all files manually
* [ ] using its own method of cataloging programs, the machine reads and displays:
  * [ ] how many tasks out of 10 have code written
  * [ ] the number of lines of code written in each problem (without taking into account the empty ones!) and the total number of lines
  * [ ] the number of unique words used in all programs and the most common word
  * [ ] list and number of keywords used during the entire challenge (use the keywords module)
  * [ ] list and number of imported modules in all programs

### Program status:

Program in progress.
