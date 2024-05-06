from connect_db import session
from models_05 import Student,Grade,Groupp,Tutor,Subject
import faker
from datetime import datetime
from random import randint, choice


def fill_tutors():
    fake_data = faker.Faker()
    for _ in range(5):
        fake_name=fake_data.name()
        tutor = Tutor(tutor_name=fake_name)
        session.add(tutor)
    session.commit()

def fill_subjects():
    tutors = (session.query(Tutor).all())
    fake_subjects = ["Anthropology","Archaeology","Linguistics","Psychology","Computer Science","Physics","Economics","Literature"]
    for i in range(len(fake_subjects)):
        subject=Subject(subject_name=fake_subjects[i],tutor_name=choice(tutors).tutor_name)
        session.add(subject)
    session.commit()

def fill_groups():
    fake_groups = ["first_group","second_group","third_group"]
    for i in range(len(fake_groups)):
        group=Groupp(group_name=fake_groups[i])
        session.add(group)
    session.commit()

def fill_students():
    fake_data=faker.Faker()
    for _ in range(50):
        fake_name=fake_data.name()
        student=Student(student_name=fake_name,group_id=randint(1,3))
        session.add(student)
    session.commit()

def fill_grades():
    student=(session.query(Student).all())
    subject=(session.query(Subject).all())
    for i in student:
        for _ in range(20):
            grade=Grade(student_name=i.student_name,subject_name=choice(subject).subject_name,grade=randint(6,12),date_of_grade=datetime(year=2023,month=randint(1,12),day=randint(1,28)))
            session.add(grade)
    session.commit()



if __name__ == "__main__":
    # fill_tutors()
    # fill_groups()
    # fill_subjects()
    # fill_students()
    # fill_grades()
    pass