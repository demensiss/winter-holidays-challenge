# Winter Holidays Challenge 2021
10 days and 10 application of coding in Python

Event link: https://www.facebook.com/events/843253696243420?active_tab=about

## Table of contents

* [Day 1: Palindromes and anagrams](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-1-palindromes-and-anagrams)
* [Day 2: Page from Callendar](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-2-page-from-callendar)
* [Day 3: Mail Sender](https://github.com/demensiss/winter-holidays-challenge#day-3-mail-sender)
* [Day 4: BMI Calculator](https://github.com/demensiss/winter-holidays-challenge#day-4-bmi-calculator)
* [Day 5: Movie Finder](https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-5-movie-finder)

## Day 1: Palindromes and anagrams

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

* library requests
* library datetime
* library random

### Helpful links:

* https://2.python-requests.org/pl/latest/user/quickstart.html#wykonaj-zadanie
* https://www.w3schools.com/python/python_datetime.asp
* https://pl.python.org/docs/lib/module-random.html

## Day 3: Mail Sender

Write a simple program that will send personalized mailing to selected people.

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

### Helpful link:

* https://realpython.com/python-send-email/
* http://www.w3big.com/pl/python/python-email.html
* https://qabrio.pl/openpyxl-2/
* https://docs.python.org/3/library/os.html

## Day 4: BMI Calculator

Write a program that calculates the BMI index based on weight [kg] and height [cm].
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

### Requirements:

* [ ] using the API search for all parts of the movie specified in the search
* [ ] filter out incorrect search results
* [ ] display basic information for each movie, e.g. year, length, rating, list of actors

### Program status:

Program under development.
