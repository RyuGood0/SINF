"""
Classes fournies pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
   
@author Kim Mens
@version 4 novembre 2021
"""
class Article :
    def __init__(self,d,p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p
        
    def description(self) :
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) :
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """    
        return 0.21   # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""

class Facture :

    def __init__(self, d, a_list, num):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__num = num
        self.__description = d
        self.__articles = a_list
        
    def description(self) :
        """
        @post: retourne la description de cette facture.
        """
        return self.__description
    
    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return f"Facture No {self.__num} - " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
               + self.barre_str()
        
    # Cette méthode doit être ajouté lors de l'étape 2.5 de la mission    
    def nombre(self, pce) :
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        for art in self.__articles :
            if isinstance(art, ArticlePiece):
                if art.piece() == pce :
                    return art.nombre()
        return 0

    def article_livraison_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
               en indiquant le nombre d'exemplaires de cet article livrés.
        """
        pc = art.piece()
        new_desc = f"{pc.description()} @ {pc.prix():.2f}" if not pc.fragile() else f"{pc.description()} @ {pc.prix():.2f} (!)"
        return "| {0:40} | {1:10.2f} | {2:10} | {3:8.3f}kg |\n".format(new_desc, art.poids(), art.nombre(), art.poids() * art.nombre())

    # Cette méthode doit être ajouté lors de l'étape 2.6 de la mission    
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = f"Livraison - Facture No {self.__num} : {self.__description}\n"
        s += self.barre_str()
        s += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids")
        s += self.barre_str()

        total_pieces = 0
        total_poids = 0.0
        is_fragile = False
        for art in self.__articles:
            if isinstance(art, ArticlePiece):
                total_pieces += art.nombre()
                total_poids += art.poids()
                if art.piece().fragile():
                    is_fragile = True
                s += self.article_livraison_str(art)
        s += self.barre_str()

        empty = " " * (30 - len(str(len(self.__articles))))

        s += "| {0} articles {1} |            | {0: >10} | {0: >8}kg |\n".format(len(self.__articles), empty, total_pieces, total_poids)
        s += self.barre_str()
        s += "(!) *** livraison fragile ***" if is_fragile else ""

        return s

#########################
### ARTICLEREPARATION ###
#########################

