from utils.utils import divider
from pprintpp import pprint as pp
from model.personagemDAO import PersonagemDAO

inputs = {
    1: '1. Para verificar se dois personagens possuem algum tipo de relação\n'
}


def view(connection):

    dao = PersonagemDAO(connection)

    print('Olá, este é um sistema para consulta de informações dos personagens de Breaking Bad')
    print('Para interagir basta selecionar uma das opções de pesquisa e seguir os passos ;)\n')
    while 1:
        option = input(inputs[1])
        divider()
        if option == '1':
            print(
                '\nInforme dois dos personagens cadastrados para verificar a relação entre eles\n')

            names = dao.getCharactersNames()
            pp(names)

            personagem1 = input('\nPersonagem 1: ')
            personagem2 = input('Personagem 2: ')
            # personagem1 = 'Mr. White'
            # personagem2 = 'Skyler White'
            divider()

            results = dao.getRelationBetweenCharacters(
                personagem1, personagem2)
            if len(results) > 0:
                print('A(s) relação(ões) entre ', personagem1,
                      ' e ', personagem2, ' são: \n', results)

            divider()

        else:
            break

    # elif option == '2':
    #     aux = dao.read_all_nodes()
    #     pp(aux)
    #     divider()

    # elif option == '3':
    #     name = input('  Name: ')
    #     age = input('   Age: ')
    #     person = {
    #         'name': name,
    #         'age': age
    #     }

    #     aux = dao.update_age(person)
    #     divider()

    # elif option == '4':
    #     name = input('  Name: ')
    #     person = {
    #         'name': name
    #     }

    #     aux = dao.delete(person)
    #     divider()

    # else:
    #     break
