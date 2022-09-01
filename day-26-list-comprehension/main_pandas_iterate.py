import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_df = pd.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)