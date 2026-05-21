import json

with open("task.json", "r") as f:  
    dati = json.load(f) 
 
for elemento in dati["studio"]: 
    print(elemento["materia"]) 



print('Welcome everyone to my list of task.')



def overwiev():
    print('Click 1 to add something to your task')



def add():
    add1 = int(input('What you wanna do: '))

    if add1 == 1:
        nuova_materia = input('cosa vuoi aggiungere: ')
        dati["studio"].append({"materia" : nuova_materia})

        with open("task.json", "w") as f:
            json.dump(dati, f, indent = 4)

        print(f'Nuova materia {nuova_materia} aggiunta!')



overwiev()
add()

