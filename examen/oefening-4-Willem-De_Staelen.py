scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95
}

hoogste_cijfer_naam = max(scores, key=scores.get)
print(f"De student met de hoogste score is {hoogste_cijfer_naam}")