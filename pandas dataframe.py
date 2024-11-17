import pandas as pd
#changing dictionary to dataframe
student = {"name": ["fgui", "asedr", "ergyh", "yghj"], "age": [10, 20, 10, 20], "city": ["london", "paris", "london", "paris"], "score": [23, 47, 23, 47]}
student_df = pd.DataFrame(student)
print(student_df)
print(type(student_df))

#number of rows and columns
print(student_df.shape)

#access columns
print(student_df["age"])
print(student_df["age"].max())
print(student_df["score"].mean())

#count of unique values
print(student_df["city"].value_counts())

#summary of data
print(student_df.info())

#statistical summary
print(student_df.describe())