from tkinter import Scale
from fltica import abscisse_souris, attend_fermeture, cree_fenetre, donne_ev, efface_tout, image, mise_a_jour, ordonnee_souris, taille_texte, texte, type_ev
import csv

def reecrire(zone, NS):

    lst = fichier(zone, NS)
    for elem in lst:
        if elem[2] == zone and elem[3] == NS:
            image(elem[0], elem[1], "flag.png", 25, 25, ancrage="sw")

def carte(zone, NS):

    image(1920 // 2 + 100, 1080 // 2, zone+NS+".png", ancrage="center", width=1636, height=670)
    if zone_clic_menu((1920//20, 1080*1/7), "Nord") == False:
        selection(zone, NS)
        reecrire(zone, NS)
    
    

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
            if zone_clic_menu((1920//20, 1080*1/7), "Nord"):
                NordSud(zone)
            if zone_clic_menu((1920//20, 1080*1/3), "Sud"):
                NordSud(zone)
            if zone_clic_menu((0,0), "Quitter"):
                quit()
            

def zone_clic_menu(bouton, text):
    """
    Permet de vérifier si le clic est dans la zone d'un bouton qui est un tuple
    """
    
    a, b = taille_texte(text)
    a1, b1 = bouton
    if (a1 - 100 <= abscisse_souris() <= a1 + a + 100) and (b1 <= ordonnee_souris() <= b1 + b):
        return True

    return False

def Zone():
    x = 1920
    y = 1080
    texte(x//2, y*1/7, "Cliquez sur la zone de location", ancrage="center")
    texte(x//20, y*1/7, "Zone 1", ancrage="nw")
    texte(x//20, y*1/3, "Zone 2",ancrage="nw")
    texte(x//20, (y//2), "Zone 3", ancrage="nw")

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
            if zone_clic_menu((x//20, y*1/7), "Zone 1"):
                return NordSud("Zone1")
            if zone_clic_menu((x//20, y*1/3), "Zone 2"):
                return NordSud("Zone2")
            if zone_clic_menu((x//20, y//2), "Zone 3"):
                return NordSud("Zone3")
            

def NordSud(Zone):
    efface_tout()

    x = 1920
    y = 1080
    
    texte(x//2, y*1/7, "Location plutot Nord ou Sud", ancrage="center")
    texte(x//20, y*1/7, "Nord", ancrage="nw")
    texte(x//20, y*1/3, "Sud",ancrage="nw")
    
    
    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'ClicGauche':
            
            if zone_clic_menu((x//20, y*1/7), 'Nord'):
                return carte(Zone, "Nord")
            if zone_clic_menu((x//20, y*1/3), "Sud"):
                return carte(Zone, "Sud")

def traitement(cordonne, file="Info.csv"):
    with open(file, 'r') as f:
        ligne = csv.reader(f)
        for row in ligne:
            pass
        
def selection(zone, ns):

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            x, y = abscisse_souris(), ordonnee_souris()
            image(x, y, "flag.png", 25, 25, ancrage="sw")

            return x, y

def fichier(zone, ns):
    lst = []
    x, y = selection(zone, ns)
    f = open("Info.txt", "a")
    f.write(f"{x, y, zone, ns}\n")
    f.close()
    a = open("Info.txt", "r")
    lignes = a.readlines()
    f.close()
    for ligne in lignes:
        lst.append(((ligne[1:-2]).replace("'", '')).split(', '))
    return lst



if __name__ == "__main__":

    
    x = 1920
    y = 1080
    cree_fenetre(x, y)

    Zone()