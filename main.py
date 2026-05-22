import json

print('Welcome everyone to my list of task. \nThis is your list right now.')

with open("task.json", "r") as f:  
    dati = json.load(f) 
 
for elemento in dati["studio"]: 
    print(elemento["materia"]) 


def overwiev():
    print('Click 1 to add something to your task')
    print('Click 2 to delete something to your task')
    print('Click 0 to exit')


    


def add():

    while True:

        try:
            decision = int(input('What you wanna do: '))
        except ValueError:
            print('It has to be a number') 
            continue  

        if decision == 1:
            nuova_attività = input('cosa vuoi aggiungere: ')
            dati["studio"].append({"materia" : nuova_attività})

            with open("task.json", "w") as f:
                json.dump(dati, f, indent = 4, ensure_ascii = False)

            print(f'Nuova materia {nuova_attività} aggiunta!')

        elif decision == 0:
            print('Goodbye')
            break   

        elif decision != 1 or decision != 2:
            print('Number has to be 1 or 2')
            continue    
            
        
        
        
        return decision
        


def delete(decision):
    
    if decision == 2:
        elimina_attività = input('Che attività vuoi eliminare dalla lista? ')
        
        # cerca e rimuove l'elemento
        for elemento in dati["studio"]:
            if elemento["materia"] == elimina_attività:
                dati["studio"].remove(elemento)
                
                with open("task.json", "w") as f:
                    json.dump(dati, f, indent=4, ensure_ascii=False)
                
                print(f'Materia {elimina_attività} eliminata!')
                return  # esce dalla funzione dopo aver eliminato
        
        # se non trova nulla
        print(f'Attività {elimina_attività} non trovata nella lista!')





overwiev()
scelta = add()
delete(scelta)