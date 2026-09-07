name = input("Enter Student Name: ")
average = float(input("Enter Average Grade: "))
attendance = float(input("Enter Attendance: "))

print("SCHOLARSHIP RESULT")
print("Name", name)

if average >= 85:
    if attendance >= 90:
        print("Result: Qualified for Scholarship")
        
    else:
        print("Result: Not Qualified - Low Attendance")
        
else:
        print("Result: Not Qualified - Average Grade is under 85")
