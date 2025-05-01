import random

names = ["Jordan", "Taylor", "Alex", "Morgan"]
ages = list(range(18, 66))
locations = ["New York", "California", "Texas", "Virginia"]
interests = ["cybersecurity", "machine learning", "signal processing", "data science"]

profile = {
    "name": random.choice(names),
    "age": random.choice(ages),
    "location": random.choice(locations),
    "interest": random.choice(interests)
}

print("Generated Profile:")
for k, v in profile.items():
    print(f"{k.title()}: {v}")
