import os
import matplotlib.pyplot as plt

def loadStudents(fileName):
  students = {}
  with open(fileName, "r") as f:
    for line in f:
      line = line.strip()
      studentID = line[:3]
      name = line[3:]
      students[name] = studentID
  return students
def loadAssignments(fileName):
  assignments = {}
  with open(fileName, "r") as f:
    lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 3):
      name = lines[i]
      assignmentID = lines[i + 1]
      pointValue = int(lines[i + 2])
      assignment[name] = {"id": assignmentID, "points": pointValue}
  return assignments

def loadSubmissions(folder):
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

def studentGrade(students, assignments, submissions):
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

def assignmentStatistics(assignments, submissions):
  assignmentSName = input("What is the assignment name: ").strip()
  if name not in assignments:
    print("Assignment no found")
    return
  assignID = assignment[name]["ID"]
  scores = [sub["percent"] for sub in submission if sub["assignmentID"] == assignID]

  if not scores:
    print("No submissions found for this assignment.")
    return

  minScore = round(min(scores))
  avgScore = round(sum(scores) / len(scores))
  maxScore = round(max(scores))

  print(f"Min: {minScore}%")
  print(f"Avg: {avgScore}%")
  print(f"Max: {maxScore}%")

def assignmentGraph(assignment, submissions):
  assignmentGName = input("What is the assignment name: ").strip()
  if name not in assignments:
    print("Assignment not found")
    return
  assignID = assignment[name]["ID"]
  scores = [sub["percent"] for sub in submissions if sub["assignmentID"] == assignID]

  if not scores:
    print("No submission found for this assignment.")
    return

  plt.figure(figSize=(8,6))
  plt.hist(scores, bin=7, edgeColor='black')

  plt.title(f"Scores for {assignmentGName}")
  plt.xlabel("Score (%)")
  plt.ylabel("Number of Students")

  plt.xlim(45, 100)
  plt.ylim(0, 8)

  plt.grid(axis='y', linestyle='--', alpha=0.7)

  plt.show()

def main():
  students = loadStudents("students.txt")
  assignments = loadAssignments("assignments.txt")
  sumbissions = loadSubmissions("submission.txt")

  print("1. Student grade")
  print("2. Assignment statistics")
  print("3. Assignment graph")
  choice = input("Enter your selection ").strip()
  
  if choice == "1":
    studentGrade(students, assignments, submissions)
  elif choice == "2":
    assignmentStatistics(assignments, submissions)
  elif choice == "3":
    assignmentGraph(assignments, submissions)

if __name__ == "__main__":
  main()
  

