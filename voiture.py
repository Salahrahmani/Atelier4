class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None
    def afficherInformations(self):

        print("Voiture:", self.marque)

        if self.chauffeur:
            print("Chauffeur:", self.chauffeur.nom)
        else:
            print("Aucun chauffeur")