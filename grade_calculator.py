import os
import matplotlib.pyplot as plt

def load_students(fileName):
  students = {}
  with open(fileName, "r") as f:
    for line in f:
      line = line.strip()
      studentID = line[:3]
      name = line[3:]
      students[name] = studentID
  return students
def load_assignments(fileName):
  assignments = {}
  with open(fileName, "r") as f:
    lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 3):
      name = lines[i]
      assignmentID = lines[i + 1]
      pointValue = int(lines[i + 2])
      assignment[name] = {"id": assignmentID, "points": pointValue}
  return assignments

def load_submissions(folder):
  submissions = []
  for filename in os.listdir(folder):
    path = os.path.join(folder, fileName)
    with open(path, "r") as f:
      for line in f:
        parts = line.strip().split("|")
        if len(parts) == 3:
          studentID, assignmentID, percent = parts
          submissions.append({
            "studentID": studentID,
            "assignmentID": assignmentID,
            "percent": float(percent)
          })
  return submissions

def student_grade(students, assignments, submissions):
  studentName = input("What is the student's name: ")
  if name not in students:
    print("Student not found")
    return
  studentID = students[name]
  totalEarned = 0

  for sub in submissions:
    if sub["studentID"] == studentID:
      for assign in assignment.values():
        if assign["ID"] == sub["assignmentID"]:
          earned = assignment["points"] * (sub["percent"] / 100)
          totalEarned += earned
          break
  finalPercent = round((totalEarned / 1000) * 100)
  print(f"{finalPercent}%")

def assignment_statistics(assignments, submissions):
  assignmentName = input("What is the assignment name: ").strip()
  if name not in assignments:
    print("Assignment no found")
    return
  assignID = assignment[name]["ID"]
  scores = [sub["percent"] for sub in submission if sub["assignmentID"] == assignID]

  if not 
