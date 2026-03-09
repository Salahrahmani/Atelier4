class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):

            print("Employe:", self.nom, self.prenom)

            if self.voitureService:
                print("Voiture:", self.voitureService.marque)
            else:
                print("Aucune voiture")
    def affecterVoiture(self, voiture):

        if self.voitureService:
            print("Employe a deja une voiture")
            return

        if voiture.chauffeur:
            print("Voiture deja attribuee")
            return

        self.voitureService = voiture
        voiture.chauffeur = self
    def retirerVoiture(self):

        if self.voitureService is None:
            print("Aucune voiture")
            return

        voiture = self.voitureService
        self.voitureService = None
        voiture.chauffeur = None
    