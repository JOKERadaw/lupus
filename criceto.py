#trova quando il criceto muore
import random
giocatori=11
vivi=[True for people in range(giocatori)]
#vivi=[True,True,True,True,True,True,True,True,True,True,True]
#indice 0 è veggente 1 è criceto
def balottaggio():
    global vivi

    n_vivi=len(vivi)
    # parte da 1 per non includere il veggente
    scelta=random.randint(1,n_vivi-1)
    vivi[scelta]=False
    return scelta==1
def lupi():
    global vivi

    n_vivi=len(vivi)
    # parte da 0 
    scelta=random.randint(0,n_vivi-1)
    if scelta!=1:
        vivi[scelta]=False
def guardia():
    global vivi

    n_vivi=len(vivi)
    # parte da 0 
    scelta=random.randint(0,n_vivi-1)
    return scelta==1 
lupi()
print(vivi)

