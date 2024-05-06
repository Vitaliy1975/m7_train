from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(255),unique=True)
    group_id = Column(Integer,ForeignKey("groups.id",ondelete="cascade"))
    group=relationship("Groupp",back_populates="student")
    grade=relationship("Grade",back_populates="student")

class Groupp(Base):
    __tablename__ = "groups"
    id = Column(Integer,primary_key=True,autoincrement=True)
    group_name = Column(String(25), unique=True)
    student=relationship("Student",back_populates="group")

class Subject(Base):
    __tablename__="subjects"
    id=Column(Integer,primary_key=True)
    subject_name=Column(String(255),unique=True)
    tutor_name=Column(String(255),ForeignKey("tutors.tutor_name",ondelete="cascade"),unique=False)
    tutor = relationship("Tutor",back_populates="subject")
    grade=relationship("Grade",back_populates="subject")


class Tutor(Base):
    __tablename__="tutors"
    id=Column(Integer,primary_key=True)
    tutor_name=Column(String(255),unique=True)
    subject=relationship("Subject",back_populates="tutor")

class Grade(Base):
    __tablename__="grades"
    id=Column(Integer,primary_key=True)
    student_name=Column(String(255),ForeignKey("students.student_name",ondelete="cascade"),unique=False)
    student=relationship("Student",back_populates="grade")
    subject_name=Column(String(255),ForeignKey("subjects.subject_name",ondelete="cascade"),unique=False)
    subject=relationship("Subject",back_populates="grade")
    grade=Column(Integer)
    date_of_grade=Column(DateTime)
