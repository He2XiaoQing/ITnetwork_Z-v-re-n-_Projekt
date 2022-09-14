import SpravaPojistenych


class KonzoleZadani:
    
    SpravaPojistenych = None

    def __init__(self):
        self.SpravaPojistenych = SpravaPojistenych.SpravaPojistenych()

    def __info_od_uzivatele(self):
        print("Prosím zadejte jméno pojištěného:")
        jmeno = input()
        print("Prosím zadajte příjmení pojištěného:")
        prijmeni = input()
        print("Prosím zadejte telefonní číslo pojištěného:")
        telefon = input()
        print("Prosím zadejte věk pojištěného:")
        vek = input()
        return (jmeno, prijmeni, telefon, vek)

    def __pridat_do_vypisu(self):
        jmeno, prijmeni, telefon, vek = self.__info_od_uzivatele()
        self.SpravaPojistenych.pridat(jmeno, prijmeni, telefon, vek)

    def __smazat_z_vypisu(self):
        jmeno, prijmeni, telefon, vek = self.__info_od_uzivatele()
        if self.SpravaPojistenych.smazat(
                jmeno, prijmeni, telefon, vek):
            print("Záznam smazán!")
        else:
            print("Záznam nenalazen, zadejte znovu.")

    def __vytvorit_hledani(self):
        hotovo = False
        jmeno = ""
        prijmeni = ""
        telefon = ""
        vek = ""

        while not hotovo:
            print("""
            Jaké informace chcete vyhledat?\n
            | 1 |  Jméno
            | 2 |  Příjmení
            | 3 |  Telefon
            | 4 |  Věk""")
            odpoved = input()
            if odpoved.lower() == "1":
                print("Zadejte jméno:")
                jmeno = input()
            else:
                if odpoved.lower() == "2":
                    print("Zadejte příjmení:")
                    prijmeni = input()
                else:
                    if odpoved.lower() == "3":
                        print("Zadejte telefonní číslo:")
                        telefon = input()
                    else:
                        if odpoved.lower() == "4":
                            print("Zadejte věk:")
                            vek = input()
                        else:
                            print("Prosím zadejte správné údaje.")
            print("Chcete přidat další informace? (ano/ne)")
            hotovo = input() == "ne"
        self.SpravaPojistenych.vyhledat(jmeno, prijmeni, telefon, vek)

    def __operace(self, odpoved):
        if odpoved.lower() == "1":
            self.SpravaPojistenych.vypis()
            return True
        if odpoved.lower() == "2":
            self.__pridat_do_vypisu()
            return True
        if odpoved.lower() == "3":
            self.__smazat_z_vypisu()
            return True
        if odpoved.lower() == "4":
            self.SpravaPojistenych.smazat_vse()
            print("Všechny záznamy smazány.")
            return True
        if odpoved.lower() == "5":
            self.__vytvorit_hledani()
            return True
        if odpoved.lower() == "6":
            print("Nashledanou.")
            return False
        else:
            print("Špatné zadání, prosím zadejte znovu.")
            return True

    def spustit(self):
        spusteno = True
        uvitat = "\nVítejte v evidenci pojištěných.\n"
        menu = """
        Zvolte akci:\n
        | 1 |   Vypsat všechny záznamy
        | 2 |   Přidat nový záznam
        | 3 |   Smazat záznam
        | 4 |   Smazat všechny záznamy
        | 5 |   Vyhledat záznam
        | 6 |   Konec"""
        print(uvitat)
        while spusteno:
            print(menu)
            odpoved = input()
            spusteno = self.__operace(odpoved)
