
# Create your views here.
import csv
import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .models import Campus, Program, Student, StudentProgram

# Reads the CSV files from the specified file path and 
# returns a list of dict where each dict represents a row of data in the file.
def read_csv_file(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

# Write the transformed data into 'student.json' file.
def write_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# convert the data from the csv files into the specified format
def transform_data(student_data, program_data):

    student_university_data = {}
    
    # Looping over student data and storing information for each student profile in separate variables

    for student in student_data:
        username = student['student_username']
        first_name = student['first_name']
        last_name = student['last_name']
        email = student['email']
        gpa = float(student['gpa'])
        campus_identifier = student['campus_identifier']
        
        # Looping over program data and storing information for each program for a particular student in separate variables

        programs = {}
        for program in program_data:
            if program['student_username'] == username:
                program_identifier = program['program_identifier']
                priority_order = int(program['priority_order'])
                programs[program_identifier] = {
                    'priority_order': priority_order
                }
        
        # creating a dict with username as the key and student's plan and profile data as value
        student_university_data[username] = {
              'plan': {
                'programs': programs
            },
            'student': {
                'campus': campus_identifier,
                'gpa': gpa,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'username': username
                
                
                
            }
          
        }
    return student_university_data


def store_data_into_database(request):

    #read student's profile and program data
    student_data=read_csv_file('UniversityRecord\student_profile.csv')
    program_data=read_csv_file('UniversityRecord\student_program.csv')

    #Transform data from the csv files into the specified json format and write it into student.json
    transformed_data=transform_data(student_data, program_data)

    write_to_json(transformed_data, 'student.json')
    with open('student.json', 'r') as f:
        student_university_data = json.load(f)

    #Retrieve each student's university data 
    for username, data in student_university_data.items():

        #Retrieves the campus object corresponding to the student's campus identifier, and if it doesn't exist, it creates a new campus object with the provided identifier.
        campus, _ = Campus.objects.get_or_create(identifier=data['student']['campus'])

        #retrieves the user object and creates a new if it doesnot exists with provided username, first name, last name, and email address.
        user, _ = User.objects.get_or_create(username=username,
                                             first_name=data['student']['first_name'],
                                             last_name=data['student']['last_name'],
                                             email=data['student']['email'])
        
        # retrieves the student object and creates a new if it doesn't exist with the provided user, campus, and GPA data.
        student, _ = Student.objects.get_or_create(user=user,
                                                   campus=campus,
                                                   gpa=data['student']['gpa'])

        #retrieves the program data for the student and iterates over each program in the student's plan.
        for program, program_data in data['plan']['programs'].items():

             #retrieves the program object and creates a new if it doesn't exist with the program identifier.
            program_obj, _ = Program.objects.get_or_create(identifier=program)

            #retrieves the student program object corresponding to the student and program objects,

            # # If it doesn't exist, it creates a new student program object.
            # #If it does exist, it updates the priority order data.
            
            student_program, _ = StudentProgram.objects.update_or_create(
                student=student,
                program=program_obj,
                defaults={
                    'priority_order': program_data['priority_order'],
                },
            )

    return HttpResponse(' Data Stored Successfully!')