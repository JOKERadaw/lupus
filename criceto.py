#trova quando il criceto muore
#senza indemoniato 
import random
giocatori=11
n_lupi=2
indice_criceto=1
indice_veggente=0
indice_guardia=2
vivi=[people for people in range(giocatori)]
#vivi=[0,1,2,3,4,5,6,7,8,9,10]

def balottaggio():
    global vivi
   
    
    if len(vivi)>1:
        scelta=indice_veggente  
        while scelta==indice_veggente:
            scelta=random.choice(vivi) 
        vivi.remove(scelta)
    
def lupi_vivi():
    global vivi
    c=0
    for i in range(indice_guardia+1,indice_guardia+1+n_lupi):
        if i in vivi:
            c+=1
    return c
def lupi(guardiato):
    global vivi


    #i lupi non si mangiano tra di loro
    
    scelta=indice_guardia+1
    while scelta>indice_guardia and scelta<=indice_guardia+n_lupi:

        scelta=random.choice(vivi)
        #print(scelta)
    if scelta!=indice_criceto and scelta!=guardiato:
        vivi.remove(scelta)
            #il criceto non muore dai lupi e il guardiato
def veggente(visti):
    global vivi
    #print(visti)
    scelta=random.choice(vivi)
    c=0
    #intersezione di array
    for i in visti:
        if i in vivi:
            c+=1
    if c==len(vivi)-1:
        return None

    while scelta in visti or scelta==indice_veggente:
        
        scelta=random.choice(vivi)
        
    if scelta==indice_criceto:
        vivi.remove(indice_criceto)
    
    return scelta
def guardia():
    global vivi
    guardiato=indice_guardia
    if len(vivi)>2 and indice_guardia in vivi:
        while guardiato==indice_guardia:
            guardiato=random.choice(vivi)
        return guardiato
    return None


criceto_morto=[0 for _ in range(giocatori)]
tot_simulazioni=1_000_000
for simulazione in range(tot_simulazioni):
    c=0
    vivi=[people for people in range(giocatori)]
    finito=False
    #per evitare che la veggente riguardi sempre i già visti
    indice_sguardoiniziale=random.choice([i for i in vivi if i!=indice_veggente])
    visti=[]
    while not finito:
        if indice_veggente in vivi:
            visti.append(veggente(visti))
        
        lupi(guardia())
        if not lupi_vivi():
            
            break
        if lupi_vivi()==len(vivi)-1 and indice_criceto in vivi:
            # lupi e criceto soli
            break

        #print(f"notte {c}:", vivi)
        #print(visti)
        if indice_criceto not in vivi: 
            criceto_morto[c]+=1
            finito=True
        else:
            c+=1
            balottaggio()
for i in range(giocatori):
    print(f"il criceto è morto alla notte {i} nel {criceto_morto[i]/tot_simulazioni*100}% delle volte")
# i lupi sbranano il criceto anche più volte