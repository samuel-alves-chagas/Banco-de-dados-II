from db.database import Graph


class PersonagemDAO(object):
    def __init__(self, connection):
        self.db = connection

    def getCharactersNames(self):
        results = self.db.execute_query('MATCH (n) RETURN n.nome as nome')
        data = []
        for record in results:
            data.append(record['nome'])
        return data

    def getRelationBetweenCharacters(self, char1, char2):
        results = self.db.execute_query(
            'MATCH (c1{nome:$nome1})-[r]-(c2{nome:$nome2}) RETURN r',
            {'nome1': char1, 'nome2': char2}
        )
        data = []
        for record in results:
            data.append(record['r'].type)
        return data
