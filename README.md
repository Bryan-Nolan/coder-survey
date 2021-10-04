# Coder Survey

![Coder Survey](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/responsive.jpg)

## Table of contents
1. [Project](#Coder-Survey)
2. [User](#User)
3. [Languages and Tools Used](#Technologies-Used)
4. [Features](#Features)
5. [Data Model](#Data-Model)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Refernces](#Referencess)
9. [Acknowledgements](#Acknowledgements)
***

## Project

This project aims to ask the user a series of questions.  Update Google sheets with answers and to relay to the user their answers and how they compare with all other answers giving results of all the question.  My aim is to be able to add more questions to the survey without having to change python code. 

[Back to top ⇧](#)

## User

![First Screen](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/first.screen.jpg)

During this the user will be asked a series of questions and give predefined answers to choose from.  After answering all questions, the user will be given a list of their choices, the total of participates to date with survey and the results in percentages of what the total of participates voted for. 

[Back to top ⇧](#)

## Features

On beginning the user is told how many questions they will be answering and that the results will be displayed at end. 

![Info](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/info.jpg)

There is also built-in error detection that if the user enters anything other than the required values they will be told of error and to ty again. 

![Error](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/Error.jpg)

After answering all questions, the user receives a summary of all the questions asked and how other participants response shown as percentages.

![Results](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/results.jpg)

### Future Features

In the future I would consider adding the following feature.
    * Users adding email addresses as to have 1 try per user
    * Adding a feature to have an admin user as to add questions through the program.

[Back to top ⇧](#)

## Data Model

I decided to use Google Sheets.  I used 2 work sheets. My aim was that if I gave access to someone to add question to question sheet that this would appear in survey without updating code.  The other sheet "results" would store the data inputted by user and be used to calculate results and then updated with latest users answers. 

![Questions Sheet]((https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/questions.jpg))

![Results Sheet]((https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/sheet-results.jpg) )

[Back to top ⇧](#)

## Languages and Tools Used

During this project the following languages were used:

### Languages

    1. Python

### Tools 
    
    1. GitPod
    2. GitHub
    3. [Google Sheets](https://docs.google.com/spreadsheets/d/1wja4s13Cgmt5oTYlDKoP_2yisQXZu67QekdpGpHWXxA/edit?usp=sharing) 
    4. [Am I responsive](http://ami.responsivedesign.is/)

[Back to top ⇧](#)

## Testing

This has been manually tested. Code has been passed through PEP8 and the only issues are lines of code exceeding 79 characters in length.  Unauthorised inputs have also been taken into account by prompting user to enter correct data. Also used GitIo terminal to show errors and Code Institute Heroku terminal.  

My Testers were my son Cormac (17) and daughter Heather (14). They provided great insight to navigating site and content.

### Validator Testing

#### Python

* PEP8
    [PEP8online.com](http://pep8online.com/)
    Passed validator

![Validator](https://github.com/Bryan-Nolan/coder-survey/blob/main/assets/readme_images/validator.jpg)    

[Back to top ⇧](#)

## Deployment

This project was deployed using Heroku

    Steps for deployment
        Fork or clone this repository
        Create a new Heroku app
        Set buildbacks to Python and NodeJS in that order
        Link the Heroku app to the repository
        Click on Deploy

### Code Survey - GitHub

[Coder Survey GitHub Link](https://github.com/Bryan-Nolan/coder-survey)

[Back to top ⇧](#)

## References

During the research of this project, I used various sites to research issues as I was going along. 

[W3 Schools] (https://www.w3schools.com/)
[Python.org](https://www.python.org/)

Also used the Code Institute material and notes for help.  


[Back to top ⇧](#)

## Acknowledgements

Credit to Kasia for help and chats during this project.
My mentor Maria who had great insight and guided me in the right direction. My classmates and my children Heather and Cormac for help testing.

[Back to top ⇧](#)
