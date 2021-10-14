sir=input("Dati primul sir:\n")
sir2=input("Dati sirul al doilea:\n")
sir3=input("Dati sirul al treilea:\n")
sir_final=sir2_final=sir3_final=""
for litera in sir:
    if(ord(litera)>=65 and ord(litera)<=89) or (ord(litera)>=97 and ord(litera)<=121):
        litera=chr(ord(litera)+1)
    sir_final+=litera
for litera in sir2:
    if(litera=="Z"):
        litera="A"
    elif(litera=="z"):
        litera="a"
    sir2_final+=litera
for litera in sir3:
    if(litera==" "):
        litera="_"
    sir3_final+=litera

print(f"Primul sir era {sir} si dupa prelucrari a devenit {sir_final}")
print(f"Al doilea sir era {sir2} si dupa prelucrari a devenit {sir2_final}")
print(f"Al treilea sir era {sir3} si dupa prelucrari a devenit {sir3_final}")