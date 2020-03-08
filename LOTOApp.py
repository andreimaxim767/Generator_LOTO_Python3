import random

class Loto:
    def __init__(self):

        self.numere_user=set()
        self.numere_loterie=set()



    def calculeaza_numere_loterie(self):


        numar_pc_1=random.randint(1,49)
        numar_pc_2=random.randint(1,49)
        numar_pc_3=random.randint(1,49)
        numar_pc_4=random.randint(1,49)
        numar_pc_5=random.randint(1,49)
        numar_pc_6=random.randint(1,49)

        iteme=numar_pc_1,numar_pc_2,numar_pc_3,numar_pc_4,numar_pc_5,numar_pc_6
        self.numere_loterie.add(iteme)
        

    def numere_introduse(self):
        while True:
            numar_user1=int(input('Introduceti primul numar norocos: '))
            if numar_user1 in range(1,49):
                self.numere_user.add(numar_user1)
                break
            else:
                print('Introduceti un numar cuprins intre 1 si 49:')
        while True:
            numar_user2=int(input('Introduceti al doilea numar norocos: '))
            if numar_user2 == numar_user1:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')

            else:
                self.numere_user.add(numar_user2)
                break
        while True:
            numar_user3=int(input('Introduceti al treilea numar norocos: '))
            if numar_user3 == numar_user1:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user3 == numar_user2:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            else:
                self.numere_user.add(numar_user3) 
                break
        while True:
            numar_user4=int(input('Introduceti al patrulea numar norocos: '))
            if numar_user4 == numar_user1:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user4 == numar_user2:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user4 == numar_user3:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            else:
                self.numere_user.add(numar_user4)  
                break   
        while True:
            numar_user5=int(input('Introduceti al cincelea numar norocos: '))
            if numar_user5 == numar_user1:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user5 == numar_user2:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user5 == numar_user3:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user5 == numar_user4:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            else:
                self.numere_user.add(numar_user5) 
                break  
        while True:
            numar_user6=int(input('Introduceti al saselea numar norocos: '))
            if numar_user6 == numar_user1:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user6 == numar_user2:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user6 == numar_user3:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user6 == numar_user4:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            elif numar_user6 == numar_user5:
                print('Ati mai introdus acest numar.Introduceti altul cuprins intre 1 si 49:')
            else:
                self.numere_user.add(numar_user6)  
                break 

    def diferenta_numere(self):
        
        
        while True:
            rezultat=input('\nIntroduceti "Da" daca vrei sa aflati daca ati castigat; \n Introduceti "Nu" daca vrei sa iestiti din aplicatie: ')
            intersectie=self.numere_user and self.numere_loterie
            rezultat.lower
            if rezultat == 'da':
                if intersectie != None:
                    print('Numerele extrase sunt:' + str(self.numere_loterie))
                    print(' Numerele dvs. sunt:' + str(sorted(self.numere_user)))
                    break
                else:
                    print('Nu ati castigat de data aceasta :(')
            else:
                break

    def diff(self):
        
        dif=self.numere_user.intersection(self.numere_loterie)
        print(dif)
                                
                         

bilet=Loto()
bilet.calculeaza_numere_loterie()
bilet.numere_introduse()
bilet.diferenta_numere()
bilet.diff()