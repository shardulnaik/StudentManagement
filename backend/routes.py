from flask import request, jsonify
from models import db, Student

def register_routes(app):

    # 1. CREATE - Add a new student
    @app.route("/students", methods=["POST"])
    def add_student():
        data = request.get_json()
        student = Student(
            name=data["name"],
            age=data["age"],
            course=data["course"]
        )
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student added successfully"}), 201

    # 2. READ - Get all students
    @app.route("/students", methods=["GET"])
    def get_students():
        students = Student.query.all()
        output = []
        for student in students:
            output.append({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course
            })
        return jsonify(output), 200

    # 3. READ - Get a single student by ID
    @app.route("/students/<int:id>", methods=["GET"])
    def get_student(id):
        student = Student.query.get_or_404(id)
        return jsonify({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course
        }), 200

    # 4. UPDATE - Update a student by ID
    @app.route("/students/<int:id>", methods=["PUT"])
    def update_student(id):
        student = Student.query.get_or_404(id)
        data = request.get_json()

        student.name = data.get("name", student.name)
        student.age = data.get("age", student.age)
        student.course = data.get("course", student.course)

        db.session.commit()
        return jsonify({"message": "Student updated successfully"}), 200

    # 5. DELETE - Delete a student by ID
    @app.route("/students/<int:id>", methods=["DELETE"])
    def delete_student(id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully"}), 200