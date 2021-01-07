# Winter Holidays Challenge 2021
10 days and 10 application of coding in Python

Event link: https://www.facebook.com/events/843253696243420?active_tab=about

## Table of contents

* [Day 1: Palindromes and anagrams] (https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-1-palindromes-and-anagrams)
* [Day 2: Page from Callendar] (https://github.com/demensiss/winter-holidays-challenge/blob/master/README.md#day-2-page-from-callendar)
* [Day 3: Mail Sender] (https://github.com/demensiss/winter-holidays-challenge#day-3-mail-sender)
* [Day 4: BMI Calculator (https://github.com/demensiss/winter-holidays-challenge#day-4-bmi-calculator)

## Day 1: Palindromes and anagrams

### Requirements:

* Write a program that asks for a string.
* The program displays this string inverted.
* The program checks if the string is a palindrome and displays a message informing you about it.
* When checking the string, the program ignores capital letters and non-letter characters.
* The program calls a website that will display anagrams of the given text.

### I learned today:

* Regular Expressions or regex
* time function that delayed opening of the browser
* how to open the url via the application

## Day 2: Page from Callendar

### Requirements:

* Write a program that, when started, displays the current date, time, day of the week and weather, i.e. temperature and pressure in a given city.
* Use requests and datetime.
* Convert units from, for example: Calvin to Celsius
* Hard version: Display the current time for cities in different time zones (e.g. Beijing, Sydney, Washington, London)

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

### Requirements:

* database: excel or csv file with two columns with the headings "email" and "name and surname"
* email subject: “Your image”
* personalized email content: “Hi {Name}! it’s file generated for you”.
* in addition to the mail: graphic file named "{Name} _ {Surname} _image.png"
* Properly secure the program (e.g. missing Excel file, missing data in Excel, no png file)
* protect against spam (e.g. one e-mail sent every second)
* Hard version: add an option to send emails with HTML content
* Hard version: add an email validator

## Day 4: BMI Calculator

Write a program that calculates the BMI index based on weight [kg] and height [cm].

### Requirements:

* the program gets the necessary information from the user
* the program informs the user to what extent is its result
* then the program randomizes one of the physical activities and the time of its execution
* the execution time cannot be longer than the free time declared by the user
* create a training plan for 7 days and save the results in a .txt file
* Hard version: Prepare a varied training plan taking into account the maximum time entered by the user. It should be a few physical activities that will fill the entire daily amount of time, have a certain minimum length (e.g. 10 minutes). Activities cannot be repeated in one day.
