cijfers = {
    'Karel': [18, 20, 19],
    'Tim': [17, 16, 20],
    'Caroline': [21, 25, 17],
    'Jasper': [26, 19, 17],
    'Hugo': [10, 14, 25],
    'Kaat': [9, 18, 25],
    'Jan': [12, 24, 30],
    'Leen': [30, 18, 24],
    'Frank': [18, 24, 26],
    }

for student, punten in cijfers.items():
    gemiddelde = sum(punten) / len(punten)
    print(f"De student {student} heeft een gemiddelde cijfer van {gemiddelde:.2f}")


   
    

    
    
    


