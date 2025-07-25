#Here we want to create a job search program where users can search for jobs in the United States, Canada and the UAE
import requests
import json
import csv


#function to handle the API

def jsearch_api(job,location):
    endpoint = ""
    api_key = ""
    method = "Get"
    params = {

    }

    headers = {
        'content-type': 'Application/JSON',

    }
    #now the response
    response = requests.request(method, endpoint, params=params, headers=headers)
    data = response.json()

    available_jobs = data

    #let's loop through the available jobs and print out the necessary results
    for jobs in available_jobs:
        print(f'Job Tile : {jobs}')
        print(f'Company Name: {jobs}')
        print(f'job location: {jobs}')
        print(f'Employment Type: {jobs}')
        print(f'Job Description: {jobs}')
        #check if there is an available link and print it out
        if jobs in available_jobs:
            print(f'Apply Link: {jobs}')


def country():
    countries = {
        'USA': 'us',
        'CANADA': 'ca',
        'UAE': 'ae'
    }
    print("We currently have 3 countries available in the system")
    print("1: USA\n2: Canada\n3: UAE")

    while True:
        choiceOfCountry = input("In which country from the above you want to search from? ")
        #let's pass in the country to the function
        if choiceOfCountry.upper() == 'USA':
            selected =  countries['USA']
            # print(selected)
            return selected
        elif choiceOfCountry.upper() == 'CANADA':
            return countries['CANADA']
        elif choiceOfCountry.upper() == 'UAE':
            return countries['UAE']
        else:
            print("Invalid country inputed, please try again")
            continue

def main():
    print("-------------------------Welcome To CodingHQ Job Search Portal-----------------------")
    typeOfJob = input("What type of job are you looking for today? ")
    pays = country()
    jsearch_api(typeOfJob, pays)

    print("Hope you could find something :-)")


country()