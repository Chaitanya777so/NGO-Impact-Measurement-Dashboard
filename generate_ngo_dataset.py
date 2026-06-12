import pandas as pd
import numpy as np
from random import choice, randint
from datetime import datetime, timedelta

# Number of records
n = 1000

# Lists
genders = ["Male", "Female"]

districts = [
    "Roorkee",
    "Haridwar",
    "Dehradun",
    "Nainital",
    "Udham Singh Nagar"
]

programs = [
    "Digital Literacy",
    "Skill Development",
    "Employment Readiness"
]

data = []

start_date = datetime(2024, 1, 1)

for i in range(n):

    beneficiary_id = f"B{1001+i}"

    gender = choice(genders)

    age = randint(18, 45)

    district = choice(districts)

    state = "Uttarakhand"

    program = choice(programs)

    program_date = start_date + timedelta(days=randint(0, 730))

    workshop_hours = choice([4, 6, 8])

    program_cost = randint(1000, 5000)

    completion_status = np.random.choice(
        ["Completed", "Incomplete"],
        p=[0.85, 0.15]
    )

    pre_score = randint(20, 70)

    improvement = randint(5, 40)

    post_score = min(pre_score + improvement, 100)

    improvement_percentage = round(
        ((post_score - pre_score) / pre_score) * 100,
        2
    )

    employment_status = np.random.choice(
        ["Employed", "Unemployed"],
        p=[0.45, 0.55]
    )

    outcome_status = (
        "Improved"
        if improvement_percentage >= 20
        else "Not Improved"
    )

    data.append([
        beneficiary_id,
        gender,
        age,
        district,
        state,
        program,
        program_date.date(),
        workshop_hours,
        program_cost,
        completion_status,
        pre_score,
        post_score,
        improvement_percentage,
        employment_status,
        outcome_status
    ])

columns = [
    "Beneficiary_ID",
    "Gender",
    "Age",
    "District",
    "State",
    "Program_Name",
    "Program_Date",
    "Workshop_Hours",
    "Program_Cost",
    "Completion_Status",
    "Pre_Assessment_Score",
    "Post_Assessment_Score",
    "Improvement_Percentage",
    "Employment_Status",
    "Outcome_Status"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("NGO_Impact_Data.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())