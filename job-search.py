#Here we want to create a job search program where users can search for jobs in the United States, Canada and the UAE
import requests
import json
import csv


#function to handle the API

def jsearch_api(job,location):
    endpoint = "https://jsearch.p.rapidapi.com/search"
    api_key = "6ad0248a75mshf9d81495887932ap17b859jsn4b4e9e15f052"
    method = "Get"
    params = {
        "query": job,
        "page": "1",
        "num_pages": "1",
        "country": location,
        "date_posted": "all"
    }

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        'content-type': 'Application/JSON',
    }
    #now the response
    response = requests.request(method, endpoint, params=params, headers=headers)
    data = response.json()
    # print(data['data'])
    available_jobs = data['data']

    #let's number our results
    count = 0

    #let's loop through the available jobs and print out the necessary results
    for jobs in available_jobs:

        count += 1
        print(f'------------------ Result Number: {count} -------------------------------\n')
        # print(count)
        print(f'Job Tile : {jobs['job_title']}')
        print(f'Company Name: {jobs['employer_name']}')
        if jobs in available_jobs:
            print(f'job location: {jobs['job_location']}')
        print(f'Employment Type: {jobs['job_employment_type']}')
        print(f'Job Description: {jobs['job_description']}')
        #check if there is an available link and print it out
        if jobs in available_jobs:
            print(f'Apply Link: {jobs['job_apply_link']}')

        print("\n")





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


main()
# jsearch_api("python developer", 'us')