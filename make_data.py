import pandas as pd  

def create_student_data_csv(filename="student_marks.csv"):
    data = {
        "Id": [1001, 1002, 1003, 1004, 1005, 1006],
        "F Name": ["Ayushi", "Shlok", "Riya", "Kara", "Akansha", "Aditya"],
        "L Name": ["Das", "Bhos", "Dubey", "Singh", "Raut", "Patil"],
        "Gender": ["Female", "Male", "Female", "Female", "Female", "Male"],
        "Age": [15, 16, 15, 14, 16, 14],
        "Marks": [50, 46, 40, 49, 39, 47],
        "Grade": ["A+", "A+", "B+", "A+", "B+", "A+"]
    }

    df = pd.DataFrame(data)
    df = df.reset_index(drop=True)
    df.index += 1
    print(df)

    print(f"✅ '{filename}' has been created successfully.")

if __name__ == "__main__":
    create_student_data_csv()  
