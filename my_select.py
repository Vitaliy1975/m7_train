from connect_db import session
from models_05 import Student,Grade,Groupp,Tutor,Subject
from sqlalchemy import func,desc, select, and_


def select_1():
    return session.query(Student.student_name, func.avg(Grade.grade).label('average_grade')).join(Grade).group_by(Student.student_name).order_by(desc('average_grade')).limit(5).all()

def select_2(subject):
    return session.query(Student.student_name, Subject.subject_name, func.avg(Grade.grade))\
        .join(Grade, Student.student_name == Grade.student_name)\
        .join(Subject, Grade.subject_name == Subject.subject_name)\
        .filter(Subject.subject_name == subject)\
        .group_by(Student.student_name, Subject.subject_name)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(1)\
        .all()

def select_3(subject):
    return session.query(Groupp.group_name, func.avg(Grade.grade).label('av'), Subject.subject_name)\
.join(Student, Grade.student_name == Student.student_name)\
.join(Groupp, Student.group_id == Groupp.id)\
.join(Subject, Grade.subject_name == Subject.subject_name)\
.filter(Subject.subject_name == subject)\
.group_by(Groupp.group_name, Subject.subject_name)\
.order_by(func.avg(Grade.grade).desc()).all()

def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(tutor_name):
    return session.query(Subject.subject_name, Tutor.tutor_name)\
.join(Tutor, Subject.tutor_name == Tutor.tutor_name)\
.filter(Tutor.tutor_name == tutor_name)\
.all()

def select_6(group):
    return session.query(Student.student_name, Groupp.group_name)\
.join(Groupp, Student.group_id == Groupp.id)\
.filter(Groupp.group_name == group)\
.all()

def select_7(group,subject):
    return session.query(Student.student_name, Grade.grade, Grade.subject_name, Groupp.group_name)\
.join(Grade, Grade.student_name == Student.student_name)\
.join(Groupp, Student.group_id == Groupp.id)\
.join(Subject, Grade.subject_name == Subject.subject_name)\
.filter(Groupp.group_name == group, Subject.subject_name == subject)\
.all()

def select_8(tutor_name):
    return session.query(func.avg(Grade.grade), Tutor.tutor_name)\
.join(Subject, Grade.subject_name == Subject.subject_name)\
.join(Tutor, Subject.tutor_name == Tutor.tutor_name)\
.filter(Tutor.tutor_name == tutor_name)\
.group_by(Tutor.tutor_name)\
.all()

def select_9(student):
    return session.query(Student.student_name, Subject.subject_name)\
.join(Grade, Student.student_name == Grade.student_name)\
.join(Subject, Grade.subject_name == Subject.subject_name)\
.filter(Student.student_name == student)\
.group_by(Subject.subject_name, Student.student_name)\
.all()

def select_10(student,tutor):
    return session.query(Student.student_name, Subject.subject_name, Tutor.tutor_name)\
.join(Grade, Student.student_name == Grade.student_name)\
.join(Subject, Grade.subject_name == Subject.subject_name)\
.join(Tutor, Subject.tutor_name == Tutor.tutor_name)\
.filter(Student.student_name ==student , Tutor.tutor_name == tutor)\
.group_by(Subject.subject_name, Student.student_name, Tutor.tutor_name)\
.all()

if __name__=="__main__":
    print(select_1())
    print(select_2("Linguistics"))
    print(select_3('Computer Science'))
    print(select_4())
    print(select_5("Jillian Klein"))
    print(select_6("second_group"))
    print(select_7(group="third_group",subject="Economics"))
    print(select_8('Christina Hernandez'))
    print(select_9('Zachary Robles'))
    print(select_10(student='Sierra Ryan',tutor="John Kidd"))