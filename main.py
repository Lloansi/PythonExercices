
import json

from act import Stars_Wars_Character
from act import Character_Films

#GlobalVariables
all_characters_list = []
characters_to_edit = ["Chewbacca", "Anakin Skywalker", "Luke Skywalker"]
info_chewabacca = ("3-8", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los ultimos Jedis")
info_anakin = ("1-6,9", "Star Wars: Episodio I - La Amenaza Fantasma", "Star Wars: Episodio VI - El retorno del Jedi")
info_luke = ("3-9", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los ultimos Jedis")


def comprobar_nuevos_valores(all_characters_list, size):
    for i in range(size):
        if all_characters_list[i].name == "Chewbacca":
            print(all_characters_list[i])
        if all_characters_list[i].name == "Anakin Skywalker":
            print(all_characters_list[i])
        if all_characters_list[i].name == "Luke Skywalker":
            print(all_characters_list[i])

def leer_lista(all_characters_list):
    for char in all_characters_list:
        print(char)

def read_json_and_write_to_list(datajson,all_characters_list:list):
    for character in datajson:
        character_info_list = Stars_Wars_Character(
                character['fields']['edited'],
                character['fields']['name'],
                character['fields']['created'],
                character['fields']['gender'],
                character['fields']['skin_color'],
                character['fields']['hair_color'],
                character['fields']['height'],
                character['fields']['eye_color'],
                character['fields']['mass'],
                character['fields']['homeworld'],
                character['fields']['birth_year']
            )
        all_characters_list.append(character_info_list)

def add_new_info_to_list(all_characters_list:list,newinfo_che,newinfo_ana,newinfo_luke,characters_to_edit,size,size2):
    for i in range(size):
            for j in range(size2):
                if all_characters_list[i].name == characters_to_edit[j]:
                    if characters_to_edit[j] == "Chewbacca":
                        info_toadd = newinfo_che
                    if characters_to_edit[j] == "Anakin Skywalker":
                        info_toadd = newinfo_ana
                    if characters_to_edit[j] == "Luke Skywalker":
                        info_toadd = newinfo_luke
                    all_characters_list[i] = Character_Films(all_characters_list[i].edited,
                                            all_characters_list[i].name,
                                            all_characters_list[i].created,
                                            all_characters_list[i].gender,
                                            all_characters_list[i].skin_color,
                                            all_characters_list[i].hair_color,
                                            all_characters_list[i].height,
                                            all_characters_list[i].eye_color,
                                            all_characters_list[i].mass,
                                            all_characters_list[i].homeworld,
                                            all_characters_list[i].birth_year,
                                            info_toadd[0],
                                            info_toadd[1],
                                            info_toadd[2]
                                            )

def main():
    #Abrimos el archivo json en modo lectura
    with open("/home/sjo/Escriptori/DADES/DavidGomez/Python/ACTIVITIES/StarWars.json", 'r') as f:
        datajson = json.load(f)

    #Leemos el json y metemos toda la info en una lista
    read_json_and_write_to_list(datajson, all_characters_list)

    #Sacamos la longitud de cada lista, para luego iterar sus valores
    size = len(all_characters_list)
    size2 = len(characters_to_edit)
                        
    #Añadimos la información nueva de los personajes elejidos a la lista anterior
    add_new_info_to_list(all_characters_list,info_chewabacca,info_anakin,info_luke,characters_to_edit,size,size2)
                
    #Abrimos el archivo json en modo escritura y añadimos los datos de la lista
    with open('/home/sjo/Escriptori/DADES/DavidGomez/Python/ACTIVITIES/datos.json', 'w') as archivo_json:
        json.dump([character.to_dict() for character in all_characters_list], archivo_json, indent=4)


main()