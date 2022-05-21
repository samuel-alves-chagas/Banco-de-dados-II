from pprintpp import pprint as pp
from operator import itemgetter
from model.personagemDAO import PersonagemDAO
from utils.utils import divider, optionStr


def view(connection):

    dao = PersonagemDAO(connection)

    print('Olá, este é um sistema para consulta de informações dos personagens de Breaking Bad')
    print('Para interagir basta selecionar uma das opções de pesquisa e seguir os passos ;)\n')
    while 1:
        option = input(optionStr)
        divider()
        if option == '1':
            print(
                '\nInforme dois dos personagens cadastrados para verificar a relação entre eles\n')

            names = dao.getCharactersNames()
            pp(names)

            personagem1 = input('\nPersonagem 1: ')
            personagem2 = input('Personagem 2: ')
            divider()

            results = dao.getRelationBetweenCharacters(
                personagem1, personagem2)
            if len(results) > 0:
                print('A(s) relação(ões) entre', personagem1,
                      'e', personagem2, 'são: \n', results)
            else:
                print('Os personagens', personagem1,
                      'e', personagem2, 'não tem relação. Por favor, verifique se os nomes foram digitados correramente')

            divider()

        elif option == '2':
            results = dao.peopleWhoHateThemself()
            if len(results) > 0:
                print('As pessoas que se odeiam são:')
                for i in range(len(results)):
                    keyName = list(results[i].keys())[0]
                    valueName = list(results[i].values())[0]
                    print(keyName, 'odeia', valueName)
            else:
                print('Nenhum dos personagens do banco se odeiam!')

            divider()

        elif option == '3':
            results = dao.goodCharacters()
            if len(results) > 0:
                print('Os personagens bonzinhos são:')
                for name in results:
                    pp(list(name)[0])

            else:
                print('Nenhum dos personagens do banco é bonzinho')

            results = dao.evilCharacters()
            if len(results) > 0:
                print('\nOs personagens malvados são:')
                for name in results:
                    pp(list(name)[0])
            else:
                print('Nenhum dos personagens do banco é malvado')

            divider()

        else:
            break
