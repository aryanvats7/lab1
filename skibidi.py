import pandas as pd

def dropMissingData(students):
    return students.dropna(axis=0)  
    

df=pd.DataFrame({
    'student_id' : [32,217,779,849],
    'name' : ['Piper',None,'Georgia','Willow'],
    'age' : [5,19,20,14]
})

print(dropMissingData(df))