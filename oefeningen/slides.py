
#oppvervlakte cirkel
# def oppvlakte_cirkel(straal):
#     try:
#         if straal == 0:
#             print("De straal mag niet nul zijn")
            
#         else:
#             straal = float(straal)
#             oppervlakte = 3.14 * straal * straal
#             print(f"De oppervlakte van de cirkel is {oppervlakte}")

#     except ValueError:
#         print("Verkeerde waarde werd ingegeven")


# print("Geef de straal van de cirkel in: ", end="")
# straal= input().strip()
# oppvlakte_cirkel(straal)

#BMI 
# def bmi(lengte, gewicht):
#     try:
#         lengte = float(lengte)
#         gewicht = float(gewicht)
#         if lengte <= 0:
#             print("De lengte moet groter zijn dan 0")
#         elif gewicht <= 0:
#             print("Het gewicht moet groter zijn dan 0")       
#         else:
#             BMI = gewicht / (lengte * lengte)
#             print(f"Op basis van uw lengte en gewicht schatten wij uw BMI op {BMI:.2f}")

#             if BMI < 18.5:
#                 print("Categorie: ondergewicht")
#             elif BMI <= 18.5 or BMI < 25:
#                 print("Categorie: gezond gewicht")
#             elif BMI <= 25 or BMI < 30:
#                 print("Categorie overgewicht")
#             else:
#                 print("Categorie: obesitas")
#     except ValueError:
#         print("De verkeerde waarden werden ingegeven")

# print("Geef uw lengte in in meter: ", end="")
# lengte = input().strip()
# print("Geef uw gewicht in in kg: ", end="")
# gewicht = input().strip()
# bmi(lengte, gewicht)

#wafels
# print("Voor hoeveel personen wilt u wafels bakken? ", end="")
# aantal = input().strip()
# aantal = (float(aantal))

# bloem = aantal * 50
# ei = aantal * 1
# melk = aantal * 120
# suiker = aantal * 10

# try:
#     if aantal <= 0:
#         print("Het aantal personen moet meer zijn dan 0")
#     else:
#         print(f"\nDit zijn de ingrediënten voor {aantal} personen: ")
#         print(f"{bloem:.0f}gr bloem")
#         print(f"{ei:.0f} eieren")
#         print(f"{melk:.0f}cl melk")
#         print(f"{suiker:.0f}gr suiker")
    
# except ValueError:
#     print("De verkeerde waarde werd ingegeven")

print("""
Dit zijn
      meerdere
      regels       
      """)
