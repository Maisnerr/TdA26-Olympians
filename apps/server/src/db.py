from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from datetime import datetime
import json

db = SQLAlchemy()

from .bases import Course, Quiz, Question, Material, Feed

class CourseDB():
    def __str__(self):
        return "Test, všechno prošlo"

    ## GET /courses
    def get_all_courses():
        courses = Course.query.all()
        mezi = []
        for course in courses:
            mezi.append({
                'uuid': str(course.uuid),
                'name': course.name,
                'description': course.description,
                'createdAt': course.createdAt.isoformat(),
                'updatedAt': course.updatedAt.isoformat()
            })
        print("[d] - Fetched all courses")
        return mezi
    
    ## POST /courses
    def post_course(name, description):
        new_course = Course(name=name, description=description)
        db.session.add(new_course)
        db.session.commit()
        print("[d] - New course added:", new_course.name)
        return jsonify({
            'uuid': str(new_course.uuid),
            'name': new_course.name,
            'description': new_course.description,
            'createdAt': new_course.createdAt.isoformat(),
            'updatedAt': new_course.updatedAt.isoformat()
        })
    
    ## GET /courses/{CourseId}
    def get_specific_course(course_id):
        try:
            course = Course.query.filter_by(uuid=course_id).first()
        except:
            raise Exception("Course not found")
        quizzes, materials, feed = [], [], []

        quizzes = GetSpecificCourseSupport().quizzes_from_id(course_id)

        materials = MaterialDB().materials_from_id(course_id)

        feed = GetSpecificCourseSupport().feed_from_id(course_id)

        return jsonify({
            "uuid": course.uuid,
            "name": course.name,
            "description": course.description, 
            "materials": materials, 
            "quizzes": quizzes,
            "feed": feed,
            "createdAt": course.createdAt
        })

    ##PUT /courses/{CourseId}
    def put_specific_course(course_id, name, description):
        course = Course.query.filter_by(uuid=course_id).first()

        try:
            if(name):
                course.name = name
            if(description):
                course.description = description
            db.session.commit()
        except Exception as e:
            print(str(e))

    ## DELETE /courses/{CourseId}
    def delete_course(course_id):
        try:
            course = Course.query.filter_by(uuid=course_id).first()
        except Exception as e:
            print(str(e))    
        if course:
            db.session.delete(course)
            db.session.commit()
            print("[d] - Deleted course with ID:", course_id)
            return jsonify({"message": "Course deleted"})
        else:
            print("[d] - Couldnt find course ID", course_id,"to delete")
            raise Exception("Course not found")
        
    ## SUPPORT FUNCTION FOR:
    ## DELETE /courses/{CourseId}
    def delete_all_courses():
        courses = Course.query.all()
        for c in courses:
            db.session.delete(c)
        db.session.commit()
        print("[d] - Deleted ALL courses")

class GetSpecificCourseSupport():
    """
        This class contains all supporting functions from get_specific_course()
    """

## QUESTIONS

    ## SUPPORT FUNCTION FOR:
    ## GET /courses/{CourseId}
    def quizzes_from_id(self, course_id):
        quizzes_table = Quiz.query.filter_by(uuid_course=course_id).all()
        quizzes = []
        for quiz in quizzes_table:
            quizzes.append({
                "uuid": quiz.uuid,
                "title": quiz.title,
                "attempsCount": quiz.attempts,
                "questions": GetSpecificCourseSupport().questions_from_id(quiz.uuid)
                
            })
        return quizzes
    
    ## SUPPORT FUNCTION FOR:
    ## GET /courses/{CourseId} (quizzes_from_id)
    def questions_from_id(self, quiz_id):
        questions_table = Question.query.filter_by(uuid_quiz=quiz_id).all()
        questions = []
        for question in questions_table:
            if (question.type == "multipleChoice"):     ## Multiple Choice
                questions.append({
                    "uuid": question.uuid,
                    "type": question.type,
                    "question": question.question,
                    "options": question.options,
                    "correctIndicies": question.correct
                })
            else:                                       ## Single Choice
                questions.append({
                    "uuid": question.uuid,
                    "type": question.type,
                    "question": question.question,
                    "options": question.options,
                    "correctIndex": question.correct
                })
        return questions    
    
    def feed_from_id(self, course_id):
        feeds_table = Feed.query.filter_by(uuid_course=course_id).all()
        feeds = []
        for feed in feeds_table:
            feeds.append({
                "uuid": feed.uuid,
                "type": feed.type,
                "message": feed.message,
                "edited": feed.edited,
                "createdAt": feed.createdAt,
                "updatedAt": feed.updatedAt
            })
        return feeds

## MATERIALS
class MaterialDB():
    def materials_from_id(self, course_id):
        try:
            materials_table = Material.query.filter_by(uuid_course=course_id).all()
        except:
            raise Exception("Error while looking for course")
        materials = []
        for material in materials_table:
            if(material.type == "url"):
                materials.append({
                    "uuid": material.uuid,
                    "type": material.type,
                    "name": material.name,
                    "description": material.description,
                    "url": material.url,
                    "faviconUrl": MaterialDB().faviconUrl(material.url)
                })
            else:
                materials.append({
                    "uuid": material.uuid,
                    "type": material.type,
                    "name": material.name,
                    "description": material.description,
                    "fileUrl": material.url,
                    "mimeType": material.mimeType,
                    "sizeBytes": material.sizeBytes
                })
        return materials

    @staticmethod
    def faviconUrl(url):
        if "://" in url:
            url = url.split("://", 1)[1]
        url = url.split("/", 1)[0]
        if url.startswith("www."):
            url = url[4:]
        return "https://www.google.com/s2/favicons?sz=64&domain_url="+url
    
    def post_materials_url(self, course_id, data):
        course_check = Course.query.filter_by(uuid = course_id).first()

        if(not course_check):
            raise Exception("Course not found")

        new_material = Material(type=data["type"],
                            name=data["name"],
                            description=data["description"],
                            url=data["url"],
                            uuid_course=course_id)
        db.session.add(new_material)
        db.session.commit()

        return {"name": new_material.name,
                "description": new_material.description,
                "url": new_material.url,
                "uuidCourse": new_material.uuid_course,
                "uuid": new_material.uuid}

class CustomDB():
    @staticmethod
    def get_studies(course_id):
        course = Course.query.filter_by(uuid=course_id).first()
        if not course:
            raise Exception("Course not found")

        quizzes = Quiz.query.filter_by(uuid_course=course_id).all()
        materials = Material.query.filter_by(uuid_course=course_id).all()

        combined = []

        for quiz in quizzes:
            combined.append({
                "typeof": "quiz",
                "uuid": quiz.uuid,
                "title": quiz.title,
                "attempts": quiz.attempts,
                "createdAt": quiz.createdAt
            })

        for material in materials:
            combined.append({
                "faviconUrl": MaterialDB().faviconUrl(material.url),
                "type": material.type,
                "typeof": "material",
                "uuid": material.uuid,
                "name": material.name,
                "description": material.description,
                "url": material.url if material.type == "url" else None,
                "fileUrl": material.fileUrl if material.type != "url" else None,
                "sizeBytes": material.sizeBytes,
                "createdAt": material.createdAt
            })

        combined.sort(key=lambda x: x["createdAt"], reverse=True)

        return jsonify(combined), 200