# Cette classe doit être ajouté lors de l'étape 2.2 de la mission    
class ArticleReparation(Article):
    """
    Définissez une méthode d'initialisation avec la durée en paramètre.
    Re-définissez la méthode description() pour fournir un descriptif adéquat comme Reparation (0.75 heures).
    Re-définissez la méthode prix() pour calculer un coût fixe de 20 euro plus un coût variable de 35 euro/h. Pour une réparation de 0.75 heures ça donne donc un coût de 20 + 35*0.75 = 46.25 euro HTVA.
    """
    
    def __init__(self, h):
        """
        @pre  d est un string décrivant l'article;
              p est le prix HTVA de l'article;
              h est le nombre d'heures de réparation de l'article.
        @post Une instance de la classe ArticleReparation avec une description d, un prix p et une durée de réparation h été crée.
        """
        self.__duree = h
        super().__init__("", self.prix())
        
    def description(self):
        """
        @post: retourne la description de cet article, au format: "{description} ({duree} heures)."
        """
        return f"Réparation ({self.__duree} heures)"
    
    def prix(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return 20 + self.__duree * 35


#############
### PIECE ###
#############

# Cette classe doit être ajouté lors de l'étape 2.3 de la mission    
"""
Créez une nouvelle classe ArticlePiece qui hérite de Article et qui représente l'achat pas d'un seul article mais d'un nombre donné d'une pièce donnée. (Par exemple, 3 souris Bluetooth à 15.99 EUR par pièce.)

Implémentez d'abord une nouvelle classe Piece qui représente la pièce dont on veut facturer plusieurs exemplaires. Elle comporte les données suivantes:

- une description (string), p.ex. 'souris bluetooth';
- un prix unitaire (float), p.ex. 15.99 Euro;
et, optionnellement

- un poids unitaire en kg (float), p.ex. 0,154 kg;
- un indicateur booléen indiquant si la pièce est fragile, p.ex. un disque dur est fragile mais pas une souris;
- un indicateur booléen indiquant si la pièce est à taux de TVA réduit, p.ex. les livres bénéficient de TVA réduite.
Ajoutez une méthode d'initialisation permettant d'initialiser toutes ces données. Cette méthode d'initialisation doit aussi être utilisable avec seulement les deux paramètres obligatoires (description et prix) pour les pièces de poids négligeable, non fragiles et à taux de TVA normal (en assignant des valeurs par défaut pour les autres paramètres dans ce cas).
Ajoutez des méthodes accèsseurs (description() , prix() , poids() , fragile() , tva_reduit()) pour toutes ces données.
Ajoutez une méthode magique __eq__ afin que deux pièces sont considérées égales ( == ) si elles ont la même description et le même prix (les autres données sont ignorées pour la comparaison).
"""
class Piece:
    def __init__(self, desc, prix, prix_par_kg=0, fragile=False, tva_reduit=False):
        self.__description = desc
        self.__prix = prix
        self.__poids = prix_par_kg
        self.__fragile = fragile
        self.__tva_reduit = tva_reduit

    def description(self):
        return self.__description

    def prix(self):
        return self.__prix
    
    def poids(self):
        return self.__poids
    
    def fragile(self):
        return self.__fragile
    
    def tva_reduit(self):
        return self.__tva_reduit
    
    def __eq__(self, other):
        return self.description() == other.description() and self.prix() == other.prix()

####################
### ARTICLEPIECE ###
####################

# Cette classe doit être ajouté lors de l'étape 2.3 de la mission   
"""
Ajoutez une méthode d'initialisation prenant le nombre et la pièce en paramètres.
Ajoutez des méthodes accèsseurs pour ces deux attributs.
Re-définissez la méthode description() pour fournir un texte reprenant la description de la pièce, le nombre souhaité de cette pièce et son prix unitaire, par exemple: 3 * souris bluetooth @ 15.99 .
Re-définissez la méthode prix() pour faire le produit du prix unitaire de la pièce par le nombre de pièces souhaité.
Re-définissez la méthode taux_tva() pour appliquer un taux de 6% aux pièces à taux de TVA réduit, tout en gardant le taux de TVA original pour d'autres pièces.
""" 
class ArticlePiece(Article):
    def __init__(self, pce, nb, poids=0):
        """
        @pre:  pce une instance de la classe Piece
              nb un entier positif
        @post: Une instance de la classe ArticlePiece avec une description de la pièce pce et un nombre d'exemplaires nb créés.
        """
        self.__poids = poids
        self.__piece = pce
        self.__nombre = nb
        super().__init__(self.description(), self.prix())

    def piece(self):
        return self.__piece

    def nombre(self):
        return self.__nombre
    
    def poids(self):
        return self.__poids

    def description(self):
        s = f"{self.__nombre} * {self.piece().description()} @ {self.piece().prix():.2f}" if self.piece().poids() == 0 else f"{self.__nombre} * {self.piece().description()} @ {self.piece().poids():.2f}/kg"
        s += " (!)" if self.piece().fragile() else ""
        return s

    def prix(self):
        return self.piece().prix() * self.nombre() if self.piece().poids() == 0 else self.piece().poids() * self.poids()

    def taux_tva(self):
        return super().taux_tva() if not self.piece().tva_reduit() else 0.06

########################
### RUNNING THE CODE ###
########################

# Ajouter votre code ici pour imprimer une facture et un borderaux
# de livraison.

viande = Piece("Viande", 0, prix_par_kg=10, tva_reduit=True)
verre = Piece("Verre", 2, fragile=True)

articles = [ ArticlePiece(viande, 1, poids=0.5),
             ArticlePiece(verre, 5, poids=.2)
             ]

facture = Facture("PC Store - 22 novembre", articles, 1)

print(facture)
print(facture.livraison_str())