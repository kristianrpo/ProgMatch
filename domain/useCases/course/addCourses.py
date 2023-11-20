import pandas as pd
from django.shortcuts import render
from domain.entities.course.courseEntity import course

def populate_database(request):

    csv_file_path = 'C:/Users/Luisa/Downloads/temporal/courses_data.csv'

    data = pd.read_csv(csv_file_path, encoding='latin1')

    for index, row in data.iterrows():
        course_instance = course(
            courseCode=row['courseCode'],
            name=row['name'],
            length=row['length'],
            price=row['price'],
            modality=row['modality'],
            content=row['content'],
            description=row['description'],
            idInstitution_id= row['idInstitution'], 
            link=row['link'],
            difficulty=row['difficulty']
        )
        course_instance.save()

    return 1