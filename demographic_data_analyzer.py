import pandas as pd

data= [
    {"age": 39, "workclass": "State-gov", "fnlwgt": 77516, "education": "Bachelors",
     "education-num": 13, "marital-status": "Never-married", "occupation": "Adm-clerical",
     "relationship": "Not-in-family", "race": "White", "sex": "Male",
     "capital-gain": 2174, "capital-loss": 0, "hours-per-week": 40,
     "native-country": "United-States", "salary": "<=50K"},
     
    {"age": 50, "workclass": "Self-emp-not-inc", "fnlwgt": 83311, "education": "Bachelors",
     "education-num": 13, "marital-status": "Married-civ-spouse", "occupation": "Exec-managerial",
     "relationship": "Husband", "race": "White", "sex": "Male",
     "capital-gain": 0, "capital-loss": 0, "hours-per-week": 13,
     "native-country": "United-States", "salary": "<=50K"},
     
    {"age": 38, "workclass": "Private", "fnlwgt": 215646, "education": "HS-grad",
     "education-num": 9, "marital-status": "Divorced", "occupation": "Handlers-cleaners",
     "relationship": "Not-in-family", "race": "White", "sex": "Male",
     "capital-gain": 0, "capital-loss": 0, "hours-per-week": 40,
     "native-country": "United-States", "salary": "<=50K"},
     
    {"age": 53, "workclass": "Private", "fnlwgt": 234721, "education": "11th",
     "education-num": 7, "marital-status": "Married-civ-spouse", "occupation": "Handlers-cleaners",
     "relationship": "Husband", "race": "Black", "sex": "Male",
     "capital-gain": 0, "capital-loss": 0, "hours-per-week": 40,
     "native-country": "United-States", "salary": "<=50K"},
     
    {"age": 28, "workclass": "Private", "fnlwgt": 338409, "education": "Bachelors",
     "education-num": 13, "marital-status": "Married-civ-spouse", "occupation": "Prof-specialty",
     "relationship": "Wife", "race": "Black", "sex": "Female",
     "capital-gain": 0, "capital-loss": 0, "hours-per-week": 40,
     "native-country": "Cuba", "salary": "<=50K"}
]

Demographic = pd.DataFrame(data)
#make a dataframe from the data list of dictionaries
print(Demographic)
# show the dataframe
count_race=Demographic["race"].value_counts()
print(count_race)
# the count of race column is as follows:
# White    3
# Black    2
age_mean=Demographic[Demographic["sex"] == "Male"]["age"].mean()
print(age_mean)
# the average men age is 45.0
education_percentage=Demographic[Demographic["education"] == "Bachelors"].shape[0] / Demographic.shape[0] * 100
print(education_percentage)
# the percentage of people with a Bachelors degree is 60.0%
education_higher_percentage=Demographic[Demographic["education"].isin(["Bachelors","Masters","Doctorate"]) & (Demographic["salary"]==">50K")].shape[0] / (Demographic["education"].isin(["Bachelors","Masters","Doctorate"])).sum()* 100
print(education_higher_percentage)
# no one with a salary of >50K has a Bachelors, Masters, or Doctorate degree in this dataset, so the output is 0.0%.
education_lower_percentage=Demographic[(Demographic["education"] != "Bachelors") & (Demographic["education"] != "Masters") & (Demographic["education"] != "Doctorate")&(Demographic["salary"]==">50K")].shape[0] / (Demographic["education"].value_counts()).sum() * 100
print(education_lower_percentage)
# no one with a salary of >50K has an education level other than Bachelors, Masters, or Doctorate in this dataset, so the output is 0.0%.
hours_min=Demographic["hours-per-week"].min()
print(hours_min)
# the minimum number of hours a person works per week is 13 hours.
hours_min=Demographic[(Demographic["salary"] == ">50K")]["hours-per-week"].min()
print(hours_min)
# there are no people with a salary of >50K in this dataset, so the output is NaN (Not a Number).
native_country_counts=Demographic[(Demographic["salary"] == ">50K")]["native-country"].value_counts()
print(native_country_counts)
# there are no people with a salary of >50K in this dataset, so the output is an empty Series.
native_country_counts_india=Demographic[(Demographic["salary"] == ">50K")&(Demographic["native-country"] == "India")].value_counts()
print(native_country_counts_india)
# there are no people with a salary of >50K and native country of India in this dataset, so the output is an empty Series.