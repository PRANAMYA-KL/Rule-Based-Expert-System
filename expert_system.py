# Expert System: Simple Medical Diagnosis
# Uses a set of rules to diagnose based on symptoms

print("=== Rule Based Expert System ===")

# Knowledge Base (Rules)
rules = [
    {"if": ["fever", "cough", "body ache"], "then": "You may have Flu"},
    {"if": ["fever", "cough"], "then": "You may have Cold"},
    {"if": ["headache", "sore throat"], "then": "You may have Viral Infection"},
    {"if": ["itchy eyes", "sneezing"], "then": "You may have Allergy"},
]

# Ask user for symptoms
print("Enter your symptoms one by one.")
print("Type 'done' when finished.\n")

facts = []
while True:
    symptom = input("Symptom: ").strip().lower()
    if symptom == "done":
        break
    if symptom:
        facts.append(symptom)

print("\nYour Symptoms:", facts)

# Inference Engine
diagnoses = []

for rule in rules:
    match = all(symptom in facts for symptom in rule["if"])
    if match:
        diagnoses.append(rule["then"])

# Output Results
if diagnoses:
    print("\nPossible Diagnosis:")
    for d in diagnoses:
        print("✔", d)
else:
    print("\nNo diagnosis could be made based on the given symptoms.")
