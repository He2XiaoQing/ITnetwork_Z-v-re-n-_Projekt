class SpravaPojistenych:
    __seznamPojistenych = []

    def pridat(self, jmeno, prijmeni, telefon, vek):
        self.__seznamPojistenych.append(Pojisteny(jmeno, prijmeni, telefon, vek))

    def vypis(self):
        if not self.__seznamPojistenych:
            print("Záznam nenalezen.")
        for pojisteny in self.__seznamPojistenych:
            pojisteny.zobrazit()

    def smazat_vse(self):
        self.__seznamPojistenych = []

    def smazat(self, jmeno, prijmeni, telefon, vek):
        for pojisteny in self.__seznamPojistenych:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni and pojisteny.telefon == telefon \
                    and pojisteny.vek == vek:
                self.__seznamPojistenych.remove(pojisteny)
                return True
        return False

    def vyhledat(self, jmeno, prijmeni, telefon, vek):
        for pojisteny in self.__seznamPojistenych:
            if jmeno in pojisteny.jmeno and prijmeni in pojisteny.prijmeni and telefon in pojisteny.telefon \
                    and vek in pojisteny.vek:
                pojisteny.zobrazit()


class Pojisteny:
    jmeno = None
    prijmeni = None
    telefon = None
    vek = None

    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

    def zobrazit(self):
        print("""
            Jméno: %s,
            Příjmení: %s,
            Telefon: %s,
            Věk: %s""" % (self.jmeno, self.prijmeni, self.telefon, self.vek))
