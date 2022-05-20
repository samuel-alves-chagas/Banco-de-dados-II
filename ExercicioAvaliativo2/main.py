import os
from dotenv import load_dotenv
from db.database import Graph

# Buscando as variáveis de ambiente
load_dotenv()

connection = Graph(
    uri=os.environ['DB_URI'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD']
)

connection.close()
