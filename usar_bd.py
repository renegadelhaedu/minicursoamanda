import DAO

DAO.inseriruser('teste@teste.com', 'user teste', 'senha123')

saida = DAO.buscar_pessoa('user teste')
print(saida)


