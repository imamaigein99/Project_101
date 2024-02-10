from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import logging


# FastAPI app instance
app = FastAPI(
    title="Student Management API",
    description="An API to manage student records",
    version="1.0.0",
    docs_url="/docs",  # Endpoint for Swagger UI
    redoc_url=None,    # Disable ReDoc
)

# In-memory storage using Python dictionary
storage: Dict[int, dict] = {}

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Student(BaseModel):
    name: str
    age: int
    sex: str
    height: float


# Create a Student resource
@app.post("/students/")
def create_student(student: Student):
    for student_id, data in storage.items():
        if data == student.dict():
            logging.info(f"Student with attributes {student.dict()} already exists.")
            raise HTTPException(status_code=400, detail="Student already exists")

    student_id = len(storage) + 1
    storage[student_id] = student.dict()
    logging.info(f"Created new student with id {student_id} and attributes {student.dict()}")
    return {"id": student_id, **student.dict()}


# Retrieve a Student resource (one Student)
@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id not in storage:
        raise HTTPException(status_code=404, detail="Student not found")
    return storage[student_id]


# Retrieve all Students
@app.get("/students/")
def read_students():
    return storage


# Update a Student resource
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in storage:
        raise HTTPException(status_code=400, detail="Student not found")
    storage[student_id] = student.dict()
    logging.info(f"Updated student with id {student_id} and attributes {student.dict()}")
    return {"message": "Student updated successfully"}


# Delete a Student resource
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in storage:
        raise HTTPException(status_code=404, detail="Student not found")
    del storage[student_id]
    logging.info(f"Deleted student with id {student_id}")
    return {"message": "Student deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8100)
