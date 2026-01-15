#trova quando il criceto muore
import random
giocatori=11
lupi=2
indice_criceto=1
indice_veggente=0
vivi=[True for people in range(giocatori)]
#vivi=[True,True,True,True,True,True,True,True,True,True,True]
#indice 0 è veggente 1 è criceto gli ultimi sono lupi 
def balottaggio():
    global vivi

    n_vivi=len(vivi)
    # parte da 1 per non includere il veggente
    scelta=random.randint(1,n_vivi-1)
    vivi[scelta]=False
    return scelta==indice_criceto
def lupi(guardiato):
    global vivi

    n_vivi=len(vivi)
    # parte da 0 e non include i lupi
    scelta=random.randint(0,n_vivi-1-lupi)
    if scelta!=indice_criceto:
        vivi[scelta]=False
        #il criceto non muore dai lupi
    
def guardia():
    global vivi
    n_vivi=len(vivi)
    # parte da 0 e include i lupi che potrebbe essere difesi inutilmente
    scelta=random.randint(0,n_vivi)
    return scelta==indice_criceto
lupi()
print(vivi)
finished=False
while not finished:
    morto=balottaggio()
    if morto:
        print("Criceto morto")
        finished=True
    else:
        saved=guardia()
        if saved:
            print("Criceto salvato")
        else:
            print("Criceto morto")
            finished=True
    print(vivi)
