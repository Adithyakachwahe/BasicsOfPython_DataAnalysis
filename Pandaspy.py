import pandas as pd

# Read the Excel file
excel_file_path = "Book2.xlsx"
df = pd.read_excel(excel_file_path)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Action 1: Selecting a specific column
age_column = df['Age']
print("\nSelected 'Age' column:")
print(age_column)

# Action 2: Filtering data based on a condition
young_people = df[df['Age'] < 30]
print("\nPeople under 30:")
print(young_people)

# Action 3: Aggregating data
average_age = df['Age'].mean()
total_age = df['Age'].sum()
print("\nAverage Age:", average_age)
print("Total Age:", total_age)


# Action 4: Handling missing data (filling missing ages with the mean)
df_filled = df.fillna({'Age': df['Age'].mean()})
print("\nDataFrame after filling missing values:")
print(df_filled)

# Action 5: Writing the modified DataFrame to a new Excel file
output_excel_path = "Modified_Book.xlsx"
df_filled.to_excel(output_excel_path, index=False)
print("\nModified DataFrame written to Excel file:", output_excel_path)
