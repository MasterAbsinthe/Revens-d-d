# Navn: Espen Sales
# Dato: 28/09/2018
# Beskrivelse: Et kort tekst-basert spill som tar deg med på et spennende eventyr!

import random

def VisIntro():
    print()
    print("(trykk enter for å gå videre)")
    input()
    print("Du er på vei tilbake fra en lang skoledag.")
    input()
    print("På vei opp en spesielt bratt bakke så merker du noe i grøften.")
    input()
    print("Det er en døende rev. Den strever for å puste og har ikke lenge igjen.")
    input()
    print("-----------------------------------------------------------------------")

def førstevalg():
    valg = ""
    feilmelding=["Prøv noe mindre kreativt.","Det vil ikke hjelpe reven...","Nei, ikke det.","Interessangt, men prøv heller noe annet."]
    ingmeld=["Mens du gjør ingenting er reven bare nærmere livets ende","Din passivitet hjelper ikke reven!","Stillheten blir bare avbrutt av revens ujevne pust"]
    while valg != "gå nærmere" and valg != "gå vekk":
        valg = input("Hva gjør du? skal du gå nærmere, eller gå vekk?   --> ")
        if valg != "gå nærmere" and valg != "gå vekk" and valg != "":
            print()
            print(random.choice(feilmelding))
            print()
            print("-----------------------------------------------------------------------")
        if valg == "":
            print()
            print(random.choice(ingmeld))
            print()
            print("-----------------------------------------------------------------------")
    print()
    print("-----------------------------------------------------------------------")
    return valg


def gånærmere():
    print()
    print("Du kommer nærmere reven, den blør fra et stort kutt på magen...")
    input()
    print("plutselig hører du reven si noe!")
    input()
    print("Den har det vanskelig med å prate, men sånn hørtes det ut:")
    input()
    print("    'Jeg har ikke lenge igjen... men oppdraget mitt må ikke myslikkes... ta dette!'")
    input()
    print("Med sine siste styrker så gir reven deg en medaljong som hang rundt halsen sin")
    input()
    print("    'Bruk det!' - sier reven - 'Passordet... er 'veldig viktig oppdrag 123'...'")
    input()
    print("Reven tar et siste åndedrag og lukker øynene. Så blir den stille.")
    input()
    print("-----------------------------------------------------------------------")
    

def gåvekk():
    print()
    print("Du fjerner deg og drar hjem.")
    input()
    print("Den stakkars reven tar sine siste åndedrag og dør helt alene nede i grøften. RIP.")
    input()

def passord():
    ordet = ""
    forsøk = 1
    tomforsøk = 1
    feilmelding=["Medaljongen er stille, urørt av dine ord.", "Forventet du at medaljongen skulle svare på det?", "Om medaljongen var et menneske så ville den blitt forstyrret av det du sa nå."]
    ingmeld=["Det skjer ingenting hvis du gjør ingenting!","Prøv noe mer konstruktivt da vel.","Det hjelper ikke å være taus!"]
    while ordet != "veldig viktig oppdrag 123":
        if forsøk == 1:
            print()
            ordet = input("Så pussig! Hva kan du muligens gjøre nå?   --> ")
            if ordet != "veldig viktig oppdrag 123" and ordet !="":
                print()
                print("Medaljongen reagerer ikke på dette, tross alt er den tilsynelatende en hvilken som helst smykke!")
                print()
                print("-----------------------------------------------------------------------")
            if ordet == "":
                if tomforsøk == 1:
                    print()
                    print("Det skjer ingenting hvis du gjør ingenting!")
                    print()
                    print("-----------------------------------------------------------------------")
                    forsøk -= 1
                if tomforsøk >= 2:
                    print()
                    print(random.choice(ingmeld))
                    print()
                    print("-----------------------------------------------------------------------")
                    forsøk -= 1
                tomforsøk += 1
            forsøk += 1
        if forsøk >= 2:
            ordet =input("Hva vil du prøve på nå da?   --> ")
            if ordet != "veldig viktig oppdrag 123" and ordet !="":
                print()
                print(random.choice(feilmelding))
                print()
                print("-----------------------------------------------------------------------")
            if ordet == "veldig viktig oppdrag 123":
                print()
                print("-----------------------------------------------------------------------")
            if ordet == "":
                print()
                print(random.choice(ingmeld))
                print()
                print("-----------------------------------------------------------------------")
    return ordet
    
def medaljong():
    print()
    print("Oi! Medaljongen skinner plutselig i henda dine!")
    input()
    print("Du ser skrekkslagen ned på smykket. Lyset blender deg, men du klarer ikke å se vekk!")
    input()
    print("Alt rundt deg blir mørkt i takt med at lyset blir sterkere og sterkere...")
    input()
    print("Du ser bare lyset nå, og du kan ikke føle kroppen din lenger!")
    input()
    print("Du kjenner at sinnet ditt flyter i stor fart bort fra veikanten du hittil sto på.")
    input()
    print("Du kjenner plutselig at føttene treffer på et nytt underlag...")
    input()
    print("Du får bare et glimt av de nye omgivelsene før det blir for mye, du besvimer!")
    input()
    print("...")
    input()
    print("Hva slags underlig sted kan reven ha tatt deg med til?")
    input()
    print()
    print("FINN UT PÅ DEL 2 AV DETTE EVENTYRET!!!!!")
    input()
    
def gjenta():
    print()
    print("-----------------------------------------------------------------------")
    print()
    igjen = input("Vil du spille igjen? ")
    return igjen

igjen = "ja"

while igjen == "ja":
    VisIntro()

    valg = førstevalg()

    if valg == "gå vekk":
        gåvekk()
        
    elif valg == "gå nærmere":
        gånærmere() 
        ordet = passord()
        if ordet == "veldig viktig oppdrag 123":
            medaljong()
    
    igjen = gjenta()
    print()
    print("-----------------------------------------------------------------------")
    
    
 