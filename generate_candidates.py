import json
import random

names = ["Rahul", "Ananya", "Amit", "Sneha", "Vikram", "Priya", "Karan", "Neha", "Arjun", "Simran"]
surnames = ["Sharma", "Verma", "Patel", "Iyer", "Singh", "Nair", "Mehta", "Gupta", "Reddy", "Kaur"]

skills_pool = [
    ["Python", "FastAPI", "Machine Learning"],
    ["React", "JavaScript", "CSS"],
    ["Java", "Spring Boot", "Microservices"],
    ["SQL", "PowerBI", "Excel"],
    ["AWS", "Docker", "Kubernetes"],
    ["TensorFlow", "Pandas", "NLP"]
]

locations = ["Delhi", "Bangalore", "Mumbai", "Hyderabad", "Chennai", "Pune", "Noida"]

candidates = []

for i in range(100):
    name = random.choice(names) + " " + random.choice(surnames)
    skills = random.choice(skills_pool)
    experience = random.randint(1, 7)
    location = random.choice(locations)

    candidates.append({
        "name": name,
        "skills": skills,
        "experience": experience,
        "location": location,
        "summary": f"{experience} years experience working with {', '.join(skills)}."
    })

with open("backend2\data\candidates.json", "w") as f:
    json.dump(candidates, f, indent=2)

print("✅ 100 candidates generated!")