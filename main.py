from employe import Employe
from voiture import Voiture

e1 = Employe("G687", "Rahmani", "Salah")
e2 = Employe("k198", "Saadi", "Ramzi")

v1 = Voiture("HA579", 2025, "Renault", 19000)
v2 = Voiture("OP372", 2026, "Kia", 4500)
# affich info
e1.afficherInformations()
e2.afficherInformations()

v1.afficherInformations()
v2.afficherInformations()
#give cars to the empl
e1.affecterVoiture(v1)
e2.affecterVoiture(v2)
e1.afficherInformations()
e2.afficherInformations()
#remove car
e1.retirerVoiture()